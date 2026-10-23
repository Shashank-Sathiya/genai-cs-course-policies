# Validation report

Explore the results interactively on the validation page (`site/tests.html`). Reproduce them with `.venv/Scripts/python scripts/build.py`.

## 1. Automated tests — 138 passing (2026-10-23)
| File | What it checks | Count |
|---|---|---|
| `tests/test_data.py` | Schema, codebook validity, https source, evidence quote, consistency rules, per policy | 127 |
| `tests/test_analysis.py` | Analysis functions vs hand-computed fixtures; totals reconcile on real data | 6 |
| `tests/test_site.py` | Site data == source + fresh analysis; pages exist and cross-link; timeline timestamps | 5 |

## 2. Do the tests actually catch bugs? (mutation check)
| Injected bug | Result |
|---|---|
| `feature_rate` counts "not stated" as "No" | 3 tests failed (fixture, all-null case, site summary drift) |
| Dashboard data edited so it no longer matches the source | 1 test failed (`test_dashboard_policies_match_source`) |
| CS 225 row's evidence quote emptied | 1 test failed (`test_quote_present_and_short[uiuc-cs225]`) |

The code was restored after each check, and the suite went back to 138/138 passing.

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

| Row id | Source matches quote? | Agree with level? | Notes |
|---|---|---|---|
| | | | |
