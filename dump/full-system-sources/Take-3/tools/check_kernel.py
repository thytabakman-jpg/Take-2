#!/usr/bin/env python3
from pathlib import Path
import yaml

root=Path(__file__).resolve().parents[1]
k=yaml.safe_load((root/"KERNEL.yaml").read_text())
assert k["experiment"]=="take_3_clean_room"
assert k["loop"]==["TASK","DISCOVER","DECIDE","ACT","VERIFY","REENTER"]
assert set(k["records"])=={"task","finding","action","result"}
for name,spec in k["records"].items():
    assert spec["required"], name
assert "authority_does_not_follow_from_evidence" in k["protected"]
print("Take-3 kernel fitness: PASS")
