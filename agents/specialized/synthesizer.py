"""
Synthesizer — final report assembly (learn-and-lay-it-out + research-automation dissemination).
"""
from typing import Any, Dict
from agents.base import BaseAgent
from utils.directives import ClaimStatus

class SynthesizerAgent(BaseAgent):
    def __init__(self, monitor, vault):
        super().__init__("Synthesizer", monitor, vault)

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("synthesizing")
        goal = task.get("goal", "")
        collected = task.get("collected", {})
        snap = task.get("vault_snapshot", {})

        self.log("Assembling structured intelligence report")

        report = {
            "title": f"Swarm Report: {goal}",
            "executive_summary": (
                "Parallel agents collected public-surface signals. "
                "All claims tagged SOLID/MAYBE. HITL required before dissemination."
            ),
            "collection_results": {k: (v.get("status") if isinstance(v, dict) else str(v)) for k, v in collected.items()},
            "memory": snap,
            "confidence_note": "Most findings currently MAYBE — primary source confirmation needed",
            "next_steps": [
                "Human review of all MAYBE claims",
                "Run TruthVerifier on high-value claims",
                "Expand collection with Wayback / dorks if authorized",
                "Update MemoryVault with confirmed SOLID items"
            ],
            "absolute_rules_observed": self.config.absolute_rules
        }

        self.set_status("idle")
        return {"status": "report_ready", "report": report}
