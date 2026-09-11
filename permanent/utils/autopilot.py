"""Self-directed autopilot goal queue — HITL for external/irreversible."""
from __future__ import annotations
import json
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULT_GOALS = [
    "Index public FOIA EpsteinDocs archive.org listings",
    "Map DocumentCloud NPA exhibit page titles only",
    "Refresh Maxwell conviction public timeline anchors",
    "Scan justice.gov FOIA guide deadlines",
    "Catalog public ACRIS-related press for 301 E 66",
]


class AutopilotQueue:
    def __init__(self, path: str = "vault/autopilot_goals.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            for g in DEFAULT_GOALS:
                self.enqueue(g, source="seed", priority=5)

    def enqueue(self, goal: str, source: str = "self", priority: int = 5, meta: Optional[Dict] = None) -> Dict[str, Any]:
        row = {
            "id": str(uuid.uuid4())[:10],
            "ts": time.time(),
            "goal": goal,
            "source": source,
            "priority": priority,
            "status": "queued",
            "meta": meta or {},
            "public_ceiling": True,
        }
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return row

    def list_queued(self) -> List[Dict[str, Any]]:
        out = []
        if not self.path.exists():
            return out
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("status") == "queued":
                out.append(row)
        out.sort(key=lambda r: (-r.get("priority", 0), r.get("ts", 0)))
        return out

    def next_goal(self) -> Optional[Dict[str, Any]]:
        q = self.list_queued()
        return q[0] if q else None

    def mark_done(self, goal_id: str) -> None:
        rows = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("id") == goal_id:
                row["status"] = "done"
                row["done_ts"] = time.time()
            rows.append(row)
        self.path.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + ("\n" if rows else ""),
            encoding="utf-8",
        )
