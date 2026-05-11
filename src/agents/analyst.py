from __future__ import annotations

from src.agents.base import AgentIO, BaseAgent
from src.providers.base import ChatMessage


class AnalystAgent(BaseAgent):
    def build_messages(self, io: AgentIO):
        return [
            ChatMessage(role="system", content=self.system_prompt),
            ChatMessage(
                role="user",
                content=(
                    f"تحلیل دقیق با تکیه بر شواهد زیر:\n\n{io.context}\n\n"
                    f"وظیفه: {io.task}\nقیود: {', '.join(io.constraints)}"
                ),
            ),
        ]

