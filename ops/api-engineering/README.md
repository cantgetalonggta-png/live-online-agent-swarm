# API / engineering / ops skill map (active)

| Skill | Role in this deploy |
|-------|---------------------|
| api-integration-master | MCP HTTP clients, retries, auth headers |
| api-key-management | Codespace/Vercel secrets only — never git |
| code-evolution | Bridge + swarm co-evolution without breaking API |
| deployment-automation | Git push → Vercel/Codespace path |
| llm-orchestration | Grok + Manus + swarm tool routing |
| metrics-self-healing | `/health` probes; restart scripts |
| multi-agent-patterns | Swarm supervisor + MCP tools |
| multi-agent-project-structure | `mcp-stack/` layout |
| multi-agent-tooling | FastAPI, httpx, uvicorn |
| python-pep8-code-reviewer | Bridge style baseline |
| gh-issues | Optional issue tracking for deploy blockers |

## Deploy paths (quota-aware)

1. **Vercel** — project `manus-mcp-bridge` (preferred; no Codespace needed)
2. **Existing Codespace** — run `mcp-stack/scripts/pull-and-run-in-existing-codespace.sh`
3. **Local** — same script
