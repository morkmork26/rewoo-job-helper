from typing import TypedDict


class ReWooState(TypedDict):
    task: str
    plan: list[dict]
    results: dict
    final_answer: str
