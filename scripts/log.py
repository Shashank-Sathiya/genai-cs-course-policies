"""Append a timestamped entry to docs/log.jsonl (the project timeline).

Usage: python scripts/log.py <student|claude> <phase> "<text>"
Phases: setup, data, analysis, code, validation, docs, evaluation
"""
import json
import sys
from datetime import datetime
from pathlib import Path

LOG = Path(__file__).resolve().parent.parent / "docs" / "log.jsonl"

if __name__ == "__main__":
    actor, phase, text = sys.argv[1], sys.argv[2], sys.argv[3]
    assert actor in ("student", "claude"), "actor must be student or claude"
    entry = {"ts": datetime.now().astimezone().isoformat(timespec="seconds"), "actor": actor, "phase": phase, "text": text}
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    print(entry)
