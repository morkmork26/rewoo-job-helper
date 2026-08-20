from langgraph.graph import StateGraph, START, END
from .state import ReWooState
from .planner import planner
from .executor import executor
from .solver import solver


def build_graph():
    """Builds the ReWoo agent graph: Plan -> Execute -> Solve."""
    builder = StateGraph(ReWooState)

    builder.add_node("planner", planner)
    builder.add_node("executor", executor)
    builder.add_node("solver", solver)

    builder.add_edge(START, "planner")
    builder.add_edge("planner", "executor")
    builder.add_edge("executor", "solver")
    builder.add_edge("solver", END)

    return builder.compile()
