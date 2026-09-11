#!/usr/bin/env python3
"""SelfMetrics background daemon — writes pulse JSONL forever (or N ticks)."""
from __future__ import annotations
import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.registry import REGISTRY


def tick(path: Path, phase: str = "daemon"):
    pulse = REGISTRY.call("pulse", phase=phase)
    ready = REGISTRY.readiness()
    row = {
        "ts": time.time(),
        "phase": phase,
        "pulse": pulse,
        "live_web": ready.get("live_web"),
        "agents_bound": ready.get("agents_bound"),
        "tools_impl": ready.get("tools_impl"),
        "always_online_policy": True,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--interval", type=int, default=30)
    ap.add_argument("--ticks", type=int, default=0, help="0 = forever")
    ap.add_argument("--path", default=str(ROOT / "vault" / "metrics.jsonl"))
    args = ap.parse_args()
    path = Path(args.path)
    n = 0
    print(json.dumps({"daemon": "self_metrics", "interval": args.interval, "always_online": True}))
    while True:
        row = tick(path)
        print(json.dumps({"tick": n, "live_web": row["live_web"]}))
        n += 1
        if args.ticks and n >= args.ticks:
            break
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
