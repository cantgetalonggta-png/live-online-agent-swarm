# Permanent Agent Swarm v2.2

**Always-on multi-agent system** — every goal routes through the full swarm.
**Always-online** — every agent, subagent, and tool is wired and readiness-checked.
Never a single-agent default.

As-of: 2026-09-11

## Planes (24 agents)

| Plane | Agents |
|-------|--------|
| **Control** | Overseer · Supervisor · Planner · FlagMonitor · Healer · SelfMetrics |
| **Work** | Researcher · Investigator · OSINTCollector · LiveWebScout · Pattern · Anticipation · Teacher · Synthesizer · AutopilotDirector |
| **Governance** | Auditor · Compliance · TruthVerifier · CompletenessAuditor |
| **Memory** | MemoryVault |
| **Subagents** | ExploreSub · ScoutSub · GeneralSub · ReviewerSub |

## Absolute rules

1. `PERMANENT_SWARM=true` — Supervisor is never bypassed  
2. `ALWAYS_ONLINE=true` — per-agent tool bindings + live probe  
3. `PUBLIC_RECORD_CEILING=true` — public records only  
4. HITL for bulk/external/irreversible/dissemination  
5. Claims tagged SOLID / MAYBE / CONTESTED / CONTRADICTED  
6. No secrets in repo  

## Quick start

```bash
cd permanent-agent-swarm
pip install -r requirements.txt
python scripts/readiness_check.py
python main.py --roster
python main.py "Map public FOIA response deadlines"
streamlit run dashboard/swarm_ops.py
streamlit run investigation/app.py
```

## Pipeline (every run)

Compliance → Overseer(pre) → FlagMonitor(arm) → SelfMetrics(start) → Planner  
→ **parallel work plane** → TruthVerifier → MemoryVault → Teacher → Synthesizer → Auditor  
→ Healer → FlagMonitor(scan) → SelfMetrics(end) → Overseer(post self-control)

## U15–U28
Always-online · logical tools · self-learning · self-control · autopilot · completeness atlas · dual-persist · Drive delta
