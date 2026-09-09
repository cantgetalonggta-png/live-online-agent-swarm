"""
Truth Verifier — full Bayesian + ACH from truth-verification skill.
"""
from typing import Any, Dict, List, Optional
from agents.base import BaseAgent
from utils.directives import Claim, ClaimStatus
from utils.bayesian import run_ach, matrix_to_dict, best_hypothesis, confidence_to_claim_status


class TruthVerifierAgent(BaseAgent):
    def __init__(self, monitor, vault):
        super().__init__("TruthVerifier", monitor, vault)

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("verifying")
        claim_text = task.get("claim") or task.get("query") or ""
        evidence_items: Optional[List[dict]] = task.get("evidence")
        hyp_texts: Optional[List[str]] = task.get("hypotheses")

        # Pull related vault context via Graph RAG if available
        rag_context = []
        try:
            rag = self.vault.rag_query(claim_text, top_k=3)
            for r in rag.get("results", []):
                rag_context.append(
                    {
                        "id": r.get("chunk_id", "rag"),
                        "description": r.get("text", "")[:200],
                        "source": r.get("source", "graph_rag"),
                        "likelihood_if_h": min(0.85, 0.5 + float(r.get("score", 0.3)) * 0.4),
                        "likelihood_if_not_h": max(0.15, 0.5 - float(r.get("score", 0.3)) * 0.3),
                        "quality": min(0.9, 0.5 + float(r.get("score", 0.3)) * 0.4),
                    }
                )
        except Exception:
            pass

        if rag_context and not evidence_items:
            evidence_items = rag_context

        self.log(f"Running Bayesian ACH on: {claim_text[:70]}...")

        matrix = run_ach(claim_text, hyp_texts=hyp_texts, evidence_items=evidence_items)
        result = matrix_to_dict(matrix)
        best = best_hypothesis(matrix)
        status_str = confidence_to_claim_status(best.posterior)

        try:
            status_enum = ClaimStatus(status_str)
        except ValueError:
            status_enum = ClaimStatus.MAYBE

        c = Claim(
            text=claim_text or "Verification of collected claims",
            status=status_enum,
            sources=task.get("sources", ["internal:Bayesian-ACH"]) + [e.source for e in matrix.evidence if e.source.startswith("http")],
            confidence=round(best.posterior, 4),
            agent=self.name,
            notes=f"Best H: {best.text} (posterior={best.posterior:.3f})",
        )
        h = self.vault.store_claim(c)
        self.vault.store_verification(result)

        self.set_status("idle")
        return {
            "status": "verified",
            "claim_hash": h,
            "final_status": status_str,
            "confidence": round(best.posterior, 4),
            "ach": result,
            "rag_used": len(rag_context) > 0,
        }
