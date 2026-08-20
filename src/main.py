from dotenv import load_dotenv
from .graph import build_graph

load_dotenv()


def run():
    graph = build_graph()
    result = graph.invoke({
        "task": "Find 3 entry-level data analyst jobs in New York and summarize requirements",
        "plan": [],
        "results": {},
        "final_answer": "",
    })
    print("\n--- Final Answer ---\n")
    print(result["final_answer"])


if __name__ == "__main__":
    run()
