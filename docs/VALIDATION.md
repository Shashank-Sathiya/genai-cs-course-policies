# Validation report

Explore the results interactively on the validation page (`site/tests.html`). Reproduce them with `.venv/Scripts/python scripts/build.py`.

## 1. Automated tests — 139 passing (2026-10-24)
| File | What it checks | Count |
|---|---|---|
| `tests/test_data.py` | Schema, codebook validity, https source, evidence quote, consistency rules, per policy | 127 |
| `tests/test_analysis.py` | Analysis functions vs hand-computed fixtures; totals reconcile on real data | 6 |
| `tests/test_site.py` | Site data == source + fresh analysis; pages exist and cross-link; timeline timestamps; token checkpoints | 6 |

## 2. Do the tests actually catch bugs? (mutation check)
| Injected bug | Result |
|---|---|
| `feature_rate` counts "not stated" as "No" | 3 tests failed (fixture, all-null case, site summary drift) |
| Dashboard data edited so it no longer matches the source | 1 test failed (`test_dashboard_policies_match_source`) |
| CS 225 row's evidence quote emptied | 1 test failed (`test_quote_present_and_short[uiuc-cs225]`) |

The code was restored after each check, and the suite went back to all tests passing.

## 3. Manual / browser checks
- All four pages loaded from a local server; the browser console showed no errors.
- KPI values on the dashboard match `data/summary.json`: 17 policies, 9 institutions, mean 1.76.

## 4. Data provenance
- Each row was coded from its primary course page, fetched on 2026-10-23. The one exception is Stanford CS106A, which comes from a Stanford Daily news article and is labeled `news` in the data.
- Georgia Tech rules were read from syllabus PDFs with text extracted by pypdf.
- **Excluded** because the primary source couldn't be read: Princeton COS 126 (SSO login), Cornell CS 1110 and UChicago CMSC 23500/23530 (TLS certificate errors), Berkeley CS 61A (404).

## 5. What is NOT validated (reviewer should check)
- Whether each 0–4 code is the right reading of its policy. One coder did all the coding, with no inter-rater check.
- **Student review log** (fill in): which rows you checked against their sources and what you found.

Reviewed by the student on 2026-10-23: the first 5 rows of `data/policies.json`, opened at their source links.

| Row id | Source matches quote? | Agree with level? | Notes |
|---|---|---|---|
| 1 (harvard-cs50x) | Yes | Yes (1, course tool only) | The CS50x 2025 honesty page lists the CS50 Duck as reasonable and other AI tools (ChatGPT, Claude, Copilot, Gemini) as not reasonable. |
| 2 (stanford-cs106a) | Yes | Yes (0, prohibited) | The source is a 2024 Stanford Daily article, not the course syllabus. It may not reflect the current CS106A policy. |
| 3 (stanford-cs106b) | Yes | Yes (0, prohibited) | Archived Summer 2024 honor code page. The ban covers graded work. |
| 4 (stanford-cs166) | Yes | Yes (0, prohibited) | The page says AI use on graded work violates the Honor Code even if disclosed. |
| 5 (stanford-cs193x) | Yes | Yes (2, restricted) | Spring 2023 page, the oldest in the dataset. AI may not write assignment code; debugging help must be cited. |

Remaining rows 6–17 have not been reviewed by the student.
