#!/usr/bin/env python3
"""Permanent Agent Swarm CLI — always multi-agent."""
from __future__ import annotations
import argparse
import asyncio
import json
import sys
from pathlib import Path

# Ensure imports resolve
sys.path.insert(0, str(Path(__file__).resolve().parent))

from agents.permanent_runtime import build_permanent_swarm

async def amain(goal: str):
    swarm = build_permanent_swarm()
    print(json.dumps(swarm.roster(), indent=2))
    print("--- running permanent swarm ---")
    result = await swarm.run(goal)
    print(json.dumps(result, indent=2, default=str))
    return result

def main():
    p = argparse.ArgumentParser(description="Permanent always-on agent swarm")
    p.add_argument("goal", nargs="?", default="Map public FOIA response deadlines")
    p.add_argument("--roster", action="store_true", help="Print roster only")
    args = p.parse_args()
    if args.roster:
        swarm = build_permanent_swarm()
        print(json.dumps(swarm.roster(), indent=2))
        return
    asyncio.run(amain(args.goal))

if __name__ == "__main__":
    main()
