import pytest

langgraph = pytest.importorskip("langgraph")

from src.agents.base import AgentIO  # noqa: E402
from src.core.types import RunState  # noqa: E402
from src.orchestration.graph import build_graph  # noqa: E402


class DummyAgent:
    def __init__(self, text: str):
        self.text = text

    def run(self, io: AgentIO) -> str:
        return self.text


def test_graph_simple_flow():
    deps = type("Deps", (), {})()
    deps.AgentIO = AgentIO
    deps.researcher = DummyAgent("r")
    deps.analyst = DummyAgent("a")
    deps.writer = DummyAgent("d")
    deps.critic = DummyAgent("خوب است")  # no loop trigger
    g = build_graph(deps)
    state = g.invoke({"task": "x"})
    rs = RunState(**state)
    assert rs.draft == "d"

