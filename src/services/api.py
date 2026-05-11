from __future__ import annotations

from fastapi import FastAPI

from src.agents.analyst import AnalystAgent
from src.agents.base import AgentIO
from src.agents.critic import CriticAgent
from src.agents.researcher import ResearcherAgent
from src.agents.writer import WriterAgent
from src.core.config import load_config
from src.core.logging import setup_logging
from src.core.tracing import setup_tracing
from src.orchestration.graph import build_graph
from src.providers.router import get_client_for
from src.services.schemas import RunRequest, RunResponse

app = FastAPI(title="AI-Orchestra Pro")
log = setup_logging()
cfg = load_config()
tracer = setup_tracing(cfg)


def _deps():
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
    return deps


@app.post("/run", response_model=RunResponse)
def run(req: RunRequest):
    deps = _deps()
    graph = build_graph(deps)
    state = graph.invoke({"task": req.task})
    draft = state.get("draft") or ""
    iterations = state.get("iterations", 0)
    log.info("run.completed", task=req.task, iterations=iterations)
    return RunResponse(draft=draft, iterations=iterations)

