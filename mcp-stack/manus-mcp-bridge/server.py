"""
Manus MCP Bridge — HTTP MCP endpoint for Codespaces / remote clients.
Auth: Authorization: Bearer <BRIDGE_TOKEN>
Upstream: MANUS_API_KEY (optional) for Manus API calls.
No secrets are hardcoded; read from environment only.
"""
from __future__ import annotations

import os
import time
from typing import Any, Optional

import httpx
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Manus MCP Bridge", version="1.0.0")

BRIDGE_TOKEN = os.environ.get("BRIDGE_TOKEN", "")
MANUS_API_KEY = os.environ.get("MANUS_API_KEY", "")
MANUS_API_BASE = os.environ.get("MANUS_API_BASE", "https://api.manus.im")  # override if needed
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8000"))


def require_bridge_auth(authorization: Optional[str]) -> None:
    if not BRIDGE_TOKEN:
        # Dev mode: allow if no token configured (Codespace should set one)
        return
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")
    token = authorization.removeprefix("Bearer ").strip()
    if token != BRIDGE_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid bridge token")


@app.get("/health")
async def health():
    return {
        "ok": True,
        "service": "manus-mcp-bridge",
        "bridge_token_configured": bool(BRIDGE_TOKEN),
        "manus_key_configured": bool(MANUS_API_KEY),
        "ts": int(time.time()),
    }


@app.get("/")
async def root():
    return {
        "name": "manus-mcp-bridge",
        "mcp": "/mcp",
        "health": "/health",
        "docs": "/docs",
    }


# Minimal MCP-like tool surface (expand when Manus API schema is known)
class ToolCall(BaseModel):
    name: str
    arguments: dict[str, Any] = {}


@app.get("/mcp")
@app.post("/mcp")
async def mcp_endpoint(
    request: Request,
    authorization: Optional[str] = Header(default=None),
):
    require_bridge_auth(authorization)
    # SSE/HTTP MCP clients often probe GET; return capabilities
    if request.method == "GET":
        return {
            "protocol": "mcp-http-bridge",
            "version": "1.0",
            "tools": [
                {
                    "name": "manus_status",
                    "description": "Check Manus API connectivity and bridge health",
                },
                {
                    "name": "manus_proxy",
                    "description": "Proxy a GET/POST to MANUS_API_BASE (path + optional body)",
                },
            ],
        }
    try:
        body = await request.json()
    except Exception:
        body = {}
    method = body.get("method") or body.get("name") or "tools/list"
    if method in ("tools/list", "list_tools"):
        return {
            "tools": [
                {"name": "manus_status", "description": "Bridge + Manus key status"},
                {
                    "name": "manus_proxy",
                    "description": "Proxy request to Manus API",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "path": {"type": "string"},
                            "method": {"type": "string", "default": "GET"},
                            "json": {"type": "object"},
                        },
                        "required": ["path"],
                    },
                },
            ]
        }
    # tool call
    name = body.get("name") or (body.get("params") or {}).get("name")
    args = body.get("arguments") or (body.get("params") or {}).get("arguments") or {}
    if name == "manus_status" or method == "manus_status":
        return await manus_status()
    if name == "manus_proxy" or method == "manus_proxy":
        return await manus_proxy(args)
    return JSONResponse({"error": f"unknown method/tool: {method}/{name}"}, status_code=400)


async def manus_status():
    status: dict[str, Any] = {
        "bridge": "ok",
        "manus_key_configured": bool(MANUS_API_KEY),
        "manus_api_base": MANUS_API_BASE,
    }
    if not MANUS_API_KEY:
        status["manus"] = "skipped (no MANUS_API_KEY)"
        return status
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            r = await client.get(
                f"{MANUS_API_BASE.rstrip('/')}/v1/health",
                headers={"Authorization": f"Bearer {MANUS_API_KEY}"},
            )
            status["manus_http"] = r.status_code
            status["manus_body"] = r.text[:500]
    except Exception as e:
        status["manus_error"] = str(e)
    return status


async def manus_proxy(args: dict[str, Any]):
    if not MANUS_API_KEY:
        raise HTTPException(status_code=503, detail="MANUS_API_KEY not configured")
    path = args.get("path") or "/"
    method = (args.get("method") or "GET").upper()
    url = f"{MANUS_API_BASE.rstrip('/')}/{path.lstrip('/')}"
    async with httpx.AsyncClient(timeout=60.0) as client:
        r = await client.request(
            method,
            url,
            headers={"Authorization": f"Bearer {MANUS_API_KEY}"},
            json=args.get("json"),
        )
        return {
            "status_code": r.status_code,
            "headers": dict(r.headers),
            "text": r.text[:8000],
        }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", host=HOST, port=PORT, reload=False)
