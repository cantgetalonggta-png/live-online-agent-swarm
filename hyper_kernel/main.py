"""
Hyper-Automation Multi-Agent Webhook Kernel
- FastAPI webhook intake
- Optional CrewAI when installed
- GitHub / Vercel / Drive hooks via env tokens only
- Public-record ceiling; no secret-store clone
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
from fastapi import BackgroundTasks, FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(
    title="MA-OS Hyper-Automation Kernel",
    version="1.0.0",
    description="Webhook kernel for Drive/GitHub/Vercel auto-heal + evidence distill hooks",
)

ARTIFACTS = Path(os.environ.get("ARTIFACTS_DIR", "/workspace/artifacts"))
KERNEL_LOG = ARTIFACTS / "hyper_kernel_log.jsonl"


def log_event(event: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    event["ts"] = datetime.now(timezone.utc).isoformat()
    with KERNEL_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


def github_put(path: str, content: str, message: str) -> dict[str, Any]:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    owner = os.environ.get("GITHUB_OWNER", "cantgetalonggta-png")
    repo = os.environ.get("GITHUB_REPO", "ma-os-12-console")
    if not token:
        return {"ok": False, "error": "GITHUB_TOKEN missing"}
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    sha = None
    get_res = requests.get(url, headers=headers, timeout=30)
    if get_res.status_code == 200:
        sha = get_res.json().get("sha")
    payload: dict[str, Any] = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "branch": os.environ.get("GITHUB_BRANCH", "main"),
    }
    if sha:
        payload["sha"] = sha
    res = requests.put(url, headers=headers, json=payload, timeout=60)
    return {"ok": res.status_code in (200, 201), "status": res.status_code, "body": res.text[:500]}


def vercel_deploy_hint() -> dict[str, Any]:
    token = os.environ.get("VERCEL_TOKEN")
    if not token:
        return {
            "ok": False,
            "error": "VERCEL_TOKEN missing",
            "fallback": "Use Grok App Builder platform deploy or set VERCEL_TOKEN",
        }
    # Documented hook — project-specific deploy via CLI preferred
    return {
        "ok": True,
        "hint": "Run: vercel --prod --token $VERCEL_TOKEN",
        "token_present": True,
    }


def ollama_status() -> dict[str, Any]:
    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
    try:
        r = requests.get(f"{host.rstrip('/')}/api/tags", timeout=3)
        if r.status_code == 200:
            models = [m.get("name") for m in r.json().get("models", [])]
            return {"ok": True, "host": host, "models": models}
    except Exception as e:
        return {"ok": False, "host": host, "error": str(e)[:200]}
    return {"ok": False, "host": host, "error": f"HTTP {r.status_code}"}


def run_automation(payload: dict[str, Any]) -> dict[str, Any]:
    """Lightweight heal path without requiring CrewAI install."""
    log_event({"type": "webhook", "payload_keys": list(payload.keys())[:20]})
    result: dict[str, Any] = {
        "status": "processed",
        "ollama": ollama_status(),
        "vercel": vercel_deploy_hint(),
        "github": {"token_present": bool(os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"))},
        "actions": [],
    }
    # Optional: re-run evidence distill script if present
    distill = Path("/workspace/artifacts/swarm_os/artifacts/SKILL_TREE_ENGINE.py")
    if distill.exists() and payload.get("action") == "distill":
        try:
            out = subprocess.run(
                ["python3", str(distill)],
                capture_output=True,
                text=True,
                timeout=120,
                cwd="/workspace/artifacts/swarm_os",
            )
            result["actions"].append(
                {
                    "name": "skill_tree_engine",
                    "returncode": out.returncode,
                    "stdout_tail": (out.stdout or "")[-800:],
                }
            )
        except Exception as e:
            result["actions"].append({"name": "skill_tree_engine", "error": str(e)})
    # CrewAI optional
    if os.environ.get("ENABLE_CREWAI") == "1":
        try:
            result["crewai"] = "ENABLE_CREWAI set — install crewai + bind YAML to kickoff in production"
        except Exception as e:
            result["crewai_error"] = str(e)
    log_event({"type": "result", "result": result})
    return result


@app.get("/health")
def health():
    return {
        "ok": True,
        "service": "ma-os-hyper-kernel",
        "ollama": ollama_status(),
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/stack")
def stack():
    """Ollama hosting options + model routing catalog."""
    return {
        "ollama_local": ollama_status(),
        "ollama_cloud_options": [
            {"name": "Ollama Cloud (native)", "url": "https://docs.ollama.com/cloud", "cost": "free tier / usage", "notes": "ollama run cloud.qwen:7b offload"},
            {"name": "Elestio Managed Ollama", "url": "https://elest.io/open-source/ollama", "cost": "paid managed", "notes": "SSL, backups, Open WebUI"},
            {"name": "Koyeb One-Click Ollama", "url": "https://www.koyeb.com/deploy/ollama", "cost": "paid", "notes": "one-click template"},
            {"name": "RunPod GPU", "url": "https://www.runpod.io/", "cost": "pay-per-second GPU", "notes": "best perf"},
            {"name": "Thunder Compute", "url": "https://thundercompute.com/", "cost": "GPU cloud", "notes": "AI workflows"},
            {"name": "Hostkey", "url": "https://hostkey.com/apps/machine-learning/ollama-ai-chatbot/", "cost": "dedicated/VPS", "notes": "RTX preinstalled"},
            {"name": "Hostinger AI VPS", "url": "https://www.hostinger.com/ca/applications/ollama", "cost": "VPS", "notes": "Docker template"},
            {"name": "DigitalOcean / Linode / GCP", "url": "https://www.digitalocean.com/", "cost": "VM", "notes": "manual Docker install"},
        ],
        "model_routing": {
            "architect": os.environ.get("LLM_ARCHITECT", "openai/grok-4"),
            "coder": os.environ.get("LLM_CODER", "ollama/qwen2.5-coder:14b"),
            "compliance": os.environ.get("LLM_COMPLIANCE", "openai/gpt-4o-mini"),
            "distiller": os.environ.get("LLM_DISTILLER", "ollama/llama3.2:3b"),
        },
        "swarm_repos": {
            "live_online_agent_swarm": "https://github.com/cantgetalonggta-png/live-online-agent-swarm",
            "ma_os_12_console": "https://github.com/cantgetalonggta-png/ma-os-12-console",
            "strand_1953": "https://github.com/cantgetalonggta-png/strand-1953-trust-efta-ia-evidence",
            "detective_codex": "https://github.com/cantgetalonggta-png/detective-codex-vault",
            "epstein_core_web": "https://github.com/cantgetalonggta-png/epstein-core-web-automation",
            "note": "live-online-agent-subswarm / background-swarm names not found as separate repos; treated as architecture layers inside live-online-agent-swarm",
        },
        "policy": "Public-record ceiling · HITL · no third-party secret reuse",
    }


@app.post("/webhooks/all-platforms")
async def intercept_system_webhook(request: Request, background_tasks: BackgroundTasks):
    try:
        payload = await request.json()
    except Exception:
        payload = {"raw": True}
    background_tasks.add_task(run_automation, payload if isinstance(payload, dict) else {"data": payload})
    return {"status": "queued", "message": "MA-OS Hyper-Agent loop initialized"}


@app.post("/webhooks/sync")
async def sync_webhook(request: Request):
    """Synchronous processing for local testing."""
    try:
        payload = await request.json()
    except Exception:
        payload = {}
    return run_automation(payload if isinstance(payload, dict) else {})


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("KERNEL_PORT", "8090"))
    uvicorn.run(app, host="0.0.0.0", port=port)
