from __future__ import annotations

from src.agents.base import AgentIO, BaseAgent
from src.providers.base import ChatMessage


class CriticAgent(BaseAgent):
    def build_messages(self, io: AgentIO):
        return [
            ChatMessage(role="system", content=self.system_prompt),
            ChatMessage(
                role="user",
                content=(
                    f"پیش‌نویس برای نقد و بازبینی:\n\n{io.context}\n\n"
                    f"معیارها/قیود: {', '.join(io.constraints)}"
                ),
            ),
        ]

