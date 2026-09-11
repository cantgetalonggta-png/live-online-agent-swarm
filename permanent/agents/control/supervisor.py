"""Supervisor — permanent orchestrator; never bypassed."""
from __future__ import annotations
import asyncio
from typing import Any, Dict, List
from agents.base import BaseAgent
from utils.directives import require_hitl

class SupervisorAgent(BaseAgent):
    plane = "control"

    def __init__(self, monitor, vault, specialists: Dict[str, BaseAgent]):
        super().__init__("Supervisor", monitor, vault)
        self.specialists = specialists

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        if not self.config.permanent_swarm:
            self.monitor.raise_flag("policy", "permanent_swarm disabled", "crit")
        if not self.config.never_bypass_supervisor:
            self.monitor.raise_flag("policy", "bypass allowed (unexpected)", "warn")

        goal = task.get("goal", "No goal provided")
        self.log(f"Supervisor permanent run: {goal[:160]}")
        results: Dict[str, Any] = {}

        async def _run(name: str, payload: Dict[str, Any]):
            agent = self.specialists.get(name)
            if not agent:
                return name, {"status": "missing", "agent": name}
            return name, await agent.run(payload)

        # 1 Compliance gate
        results["Compliance"] = (await _run("Compliance", {"action": "pre_check", "goal": goal}))[1]
        if not results["Compliance"].get("allowed", False):
            return {"status": "blocked", "reason": results["Compliance"].get("reason"), "results": results, "hitl": True}

        # 2 Overseer pre
        results["Overseer_pre"] = (await _run("Overseer", {"phase": "pre", "goal": goal}))[1]
        if results["Overseer_pre"].get("status") == "blocked":
            return {"status": "blocked", "reason": "overseer", "results": results}

        # 3 Arm FlagMonitor + SelfMetrics start
        results["FlagMonitor_arm"] = (await _run("FlagMonitor", {"action": "arm"}))[1]
        results["SelfMetrics_start"] = (await _run("SelfMetrics", {"phase": "start"}))[1]

        # 4 Planner
        plan_out = (await _run("Planner", {"goal": goal}))[1]
        results["Planner"] = plan_out
        plan = plan_out.get("plan", {})

        # 5 Parallel work plane
        parallel = plan.get("parallel_work", [])[: self.config.max_parallel_work]
        work_coros = []
        work_names: List[str] = []
        for step in parallel:
            an = step["agent"]
            if an in self.specialists:
                work_coros.append(self.specialists[an].run(step.get("task", {})))
                work_names.append(an)
        if work_coros:
            collected = await asyncio.gather(*work_coros, return_exceptions=True)
            for i, res in enumerate(collected):
                name = work_names[i]
                results[name] = res if not isinstance(res, Exception) else {"status": "failed", "error": str(res)}

        # 6 Sequential governance/memory/teach/synth
        for name in plan.get("sequential", ["TruthVerifier", "MemoryVault", "Teacher", "Synthesizer", "Auditor"]):
            if name == "TruthVerifier":
                payload = {"claim": goal, "query": goal, "sources": ["swarm:goal"]}
            elif name == "MemoryVault":
                payload = {"action": "snapshot"}
            elif name == "Teacher":
                payload = {"goal": goal, "collected": {k: results[k] for k in work_names if k in results}}
            elif name == "Synthesizer":
                payload = {"goal": goal, "collected": results, "vault_snapshot": self.vault.snapshot()}
            elif name == "Auditor":
                payload = {"action": "seal", "goal": goal, "results_keys": list(results.keys())}
            else:
                payload = {"goal": goal}
            results[name] = (await _run(name, payload))[1]

        # 7 Healer post-scan
        results["Healer"] = (await _run("Healer", {"results": results}))[1]

        # 8 Flag scan + metrics end + Overseer post
        results["FlagMonitor_scan"] = (await _run("FlagMonitor", {"action": "scan"}))[1]
        results["SelfMetrics_end"] = (await _run("SelfMetrics", {"phase": "end"}))[1]
        results["Overseer_post"] = (await _run("Overseer", {"phase": "post", "goal": goal}))[1]

        if self.config.hitl_required:
            results["hitl_notice"] = require_hitl("final dissemination of findings")

        return {
            "status": "completed",
            "goal": goal,
            "permanent_swarm": True,
            "results": results,
            "memory_snapshot": self.vault.snapshot(),
            "claims": self.vault.all_claims(),
            "health": self.monitor.health(),
        }
