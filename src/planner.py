from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(model="gpt-4.1", temperature=0)

PLANNER_PROMPT = """You are a task planner. Given a user task, decompose it into a numbered list of subtasks.
Each subtask should specify:
- step_id: sequential number
- tool: which tool to use (web_search or file_reader)
- input: what to pass to the tool
- dependency: which previous step_id result this depends on (or null)

Return as a JSON array of objects."""


def planner(state: dict) -> dict:
    """Decomposes the task into a plan of subtasks."""
    response = llm.invoke([
        SystemMessage(content=PLANNER_PROMPT),
        HumanMessage(content=f"Task: {state['task']}")
    ])
    import json
    try:
        plan = json.loads(response.content)
    except json.JSONDecodeError:
        plan = [{"step_id": 1, "tool": "web_search", "input": state["task"], "dependency": None}]
    return {"plan": plan, "results": {}}
