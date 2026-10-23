"""The built site must ship data identical to the source dataset and analysis."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT / "analysis"))
import analyze  # noqa: E402


def read_js_data(name):
    text = (SITE / "data" / f"{name}.js").read_text(encoding="utf-8")
    m = re.match(r"window\.\w+\s*=\s*(.*);\s*$", text, re.S)
    assert m, f"{name}.js not in expected format"
    return json.loads(m.group(1))


def test_pages_exist():
    for page in ("index.html", "tests.html", "timeline.html", "tokens.html"):
        assert (SITE / page).is_file(), page


def test_pages_link_each_other():
    for page in ("index.html", "tests.html", "timeline.html", "tokens.html"):
        html = (SITE / page).read_text(encoding="utf-8")
        for target in ("index.html", "tests.html", "timeline.html", "tokens.html"):
            assert f'href="{target}"' in html, f"{page} missing nav to {target}"


def test_dashboard_policies_match_source():
    assert read_js_data("policies") == analyze.load()


def test_dashboard_summary_matches_analysis():
    shipped = read_js_data("summary")
    fresh = json.loads(json.dumps(analyze.summarize(analyze.load())))
    assert shipped == fresh


def test_timeline_entries_timestamped():
    entries = read_js_data("timeline")
    assert entries
    for e in entries:
        assert re.match(r"\d{4}-\d\d-\d\dT\d\d:\d\d", e["ts"]) and e["actor"] in ("student", "claude")
