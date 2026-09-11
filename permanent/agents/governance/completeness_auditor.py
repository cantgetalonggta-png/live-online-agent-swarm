"""CompletenessAuditor — investigation atlas completion scoring."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List
from agents.base import BaseAgent
from tools.registry import REGISTRY

ATLAS_CANDIDATES = [
    Path("/workspace/artifacts/investigation-complete/COMPLETION_ATLAS.json"),
    Path("investigation/COMPLETION_ATLAS.json"),
]


class CompletenessAuditorAgent(BaseAgent):
    plane = "governance"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.log("Completeness audit of investigation atlas")
        atlas_path = None
        for p in ATLAS_CANDIDATES:
            if p.exists():
                atlas_path = p
                break
        if not atlas_path:
            return {"status": "missing_atlas", "score": 0.0}

        data = json.loads(atlas_path.read_text(encoding="utf-8"))
        pipes = data.get("pipelines") or []
        associates = data.get("associates_public") or []
        dms = data.get("discovery_methods") or []
        scores: List[Dict[str, Any]] = []
        total = 0.0
        for p in pipes:
            status = p.get("status", "")
            if p.get("completeness_hint") is not None:
                s = float(p["completeness_hint"])
            else:
                wp = len(p.get("waypoints") or [])
                roles = len(p.get("roles") or []) if isinstance(p.get("roles"), list) else (1 if p.get("roles") else 0)
                tl = len(p.get("timeline") or [])
                exhibits = len(p.get("exhibits") or [])
                nxt = len(p.get("next") or [])
                s = min(100.0, wp * 8 + roles * 5 + tl * 4 + exhibits * 3 + nxt * 2)
                if status == "paused_CONTRADICTED":
                    s = min(s, 40.0)
                if status == "active" and s < 30:
                    s += 10
            scores.append({"id": p.get("id"), "name": p.get("name"), "score": round(s, 1), "status": status})
            total += s
        overall = round(total / max(len(pipes), 1), 1)
        report = {
            "status": "ok",
            "overall_completion_pct": overall,
            "pipelines": scores,
            "n_associates": len(associates),
            "n_discovery_methods": len(dms),
            "ceiling": data.get("ceiling"),
            "gaps": [s for s in scores if s["score"] < 50],
        }
        REGISTRY.call("report_write", title="completeness_audit", body=json.dumps(report)[:1500])
        REGISTRY.call("audit_write", event="completeness_audit", payload={"overall": overall})
        return {**report, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}
