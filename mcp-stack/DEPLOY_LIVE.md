# LIVE — manus-mcp-bridge on Vercel

| Field | Value |
|-------|--------|
| Status | READY |
| Project | `manus-mcp-bridge` (`prj_SuTX6tfZ84FFE6HvgZV6YdWKY2Eg`) |
| Production alias | https://manus-mcp-bridge-olive.vercel.app |
| Team alias | https://manus-mcp-bridge-echo-ec69.vercel.app |
| MCP | https://manus-mcp-bridge-olive.vercel.app/mcp |
| Health | https://manus-mcp-bridge-olive.vercel.app/health |
| Deployments | `dpl_FDTeU56n…` then redeploy `dpl_6e4xGpNz…` |
| `BRIDGE_TOKEN` | set encrypted on project (all targets) |
| `MANUS_API_KEY` | **not set** — add in Vercel dashboard or ask Grok after you provide key |

## Client config

```json
"manus": {
  "type": "http",
  "url": "https://manus-mcp-bridge-olive.vercel.app/mcp",
  "headers": { "Authorization": "Bearer <BRIDGE_TOKEN>" }
}
```

BRIDGE_TOKEN value is in Vercel project env (not in git). Retrieve from Vercel UI if needed.
