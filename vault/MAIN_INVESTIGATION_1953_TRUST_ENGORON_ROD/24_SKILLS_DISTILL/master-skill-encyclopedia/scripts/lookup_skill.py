#!/usr/bin/env python3
import json,sys
from pathlib import Path
reg=json.loads((Path(__file__).resolve().parents[1]/"assets"/"MASTERSKILLS_v1.json").read_text())
q=" ".join(sys.argv[1:]).lower()
hits=[s for s in reg["skills"] if not q or q in " ".join([s["id"],s["category"],s["trigger"],s["domain"]," ".join(s["inputs"])," ".join(s["outputs"])]).lower()]
for s in hits[:25]:
    print(f"{s['id']:32} D{s['domain_id']}  {s['trigger'][:70]}")
print(f"// {len(hits)} hits")
