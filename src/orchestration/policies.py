from __future__ import annotations


def need_more_refine(state) -> bool:
    if state.iterations >= 2:
        return False
    text = (state.critique or "")
    return any(w in text for w in ["اشتباه", "ابهام", "نامعتبر"])  # Farsi keywords

