# H15 Public Deploy Report
UTC: 2026-09-10T02:31:46Z
HITL window expires: 2026-09-10T03:31:46Z (60 min from grant)
Region ops: America/Vancouver · public tunnels via Cloudflare (international edge)

## Local services (healthy)
| Service | Bind | Local health |
|---|---|---|
| FastAPI (uvicorn) | 0.0.0.0:8000 | /health = ok · HITL_REQUIRED=true · public_record_ceiling=true |
| Streamlit dashboard | 0.0.0.0:8501 | HTTP 200 |
| Roles | — | Supervisor, MemoryVault, PatternDetector, Anticipation, Compliance, OSINTCollector, TruthVerifier, ResearchPlanner, Synthesizer, LiveWebScout |

## Public URLs (Cloudflare quick tunnel — ephemeral)
| Surface | Public URL |
|---|---|
| **API** | https://gratuit-lambda-ipod-dublin.trycloudflare.com |
| **API docs** | https://gratuit-lambda-ipod-dublin.trycloudflare.com/docs |
| **API health** | https://gratuit-lambda-ipod-dublin.trycloudflare.com/health |
| **Dashboard** | https://airline-checkout-test-abu.trycloudflare.com |

## Tunnel status
- cloudflared registered: API location=iad08 · Dashboard location=iad15
- Prechecks: DNS/UDP/TCP/API PASS
- Note: sandbox DNS may lag resolving *.trycloudflare.com; external clients use CF anycast

## Security posture
- HITL_REQUIRED=true in runtime config
- PUBLIC_RECORD_CEILING=true
- No secrets in .env (example only)
- CORS open for demo (tighten for long-lived prod)
- Quick tunnels are temporary public — rotate/stop after HITL window

## Process PIDs (this host)
See `ps` snapshot in deploy log; managed via nohup.

## Rollback
```
pkill -f 'uvicorn api.app' || true
pkill -f 'streamlit run' || true
pkill -f 'cloudflared tunnel' || true
```
