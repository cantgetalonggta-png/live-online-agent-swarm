# Always-Online Deploy Manifest
As-of: 2026-09-11

## Policy
- `PERMANENT_SWARM=true` — Supervisor never bypassed
- `ALWAYS_ONLINE=true` — every agent + subagent + tool wired
- `PUBLIC_RECORD_CEILING=true`
- HITL for bulk/external/irreversible/dissemination

## Agents (24)
Control: Overseer, Supervisor, Planner, FlagMonitor, Healer, SelfMetrics
Work: Researcher, Investigator, OSINTCollector, LiveWebScout, Pattern, Anticipation, Teacher, Synthesizer, AutopilotDirector
Governance: Compliance, TruthVerifier, Auditor, CompletenessAuditor
Memory: MemoryVault
Subagents: ExploreSub, ScoutSub, GeneralSub, ReviewerSub

## Deploy steps
```bash
cd permanent-agent-swarm
pip install -r requirements.txt
python scripts/readiness_check.py
python -m daemon.self_metrics_daemon --ticks 3 --interval 2
streamlit run dashboard/swarm_ops.py
streamlit run investigation/app.py   # or investigation-complete/app.py
python main.py "Public FOIA EpsteinDocs archive.org index"
```

## Dual-persist
- Drive: skill-tree/permanent-agent-swarm + investigation-complete
- GitHub: live-online-agent-swarm (permanent/) + meridian-drive-vault-atlas (skills/)
