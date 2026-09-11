---
name: permanent-agent-swarm
description: >
  Always-on permanent multi-agent swarm: Overseer, Supervisor, Planner, FlagMonitor,
  Healer, SelfMetrics, Researcher, Investigator, Teacher, Auditor, Compliance,
  TruthVerifier, MemoryVault, subagents. Use when user wants swarm of agents,
  permanent swarm, always multi-agent, flag monitors, overseers, planners, healers,
  self-metrics, researchers, investigators, teachers, auditors. Never single-agent default.
metadata:
  short-description: "Permanent always-on multi-agent swarm (all planes)"
  as-of: "2026-09-11"
user-invocable: true
---

# Permanent Agent Swarm

As-of: 2026-09-11  
Policy: **PERMANENT_SWARM=true** · **NEVER_BYPASS_SUPERVISOR=true**  
Ceiling: public-record only · HITL for irreversible/external · no secrets

## When to use
- "swarm of agents", "always multi-agent", "permanent swarm"
- flag monitors / overseers / planners / healers / self-metrics
- researchers / investigators / teachers / auditors
- Any operator goal that must not collapse to a single LLM reply

## Absolute rules
1. Every goal enters **only** via Supervisor → full pipeline
2. `PUBLIC_RECORD_CEILING=true`
3. HITL for bulk_ingest, external_action, irreversible, dissemination, fee_paid, contact_living_people
4. Claims tagged **SOLID | MAYBE | CONTESTED | CONTRADICTED** with provenance
5. No API keys in skill or public git

## Planes & roster (22 agents)

### Control (always online)
| Agent | Role |
|-------|------|
| **Overseer** | Constitution, ceiling, escalation, pre/post sign-off |
| **Supervisor** | Orchestrator — never skipped |
| **Planner** | Parallel/sequential plan + cost bounds |
| **FlagMonitor** | HITL / ceiling / fail / quality / rate flags |
| **Healer** | Retry, circuit-break, degrade failed agents |
| **SelfMetrics** | Latency, SOLID ratio, health pulse |

### Work
| Agent | Role |
|-------|------|
| Researcher | Broad public research |
| Investigator | Public-record leads / timelines |
| OSINTCollector | Passive public OSINT only |
| LiveWebScout | Live public fetch |
| Pattern | Cluster detection |
| Anticipation | Forward risks / next sources |
| Teacher | Explain + skill proposals (HITL apply) |
| Synthesizer | Final report |

### Governance
| Agent | Role |
|-------|------|
| Compliance | First gate every run |
| TruthVerifier | Bayesian ACH stub → SOLID/MAYBE |
| Auditor | Append-only JSONL decisions |

### Memory
| Agent | Role |
|-------|------|
| MemoryVault | Claim store + Graph RAG hook |

### Subagents
ExploreSub · ScoutSub · GeneralSub · ReviewerSub

## Default pipeline (every run)
```
Compliance → Overseer(pre) → FlagMonitor(arm) → SelfMetrics(start) → Planner
  → parallel[Researcher, Investigator, OSINT, LiveWebScout, Pattern, Anticipation]
  → TruthVerifier → MemoryVault → Teacher → Synthesizer → Auditor
  → Healer → FlagMonitor(scan) → SelfMetrics(end) → Overseer(post)
```

## Quick ops
```bash
cd permanent-agent-swarm   # or live-online-agent-swarm/permanent/
python main.py --roster
python main.py "Map public FOIA response deadlines"
```

Env:
```
PERMANENT_SWARM=true
NEVER_BYPASS_SUPERVISOR=true
PUBLIC_RECORD_CEILING=true
HITL_REQUIRED=true
```

## OpenCode integration
Install agents from `opencode/agents/*.md` into `.opencode/agents/` or set in `opencode.json` `agent` map with Plan/Build temperatures. Pair with `models` skill for per-agent model IDs.

## Related skills
swarm-ops-desk · hitl-governance · osint-public-ceiling · nlla-debate-system · models · secret-store-hygiene · meridian-globe-atlas

## References
- references/workflows.md
- references/tools.md
- references/examples.md
- references/deployments.md
- config/roster.yaml in package root
