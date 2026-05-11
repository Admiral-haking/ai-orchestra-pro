from __future__ import annotations

from collections.abc import Iterable


class SimpleVectorStore:
    """Placeholder vector store with naive embeddings (length-based)."""

    def __init__(self):
        self._docs: list[tuple[str, str, float]] = []  # (id, text, score)

    def add_texts(self, docs: Iterable[tuple[str, str]]):
        for doc_id, text in docs:
            self._docs.append((doc_id, text, float(len(text))))

    def search(self, query: str, k: int = 3) -> list[tuple[str, str, float]]:
        qlen = float(len(query))
        scored = [(doc_id, text, 1.0 / (1.0 + abs(score - qlen))) for doc_id, text, score in self._docs]
        scored.sort(key=lambda x: x[2], reverse=True)
        return scored[:k]

