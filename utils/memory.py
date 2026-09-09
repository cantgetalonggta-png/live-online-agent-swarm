"""
MemoryVault — durable shared state for the swarm.
Integrates GraphRAG (RedisGraph-compatible) for hybrid retrieval.
"""
from typing import Dict, List, Optional, Any
from utils.directives import Claim, ClaimStatus
from utils.graph_rag import get_graph_rag
from datetime import datetime


class MemoryVault:
    def __init__(self):
        self.claims: Dict[str, Claim] = {}
        self.timeline: List[dict] = []
        self.entities: Dict[str, dict] = {}
        self.logs: List[str] = []
        self.graph = get_graph_rag()
        self.verification_history: List[dict] = []

    def store_claim(self, claim: Claim) -> str:
        claim.provenance_hash = claim.compute_hash()
        self.claims[claim.provenance_hash] = claim
        self.logs.append(
            f"[{datetime.utcnow().isoformat()}] Stored {claim.status}: {claim.text[:80]}..."
        )
        # Mirror into Graph RAG
        try:
            self.graph.add_claim_node(
                claim.provenance_hash,
                claim.text,
                claim.status.value if hasattr(claim.status, "value") else str(claim.status),
                claim.confidence,
                claim.sources or [],
            )
        except Exception as e:
            self.logs.append(f"[graph] store error: {e}")
        return claim.provenance_hash

    def store_verification(self, ach_dict: dict) -> None:
        self.verification_history.append(ach_dict)
        self.logs.append(f"[{datetime.utcnow().isoformat()}] ACH verification stored for claim")

    def query(self, keyword: str) -> List[Claim]:
        return [c for c in self.claims.values() if keyword.lower() in c.text.lower()]

    def rag_query(self, query: str, top_k: int = 5) -> dict:
        return self.graph.hybrid_query(query, top_k=top_k)

    def add_document(self, doc_id: str, title: str, source: str, chunks: List[str], meta: Optional[dict] = None):
        return self.graph.add_document(doc_id, title, source, chunks, meta)

    def add_timeline_event(
        self,
        date: str,
        event: str,
        sources: List[str],
        status: ClaimStatus = ClaimStatus.MAYBE,
    ):
        self.timeline.append(
            {
                "date": date,
                "event": event,
                "sources": sources,
                "status": status.value if hasattr(status, "value") else status,
                "recorded": datetime.utcnow().isoformat(),
            }
        )
        self.timeline.sort(key=lambda x: x["date"])

    def snapshot(self) -> dict:
        return {
            "claim_count": len(self.claims),
            "timeline_events": len(self.timeline),
            "entities": len(self.entities),
            "verifications": len(self.verification_history),
            "graph": self.graph.stats(),
            "recent_logs": self.logs[-10:],
        }

    def all_claims(self) -> List[dict]:
        out = []
        for h, c in self.claims.items():
            out.append(
                {
                    "hash": h,
                    "text": c.text,
                    "status": c.status.value if hasattr(c.status, "value") else str(c.status),
                    "confidence": c.confidence,
                    "sources": c.sources,
                    "agent": c.agent,
                    "notes": c.notes,
                    "created_at": c.created_at.isoformat() if c.created_at else None,
                }
            )
        return out
