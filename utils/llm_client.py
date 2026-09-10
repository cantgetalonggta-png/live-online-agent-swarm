"""
Multi-provider LLM hooks with graceful fallback.
Providers: anthropic | openai | grok | groq
If no keys: returns None / offline stub — swarm keeps working.
Never logs API keys.
"""
from __future__ import annotations
import os
import json
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional


def _env(*names: str) -> str:
    for n in names:
        v = (os.getenv(n) or "").strip()
        if v:
            return v
    return ""


class LLMClient:
    def __init__(self):
        self.primary = (os.getenv("LLM_PRIMARY") or "anthropic").strip().lower()
        self.fallback = (os.getenv("LLM_FALLBACK") or "groq").strip().lower()
        self.keys = {
            "openai": _env("OPENAI_API_KEY"),
            "anthropic": _env("ANTHROPIC_API_KEY", "ANTHROPIC_KEY"),
            "grok": _env("GROK_API_KEY", "XAI_API_KEY"),
            "groq": _env("GROQ_API_KEY"),
        }
        self.models = {
            "openai": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            "anthropic": os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-latest"),
            "grok": os.getenv("GROK_MODEL", "grok-2-latest"),
            "groq": os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
        }

    def available_providers(self) -> List[str]:
        return [p for p, k in self.keys.items() if k]

    def is_available(self) -> bool:
        return bool(self.available_providers())

    def status(self) -> Dict[str, Any]:
        return {
            "available": self.is_available(),
            "providers_configured": self.available_providers(),
            "primary": self.primary,
            "fallback": self.fallback,
            "keys_present": {p: bool(k) for p, k in self.keys.items()},
        }

    def complete(
        self,
        prompt: str,
        system: str = "You are a lawful public-record investigation assistant. Never invent private data. Prefer SOLID/MAYBE discipline. No bypass advice.",
        max_tokens: int = 800,
    ) -> Optional[str]:
        order = []
        for p in (self.primary, self.fallback, "groq", "anthropic", "openai", "grok"):
            if p not in order:
                order.append(p)
        last_err = None
        for provider in order:
            if not self.keys.get(provider):
                continue
            try:
                text = self._call(provider, prompt, system, max_tokens)
                if text:
                    return text
            except Exception as e:
                last_err = str(e)
                continue
        if last_err:
            return None
        return None

    def _call(self, provider: str, prompt: str, system: str, max_tokens: int) -> str:
        if provider == "openai":
            return self._openai_compatible(
                url="https://api.openai.com/v1/chat/completions",
                key=self.keys["openai"],
                model=self.models["openai"],
                prompt=prompt,
                system=system,
                max_tokens=max_tokens,
            )
        if provider == "groq":
            return self._openai_compatible(
                url="https://api.groq.com/openai/v1/chat/completions",
                key=self.keys["groq"],
                model=self.models["groq"],
                prompt=prompt,
                system=system,
                max_tokens=max_tokens,
            )
        if provider == "grok":
            return self._openai_compatible(
                url="https://api.x.ai/v1/chat/completions",
                key=self.keys["grok"],
                model=self.models["grok"],
                prompt=prompt,
                system=system,
                max_tokens=max_tokens,
            )
        if provider == "anthropic":
            return self._anthropic(prompt, system, max_tokens)
        raise ValueError(f"unknown provider {provider}")

    def _openai_compatible(self, url, key, model, prompt, system, max_tokens) -> str:
        body = {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": max_tokens,
            "temperature": 0.2,
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode(),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {key}",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
        return data["choices"][0]["message"]["content"]

    def _anthropic(self, prompt, system, max_tokens) -> str:
        body = {
            "model": self.models["anthropic"],
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": prompt}],
        }
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps(body).encode(),
            headers={
                "Content-Type": "application/json",
                "x-api-key": self.keys["anthropic"],
                "anthropic-version": "2023-06-01",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
        parts = data.get("content") or []
        texts = [p.get("text", "") for p in parts if p.get("type") == "text"]
        return "\n".join(texts).strip()


_llm: Optional[LLMClient] = None


def get_llm() -> LLMClient:
    global _llm
    if _llm is None:
        _llm = LLMClient()
    return _llm
