from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import tenacity
from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class LLMResponse(BaseModel):
    content: str
    usage: dict[str, Any] = {}
    raw: dict[str, Any] | None = None


class LLMClient(ABC):
    @abstractmethod
    def chat(self, messages: list[ChatMessage], **kwargs) -> LLMResponse:  # pragma: no cover
        ...

    @abstractmethod
    def embed(self, texts: list[str], **kwargs) -> list[list[float]]:  # pragma: no cover
        ...

    @abstractmethod
    def name(self) -> str:  # pragma: no cover
        ...


retry_policy = tenacity.retry(
    wait=tenacity.wait_exponential(multiplier=0.5, min=1, max=30),
    stop=tenacity.stop_after_attempt(6),
    retry=tenacity.retry_if_exception_type(Exception),
    reraise=True,
)

