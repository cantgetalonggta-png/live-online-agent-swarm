#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"assets"/"MASTERSKILLS_v1.json"
reg=json.loads(p.read_text())
skills=reg["skills"]
assert reg["skill_count"]==len(skills)
assert len({s["id"] for s in skills})==len(skills)
req={"id","name","domain_id","domain","category","trigger","inputs","outputs","execution_rules","version"}
for s in skills:
    assert req<=set(s), s["id"]
print("OK", len(skills), "skills")
