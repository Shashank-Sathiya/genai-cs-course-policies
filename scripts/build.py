"""Build the site: run analysis, export data to site/data/*.js, run tests, export test results.

Usage: python scripts/build.py
Exit code is pytest's exit code, so a failing test fails the build.
"""
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "data"
sys.path.insert(0, str(ROOT / "analysis"))
import analyze  # noqa: E402


def write_js(name, var, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.js").write_text(f"window.{var} = {json.dumps(obj, indent=1)};\n", encoding="utf-8")


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def junit_to_records(xml_path):
    records = []
    for case in ET.parse(xml_path).getroot().iter("testcase"):
        status, message = "passed", ""
        for tag in ("failure", "error", "skipped"):
            el = case.find(tag)
            if el is not None:
                status = "failed" if tag in ("failure", "error") else "skipped"
                message = (el.get("message") or "") + "\n" + (el.text or "")
        file = case.get("classname", "").split(".")[-1]
        records.append({"file": file, "name": case.get("name"), "status": status,
                        "time": float(case.get("time", 0)), "message": message.strip()})
    return records


def main():
    data = analyze.load()
    summary = analyze.summarize(data)
    (ROOT / "data" / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_js("policies", "POLICIES", data)
    write_js("summary", "SUMMARY", summary)
    write_js("timeline", "TIMELINE", read_jsonl(ROOT / "docs" / "log.jsonl"))
    write_js("tokens", "TOKENS", json.loads((ROOT / "docs" / "tokens.json").read_text(encoding="utf-8")))

    xml = ROOT / "data" / "junit.xml"
    rc = subprocess.call([sys.executable, "-m", "pytest", "-q", f"--junitxml={xml}", str(ROOT / "tests")])
    tests = junit_to_records(xml)
    write_js("tests", "TESTS", {"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                "python": sys.version.split()[0], "exit_code": rc, "tests": tests})
    print(f"{len(tests)} tests, exit code {rc}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
