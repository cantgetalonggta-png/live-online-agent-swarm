"""
Synthesizer — final report assembly.
Uses LLM when keys present; otherwise deterministic template summary.
"""
from typing import Any, Dict
from agents.base import BaseAgent
from utils.llm_client import get_llm


class SynthesizerAgent(BaseAgent):
    def __init__(self, monitor, vault):
        super().__init__("Synthesizer", monitor, vault)

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("synthesizing")
        goal = task.get("goal") or task.get("query") or ""
        claims = []
        try:
            claims = self.vault.all_claims()[:15]
        except Exception:
            pass
        claim_lines = []
        for c in claims:
            if isinstance(c, dict):
                claim_lines.append(f"- [{c.get('status')}] {c.get('text','')[:160]}")
            else:
                claim_lines.append(f"- {str(c)[:160]}")

        base = (
            f"## Investigation synthesis\nGoal: {goal}\n\n"
            f"Claims ({len(claim_lines)}):\n" + ("\n".join(claim_lines) or "- none yet") +
            "\n\nRules: public-record only · SOLID/MAYBE · HITL for irreversible.\n"
        )

        llm = get_llm()
        llm_text = None
        if llm.is_available() and goal:
            prompt = (
                f"Synthesize a concise lawful public-record investigation brief.\n"
                f"Goal: {goal}\nExisting claims:\n" + "\n".join(claim_lines[:12]) +
                "\n\nOutput: executive summary, SOLID vs MAYBE split, next public-record actions. No private data."
            )
            llm_text = llm.complete(prompt, max_tokens=700)

        self.set_status("idle")
        return {
            "status": "ok",
            "goal": goal,
            "summary": llm_text or base,
            "llm_used": bool(llm_text),
            "llm_status": llm.status(),
            "claim_count": len(claim_lines),
        }
