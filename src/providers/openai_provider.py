from __future__ import annotations

import os
from typing import Any

from openai import OpenAI

from .base import ChatMessage, LLMClient, LLMResponse, retry_policy


class OpenAIClient(LLMClient):
    def __init__(self, model: str):
        self.model = model
        self._api_key = os.getenv("OPENAI_API_KEY")
        self.client: Any = None  # lazy init to avoid requiring key during tests

    def name(self) -> str:
        return f"openai:{self.model}"

    @retry_policy
    def chat(self, messages: list[ChatMessage], **kwargs) -> LLMResponse:
        if self.client is None:
            if not self._api_key:
                raise RuntimeError("OPENAI_API_KEY not set for OpenAIClient.chat")
            self.client = OpenAI(api_key=self._api_key)
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[m.model_dump() for m in messages],
            **kwargs,
        )
        content = resp.choices[0].message.content
        return LLMResponse(content=content, raw=resp.model_dump())

    def embed(self, texts: list[str], **kwargs) -> list[list[float]]:
        raise NotImplementedError
