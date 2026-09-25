# Grok / xAI System Status — Combined Publication
**References 1–8 · Combined & Published**  
**Generated:** Friday, September 25, 2026 · ~07:43 AM PDT  
**Mode:** Theoretical full-system inventory (all connectors, skills, MCP bridges, and secrets assumed live)

---

## Document control

| Field | Value |
|-------|--------|
| Title | Grok / xAI System Status — Combined Publication |
| Scope | References 1–8 (Status · Connectors · Tools · Skills · Models · Effort · Research Synthesis · MCP Config) |
| Audience | Operator / architect / integration |
| Assumption | Every connector re-authed, every skill loaded, MCP bridges up, Codespace secrets injected |
| Source thread | Supabase re-auth · Manus bridge · Codespace secrets · GitHub Copilot MCP config |

---

# 1. /STATUS (snapshot)

| Axis | State | Notes |
|------|--------|-------|
| **Runtime** | LIVE | Grok agent session + remote sandbox `/workspace/artifacts` |
| **Primary identity** | Grok 4.x family (xAI) | Current chat model; Imagine pipeline separate |
| **Sandbox** | Linux · bash · internet enabled | Working dir: `/workspace/artifacts` |
| **Tool orchestration** | Active | Parallel tool calls supported |
| **Imagine media** | Active | Image + video gen / edit / upscale |
| **Connected services** | Full (assumed) | See §2 |
| **Custom skills** | ~70+ loaded | User + server skills |
| **MCP custom** | Configured | GitHub Copilot MCP + Manus bridge + Supabase MCP |
| **Secrets** | Codespace injected (assumed) | `MANUS_API_KEY`, `BRIDGE_TOKEN`, Supabase PAT / project_ref |
| **Rate / safety** | Normal | Moderation gates on Imagine |
| **Session continuity** | Continuous | Multi-turn context retained across connector/Manus work |

---

# 2. CONNECTORS

## 2.1 Native Grok connectors (account-level)

| Connector | Status (assumed full) | Core capabilities |
|-----------|------------------------|-------------------|
| **SUPABASE_SERVICE** | Connected + tools live | List projects, schema inspect, SQL, migrations, security advisors, docs |
| **GitHub** | Connected | Repos, code search, issues, PRs, Actions, Projects, trees, files, push, notifications, secret scan |
| **Vercel** | Connected | Projects, deploys, envs, teams, domains, sandboxes, edge config, observability, API keys |
| **HyperFrames by HeyGen** | Connected | List / compose / render video projects |
| **Google Drive** | Connected | Files, search, read |
| **Voice** | Connected | TTS (spoken audio from text) |
| **Automations** | Connected | Schedule prompts, event triggers (GitHub / Linear / etc.), list / create / update |

## 2.2 Available-to-connect (catalog)

Gmail · Google Calendar · Outlook · Outlook Calendar · Box · Buffer · Calendly · Canva · Coinbase · Daloopa · Excalidraw · Figma · Gamma · Google Cloud BigQuery · HubSpot · Interactive Brokers (IBKR) · Linear · Meltwater · Microsoft Teams · Mixpanel · Netlify · Notion · Robinhood · S&P Global · Stripe · Webull · Whop · Wix · X Ads · X Money · etoro · Finance (bank / credit / investment)

## 2.3 External MCP servers

| Name | Type | Endpoint | Auth |
|------|------|----------|------|
| **github** (Copilot MCP) | http | `https://api.githubcopilot.com/mcp/` | Copilot session |
| **manus** (custom bridge) | http | Codespace-forwarded MCP URL | `Authorization: Bearer ${BRIDGE_TOKEN}` |
| **supabase** (official MCP) | http | `https://mcp.supabase.com/mcp?…` | OAuth / scoped PAT |

---

# 3. BUILT-IN TOOLS

| Category | Tools |
|----------|--------|
| **Web / research** | `web_search` |
| **Connected services** | `search_connected_tools`, `call_connected_tool` |
| **Sandbox** | `run_terminal_command`, `kill_terminal_command`, `get_terminal_command_output`, `read_file` |
| **Imagine — image** | `imagine_text_to_image`, `imagine_image_to_image`, `imagine_reference_to_image`, `imagine_create_asset`, `imagine_view_media`, `imagine_extract_subject`, `imagine_region_edit`, `imagine_share_asset` |
| **Imagine — video** | `imagine_text_to_video`, `imagine_image_to_video`, `imagine_reference_to_video`, `imagine_upscale_video` |
| **Render** | `render_imagine_media` (final user-visible media only) |

---

# 4. SKILLS

## 4.1 Bundled document & media skills

`docx` · `pdf` · `pptx` · `xlsx` · `ffmpeg` · `skill-creator`

## 4.2 Investigation / OSINT / research

`advanced-swarm-v2-pdf-agents` · `agent-roles-memory-pattern-anticipation` · `anomaly-detection-research` · `autoresearch` · `document-intelligence` · `dorking-mastery` · `epstein-investigation-synthesizer` · `epstein-pdf-batch-ingest` · `ethical-data-harvesting` · `ethical-scraper-orchestration` · `integrity-investigative-system` · `investigation-process-video` · `knowledge-base-builder` · `legal-osint-compliance-layer` · `live-web-mastery` · `osint-rag-master` · `public-dataset-discovery` · `research-automation` · `rex-export-x5-master` · `search-encyclopedia` · `search-techniques-master` · `truth-verification` · `wayback-ghost-index-public` · `wayback-machine-mastery`

## 4.3 API / engineering / ops

`api-integration-master` · `api-key-management` · `code-evolution` · `deployment-automation` · `llm-orchestration` · `metrics-self-healing` · `multi-agent-patterns` · `multi-agent-project-structure` · `multi-agent-tooling` · `python-pep8-code-reviewer` · `gh-issues`

## 4.4 Communication / persona / debate

`aggressive-debate-persona` · `aggressive-logic-combat` · `coherent-communication` · `comedian-persona-debate` · `complex-rewriting` · `debate-argument-structure` · `george-carlin-persona` · `lenny-bruce-persona` · `richard-pryor-persona` · `learn-and-lay-it-out`

## 4.5 Domain / advocacy

`tenant-misconceptions-rebuttal` · `tenant-rights-advocacy`

## 4.6 Self / misc

`native-lang-learning` · `ontological-self-update` · `pdf-breakdown-explainer` · `self-dev-resources` · `sensitive-data-defensive-scan` · `termux-sovereign-setup`

**Total skills:** ~70+ (bundled + custom).

---

# 5. MODELS (xAI / Grok family — Sep 2026)

| Model | Role | Context | Notes |
|-------|------|---------|--------|
| **Grok 4.7** | Flagship (current) | 500K | Coding, agentic, reasoning; configurable effort |
| **Grok 4.6 / 4.5** | Prior flagships | 500K | Still widely available |
| **Grok 4.20** | Long-context / multi-agent | up to 2M | Reasoning + multi-agent variants |
| **Grok 4.3** | Strong mid | 1M | |
| **Grok 4.1 Fast / Fast-Reasoning** | Speed / cost | 128K–2M | |
| **Grok Code Fast 1 / Build 0.1** | Coding specialist | 256K | |
| **Grok Imagine (Image / 2.0 / Quality)** | Image gen/edit | — | Powers Imagine tools |
| **Grok Imagine Video / 1.5** | Video gen | — | 480p / 720p / 1080p (Pro) |
| **Voice / TTS / STT** | Audio | — | Voice connector + API |
| **This session** | Grok 4.x + Imagine | Large | Tools + skills + connectors |

---

# 6. EFFORT / REASONING CONTROLS

| Level | Typical use |
|-------|-------------|
| **low** | Fast replies, simple lookups |
| **medium** | Standard multi-step work |
| **high** | Deep analysis, multi-tool plans (default for hard tasks) |
| **xhigh** | Maximum deliberation (Grok 4.7 Responses API) |
| **Parallel tools** | Multiple connected / Imagine / bash calls in one turn |
| **Outer research loop** | `autoresearch`: experiment → synthesize → steer |

No fixed public “tokens of effort” meter in chat; behavior scales with task complexity and explicit high-reasoning requests.

---

# 7. RESEARCH_SYNTHESIS

Pipeline when research synthesis is requested (or via `autoresearch` / `osint-rag-master` / `learn-and-lay-it-out` / `truth-verification`):

1. **Plan** — multi-hypothesis / multi-source plan  
2. **Collect** — `web_search`, dorking, Wayback, connected APIs (GitHub / Vercel / Supabase / Drive), ethical scrapers  
3. **Structure** — entity graphs, timelines, ACH / Bayesian updating (`truth-verification`)  
4. **Synthesize** — plain-English + structured report (`learn-and-lay-it-out`, knowledge-base-builder)  
5. **Deliver** — markdown / PDF / pptx / xlsx / video narrative (`investigation-process-video`, HyperFrames)  
6. **Memory** — long-horizon pattern vault (`agent-roles-memory-pattern-anticipation`)  

**Canonical invocation (theoretical):**  
`/research_synthesis <topic> --depth high --sources web,github,supabase,wayback --output report+timeline+graph`

---

# 8. THEORETICAL FULL MCP CONFIG (published)

Authoritative combined MCP server map (GitHub Copilot + Manus bridge + Supabase).  
Replace placeholders before production use.

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "manus": {
      "type": "http",
      "url": "https://YOUR-CODESPACE-8000.app.github.dev/mcp",
      "headers": {
        "Authorization": "Bearer ${BRIDGE_TOKEN}"
      }
    },
    "supabase": {
      "type": "http",
      "url": "https://mcp.supabase.com/mcp?project_ref=YOUR_REF&read_only=true&features=database,docs"
    }
  }
}
```

### Placeholder checklist

| Placeholder | Replace with |
|-------------|--------------|
| `YOUR-CODESPACE-8000.app.github.dev` | Real Codespaces forwarded URL (Ports panel) |
| `/mcp` path | Actual mount path from `server.py` (`/mcp` or `/sse`) |
| `${BRIDGE_TOKEN}` | Codespace secret or client secret store |
| `YOUR_REF` | Supabase `project_ref` |
| `read_only=true` / `features=…` | Scope to least privilege |

### Client placement (typical)

| Client | Config location |
|--------|-----------------|
| Cursor | `.cursor/mcp.json` or Settings → MCP |
| Claude Desktop | `claude_desktop_config.json` (often `mcpServers` key) |
| VS Code + Copilot | Copilot / workspace MCP settings |
| Windsurf / others | Product MCP panel or `mcp.json` |

---

# Combined summary

| Layer | Count / state |
|-------|----------------|
| Native Grok connectors (live assumed) | 7 core |
| Connectable catalog | 30+ |
| MCP servers in this publish | 3 (github · manus · supabase) |
| Built-in tool families | Web · Connected · Sandbox · Imagine image/video · Render |
| Skills | ~70+ |
| Model family | Grok 4.7 flagship + Imagine + Voice + Fast/Code variants |
| Effort knobs | low · medium · high · xhigh |
| Research path | Full synthesis stack (§7) |

---

**Publication complete.**  
References 1–8 combined into this single document.  
File: `SYSTEM_STATUS_PUBLISHED.md` under workspace artifacts.

---

*End of published system status.*
