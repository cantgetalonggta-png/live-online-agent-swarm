#!/usr/bin/env python3
"""
Live Online Agent Swarm — entry point.
Run: python main.py "your investigation goal here"
"""
import asyncio
import sys
import json
from utils.monitor import SwarmMonitor
from utils.memory import MemoryVault
from agents import (
    SupervisorAgent,
    OSINTCollectorAgent,
    TruthVerifierAgent,
    LiveWebScoutAgent,
    MemoryVaultAgent,
    ComplianceAgent,
    PatternAgent,
    AnticipationAgent,
    SynthesizerAgent,
)
from swarm_config import config

async def build_swarm():
    monitor = SwarmMonitor()
    vault = MemoryVault()

    specialists = {
        "Compliance": ComplianceAgent(monitor, vault),
        "OSINTCollector": OSINTCollectorAgent(monitor, vault),
        "LiveWebScout": LiveWebScoutAgent(monitor, vault),
        "Pattern": PatternAgent(monitor, vault),
        "TruthVerifier": TruthVerifierAgent(monitor, vault),
        "MemoryVault": MemoryVaultAgent(monitor, vault),
        "Anticipation": AnticipationAgent(monitor, vault),
        "Synthesizer": SynthesizerAgent(monitor, vault),
    }

    supervisor = SupervisorAgent(monitor, vault, specialists)
    return supervisor, monitor, vault

async def main(goal: str):
    print("=" * 60)
    print(f"  {config.name} v{config.version}")
    print("  Public-record ceiling · HITL enforced · SOLID/MAYBE discipline")
    print("=" * 60)
    print(f"Goal: {goal}\n")

    supervisor, monitor, vault = await build_swarm()
    result = await supervisor.run({"goal": goal})

    print("\n" + "=" * 60)
    print("  FINAL SWARM OUTPUT")
    print("=" * 60)
    print(json.dumps(result, indent=2, default=str))
    return result

if __name__ == "__main__":
    goal = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Map public records on a current open investigation topic"
    asyncio.run(main(goal))
