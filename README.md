# GenAI in CS Courses

How do US computer science courses permit or encourage students to use generative AI?
This repo has a coded dataset of 17 course policies, an analysis, and a dashboard. It also has the process documentation for an agentic-development class project.

| Page | What it shows |
|---|---|
| `site/index.html` | Dashboard: findings, searchable policy table with source links, analysis approach |
| `site/tests.html` | Validation explorer: every test, searchable and filterable |
| `site/timeline.html` | Timestamped student and Claude contributions |
| `site/tokens.html` | Token usage checkpoints by project phase |

## Headline findings (n=17, descriptive only)
- 12 of 17 policies allow at least some AI use. Only 2 actively encourage or require it (CMU 15-112, UIUC CS 124).
- The most common stance is **Restricted** (6 of 17): AI is fine for learning and debugging, but submitted work must be the student's own.
- Every policy that addresses disclosure requires it (6/6). 9 of the 10 that address exams ban AI on them.
- In this sample, CS2 courses are stricter than CS1 courses (mean 1.29 vs 2.20 on the 0–4 scale).

## Run
```bash
python -m venv .venv
.venv/Scripts/pip install pytest pypdf
.venv/Scripts/python scripts/build.py
python -m http.server 8765 --directory site
```

## Docs
`CLAUDE.md` (agent context), `specs/` (spec + status), `docs/VALIDATION.md`, `docs/EVALUATION.md`, `docs/REFLECTION.md`.
