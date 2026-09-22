# DEEP RESEARCH CYCLE 5 — Permanent Learning Pack
Updated: 2026-09-22T05:13:13.089161+00:00

**Pipeline:** LVS → SLMVP → AAO  
**UI:** `/explore` v2.0 · `/doctrine` modifiers M1–M18  
**Prior:** Cycle 4 vector DBs + LLM roles + M7–M12 + first five methods

---

## 1. Vector databases (refresher + decision)

| Store | Constraint win |
|-------|----------------|
| pgvector | Postgres already; SQL; <50M |
| Qdrant | Filters + self-host price/perf |
| Weaviate | Native hybrid + modules |
| Pinecone | Zero ops (if residency OK) |
| Milvus | Billions / K8s |
| Chroma | Prototype |
| LanceDB/Turbopuffer-class | Sparse / offline re-embed |

**Rule:** DB brand < chunking + embedding + rerank + eval.

---

## 2. Embedding models (new depth — M13)

| Model family | Best for |
|--------------|----------|
| Voyage 3/4 large | Managed quality-first; domain variants |
| OpenAI text-embedding-3-large/small | Default + Matryoshka + cheap small |
| Cohere Embed v3/v4 | Multilingual + matched rerank |
| Jina v3/v4 | Long docs, multimodal, OSS self-host |
| BGE-M3 / Qwen3-Embedding | Sovereign open hybrid |
| ColBERT-class late interaction | Rare IDs (grants, FCS, dates) |

**Switching models requires full re-embed + M18 eval-set freeze.**

---

## 3. LLMs (M11)

- Frontier closed → hard ACH / educator  
- Open-weight → bulk tag / self-host / coding  
- Flash → extract/NER  
- LLM-as-judge → Ragas / debate (never same model gen+grade without gold)

---

## 4. SLMVP gates M1–M18

### Core M1–M6
Public-record · HITL · dual-anti-narrative · tag · process≠origin · category-error

### Cycle 4 M7–M12
Reconstructability · conf≠prob · capture audit · blend ban · model-role · vector-store

### Cycle 5 M13–M18
| ID | Gate | Test |
|----|------|------|
| M13 | Embedding fit | quality/cost/sovereignty; re-embed plan |
| M14 | RAG eval gate | faithfulness + context P/R before ship |
| M15 | Rerank required | hybrid → cross-encoder for investigation |
| M16 | Constitutional audit | modifier changes versioned + dual-tribe |
| M17 | Memory provenance | memory cites Claim/Source IDs |
| M18 | Eval-set freeze | gold set frozen before store/model swap |

### Composition patterns
| Pattern | Gates |
|---------|-------|
| Ingest | M1 M2 M4 M10 M12 M13 |
| Retrieve | M12 M13 M14 M15 M18 |
| Origin ACH | M3 M5 M8 M9 M11 |
| Ship | M2 M7 M14 M16 |
| Agent memory | M17 M4 M8 |

---

## 5. Ten advanced methods

### Cycle 4
1. Agentic GraphRAG  
2. SAE / Atom Theory  
3. Bayesian ACH + belief layers  
4. Multi-agent science loops  
5. Hybrid + late-interaction  

### Cycle 5 (new)
6. **RAG evaluation (Ragas triad)** — faithfulness / relevancy / context precision / recall  
7. **Cross-encoder rerank stack** — retrieve 50–100 → rerank 5–10  
8. **Constitutional governance** — SLMVP is the swarm constitution; version principles  
9. **Agent memory + provenance** — EnterpriseRAG-class; no sticky uncited beliefs  
10. **Debate + weak-to-strong oversight** — FOR/AGAINST + judge; freeze gold sets  

---

## 6. Emergent synthesis cycle 5

1. **Embedding choice moves quality more than vector DB choice** at Meridian scale.  
2. **Without M14/M18 you cannot know if a store/model swap helped.**  
3. **M15 makes investigation retrieval real** — dense-only is cargo cult.  
4. **M16 makes SLMVP a constitution**, not a prompt vibe.  
5. **M17 stops multi-agent memory from laundering OVERSTATED claims.**  

**Epistemic status:** secondary industry synthesis (not SOLID primary SSCP facts). M4 still binds primary claims.

Lineage: research_cycle5 · doctrine_v1.3 · skill_cycle5
