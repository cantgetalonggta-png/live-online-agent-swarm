"""
Supervisor / Orchestrator Agent
Decomposes goals, assigns specialists, reviews, synthesizes.
Default pattern from multi-agent-patterns skill.
"""
import asyncio
from typing import Any, Dict, List
from agents.base import BaseAgent
from utils.directives import Claim, ClaimStatus, require_hitl

class SupervisorAgent(BaseAgent):
    def __init__(self, monitor, vault, specialists: Dict[str, BaseAgent]):
        super().__init__("Supervisor", monitor, vault)
        self.specialists = specialists

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("orchestrating")
        goal = task.get("goal", "No goal provided")
        self.log(f"Received goal: {goal}")

        # 1. Compliance gate first
        compliance = self.specialists.get("Compliance")
        if compliance:
            gate = await compliance.run({"action": "pre_check", "goal": goal})
            if not gate.get("allowed", False):
                self.log("Compliance blocked the request.")
                return {"status": "blocked", "reason": gate.get("reason"), "hitl": True}

        # 2. Plan (simple sequential + parallel fan-out)
        plan = self._decompose(goal)
        self.log(f"Plan: {plan}")

        results = {}
        # Parallel collection phase
        collection_tasks = []
        for step in plan.get("parallel", []):
            agent_name = step["agent"]
            if agent_name in self.specialists:
                collection_tasks.append(self.specialists[agent_name].run(step["task"]))
        
        if collection_tasks:
            collected = await asyncio.gather(*collection_tasks, return_exceptions=True)
            for i, res in enumerate(collected):
                agent_name = plan["parallel"][i]["agent"]
                results[agent_name] = res if not isinstance(res, Exception) else {"error": str(res)}

        # Sequential synthesis
        if "Synthesizer" in self.specialists:
            synth_input = {"goal": goal, "collected": results, "vault_snapshot": self.vault.snapshot()}
            results["Synthesizer"] = await self.specialists["Synthesizer"].run(synth_input)

        # Final HITL check if required
        if self.config.hitl_required:
            results["hitl_notice"] = require_hitl("final dissemination of findings")

        self.set_status("idle")
        self.log("Orchestration complete.")
        return {
            "status": "completed",
            "goal": goal,
            "results": results,
            "memory_snapshot": self.vault.snapshot(),
            "health": self.monitor.health()
        }

    def _decompose(self, goal: str) -> dict:
        """Simple rule-based decomposition. In production use LLM planner."""
        return {
            "parallel": [
                {"agent": "OSINTCollector", "task": {"query": goal, "mode": "public_search"}},
                {"agent": "LiveWebScout", "task": {"query": goal, "mode": "live"}},
                {"agent": "Pattern", "task": {"query": goal}},
            ],
            "sequential": ["TruthVerifier", "MemoryVault", "Synthesizer"]
        }
