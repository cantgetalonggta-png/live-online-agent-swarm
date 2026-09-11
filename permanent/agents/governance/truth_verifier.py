"""TruthVerifier — full Bayesian ACH + SOLID/MAYBE mapping."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

try:
    from utils.bayesian import run_ach, matrix_to_dict, confidence_to_claim_status, best_hypothesis
    HAS_BAYES = True
except Exception:
    HAS_BAYES = False

class TruthVerifierAgent(BaseAgent):
    plane = "governance"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        claim = task.get("claim", "")
        sources = task.get("sources", [])
        evidence_items = task.get("evidence_items")
        self.log(f"Verify ACH: {claim[:100]}")

        if HAS_BAYES:
            # Enrich evidence from sources if provided
            if not evidence_items and sources:
                evidence_items = [
                    {
                        "id": f"S{i+1}",
                        "description": f"Public source: {s}",
                        "source": s,
                        "likelihood_if_h": 0.75,
                        "likelihood_if_not_h": 0.35,
                        "quality": 0.7,
                    }
                    for i, s in enumerate(sources[:6])
                ]
            matrix = run_ach(claim, evidence_items=evidence_items)
            payload = matrix_to_dict(matrix)
            tag = payload.get("claim_status", "MAYBE")
            conf = best_hypothesis(matrix).posterior
        else:
            conf = 0.5 if sources else 0.3
            tag = "MAYBE" if conf < 0.8 else "SOLID"
            payload = {"claim": claim, "method": "fallback", "note": "bayesian module missing"}

        c = self.vault.add_claim(
            text=claim,
            status=tag,
            sources=sources or ["swarm:ach"],
            agent=self.name,
            confidence=float(conf),
        )
        return {
            "status": "ok",
            "claim": claim,
            "tag": tag,
            "confidence": round(float(conf), 4),
            "method": "ACH-bayesian" if HAS_BAYES else "fallback",
            "ach": payload,
            "claim_hash": c.hash,
            "live": True,
        }
