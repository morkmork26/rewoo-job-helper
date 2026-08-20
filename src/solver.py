from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(model="gpt-4.1", temperature=0)

SOLVER_PROMPT = """You are a synthesis agent. Given the original task and results from executed subtasks,
produce a comprehensive final answer that addresses the user's original request."""


def solver(state: dict) -> dict:
    """Synthesizes all results into a final answer."""
    context = "\n\n".join(
        f"Step {k} result:\n{v[:2000]}" for k, v in state["results"].items()
    )
    response = llm.invoke([
        SystemMessage(content=SOLVER_PROMPT),
        HumanMessage(content=f"Original task: {state['task']}\n\nResults:\n{context}")
    ])
    return {"final_answer": response.content}
