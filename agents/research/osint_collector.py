"""
OSINT Collector — public-data only, from osint-rag-master + ethical-data-harvesting.
"""
from typing import Any, Dict
from agents.base import BaseAgent
from utils.directives import Claim, ClaimStatus, enforce_public_record

class OSINTCollectorAgent(BaseAgent):
    def __init__(self, monitor, vault):
        super().__init__("OSINTCollector", monitor, vault)

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("collecting")
        query = task.get("query", "")
        self.log(f"Collecting public sources for: {query}")

        # Simulated public collection (in live system would call web_search / dorks / archives)
        # Here we return structured placeholder with provenance discipline
        demo_claims = [
            Claim(
                text=f"Public search surface for '{query}' contains open records and news",
                status=ClaimStatus.MAYBE,
                sources=["https://example-public-search.org/results", "https://web.archive.org/"],
                confidence=0.6,
                agent=self.name,
                notes="Placeholder — replace with live ethical harvest"
            )
        ]

        stored = []
        for c in demo_claims:
            if enforce_public_record(c):
                h = self.vault.store_claim(c)
                stored.append(h)
            else:
                self.log(f"Rejected non-public claim: {c.text[:50]}")

        self.set_status("idle")
        return {
            "status": "ok",
            "query": query,
            "claims_stored": stored,
            "count": len(stored),
            "note": "Live mode would use search_techniques_master + ethical-scraper-orchestration"
        }
