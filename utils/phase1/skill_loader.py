"""
M1.4 Skill-tree loader — Load 200-node GOD-TIER skill tree from JSON.
Query by domain / id. Used by Supervisor and Self-Learning phase.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULT_TREE = Path("docs/GOD_TIER_SYSTEM/II_SKILL_TREE/SKILL_TREE_200_NODES.json")
FALLBACK_TREE = Path("skills/master-skill-encyclopedia/MASTERSKILLS_v1.json")


class SkillTreeLoader:
    def __init__(self, tree_path: Optional[Path] = None):
        self.tree_path = Path(tree_path) if tree_path else DEFAULT_TREE
        self.nodes: List[Dict[str, Any]] = []
        self.by_id: Dict[str, Dict[str, Any]] = {}
        self.by_domain: Dict[str, List[Dict[str, Any]]] = {}
        self._loaded = False

    def load(self) -> int:
        path = self.tree_path
        if not path.exists():
            path = FALLBACK_TREE
        if not path.exists():
            self.nodes = []
            self._loaded = True
            return 0

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Support both list-of-nodes and {nodes: [...]} shapes
        if isinstance(data, list):
            nodes = data
        elif isinstance(data, dict):
            nodes = data.get("nodes") or data.get("skills") or data.get("skill_tree") or []
            if not nodes and all(isinstance(v, dict) for v in data.values()):
                nodes = list(data.values())
        else:
            nodes = []

        self.nodes = nodes
        self.by_id = {}
        self.by_domain = {}
        for n in nodes:
            if not isinstance(n, dict):
                continue
            nid = str(n.get("id") or n.get("node_id") or n.get("name") or "")
            if nid:
                self.by_id[nid] = n
            domain = str(n.get("domain") or n.get("category") or "general")
            self.by_domain.setdefault(domain, []).append(n)

        self._loaded = True
        return len(self.nodes)

    def ensure_loaded(self) -> None:
        if not self._loaded:
            self.load()

    def get(self, node_id: str) -> Optional[Dict[str, Any]]:
        self.ensure_loaded()
        return self.by_id.get(node_id)

    def query_domain(self, domain: str) -> List[Dict[str, Any]]:
        self.ensure_loaded()
        return list(self.by_domain.get(domain, []))

    def domains(self) -> List[str]:
        self.ensure_loaded()
        return sorted(self.by_domain.keys())

    def stats(self) -> Dict[str, Any]:
        self.ensure_loaded()
        return {
            "total_nodes": len(self.nodes),
            "domains": {d: len(v) for d, v in self.by_domain.items()},
            "path": str(self.tree_path),
            "loaded": self._loaded,
        }

    def search(self, text: str, limit: int = 20) -> List[Dict[str, Any]]:
        self.ensure_loaded()
        q = text.lower().strip()
        if not q:
            return self.nodes[:limit]
        hits = []
        for n in self.nodes:
            blob = json.dumps(n, default=str).lower()
            if q in blob:
                hits.append(n)
            if len(hits) >= limit:
                break
        return hits


_default: Optional[SkillTreeLoader] = None


def get_skill_tree() -> SkillTreeLoader:
    global _default
    if _default is None:
        _default = SkillTreeLoader()
        _default.load()
    return _default
