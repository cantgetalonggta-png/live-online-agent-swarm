# Deployments — permanent-agent-swarm

## Layout
```
permanent-agent-swarm/
  main.py
  swarm_config.py
  config/roster.yaml
  agents/{control,work,governance,memory,subagents}/
  utils/
  opencode/agents/
  vault/   # runtime audit (gitignored if sensitive)
```

## Dual-persist
1. GitHub: cantgetalonggta-png/live-online-agent-swarm → `permanent/` or root merge
2. GitHub: meridian-drive-vault-atlas → `skills/permanent-agent-swarm/`
3. Drive skill-tree: 12_VD_KWRsrhxLrVMXfXvlTKKQ4e11dmY
4. Workspace: .grok/skills/permanent-agent-swarm/

## Install skill
Copy SKILL.md + references to:
- `.opencode/skills/permanent-agent-swarm/`
- or `~/.config/opencode/skills/permanent-agent-swarm/`

## Parent system
Extends live-online-agent-swarm Phase-1 engines with permanent control plane
(FlagMonitor, Healer, SelfMetrics, Overseer, Planner, Teacher, Auditor, Researcher, Investigator).
