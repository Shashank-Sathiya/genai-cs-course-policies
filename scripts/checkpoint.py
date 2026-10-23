"""Append a token-usage checkpoint to docs/tokens.json.

Claude fills the numbers from the desktop app's usage report (get_usage).
Usage:
  python scripts/checkpoint.py --phase experiment --event "before /clear" --experiment clear \
      --tokens 212345 --pct5h 20 --weekly 6 --breakdown '{"Messages": 150000, "System tools": 38488}'
"""
import argparse
import json
from datetime import datetime
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "docs" / "tokens.json"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", required=True)
    ap.add_argument("--event", required=True)
    ap.add_argument("--experiment", choices=["clear", "compact"], help="groups before/after readings on the token page")
    ap.add_argument("--tokens", type=int, required=True, help="context tokensUsed")
    ap.add_argument("--pct5h", type=int, required=True)
    ap.add_argument("--weekly", type=int, required=True)
    ap.add_argument("--breakdown", default="{}", help="JSON object of context categories")
    a = ap.parse_args()
    cp = {"ts": datetime.now().astimezone().isoformat(timespec="seconds"), "phase": a.phase, "event": a.event,
          "context_tokens": a.tokens, "plan_5h_pct": a.pct5h, "weekly_pct": a.weekly, "breakdown": json.loads(a.breakdown)}
    if a.experiment:
        cp["experiment"] = a.experiment
    data = json.loads(PATH.read_text(encoding="utf-8"))
    data["checkpoints"].append(cp)
    PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(cp)
