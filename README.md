# Live Online Investigation Swarm

**Bayesian ACH · RedisGraph-compatible Hybrid RAG · FastAPI + Streamlit · HITL · Public-record ceiling**

See full docs in repo. Live: FastAPI :8000, Streamlit :8501.

## Quick start
```bash
pip install -r requirements.txt
python main.py "Map public FOIA response deadlines"
python main.py --api   # :8000
streamlit run dashboard/app.py --server.port 8501
```

Optional: `export REDIS_URL=redis://localhost:6379` for RedisGraph persistence.

## Stack
- Bayesian ACH (`utils/bayesian.py`)
- Hybrid Graph RAG (`utils/graph_rag.py`) — networkx + optional Redis/RedisGraph
- FastAPI (`api/app.py`)
- Streamlit dashboard (`dashboard/app.py`)
- Multi-agent Supervisor with Compliance, OSINT, TruthVerifier, MemoryVault, etc.

Absolute rules: public-record only, HITL, SOLID/MAYBE, provenance hashes.
