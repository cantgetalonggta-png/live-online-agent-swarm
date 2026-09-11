# Workflows — permanent-agent-swarm

## W1 · Cold start permanent swarm
1. Confirm env: PERMANENT_SWARM=true, PUBLIC_RECORD_CEILING=true, HITL_REQUIRED=true
2. `python main.py --roster` → expect 22 agents
3. Run one public goal through full pipeline
4. Inspect health + claims + audit.jsonl

## W2 · Operator goal (always swarm)
1. Do NOT answer as single agent
2. Invoke PermanentSwarm.run(goal) / skill permanent-agent-swarm
3. Compliance must pass before work plane
4. Tag all claims; surface HITL notice before dissemination

## W3 · Flag handling
1. FlagMonitor arm at start
2. On agent_fail → Healer retries (heal_retries)
3. On ceiling_breach → Overseer blocks + escalate
4. On quality (low SOLID ratio) → warn Teacher/Supervisor

## W4 · Self-metrics pulse
1. SelfMetrics start + end every run
2. Track avg latency per agent, solid_ratio, open_flags
3. Optional background pulse every metrics_every_n_sec

## W5 · Skill proposal (Teacher)
1. Teacher emits skill_proposals with hitl_required=true
2. Operator approves via HITL grant
3. Apply via skill-creator — never auto-apply

## W6 · Dual-persist
1. Code → live-online-agent-swarm (GitHub)
2. Skill → .grok/skills + Drive skill-tree
3. Audit/claims → vault/ (local; not secret-store)

## W7 · Failure recovery
| Symptom | Action |
|---------|--------|
| Bypass attempt | Overseer/Supervisor flag policy |
| Agent fail | Healer retry → degrade |
| HITL expired | hitl-governance re-ask H-codes |
| Ceiling block | Stop; rewrite goal public-only |
