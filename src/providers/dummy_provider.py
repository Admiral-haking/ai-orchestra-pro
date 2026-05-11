from __future__ import annotations

from .base import ChatMessage, LLMClient, LLMResponse


class DummyClient(LLMClient):
    """Local dummy provider for dev/testing without network.
    Generates deterministic placeholder text from the last user message.
    """

    def __init__(self, model: str = "local"):
        self._model = model

    def name(self) -> str:
        return f"dummy:{self._model}"

    def chat(self, messages: list[ChatMessage], **kwargs) -> LLMResponse:
        user = next((m.content for m in reversed(messages) if m.role == "user"), "" )
        content = f"[DUMMY-{self._model}]\n{user[:1200]}"
        return LLMResponse(content=content, raw={"provider": "dummy", "model": self._model})

    def embed(self, texts: list[str], **kwargs) -> list[list[float]]:
        return [[float(len(t))] for t in texts]

