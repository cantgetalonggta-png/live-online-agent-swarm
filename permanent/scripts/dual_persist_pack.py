#!/usr/bin/env python3
"""Package key artifacts for Drive+GitHub dual-persist (no secrets)."""
from __future__ import annotations
import json
import shutil
import tarfile
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
ART = Path("/workspace/artifacts")
OUT = ART / "tmp" / "dual-persist-pack"
OUT.mkdir(parents=True, exist_ok=True)

# Never pack secrets
BLOCK = {"keys.env", "god_tier_keys.env", "api-keys-secret-store", "fourth_round.env", ".env"}

def copy_tree(src: Path, dest: Path):
    if not src.exists():
        return
    if src.is_file():
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.name in BLOCK:
            return
        shutil.copy2(src, dest)
        return
    for p in src.rglob("*"):
        if p.is_dir():
            continue
        if p.name in BLOCK or "secret" in p.name.lower() and p.suffix == ".env":
            continue
        rel = p.relative_to(src)
        d = dest / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, d)

# packs
copy_tree(ROOT, OUT / "permanent-agent-swarm")
copy_tree(ART / "investigation-complete", OUT / "investigation-complete")
copy_tree(ART / "drive-delta-2026-09-11", OUT / "drive-delta-2026-09-11")
copy_tree(ART / "skill-packages" / "investigation-interactive", OUT / "skills" / "investigation-interactive")
copy_tree(ART / "skill-packages" / "permanent-agent-swarm", OUT / "skills" / "permanent-agent-swarm")
copy_tree(ART / "skill-packages" / "always-online-swarm", OUT / "skills" / "always-online-swarm")
copy_tree(ART / "skill-packages" / "drive-delta-distill", OUT / "skills" / "drive-delta-distill")

manifest = {
    "as_of": datetime.now(timezone.utc).isoformat(),
    "ceiling": "public_only_no_secrets",
    "packs": [p.name for p in OUT.iterdir()],
}
(OUT / "MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
tgz = ART / f"dual-persist-always-online-{datetime.now(timezone.utc).strftime('%Y%m%d')}.tar.gz"
with tarfile.open(tgz, "w:gz") as tar:
    tar.add(OUT, arcname="dual-persist-pack")
print(json.dumps({"tgz": str(tgz), "manifest": manifest}, indent=2))
