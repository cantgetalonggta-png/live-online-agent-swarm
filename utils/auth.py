"""
SWARM_API_KEY authentication for FastAPI.
- If SWARM_API_KEY unset/empty: open dev mode.
- If set: require Authorization: Bearer or X-API-Key on protected routes.
- Optional SWARM_API_KEY_READ for GET-only.
Never log raw key values.
"""
from __future__ import annotations
import os
import hmac
import hashlib
from typing import Optional
from fastapi import Header, HTTPException, Request, status


def _get_write_key() -> str:
    return (os.getenv("SWARM_API_KEY") or "").strip()


def _get_read_key() -> str:
    return (os.getenv("SWARM_API_KEY_READ") or "").strip()


def auth_enabled() -> bool:
    return bool(_get_write_key())


def _extract_key(authorization: Optional[str], x_api_key: Optional[str]) -> Optional[str]:
    if x_api_key and x_api_key.strip():
        return x_api_key.strip()
    if authorization and authorization.lower().startswith("bearer "):
        return authorization[7:].strip()
    return None


def _match(provided: Optional[str], expected: str) -> bool:
    if not provided or not expected:
        return False
    # hash to fixed length so compare_digest always works
    a = hashlib.sha256(provided.encode("utf-8")).digest()
    b = hashlib.sha256(expected.encode("utf-8")).digest()
    return hmac.compare_digest(a, b)


async def require_api_key(
    request: Request,
    authorization: Optional[str] = Header(default=None),
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key"),
) -> str:
    write_key = _get_write_key()
    if not write_key:
        return "open"
    provided = _extract_key(authorization, x_api_key)
    if _match(provided, write_key):
        return "write"
    read_key = _get_read_key()
    if request.method in ("GET", "HEAD", "OPTIONS") and read_key and _match(provided, read_key):
        return "read"
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API key. Use Authorization: Bearer <SWARM_API_KEY> or X-API-Key.",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def require_write_key(
    authorization: Optional[str] = Header(default=None),
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key"),
) -> str:
    write_key = _get_write_key()
    if not write_key:
        return "open"
    provided = _extract_key(authorization, x_api_key)
    if _match(provided, write_key):
        return "write"
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Write API key required for this endpoint.",
        headers={"WWW-Authenticate": "Bearer"},
    )
