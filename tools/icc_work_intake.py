#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys
R=Path(__file__).resolve().parents[1]
candidates=[p for p in R.rglob("*.md") if "challenge" in p.name.lower() and ".git" not in p.parts]
if not candidates:
 print("WORK INTAKE: FAIL; no challenge markdown found"); sys.exit(1)
items=[]
for p in sorted(candidates):
 text=p.read_text(errors="replace")
 items.append({"path":str(p.relative_to(R)),"sha256":hashlib.sha256(text.encode()).hexdigest(),"bytes":len(text)})
out={"status":"RECOGNIZED","count":len(items),"items":items,
     "next_state":"EXECUTION_REQUIRED",
     "invariant":"recognition is not completion"}
(R/"state").mkdir(exist_ok=True)
(R/"state"/"work_intake.json").write_text(json.dumps(out,indent=2)+"\n")
print(f"WORK INTAKE: PASS; recognized={len(items)}")
