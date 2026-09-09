"""
FastAPI live backend for the Investigation Swarm.
Endpoints: run swarm, verify claim (Bayesian ACH), Graph RAG query, health, claims.
"""
from __future__ import annotations
import sys
from pathlib import Path

# Allow imports from project root
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
import asyncio

from swarm_runtime import get_runtime
from utils.bayesian import run_ach, matrix_to_dict
from swarm_config import config

app = FastAPI(
    title="Live Online Investigation Swarm API",
    description="Bayesian ACH · RedisGraph RAG · Multi-agent Supervisor · HITL",
    version=config.version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GoalRequest(BaseModel):
    goal: str = Field(..., min_length=3, description="Investigation goal / question")


class VerifyRequest(BaseModel):
    claim: str
    evidence: Optional[List[Dict[str, Any]]] = None
    hypotheses: Optional[List[str]] = None
    sources: Optional[List[str]] = None


class RAGRequest(BaseModel):
    query: str
    top_k: int = 5


class DocIngest(BaseModel):
    doc_id: str
    title: str
    source: str
    chunks: List[str]
    meta: Optional[Dict[str, Any]] = None


@app.get("/")
def root():
    return {
        "name": config.name,
        "version": config.version,
        "docs": "/docs",
        "dashboard_hint": "streamlit run dashboard/app.py",
        "absolute_rules": config.absolute_rules,
    }


@app.get("/health")
def health():
    _, monitor, vault = get_runtime()
    return {
        "status": "ok",
        "swarm": monitor.health(),
        "memory": vault.snapshot(),
        "config": {
            "hitl_required": config.hitl_required,
            "public_record_ceiling": config.public_record_ceiling,
            "roles": config.roles,
        },
    }


@app.post("/swarm/run")
async def swarm_run(req: GoalRequest):
    supervisor, _, _ = get_runtime()
    try:
        result = await supervisor.run({"goal": req.goal})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/verify")
async def verify_claim(req: VerifyRequest):
    """Direct Bayesian ACH verification (also stores in vault + graph)."""
    _, _, vault = get_runtime()
    # Enrich with RAG
    evidence = list(req.evidence or [])
    try:
        rag = vault.rag_query(req.claim, top_k=3)
        for r in rag.get("results", []):
            evidence.append(
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

    matrix = run_ach(req.claim, hyp_texts=req.hypotheses, evidence_items=evidence or None)
    result = matrix_to_dict(matrix)
    vault.store_verification(result)

    from utils.directives import Claim, ClaimStatus
    from utils.bayesian import confidence_to_claim_status, best_hypothesis

    best = best_hypothesis(matrix)
    status_str = confidence_to_claim_status(best.posterior)
    try:
        st = ClaimStatus(status_str)
    except ValueError:
        st = ClaimStatus.MAYBE
    c = Claim(
        text=req.claim,
        status=st,
        sources=req.sources or ["api:/verify"],
        confidence=round(best.posterior, 4),
        agent="API-TruthVerifier",
        notes=f"Best: {best.text}",
    )
    h = vault.store_claim(c)
    result["claim_hash"] = h
    return result


@app.post("/rag/query")
def rag_query(req: RAGRequest):
    _, _, vault = get_runtime()
    return vault.rag_query(req.query, top_k=req.top_k)


@app.post("/rag/ingest")
def rag_ingest(doc: DocIngest):
    _, _, vault = get_runtime()
    vault.add_document(doc.doc_id, doc.title, doc.source, doc.chunks, doc.meta)
    return {"status": "ingested", "doc_id": doc.doc_id, "chunks": len(doc.chunks), "graph": vault.graph.stats()}


@app.get("/claims")
def list_claims():
    _, _, vault = get_runtime()
    return {"claims": vault.all_claims(), "count": len(vault.claims)}


@app.get("/graph/stats")
def graph_stats():
    _, _, vault = get_runtime()
    return vault.graph.stats()


@app.get("/graph/cypher")
def graph_cypher(pattern: str = "MATCH (c:Claim) RETURN c LIMIT 20"):
    _, _, vault = get_runtime()
    return {"pattern": pattern, "results": vault.graph.cypher_like(pattern)}


@app.get("/verifications")
def list_verifications():
    _, _, vault = get_runtime()
    return {"verifications": vault.verification_history[-20:], "count": len(vault.verification_history)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=False)
