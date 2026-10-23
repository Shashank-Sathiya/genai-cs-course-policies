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

## Commands
```
.venv/Scripts/python scripts/build.py
python -m http.server 8765 --directory site
```
