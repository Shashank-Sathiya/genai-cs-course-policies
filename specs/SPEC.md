# Project specification

## Goal
Gather data on how students are permitted or encouraged to use genAI in CS courses across the US.
Communicate the findings in a dashboard, and define an approach for analyzing them.

## Phases and acceptance criteria

### P1 Data (`data/policies.json`)
- ≥15 policies, ≥5 institutions, mix of CS1 / CS2 / upper-level, at least one non-R1 institution.
- Each row has: institution, state, institution type, course, course level, term, year, level (0–4),
  disclosure_required / exams_ai_banned / course_tool (true/false/null), quote (10–200 chars), https source, source type.
- Null means "policy doesn't say"; it never means "no".
- Verified by `tests/test_data.py`.

### P2 Analysis (`analysis/analyze.py`)
- Level distribution; mean level by course level, institution type, year; feature rates among stated values.
- Verified against hand-computed fixtures in `tests/test_analysis.py`.

### P3 Dashboard (`site/index.html`)
- KPIs, distribution chart, group means, a searchable/filterable table where every row links to its source, the codebook, and the analysis approach + limitations.
- Shipped data must equal source + fresh analysis (`tests/test_site.py`).

### P4 Validation explorer (`site/tests.html`)
- Every test with its status, file and time, and failure message if any; search and filters; what the tests do and don't prove; how to reproduce.
- Validation report: `docs/VALIDATION.md`.

### P5 Timeline (`site/timeline.html`)
- Every student prompt/decision and Claude action, timestamped, filterable by actor/phase.

### P6 Tokens (`site/tokens.html`)
- Checkpoints after each phase and around every /clear or /compact, with the context breakdown.

### P7 Evaluation + reflection — student-authored (`docs/EVALUATION.md`, `docs/REFLECTION.md`).

### P8 Publish — GitHub repo + GitHub Pages serving `site/`.
