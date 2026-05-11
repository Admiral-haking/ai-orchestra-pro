from __future__ import annotations

from langgraph.graph import END, StateGraph

from src.core.types import RunState
from src.orchestration.feedback import apply_feedback
from src.orchestration.policies import need_more_refine


def build_graph(deps):
    g = StateGraph(RunState)

    def do_research(state: RunState):
        state.research = deps.researcher.run(
            io=deps.AgentIO(task=state.task, context="", constraints=[])
        )
        return state

    def do_analysis(state: RunState):
        state.analysis = deps.analyst.run(
            io=deps.AgentIO(
                task=state.task, context=state.research or "", constraints=["تحلیل دقیق، منابع معتبر"]
            )
        )
        return state

    def do_write(state: RunState):
        state.draft = deps.writer.run(io=deps.AgentIO(task=state.task, context=state.analysis or ""))
        return state

    def do_critique(state: RunState):
        state.critique = deps.critic.run(
            io=deps.AgentIO(
                task=state.task, context=state.draft or "", constraints=["کیفیت/دقت/شفافیت"]
            )
        )
        return state

    def revise_loop(state: RunState):
        state.iterations += 1
        state.draft = apply_feedback(state.draft or "", state.critique or "")
        return state

    g.add_node("research", do_research)
    g.add_node("analysis", do_analysis)
    g.add_node("write", do_write)
    g.add_node("critique", do_critique)
    g.add_node("revise", revise_loop)

    g.set_entry_point("research")
    g.add_edge("research", "analysis")
    g.add_edge("analysis", "write")
    g.add_edge("write", "critique")

    g.add_conditional_edges("critique", need_more_refine, {True: "revise", False: END})
    g.add_edge("revise", "critique")
    return g.compile()

