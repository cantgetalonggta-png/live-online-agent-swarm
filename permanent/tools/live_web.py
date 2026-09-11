"""Live public web search/fetch — no API keys required (DuckDuckGo HTML + urllib).
Public-record ceiling: only public URLs; no auth walls bypassed.
"""
from __future__ import annotations
import json
import re
import time
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional

USER_AGENT = "PermanentAgentSwarm/2.1 (+public-research; no secrets)"
TIMEOUT = 12

def _get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")

def live_public_search(query: str, max_results: int = 5) -> Dict[str, Any]:
    """DuckDuckGo HTML lite search — public results only."""
    q = query.strip()
    if not q:
        return {"status": "error", "error": "empty query", "results": []}
    # Block clearly non-public intent tokens (ceiling)
    blocked = ["password dump", "private key", "doxx", "ssn list"]
    low = q.lower()
    for b in blocked:
        if b in low:
            return {"status": "blocked", "error": f"ceiling: {b}", "results": []}
    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": q})
    try:
        html = _get(url)
    except Exception as e:
        return {"status": "error", "error": str(e), "results": [], "query": q}
    # Parse result links
    results: List[Dict[str, str]] = []
    # uddg redirect links
    for m in re.finditer(r'uddg=([^&"]+)', html):
        if len(results) >= max_results:
            break
        link = urllib.parse.unquote(m.group(1))
        if not link.startswith("http"):
            continue
        if any(r["url"] == link for r in results):
            continue
        results.append({"url": link, "title": link.split("/")[2] if "://" in link else link})
    # Also try result__a anchors
    for m in re.finditer(r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.I | re.S):
        if len(results) >= max_results:
            break
        href = m.group(1)
        title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if "uddg=" in href:
            um = re.search(r"uddg=([^&]+)", href)
            if um:
                href = urllib.parse.unquote(um.group(1))
        if not href.startswith("http"):
            continue
        if any(r["url"] == href for r in results):
            continue
        results.append({"url": href, "title": title or href})
    return {
        "status": "ok",
        "query": q,
        "n": len(results),
        "results": results[:max_results],
        "ts": time.time(),
        "provider": "duckduckgo_html",
        "ceiling": "public_only",
    }

def fetch_public_url(url: str, max_chars: int = 4000) -> Dict[str, Any]:
    if not url.startswith("http"):
        return {"status": "error", "error": "only http(s)"}
    try:
        body = _get(url)
        text = re.sub(r"<script[\s\S]*?</script>", " ", body, flags=re.I)
        text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return {"status": "ok", "url": url, "text": text[:max_chars], "n_chars": len(text)}
    except Exception as e:
        return {"status": "error", "url": url, "error": str(e)}
