"""
OSINT Collector — public-data only.
Uses Tavily when TAVILY_API_KEY is set; otherwise structured placeholder.
"""
from typing import Any, Dict
from agents.base import BaseAgent
from utils.directives import Claim, ClaimStatus, enforce_public_record
from utils.tavily_client import get_tavily


class OSINTCollectorAgent(BaseAgent):
    def __init__(self, monitor, vault):
        super().__init__("OSINTCollector", monitor, vault)

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("collecting")
        query = task.get("query") or task.get("goal") or ""
        self.log(f"Collecting public sources for: {query}")

        tavily = get_tavily()
        search = tavily.search(query, max_results=5) if query else {"results": [], "status": "no_query"}
        stored = []
        claims_out = []

        if search.get("status") == "ok" and search.get("results"):
            for r in search["results"][:5]:
                url = r.get("url") or ""
                title = r.get("title") or ""
                snippet = (r.get("content") or "")[:300]
                c = Claim(
                    text=f"Public source: {title} — {snippet}",
                    status=ClaimStatus.MAYBE,
                    sources=[url] if url else ["tavily:unknown"],
                    confidence=min(0.75, 0.45 + float(r.get("score") or 0.3) * 0.4),
                    agent=self.name,
                    notes="Tavily public search hit — verify before SOLID",
                )
                if enforce_public_record(c):
                    h = self.vault.store_claim(c)
                    stored.append(h)
                    claims_out.append(c.text[:120])
                # ingest snippet for RAG
                try:
                    if url and snippet:
                        self.vault.add_document(
                            doc_id=f"tavily-{abs(hash(url)) % 10**10}",
                            title=title or url,
                            source=url,
                            chunks=[snippet],
                            meta={"provider": "tavily", "public_record_only": True},
                        )
                except Exception:
                    pass
        else:
            # Offline / no-key placeholder with provenance discipline
            c = Claim(
                text=f"Public search surface for '{query}' (Tavily offline or no key) — use vault ACRIS/public records",
                status=ClaimStatus.MAYBE,
                sources=["internal:osint-offline"],
                confidence=0.4,
                agent=self.name,
                notes=search.get("note") or search.get("status") or "offline",
            )
            if enforce_public_record(c):
                h = self.vault.store_claim(c)
                stored.append(h)

        self.set_status("idle")
        return {
            "status": "ok",
            "query": query,
            "tavily": search.get("status"),
            "claims_stored": stored,
            "count": len(stored),
            "samples": claims_out[:3],
        }
