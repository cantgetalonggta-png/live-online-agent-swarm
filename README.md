# Live Online Investigation Swarm

**Bayesian ACH · RedisGraph-compatible Hybrid RAG · FastAPI + Streamlit · HITL · Public-record ceiling**

Multi-agent investigation system built from Grok skills:
`multi-agent-patterns`, `truth-verification`, `knowledge-base-builder`, `osint-rag-master`,
`agent-roles-memory-pattern-anticipation`, `integrity-investigative-system`, `research-automation`.

## Live endpoints (this session)

| Service | URL |
|---------|-----|
| **FastAPI** | http://0.0.0.0:8000 · docs at `/docs` |
| **Streamlit dashboard** | http://0.0.0.0:8501 |
| **GitHub** | https://github.com/cantgetalonggta-png/live-online-agent-swarm |

## Quick start

```bash
cd agent_swarm_live
pip install -r requirements.txt

# CLI swarm run
python main.py "Map public FOIA response deadlines"

# FastAPI
python main.py --api
# or: uvicorn api.app:app --host 0.0.0.0 --port 8000

# Streamlit dashboard
streamlit run dashboard/app.py --server.port 8501 --server.address 0.0.0.0
```

Optional Redis for persistence + RedisGraph module:
```bash
export REDIS_URL=redis://localhost:6379
```
Without Redis the graph runs in-memory (networkx) and still supports hybrid vector+graph retrieval.

## Architecture

```
Supervisor
  ├── Compliance (public-record + HITL gate)
  ├── OSINTCollector  ──┐
  ├── LiveWebScout    ──┼── parallel fan-out
  ├── Pattern         ──┘
  ├── TruthVerifier   ← Bayesian Belief Network + ACH
  │                     (priors → likelihoods → posteriors → SOLID/MAYBE)
  ├── MemoryVault     ← Hybrid Graph RAG
  │                     Document-HAS_CHUNK-Chunk-MENTIONS-Entity
  │                     Claim-SUPPORTED_BY-Source
  ├── Anticipation
  └── Synthesizer
```

### Bayesian verification (`utils/bayesian.py`)
- Sequential Bayesian update with source-quality weighting
- Analysis of Competing Hypotheses (ACH) matrix
- Maps posteriors → SOLID / MAYBE / CONTESTED / CONTRADICTED
- Enriched automatically with Graph RAG hits as soft evidence

### RedisGraph RAG (`utils/graph_rag.py`)
- Schema: `(:Document)-[:HAS_CHUNK]->(:Chunk)-[:MENTIONS]->(:Entity)`
- TF-IDF vector search + graph expansion (hybrid)
- Redis key-value persistence when `REDIS_URL` set
- RedisGraph Cypher mirror when module present
- Fallback: pure networkx (always available)

### Live dashboard (Streamlit)
Views: **Run Swarm** · **Bayesian Verify** · **Graph RAG** · **Claims & Memory** · **Health**

### FastAPI routes
- `POST /swarm/run` `{goal}`
- `POST /verify` Bayesian ACH (+ RAG enrichment)
- `POST /rag/query` · `POST /rag/ingest`
- `GET /claims` · `GET /graph/stats` · `GET /graph/cypher` · `GET /health` · `GET /verifications`

## Absolute rules

1. Only public records / operator-supplied public material  
2. HITL = YES for bulk ingest, external actions, irreversible decisions  
3. SOLID / MAYBE tagging on every claim  
4. No private data, credentials, or unauthorized access  
5. Provenance (URL + timestamp + hash) on every claim  

## Project layout

```
agent_swarm_live/
├── main.py                 # CLI / --api / --dashboard
├── swarm_runtime.py        # shared factory (API + dashboard)
├── swarm_config.py
├── api/app.py              # FastAPI
├── dashboard/app.py        # Streamlit
├── agents/                 # Supervisor + specialists
├── utils/
│   ├── bayesian.py         # ACH + Bayesian BN
│   ├── graph_rag.py        # Hybrid Graph RAG
│   ├── memory.py           # MemoryVault + graph mirror
│   ├── directives.py
│   └── monitor.py
├── tools/
└── requirements.txt
```

## Example API calls

```bash
# Verify a claim
curl -X POST http://localhost:8000/verify \
  -H 'Content-Type: application/json' \
  -d '{"claim":"Federal agencies must respond to FOIA requests within 20 working days","sources":["https://www.justice.gov/oip/foia-guide"]}'

# Ingest public document chunks
curl -X POST http://localhost:8000/rag/ingest \
  -H 'Content-Type: application/json' \
  -d '{"doc_id":"foia-guide","title":"FOIA Guide","source":"https://www.justice.gov/oip/foia-guide","chunks":["..."]}'

# Run full swarm
curl -X POST http://localhost:8000/swarm/run \
  -H 'Content-Type: application/json' \
  -d '{"goal":"Map public FOIA response deadlines"}'
```

## License / Ethics

Lawful public-record research only. Operator owns jurisdiction and ToS compliance.
