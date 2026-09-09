"""
Truth Verifier — Bayesian / ACH from truth-verification skill.
"""
from typing import Any, Dict
from agents.base import BaseAgent
from utils.directives import Claim, ClaimStatus

class TruthVerifierAgent(BaseAgent):
    def __init__(self, monitor, vault):
        super().__init__("TruthVerifier", monitor, vault)

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("verifying")
        claim_text = task.get("claim", task.get("query", ""))
        self.log(f"Running ACH / Bayesian check on: {claim_text[:60]}...")

        # Simplified ACH: list hypotheses, score consistency (demo)
        hypotheses = [
            {"h": "Claim is accurate and well-sourced", "consistency": 0.55},
            {"h": "Claim is partially true but incomplete", "consistency": 0.70},
            {"h": "Claim is contradicted by stronger evidence", "consistency": 0.30},
        ]
        best = max(hypotheses, key=lambda x: x["consistency"])

        status = ClaimStatus.MAYBE
        if best["consistency"] > 0.8:
            status = ClaimStatus.SOLID
        elif best["consistency"] < 0.4:
            status = ClaimStatus.CONTESTED

        c = Claim(
            text=claim_text or "Verification of collected claims",
            status=status,
            sources=task.get("sources", ["internal:ACH"]),
            confidence=best["consistency"],
            agent=self.name,
            notes=f"Best hypothesis: {best['h']}"
        )
        h = self.vault.store_claim(c)

        self.set_status("idle")
        return {
            "status": "verified",
            "claim_hash": h,
            "final_status": status.value,
            "confidence": best["consistency"],
            "hypotheses": hypotheses
        }
