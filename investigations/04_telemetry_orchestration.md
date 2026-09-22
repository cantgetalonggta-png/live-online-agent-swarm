# Phase 4 / Node 4: Open-Access Telemetry Orchestration & Document Verification

## 1. System Topology — Transparent Public Ingestion Mesh

```
[.gov / Oversight FOIA seeds]
[GAO / WHO public products]     ──► [Local hash staging cache]
[OpenAlex / Crossref OA APIs]        │
[User-supplied public PDFs]          ▼
                              [Decoupled Telemetry Struct]
                                         │
                    ┌────────────────────┼────────────────────┐
                    ▼                    ▼                    ▼
           [Forensic Integrity]   [Polarity LEO Core]   [Ops Monitor]
                    └────────────────────┬────────────────────┘
                                         ▼
                              [C01–C11 Auto-Verdict Matrix]
                                         ▼
                              [HQ /primary + JSON log]
```

## 2. Scope Fence (absolute)

### IN
- Official `.gov` registries and Oversight FOIA PDFs
- GAO / WHO / SAGO public assessments
- OpenAlex, Crossref, Unpaywall-class **open-access** metadata and OA PDFs
- Document hash timelines, metadata anachronism, polarity LEO
- Decoupled ingest telemetry (counts, latency, failures)

### OUT (refused)
- `intitle:"index of" backup|db|conf|env` secret hunting on third parties
- Gobuster / Dirbuster directory fuzzing of non-owned systems
- Production Tor / I2P harvest pipelines for claim filling
- Credential pools, paywall pierce, runtime client mutation

## 3. Decoupled Telemetry Struct
Independent event log: `claim_start`, `foia_seed`, `openalex`, `claim_done`, failures.
Does not mutate claim schema. Adverse omission still flows to LEO via missing primary lists.

## 4. Build Chain
- Modules: `document_forensic_integrity.py`, `phase4` orchestrator, `leoAuto.ts`
- HQ: `http://localhost:8080/primary` LEO table
- Artifacts: `PHASE4_OPEN_ACCESS_ORCHESTRATION.json`

## 5. Swarm Consolidation
FOIA seeds + OpenAlex titles → secondary disclosure text → clash engine → omission weight → tag + FOIA warrant.
