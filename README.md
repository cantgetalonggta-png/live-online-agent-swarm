# Live Online Investigation Swarm

**Bayesian ACH · RedisGraph Hybrid RAG · FastAPI + Streamlit · HITL · Public-record ceiling**

Multi-agent investigation system built from Grok skills (`multi-agent-patterns`, `truth-verification`, `osint-rag-master`, `knowledge-base-builder`, `integrity-investigative-system`, …).

## Features

| Layer | What |
|-------|------|
| **Supervisor** | Orchestrates Compliance → parallel OSINT/LiveWeb/Pattern → Bayesian TruthVerifier → MemoryVault → Anticipation → Synthesizer |
| **Bayesian ACH** | Full Analysis of Competing Hypotheses + sequential Bayesian updates with source quality weights |
| **Graph RAG** | Hybrid vector (TF-IDF) + networkx graph; Redis persistence + RedisGraph Cypher mirror when `REDIS_URL` is set. Schema: `Document-HAS_CHUNK-Chunk-MENTIONS-Entity`, `Claim-SUPPORTED_BY-Source` |
| **Dashboard** | Streamlit: Run Swarm, Bayesian Verify, Graph RAG ingest/query, Claims, Health |
| **API** | FastAPI: `/swarm/run`, `/verify`, `/rag/query`, `/rag/ingest`, `/claims`, `/graph/*`, `/health` |

## Quick start

```bash
pip install -r requirements.txt

# CLI
python main.py "Map public FOIA records on agency X"

# FastAPI (OpenAPI at /docs)
python main.py --api
# or: uvicorn api.app:app --host 0.0.0.0 --port 8000

# Streamlit dashboard
streamlit run dashboard/app.py --server.port 8501 --server.address 0.0.0.0
```

### Optional Redis / RedisGraph

```bash
export REDIS_URL=redis://localhost:6379/0
# If RedisGraph module is loaded, Cypher mirror activates automatically.
```

Without Redis the graph runs fully in-memory (networkx) and still supports hybrid RAG.

## Absolute rules

1. Only public records and operator-supplied public material  
2. HITL = YES for bulk ingest / external / irreversible actions  
3. SOLID / MAYBE tagging on every claim  
4. No private data, no credential packs, no unauthorized access  
5. Provenance (URL + timestamp + hash) on every claim  

## API examples

```bash
curl -s http://localhost:8000/health | jq
curl -s -X POST http://localhost:8000/swarm/run \
  -H 'Content-Type: application/json' \
  -d '{"goal":"Public records on open data portals"}' | jq .results.TruthVerifier
curl -s -X POST http://localhost:8000/verify \
  -H 'Content-Type: application/json' \
  -d '{"claim":"Agency X published FOIA log in 2025"}' | jq .best
curl -s -X POST http://localhost:8000/rag/query \
  -H 'Content-Type: application/json' \
  -d '{"query":"transparency FOIA","top_k":5}' | jq
```

## Layout

```
agent_swarm_live/
├── main.py / swarm_runtime.py / swarm_config.py
├── api/app.py              # FastAPI
├── dashboard/app.py        # Streamlit
├── agents/                 # Supervisor + specialists
├── utils/
│   ├── bayesian.py         # ACH + Bayesian updates
│   ├── graph_rag.py        # RedisGraph-compatible hybrid RAG
│   ├── memory.py           # MemoryVault + graph mirror
│   ├── directives.py
│   └── monitor.py
└── tools/
```

## License / ethics

Lawful public-record research only. Operator is responsible for jurisdiction and ToS.
