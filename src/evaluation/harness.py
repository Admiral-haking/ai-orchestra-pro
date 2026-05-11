from __future__ import annotations


def evaluate_faithfulness(output: str, evidence: str) -> float:
    return 1.0 if output and evidence else 0.5


def evaluate_style(output: str) -> float:
    return 1.0 if len(output) > 100 else 0.5


def run_harness(samples: list[dict[str, str]]) -> dict[str, float]:
    scores = []
    for s in samples:
        f = evaluate_faithfulness(s.get("output", ""), s.get("evidence", ""))
        st = evaluate_style(s.get("output", ""))
        scores.append((f, st))
    if not scores:
        return {"faithfulness": 0.0, "style": 0.0}
    return {
        "faithfulness": sum(s[0] for s in scores) / len(scores),
        "style": sum(s[1] for s in scores) / len(scores),
    }

