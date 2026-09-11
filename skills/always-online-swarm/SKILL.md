---
name: always-online-swarm
description: >
  Policy + tooling so every permanent swarm agent, subagent, and tool stays online:
  readiness matrix, tool registry, self-metrics daemon, deploy manifest.
metadata:
  short-description: "Always-online policy for permanent swarm"
  as-of: "2026-09-11"
user-invocable: true
---

# Always-Online Swarm

```bash
python scripts/readiness_check.py
python -m daemon.self_metrics_daemon --ticks 3 --interval 2
```

See deploy/ALWAYS_ONLINE_MANIFEST.md
