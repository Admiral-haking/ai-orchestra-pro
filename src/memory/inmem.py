from __future__ import annotations

from typing import Any

from .base import Memory


class InMemoryMemory(Memory):
    def __init__(self):
        self._store: dict[str, Any] = {}

    def add(self, key: str, value: Any) -> None:
        self._store[key] = value

    def get(self, key: str) -> Any | None:
        return self._store.get(key)

    def search(self, query: str, k: int = 3) -> list[tuple[str, Any]]:
        # Naive: return any keys containing the substring
        matches: list[tuple[str, Any]] = []
        for k_, v in self._store.items():
            if query.lower() in str(v).lower() or query.lower() in k_.lower():
                matches.append((k_, v))
        return matches[:k]

