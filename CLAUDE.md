# GenAI-in-CS-courses policy project

Read this first after any /clear. The full state of the project lives in files, not chat history.

## What this is
A dataset + dashboard of how US CS courses let students use generative AI, plus three process pages
(validation explorer, timeline, token usage). Specs are in `specs/` — one per phase.

## Layout
- `data/policies.json` — the coded dataset + codebook (source of truth). `data/summary.json` is generated.
- `analysis/analyze.py` — analysis functions (pure, tested).
- `scripts/build.py` — runs analysis, exports `site/data/*.js`, runs pytest, exports test results. Run after ANY change.
- `scripts/log.py <student|claude> <phase> "<text>"` — append a timestamped timeline entry.
- `docs/log.jsonl` — timeline. `docs/tokens.json` — token checkpoints.
- `site/` — static site (GitHub Pages serves this folder).

## Rules for Claude
1. Every policy row needs a primary-source https URL and a short verbatim quote. Never code a course from memory or a search snippet.
2. After every phase: run `scripts/build.py`, append a `scripts/log.py claude ...` entry, and add a token checkpoint to `docs/tokens.json`.
3. Log every student question/decision with `scripts/log.py student ...`.
4. Do not write `docs/EVALUATION.md` or `docs/REFLECTION.md` content — those are the student's.
5. Before the student runs /clear: make sure the log, tokens and specs are up to date, and note the next step in `specs/STATUS.md`.

## Recording a token checkpoint
When the student says "record a token checkpoint: <event>":
1. Call the `get_usage` tool (mcp__ccd_session_mgmt__get_usage, load via ToolSearch if deferred).
2. Run `scripts/checkpoint.py` with `--tokens` = context.tokensUsed, `--pct5h` / `--weekly` from the plan windows,
   `--breakdown` = context categories as a JSON object, `--event` as given, `--phase experiment`, and
   `--experiment clear` or `--experiment compact` if the event mentions /clear or /compact.
3. Add a timeline entry with scripts/log.py, run scripts/build.py, commit and push.
Do not read other files first; the point is to measure the context cost of a bare reload.

## /clear vs /compact experiment (in progress — see specs/STATUS.md for which step is next)
Order of checkpoints: before /clear → after /clear → after reload task → before /compact → after /compact.

## Commands
```
.venv/Scripts/python scripts/build.py
python -m http.server 8765 --directory site
```
