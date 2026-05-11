from __future__ import annotations


def apply_feedback(draft: str, critique: str) -> str:
    """Simple heuristic: append actionable critique notes as a todo block."""
    if not critique:
        return draft
    return f"{draft}\n\n[بازخورد برای اصلاح]\n{critique}\n"

