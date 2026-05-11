from __future__ import annotations

import os

import requests

from .base import ChatMessage, LLMClient, LLMResponse, retry_policy


class DeepSeekClient(LLMClient):
    def __init__(self, model: str):
        self.model = model
        self.base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
        self.token = os.getenv("DEEPSEEK_API_KEY")

    def name(self) -> str:
        return f"deepseek:{self.model}"

    @retry_policy
    def chat(self, messages: list[ChatMessage], **kwargs) -> LLMResponse:
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {"model": self.model, "messages": [m.model_dump() for m in messages]}
        r = requests.post(
            f"{self.base_url}/chat/completions", json=data, headers=headers, timeout=60
        )
        r.raise_for_status()
        j = r.json()
        content = j["choices"][0]["message"]["content"]
        return LLMResponse(content=content, raw=j)

    def embed(self, texts: list[str], **kwargs) -> list[list[float]]:
        raise NotImplementedError

