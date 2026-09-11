# Examples — permanent-agent-swarm

## Basic 1 — Roster
User: "show swarm agents"  
Agent: run permanent swarm roster; list 22 by plane.

## Basic 2 — Public goal
User: "Map public FOIA response deadlines"  
Agent: PermanentSwarm.run(goal) → full pipeline → report + MAYBE claims + HITL notice.

## Basic 3 — Blocked ceiling
User: goal containing unauthorized access language  
Agent: Compliance/Overseer block; no work plane.

## Advanced 1 — Investigation
User: "Investigate public ACRIS filings for [address]"  
Agent: Investigator + OSINT + Pattern + TruthVerifier; public ceiling; HITL before any contact.

## Advanced 2 — Metrics review
User: "swarm health"  
Agent: SelfMetrics pulse + FlagMonitor scan + open flags.

## Advanced 3 — OpenCode wiring
```json
{
  "agent": {
    "build": { "mode": "primary", "model": "xai/grok-4.6" },
    "plan": { "mode": "primary", "model": "anthropic/claude-haiku-4-20250514", "permission": { "edit": "deny" } }
  }
}
```
Permanent swarm still wraps every goal; OpenCode agents are model hosts for roles.
