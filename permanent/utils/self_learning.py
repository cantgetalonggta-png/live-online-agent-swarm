"""Self-learning SkillProposalQueue — HITL-gated proposals only."""
from __future__ import annotations
import json
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional


class SkillProposalQueue:
    """Append-only proposal log. Apply only after HITL approval."""

    def __init__(self, path: str = "vault/skill_proposals.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8")

    def propose(
        self,
        skill: str,
        change: str,
        rationale: str,
        agent: str,
        meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        prop = {
            "id": str(uuid.uuid4())[:12],
            "ts": time.time(),
            "skill": skill,
            "change": change,
            "rationale": rationale,
            "agent": agent,
            "status": "pending",
            "hitl_required": True,
            "meta": meta or {},
        }
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(prop, ensure_ascii=False) + "\n")
        return prop

    def list_pending(self) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        if not self.path.exists():
            return out
        for line in self.path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("status") == "pending":
                out.append(row)
        return out

    def approve(self, prop_id: str, operator: str = "HITL") -> Dict[str, Any]:
        """Mark proposal approved (does not auto-apply code changes)."""
        rows = []
        found = None
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("id") == prop_id and row.get("status") == "pending":
                row["status"] = "approved"
                row["approved_by"] = operator
                row["approved_ts"] = time.time()
                found = row
            rows.append(row)
        self.path.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + ("\n" if rows else ""),
            encoding="utf-8",
        )
        return found or {"status": "not_found", "id": prop_id}

    def reject(self, prop_id: str, reason: str = "") -> Dict[str, Any]:
        rows = []
        found = None
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("id") == prop_id and row.get("status") == "pending":
                row["status"] = "rejected"
                row["reject_reason"] = reason
                row["rejected_ts"] = time.time()
                found = row
            rows.append(row)
        self.path.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + ("\n" if rows else ""),
            encoding="utf-8",
        )
        return found or {"status": "not_found", "id": prop_id}
