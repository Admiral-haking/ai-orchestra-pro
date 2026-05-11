from __future__ import annotations

from src.agents.base import AgentIO, BaseAgent
from src.providers.base import ChatMessage


class ResearcherAgent(BaseAgent):
    def build_messages(self, io: AgentIO):
        return [
            ChatMessage(role="system", content=self.system_prompt),
            ChatMessage(
                role="user",
                content=f"موضوع تحقیق: {io.task}\n\nبستر/متن: {io.context}\n\nقیود: {', '.join(io.constraints)}",
            ),
        ]

