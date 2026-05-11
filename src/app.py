from __future__ import annotations

import argparse

from src.agents.analyst import AnalystAgent
from src.agents.base import AgentIO
from src.agents.critic import CriticAgent
from src.agents.researcher import ResearcherAgent
from src.agents.writer import WriterAgent
from src.core.config import load_config
from src.orchestration.graph import build_graph
from src.providers.router import get_client_for


def main(task: str):
    cfg = load_config()
    deps = type("Deps", (), {})()
    deps.AgentIO = AgentIO
    deps.researcher = ResearcherAgent(
        "researcher",
        open("prompts/system/researcher.md", encoding="utf-8").read(),
        get_client_for("research", cfg),
    )
    deps.analyst = AnalystAgent(
        "analyst",
        open("prompts/system/analyst.md", encoding="utf-8").read(),
        get_client_for("analysis", cfg),
    )
    deps.writer = WriterAgent(
        "writer",
        open("prompts/system/writer.md", encoding="utf-8").read(),
        get_client_for("writing", cfg),
    )
    deps.critic = CriticAgent(
        "critic",
        open("prompts/system/critic.md", encoding="utf-8").read(),
        get_client_for("critic", cfg),
    )

    graph = build_graph(deps)
    state = graph.invoke({"task": task})
    print("\n--- FINAL OUTPUT ---\n", state["draft"])  # noqa: T201


def cli():
    parser = argparse.ArgumentParser(description="AI-Orchestra Pro CLI")
    parser.add_argument("task", type=str, nargs="?", default="کاربردهای محاسبات کوانتومی در پزشکی")
    args = parser.parse_args()
    main(args.task)


if __name__ == "__main__":
    cli()

