# Live Online Agent Swarm

**Public-record ceiling · HITL enforced · SOLID / MAYBE discipline**

A multi-agent investigation swarm built from the loaded Grok skills:

- `multi-agent-patterns` (Supervisor + Parallel Fan-out + Swarm roles)
- `multi-agent-project-structure` (this layout)
- `multi-agent-tooling`
- `llm-orchestration`
- `agent-roles-memory-pattern-anticipation` (MemoryVault, Pattern, Anticipation, Compliance)
- `osint-rag-master` + `ethical-data-harvesting` + `live-web-mastery`
- `truth-verification` (ACH / Bayesian)
- `research-automation`
- `legal-osint-compliance-layer` + `sensitive-data-defensive-scan`
- `integrity-investigative-system` concepts (provenance hashing)

## Quick Start

```bash
cd agent_swarm_live
python -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt
python main.py "Map public FOIA and court records on a current open case"
```

## Architecture

```
Supervisor (orchestrator)
    ├── Compliance (gate)
    ├── OSINTCollector  ──┐
    ├── LiveWebScout    ──┬── parallel fan-out
    ├── Pattern         ──┘
    ├── TruthVerifier
    ├── MemoryVault
    ├── Anticipation (background)
    └── Synthesizer (final report)
```

## Absolute Rules (non-negotiable)

1. Only public records and operator-supplied public material.
2. HITL = YES for bulk ingest, external actions, irreversible decisions.
3. SOLID / MAYBE tagging on every claim.
4. No private data, no credential packs, no unauthorized access.
5. Every claim carries provenance (URL + timestamp + hash).

## Live Online

This repo is designed to be pushed to GitHub and run as a scheduled automation or interactive service.
Extend the agents with real tool calls (web_search, Wayback, dorks, Graph RAG) under the same compliance gates.

## Extending

- Add real collection under `tools/web_tools.py` using ethical recipes only.
- Swap in-memory MemoryVault for Redis + Neo4j (see integrity-investigative-system).
- Wire Prometheus metrics via `metrics-self-healing`.
- Deploy with Docker / Kubernetes (see multi-agent-tooling).

## License / Ethics

Lawful public-record research only. Operator is responsible for jurisdiction and ToS compliance.
