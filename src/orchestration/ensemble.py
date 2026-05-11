from __future__ import annotations


def majority_vote(candidates: list[str]) -> str:
    if not candidates:
        return ""
    # naive: longest output as proxy for coverage
    return max(candidates, key=len)

