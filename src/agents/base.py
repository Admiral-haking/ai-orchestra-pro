from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from src.providers.base import ChatMessage, LLMClient


class AgentIO(BaseModel):
    task: str = Field(..., description="شرح کاری که باید انجام شود")
    context: str = Field("", description="متن/شواهد ورودی")
    constraints: list[str] = Field(default_factory=list)


class BaseAgent(ABC):
    role: str
    system_prompt: str
    client: LLMClient

    def __init__(self, role: str, system_prompt: str, client: LLMClient):
        self.role = role
        self.system_prompt = system_prompt
        self.client = client

    @abstractmethod
    def build_messages(self, io: AgentIO) -> list[ChatMessage]:  # pragma: no cover
        ...

    def run(self, io: AgentIO) -> str:
        messages = self.build_messages(io)
        resp = self.client.chat(messages, temperature=0.3)
        return resp.content

