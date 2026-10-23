"""Analysis functions checked against hand-computed fixtures and the real dataset."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "analysis"))
import analyze  # noqa: E402

FIX = [
    {"level": 0, "course_level": "CS1", "institution": "A", "institution_type": "Public R1", "year": 2024,
     "disclosure_required": None, "exams_ai_banned": True, "course_tool": False},
    {"level": 2, "course_level": "CS1", "institution": "A", "institution_type": "Public R1", "year": 2025,
     "disclosure_required": True, "exams_ai_banned": True, "course_tool": False},
    {"level": 4, "course_level": "CS2", "institution": "B", "institution_type": "Private R1", "year": 2025,
     "disclosure_required": False, "exams_ai_banned": None, "course_tool": True},
]


def test_distribution_fixture():
    assert analyze.level_distribution(FIX) == {0: 1, 1: 0, 2: 1, 3: 0, 4: 1}


def test_mean_by_course_level_fixture():
    r = analyze.mean_level_by(FIX, "course_level")
    assert r["CS1"] == {"n": 2, "mean": 1.0}
    assert r["CS2"] == {"n": 1, "mean": 4.0}


def test_feature_rate_ignores_nulls():
    assert analyze.feature_rate(FIX, "disclosure_required") == {"stated": 2, "true": 1, "rate": 0.5}
    assert analyze.feature_rate(FIX, "exams_ai_banned") == {"stated": 2, "true": 2, "rate": 1.0}


def test_feature_rate_all_null():
    assert analyze.feature_rate([{"x": None}], "x")["rate"] is None


def test_summary_fixture():
    s = analyze.summarize({"policies": FIX})
    assert s["n_policies"] == 3 and s["n_institutions"] == 2
    assert s["mean_level"] == 2.0 and s["any_ai_allowed"] == 2


def test_summary_real_data_consistent():
    data = analyze.load()
    s = analyze.summarize(data)
    assert sum(s["level_distribution"].values()) == s["n_policies"] == len(data["policies"])
    assert sum(g["n"] for g in s["by_course_level"].values()) == s["n_policies"]
    assert sum(g["n"] for g in s["by_institution_type"].values()) == s["n_policies"]
    assert 0 <= s["mean_level"] <= 4
