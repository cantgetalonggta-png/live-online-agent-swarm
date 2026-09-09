"""
RedisGraph-compatible Hybrid Graph RAG
Schema (integrity skill style):
  (:Document)-[:HAS_CHUNK]->(:Chunk)-[:MENTIONS]->(:Entity)
  (:Claim)-[:SUPPORTED_BY|CONTRADICTED_BY]->(:Evidence)
  (:Entity)-[:RELATED_TO]->(:Entity)

Uses:
  - Redis (if REDIS_URL available) for key-value + optional RedisGraph Cypher
  - networkx in-memory graph always as source of truth / fallback
  - sklearn TF-IDF + cosine for vector retrieval (no heavy embedding model required)
"""
from __future__ import annotations
import os
import json
import hashlib
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
from collections import defaultdict

import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

try:
    import redis
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False


class GraphRAG:
    """
    Hybrid Graph + Vector RAG with Redis persistence option.
    """

    def __init__(self, redis_url: Optional[str] = None):
        self.redis_url = redis_url or os.getenv("REDIS_URL", "")
        self.redis = None
        self.redis_graph_available = False
        if HAS_REDIS and self.redis_url:
            try:
                self.redis = redis.from_url(self.redis_url, decode_responses=True)
                self.redis.ping()
                # Probe RedisGraph module
                try:
                    self.redis.execute_command("GRAPH.LIST")
                    self.redis_graph_available = True
                except Exception:
                    self.redis_graph_available = False
            except Exception:
                self.redis = None

        self.G = nx.MultiDiGraph()
        self.chunks: Dict[str, dict] = {}  # chunk_id -> {text, meta}
        self.vectorizer = TfidfVectorizer(max_features=4096, stop_words="english", ngram_range=(1, 2))
        self.tfidf_matrix = None
        self.chunk_ids_order: List[str] = []
        self._load_from_redis()

    # ── Persistence ──────────────────────────────────────────────
    def _load_from_redis(self):
        if not self.redis:
            return
        raw = self.redis.get("swarm:graph_rag:state")
        if raw:
            try:
                state = json.loads(raw)
                self.chunks = state.get("chunks", {})
                # rebuild graph edges
                for edge in state.get("edges", []):
                    self.G.add_edge(edge["u"], edge["v"], key=edge.get("key", 0), **edge.get("attr", {}))
                for n, attr in state.get("nodes", {}).items():
                    self.G.add_node(n, **attr)
                self._rebuild_index()
            except Exception:
                pass

    def save(self):
        if not self.redis:
            return
        edges = []
        for u, v, k, attr in self.G.edges(keys=True, data=True):
            edges.append({"u": u, "v": v, "key": k, "attr": dict(attr)})
        nodes = {n: dict(attr) for n, attr in self.G.nodes(data=True)}
        state = {"chunks": self.chunks, "edges": edges, "nodes": nodes, "saved_at": datetime.utcnow().isoformat()}
        self.redis.set("swarm:graph_rag:state", json.dumps(state, default=str))
        if self.redis_graph_available:
            self._sync_redis_graph()

    def _sync_redis_graph(self):
        """Best-effort Cypher mirror into RedisGraph (graph name: swarm)."""
        if not self.redis or not self.redis_graph_available:
            return
        try:
            # Clear & rebuild lightweight
            self.redis.execute_command("GRAPH.DELETE", "swarm")
        except Exception:
            pass
        # Create nodes/edges in batches via Cypher
        for n, attr in list(self.G.nodes(data=True))[:500]:
            labels = attr.get("labels", ["Node"])
            label = labels[0] if labels else "Node"
            props = {k: v for k, v in attr.items() if k != "labels" and isinstance(v, (str, int, float, bool))}
            props["id"] = n
            prop_str = ", ".join(f"{k}: '{str(v)[:200].replace(chr(39), '')}'" if isinstance(v, str) else f"{k}: {v}" for k, v in props.items())
            try:
                self.redis.execute_command("GRAPH.QUERY", "swarm", f"CREATE (:{label} {{{prop_str}}})")
            except Exception:
                continue

    # ── Ingest ───────────────────────────────────────────────────
    def _cid(self, text: str, prefix: str = "c") -> str:
        return f"{prefix}:{hashlib.sha256(text.encode()).hexdigest()[:12]}"

    def add_document(self, doc_id: str, title: str, source: str, chunks: List[str], meta: Optional[dict] = None) -> str:
        self.G.add_node(doc_id, labels=["Document"], title=title, source=source, **(meta or {}))
        for i, text in enumerate(chunks):
            if not text or not text.strip():
                continue
            chunk_id = self._cid(f"{doc_id}:{i}:{text}")
            self.chunks[chunk_id] = {
                "text": text,
                "doc_id": doc_id,
                "source": source,
                "title": title,
                "index": i,
                "meta": meta or {},
            }
            self.G.add_node(chunk_id, labels=["Chunk"], text=text[:200], source=source)
            self.G.add_edge(doc_id, chunk_id, relation="HAS_CHUNK")
        self._rebuild_index()
        self.save()
        return doc_id

    def add_claim_node(self, claim_hash: str, text: str, status: str, confidence: float, sources: List[str]):
        self.G.add_node(
            f"claim:{claim_hash}",
            labels=["Claim"],
            text=text[:300],
            status=status,
            confidence=confidence,
        )
        for s in sources:
            eid = self._cid(s, "src")
            self.G.add_node(eid, labels=["Source"], url=s)
            self.G.add_edge(f"claim:{claim_hash}", eid, relation="SUPPORTED_BY")
        # also as chunk for retrieval
        chunk_id = self._cid(text, "claimchunk")
        self.chunks[chunk_id] = {
            "text": text,
            "doc_id": f"claim:{claim_hash}",
            "source": sources[0] if sources else "internal",
            "title": f"Claim {status}",
            "index": 0,
            "meta": {"status": status, "confidence": confidence},
        }
        self._rebuild_index()
        self.save()

    def add_entity(self, name: str, entity_type: str = "Entity", mentioned_in: Optional[List[str]] = None):
        eid = f"entity:{name.lower().replace(' ', '_')}"
        self.G.add_node(eid, labels=["Entity"], name=name, entity_type=entity_type)
        for mid in mentioned_in or []:
            if mid in self.G or mid in self.chunks:
                self.G.add_edge(mid if mid.startswith("c:") or mid.startswith("claim:") else mid, eid, relation="MENTIONS")
        self.save()
        return eid

    def link_entities(self, a: str, b: str, relation: str = "RELATED_TO"):
        ea = f"entity:{a.lower().replace(' ', '_')}"
        eb = f"entity:{b.lower().replace(' ', '_')}"
        self.G.add_edge(ea, eb, relation=relation)
        self.save()

    # ── Index & retrieve ─────────────────────────────────────────
    def _rebuild_index(self):
        self.chunk_ids_order = list(self.chunks.keys())
        if not self.chunk_ids_order:
            self.tfidf_matrix = None
            return
        texts = [self.chunks[cid]["text"] for cid in self.chunk_ids_order]
        try:
            self.tfidf_matrix = self.vectorizer.fit_transform(texts)
        except ValueError:
            self.tfidf_matrix = None

    def vector_search(self, query: str, top_k: int = 5) -> List[dict]:
        if self.tfidf_matrix is None or not self.chunk_ids_order:
            return []
        q = self.vectorizer.transform([query])
        sims = cosine_similarity(q, self.tfidf_matrix).flatten()
        idx = np.argsort(sims)[::-1][:top_k]
        results = []
        for i in idx:
            if sims[i] <= 0:
                continue
            cid = self.chunk_ids_order[i]
            c = self.chunks[cid]
            results.append({
                "chunk_id": cid,
                "score": float(sims[i]),
                "text": c["text"],
                "source": c.get("source"),
                "title": c.get("title"),
                "meta": c.get("meta", {}),
            })
        return results

    def graph_neighbors(self, node_id: str, depth: int = 2) -> dict:
        if node_id not in self.G:
            # try claim / entity prefixes
            for prefix in ("claim:", "entity:", "c:"):
                if f"{prefix}{node_id}" in self.G:
                    node_id = f"{prefix}{node_id}"
                    break
            else:
                return {"node": node_id, "found": False, "neighbors": []}
        neighbors = []
        for u, v, attr in self.G.edges(node_id, data=True):
            neighbors.append({"from": u, "to": v, "relation": attr.get("relation", "RELATED")})
        # reverse
        for u, v, attr in self.G.in_edges(node_id, data=True):
            neighbors.append({"from": u, "to": v, "relation": attr.get("relation", "RELATED")})
        return {"node": node_id, "found": True, "neighbors": neighbors[:50], "node_data": dict(self.G.nodes[node_id])}

    def hybrid_query(self, query: str, top_k: int = 5) -> dict:
        """Vector + graph expansion (simple hybrid retriever)."""
        vec = self.vector_search(query, top_k=top_k)
        expanded = []
        seen = set()
        for hit in vec:
            expanded.append({**hit, "via": "vector"})
            seen.add(hit["chunk_id"])
            # expand via graph from doc
            doc_id = self.chunks.get(hit["chunk_id"], {}).get("doc_id")
            if doc_id and doc_id in self.G:
                for _, nbr, attr in list(self.G.edges(doc_id, data=True))[:3]:
                    if nbr in self.chunks and nbr not in seen:
                        c = self.chunks[nbr]
                        expanded.append({
                            "chunk_id": nbr,
                            "score": hit["score"] * 0.7,
                            "text": c["text"],
                            "source": c.get("source"),
                            "title": c.get("title"),
                            "meta": c.get("meta", {}),
                            "via": f"graph:{attr.get('relation', 'HAS_CHUNK')}",
                        })
                        seen.add(nbr)
        expanded.sort(key=lambda x: x["score"], reverse=True)
        return {
            "query": query,
            "results": expanded[: top_k * 2],
            "graph_stats": self.stats(),
            "backend": "redis+networkx" if self.redis else "networkx-only",
            "redis_graph": self.redis_graph_available,
        }

    def cypher_like(self, pattern: str = "MATCH (c:Claim) RETURN c LIMIT 20") -> List[dict]:
        """Tiny subset: return claims / entities by label."""
        results = []
        for n, attr in self.G.nodes(data=True):
            labels = attr.get("labels", [])
            if "Claim" in labels and "Claim" in pattern:
                results.append({"id": n, **{k: v for k, v in attr.items() if k != "labels"}})
            elif "Entity" in labels and "Entity" in pattern:
                results.append({"id": n, **{k: v for k, v in attr.items() if k != "labels"}})
            elif "Document" in labels and "Document" in pattern:
                results.append({"id": n, **{k: v for k, v in attr.items() if k != "labels"}})
            if len(results) >= 20:
                break
        return results

    def stats(self) -> dict:
        labels = defaultdict(int)
        for _, attr in self.G.nodes(data=True):
            for L in attr.get("labels", ["Node"]):
                labels[L] += 1
        return {
            "nodes": self.G.number_of_nodes(),
            "edges": self.G.number_of_edges(),
            "chunks": len(self.chunks),
            "labels": dict(labels),
            "redis_connected": self.redis is not None,
            "redis_graph": self.redis_graph_available,
        }


# Singleton for swarm
_graph_rag: Optional[GraphRAG] = None

def get_graph_rag() -> GraphRAG:
    global _graph_rag
    if _graph_rag is None:
        _graph_rag = GraphRAG()
    return _graph_rag
