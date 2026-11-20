#!/usr/bin/env python3
from pathlib import Path
import yaml,sys
from legacy_reference import legacy_reference
R=Path(__file__).resolve().parents[1]
k=yaml.safe_load((R/"KERNEL.yaml").read_text())
l=yaml.safe_load((R/"state/ledger.yaml").read_text())
pd=yaml.safe_load(legacy_reference("pd/CORE.yaml").read_text(encoding="utf-8"))
errors=[]
required=k["primitives"]
ids={}
for group in ["objects","relations","events","transitions","observations"]:
 for x in l.get(group,[]):
  if x.get("id") in ids: errors.append(f"duplicate id {x.get('id')}")
  ids[x.get("id")]=group
  primitive=group[:-1] if group!="observations" else "observation"
  miss=[f for f in required[primitive]["required"] if f not in x]
  if miss: errors.append(f"{x.get('id')} missing {miss}")
obj={x["id"] for x in l.get("objects",[])}
for x in l.get("relations",[]):
 for end in ["source","target"]:
  if x[end] not in obj: errors.append(f"{x['id']} dangling {end} {x[end]}")
stable={x["id"] for x in pd.get("stable",[])}
experimental={x["id"] for x in pd.get("experimental",[])}
if stable & experimental: errors.append("PD capability both stable and experimental")
if not stable: errors.append("no stable PD capabilities")
if errors:
 print("KERNEL FITNESS: FAIL")
 print("\n".join(errors));sys.exit(1)
print(f"KERNEL FITNESS: PASS; objects={len(obj)} stable_pd={len(stable)} experimental_pd={len(experimental)}")
