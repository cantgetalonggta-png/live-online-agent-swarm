"""
Tavily public web search hook.
If TAVILY_API_KEY missing: returns empty results (offline demo path).
Public-record ceiling: caller must still enforce domain/policy.
"""
from __future__ import annotations
import os
import json
import urllib.request
from typing import Any, Dict, List, Optional


class TavilyClient:
    def __init__(self):
        self.api_key = (os.getenv("TAVILY_API_KEY") or "").strip()
        self.base = "https://api.tavily.com"

    def is_available(self) -> bool:
        return bool(self.api_key)

    def status(self) -> Dict[str, Any]:
        return {"available": self.is_available(), "key_present": bool(self.api_key)}

    def search(
        self,
        query: str,
        max_results: int = 5,
        search_depth: str = "basic",
        include_answer: bool = False,
    ) -> Dict[str, Any]:
        if not self.api_key:
            return {
                "query": query,
                "results": [],
                "provider": "tavily",
                "status": "skipped_no_key",
                "note": "Set TAVILY_API_KEY for live public search",
            }
        body = {
            "api_key": self.api_key,
            "query": query,
            "max_results": max_results,
            "search_depth": search_depth,
            "include_answer": include_answer,
        }
        req = urllib.request.Request(
            f"{self.base}/search",
            data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode())
        # Normalize
        results = []
        for r in data.get("results") or []:
            results.append(
                {
                    "title": r.get("title"),
                    "url": r.get("url"),
                    "content": (r.get("content") or "")[:1000],
                    "score": r.get("score"),
                }
            )
        return {
            "query": query,
            "results": results,
            "answer": data.get("answer"),
            "provider": "tavily",
            "status": "ok",
        }


_tavily: Optional[TavilyClient] = None


def get_tavily() -> TavilyClient:
    global _tavily
    if _tavily is None:
        _tavily = TavilyClient()
    return _tavily
