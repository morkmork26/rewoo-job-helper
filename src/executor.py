from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def web_search(query: str) -> str:
    """Executes a web search using GPT-4o search preview."""
    completion = client.chat.completions.create(
        model="gpt-4o-search-preview",
        web_search_options={"search_context_size": "medium"},
        messages=[{"role": "user", "content": query}],
    )
    return completion.choices[0].message.content


def file_reader(file_path: str) -> str:
    """Reads and returns file contents."""
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"


TOOLS = {"web_search": web_search, "file_reader": file_reader}


def executor(state: dict) -> dict:
    """Executes each step in the plan sequentially."""
    results = dict(state.get("results", {}))
    for step in state["plan"]:
        tool_name = step["tool"]
        tool_input = step["input"]
        if step.get("dependency"):
            dep_result = results.get(str(step["dependency"]), "")
            tool_input = f"{tool_input}\nContext: {dep_result}"
        tool_fn = TOOLS.get(tool_name, web_search)
        results[str(step["step_id"])] = tool_fn(tool_input)
    return {"results": results}
