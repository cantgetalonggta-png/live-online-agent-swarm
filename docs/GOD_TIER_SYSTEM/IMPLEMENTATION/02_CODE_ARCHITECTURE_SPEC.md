# Code Architecture Specification — GOD-TIER
Stack: Python 3.10+ · FastAPI · Streamlit · networkx (RedisGraph optional) · Cloudflare Tunnel

## Repository layout
```
live-online-agent-swarm/
  api/app.py              # FastAPI routes
  dashboard/app.py        # Streamlit UI
  swarm_runtime.py        # Supervisor + agents
  swarm_config.py         # HITL + public ceiling flags
  agents/                 # role agents
  utils/bayesian.py       # ACH verify
  skills/                 # skill packages
  docs/GOD_TIER_SYSTEM/   # blueprint, skill tree, constitution
  vault/                  # investigation dual-persist
```

## API surface (contract)
| Method | Path | Body | Purpose |
|---|---|---|---|
| GET | /health | — | status, hitl, ceiling, graph |
| POST | /swarm/run | {goal} | multi-agent run |
| POST | /verify | {claim, evidence, hypotheses, sources} | Bayesian ACH |
| POST | /rag/query | {query, top_k} | graph/vector retrieval |
| POST | /rag/ingest | {doc_id, title, source, chunks, meta} | document ingest |
| GET | /claims | — | claim store |
| GET | /verifications | — | verification store |
| GET | /graph/stats | — | ontology stats |
| POST | /graph/cypher | (if enabled) | graph query |

## Module map
| Module | Responsibility |
|---|---|
| Input Layer | query + public metadata intake |
| Metadata Intelligence | extract/normalize/cluster (skill D1) |
| Access Logic | barrier classify (D2) |
| Routing | FOIA/ATIP/library paths (D3) |
| HITL | grant files + irreversible gates (D4) |
| Self-Learning | skill proposals only (D5) — apply with HITL |
| Ethics | constitution checks (D6) |
| Audit | JSONL decision log (D7) |
| Investigative | leads from public records (D8) |
| Supervisor | orchestrates /swarm/run cycle |

## Data schemas (logical)
- Claim: {hash, text, status SOLID|MAYBE, confidence, sources, agent}
- Evidence: {id, description, source, likelihood_if_h, likelihood_if_not_h, quality}
- SkillNode: {id, name, domain, trigger, inputs, outputs, execution_rules, version}
- HITLGrant: {id, start_utc, expiry_utc, scope, not_granted[]}
- AuditEvent: {ts, actor, action, inputs_hash, decision, hitl_required}

## Deployment
- Local: uvicorn :8000 · streamlit :8501
- Public: cloudflared quick tunnel (ephemeral) or named tunnel
- Env: HITL_REQUIRED=true PUBLIC_RECORD_CEILING=true (no secrets in repo)

## Security
- CORS tighten for prod · no .env secrets committed · metadata-only for restricted surfaces
