"""Dataset integrity: every coded policy must be traceable to a source."""
import json
from pathlib import Path
from urllib.parse import urlparse

import pytest

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "policies.json").read_text(encoding="utf-8"))
POLICIES = DATA["policies"]
REQUIRED = ["id", "institution", "state", "institution_type", "course", "course_level", "term",
            "year", "level", "disclosure_required", "exams_ai_banned", "course_tool", "quote",
            "source", "source_type"]


def test_dataset_not_empty():
    assert len(POLICIES) >= 15


def test_ids_unique():
    ids = [p["id"] for p in POLICIES]
    assert len(ids) == len(set(ids))


@pytest.mark.parametrize("p", POLICIES, ids=lambda p: p["id"])
def test_required_fields(p):
    missing = [k for k in REQUIRED if k not in p]
    assert not missing, missing


@pytest.mark.parametrize("p", POLICIES, ids=lambda p: p["id"])
def test_level_in_codebook(p):
    assert str(p["level"]) in DATA["codebook"]["level"]


@pytest.mark.parametrize("p", POLICIES, ids=lambda p: p["id"])
def test_categoricals_in_codebook(p):
    assert p["course_level"] in DATA["codebook"]["course_level"]
    assert p["institution_type"] in DATA["codebook"]["institution_type"]


@pytest.mark.parametrize("p", POLICIES, ids=lambda p: p["id"])
def test_source_is_https_url(p):
    u = urlparse(p["source"])
    assert u.scheme == "https" and u.netloc


@pytest.mark.parametrize("p", POLICIES, ids=lambda p: p["id"])
def test_quote_present_and_short(p):
    # Short quotes only (fair use) and never empty: each code must be backed by evidence.
    assert 10 <= len(p["quote"]) <= 200


@pytest.mark.parametrize("p", POLICIES, ids=lambda p: p["id"])
def test_tristate_fields(p):
    for k in ("disclosure_required", "exams_ai_banned", "course_tool"):
        assert p[k] in (True, False, None)


@pytest.mark.parametrize("p", POLICIES, ids=lambda p: p["id"])
def test_year_plausible(p):
    assert 2022 <= p["year"] <= 2026


@pytest.mark.parametrize("p", [p for p in POLICIES if p["level"] == 0], ids=lambda p: p["id"])
def test_prohibited_not_marked_as_course_tool(p):
    assert p["course_tool"] is False


@pytest.mark.parametrize("p", [p for p in POLICIES if p["level"] == 1], ids=lambda p: p["id"])
def test_course_tool_level_has_tool(p):
    assert p["course_tool"] is True
