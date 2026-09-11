# Permanent Agent Swarm

**Always-on multi-agent system** — every goal routes through the full swarm.
Never a single-agent default.

As-of: 2026-09-11T08:00Z

## Planes

| Plane | Agents |
|-------|--------|
| **Control** | Overseer · Supervisor · Planner · FlagMonitor · Healer · SelfMetrics |
| **Work** | Researcher · Investigator · OSINTCollector · LiveWebScout · Pattern · Anticipation · Teacher · Synthesizer |
| **Governance** | Auditor · Compliance · TruthVerifier |
| **Memory** | MemoryVault |
| **Subagents** | ExploreSub · ScoutSub · GeneralSub · ReviewerSub |

## Absolute rules

1. `PERMANENT_SWARM=true` — Supervisor is never bypassed  
2. `PUBLIC_RECORD_CEILING=true` — public records only  
3. HITL for bulk/external/irreversible/dissemination  
4. Claims tagged SOLID / MAYBE / CONTESTED / CONTRADICTED with provenance  
5. No secrets in repo  

## Quick start

```bash
cd permanent-agent-swarm
pip install -r requirements.txt
python main.py --roster
python main.py "Map public FOIA response deadlines"
```

## Pipeline (every run)

Compliance → Overseer(pre) → FlagMonitor(arm) → SelfMetrics(start) → Planner  
→ **parallel work plane** → TruthVerifier → MemoryVault → Teacher → Synthesizer → Auditor  
→ Healer → FlagMonitor(scan) → SelfMetrics(end) → Overseer(post)

## Related

- live-online-agent-swarm (parent system)
- skills: permanent-agent-swarm, swarm-ops-desk, hitl-governance, osint-public-ceiling, nlla-debate-system
- models skill for per-agent model routing
