"""Analyze coded genAI course policies.

Approach: each policy is hand-coded on an ordinal 0-4 permissiveness scale
(see codebook in data/policies.json) plus binary features (disclosure, exam ban,
course-provided tool). We report distributions and cross-tabs by course level,
institution type, and policy year. Sample is small and non-random, so results are
descriptive only.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = [0, 1, 2, 3, 4]


def load(path=ROOT / "data" / "policies.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def level_distribution(policies):
    c = Counter(p["level"] for p in policies)
    return {lvl: c.get(lvl, 0) for lvl in LEVELS}


def mean_level_by(policies, key):
    groups = defaultdict(list)
    for p in policies:
        groups[p[key]].append(p["level"])
    return {k: {"n": len(v), "mean": round(sum(v) / len(v), 2)} for k, v in sorted(groups.items(), key=lambda kv: str(kv[0]))}


def feature_rate(policies, field):
    """Share of policies where field is True, among those that state it (non-null)."""
    stated = [p[field] for p in policies if p[field] is not None]
    if not stated:
        return {"stated": 0, "true": 0, "rate": None}
    t = sum(1 for v in stated if v)
    return {"stated": len(stated), "true": t, "rate": round(t / len(stated), 2)}


def summarize(data):
    ps = data["policies"]
    return {
        "n_policies": len(ps),
        "n_institutions": len({p["institution"] for p in ps}),
        "level_distribution": level_distribution(ps),
        "mean_level": round(sum(p["level"] for p in ps) / len(ps), 2),
        "by_course_level": mean_level_by(ps, "course_level"),
        "by_institution_type": mean_level_by(ps, "institution_type"),
        "by_year": mean_level_by(ps, "year"),
        "disclosure_required": feature_rate(ps, "disclosure_required"),
        "exams_ai_banned": feature_rate(ps, "exams_ai_banned"),
        "course_tool": feature_rate(ps, "course_tool"),
        "any_ai_allowed": sum(1 for p in ps if p["level"] >= 1),
    }


if __name__ == "__main__":
    s = summarize(load())
    out = ROOT / "data" / "summary.json"
    out.write_text(json.dumps(s, indent=2), encoding="utf-8")
    print(json.dumps(s, indent=2))
