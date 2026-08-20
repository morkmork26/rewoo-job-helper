# ReWoo Job-Helper Agent

A planning-first AI agent using the ReWoo (Reasoning Without Observation) architecture. Unlike ReAct which interleaves reasoning and action, ReWoo plans all steps upfront, executes them in batch, then synthesizes results.

## Architecture

```
START → Planner → Executor → Solver → END
```

**Nodes:**
- `planner` - Decomposes the task into ordered subtasks with tool assignments and dependencies
- `executor` - Executes all planned subtasks sequentially, respecting dependencies
- `solver` - Synthesizes all results into a comprehensive final answer

**Advantages over ReAct:**
- Fewer LLM calls (plan once, execute all, synthesize once)
- Predictable execution flow
- Lower cost and latency for multi-step tasks

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
python -m src.main
```
