#!/usr/bin/env python3
"""
Live Online Agent Swarm — CLI entry point.
  python main.py "your goal"
  python main.py --api          # start FastAPI :8000
  python main.py --dashboard    # hint for streamlit
"""
import asyncio
import sys
import json

from swarm_runtime import get_runtime
from swarm_config import config


async def main(goal: str):
    print("=" * 60)
    print(f"  {config.name} v{config.version}")
    print("  Bayesian ACH · RedisGraph RAG · HITL · Public-record ceiling")
    print("=" * 60)
    print(f"Goal: {goal}\n")

    supervisor, monitor, vault = get_runtime()
    result = await supervisor.run({"goal": goal})

    print("\n" + "=" * 60)
    print("  FINAL SWARM OUTPUT")
    print("=" * 60)
    print(json.dumps(result, indent=2, default=str))
    return result


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--api" in args:
        import uvicorn
        print("Starting FastAPI on http://0.0.0.0:8000  (docs: /docs)")
        uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=False)
    elif "--dashboard" in args:
        print("Run:  streamlit run dashboard/app.py --server.port 8501 --server.address 0.0.0.0")
        sys.exit(0)
    else:
        goal = " ".join(a for a in args if not a.startswith("--")) or (
            "Map public records on open government transparency initiatives"
        )
        asyncio.run(main(goal))
