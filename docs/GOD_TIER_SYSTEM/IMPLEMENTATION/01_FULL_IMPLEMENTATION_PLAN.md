# Full Implementation Plan — GOD-TIER Lawful Investigative System
Version 1.0 · Metadata-only · PUBLIC_RECORD_CEILING=true · HITL for irreversible actions

## Phases & milestones

### Phase 0 — Baseline (Done)
- [x] Swarm API FastAPI + Streamlit dashboard
- [x] Autonomous Supervisor cycle reports
- [x] GOD-TIER blueprint + 200-node skill tree + constitution
- [x] Dual-persist GitHub + Drive vault

### Phase 1 — Core engines (Week 1–2)
| Milestone | Acceptance test |
|---|---|
| M1.1 Metadata extraction pipeline | Ingest public MD/CSV → schema-normalized entities ≥95% parse success |
| M1.2 Barrier classifier | Input barrier type → lawful route enum (FOIA/ATIP/library/public/HITL) |
| M1.3 Audit trail | Every /verify /rag /swarm decision append-only JSONL |
| M1.4 Skill-tree loader | Load 200 nodes from JSON; query by domain/id |

### Phase 2 — Routing & HITL (Week 2–3)
| Milestone | Acceptance test |
|---|---|
| M2.1 FOIA/ATIP field generator | Template filled from metadata only |
| M2.2 HITL gate service | Irreversible flags block until grant file present |
| M2.3 Compliance middleware | Swarm goals with bypass language → blocked |

### Phase 3 — Self-learning (Week 3–4)
| Milestone | Acceptance test |
|---|---|
| M3.1 Pattern miner | Frequency clusters from public metadata |
| M3.2 Skill evolution log | Proposed node diffs require HITL approve |
| M3.3 Ontology export | Graph stats + entity dump versioned |

### Phase 4 — Hardening (Week 4–5)
| Milestone | Acceptance test |
|---|---|
| M4.1 Rate limits / robots respect | Documented per-source policies |
| M4.2 Public deploy | Health 200 via tunnel; HITL_REQUIRED true |
| M4.3 Rollback | Documented pkill/redeploy runbook |

## Non-goals (never)
- Barrier bypass · credential stuffing · paywall full-text scrape · sealed records

## Deliverables map
Blueprint → Engines → Skill runtime → Constitution checks → Handbook SOPs
