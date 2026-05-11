from __future__ import annotations

from src.agents.base import AgentIO, BaseAgent
from src.providers.base import ChatMessage


class WriterAgent(BaseAgent):
    def build_messages(self, io: AgentIO):
        return [
            ChatMessage(role="system", content=self.system_prompt),
            ChatMessage(
                role="user",
                content=f"وظیفه: {io.task}\n\nطرح و تحلیل برای نگارش:\n{io.context}",
            ),
        ]

