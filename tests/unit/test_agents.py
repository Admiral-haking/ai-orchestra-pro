from src.agents.base import AgentIO
from src.agents.researcher import ResearcherAgent


class DummyClient:
    def __init__(self):
        self._name = "dummy:model"

    def name(self):
        return self._name

    def chat(self, messages, **kwargs):
        class R:
            content = "ok"

        return R()


def test_researcher_agent_builds_messages():
    a = ResearcherAgent("researcher", "SYSTEM", DummyClient())
    out = a.run(AgentIO(task="t", context="c"))
    assert isinstance(out, str)

