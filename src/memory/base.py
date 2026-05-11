from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Memory(ABC):
    @abstractmethod
    def add(self, key: str, value: Any) -> None:  # pragma: no cover
        ...

    @abstractmethod
    def get(self, key: str) -> Any | None:  # pragma: no cover
        ...

    @abstractmethod
    def search(self, query: str, k: int = 3) -> list[tuple[str, Any]]:  # pragma: no cover
        ...

