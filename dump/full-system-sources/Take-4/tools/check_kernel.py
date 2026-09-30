#!/usr/bin/env python3
from pathlib import Path
import yaml

root=Path(__file__).resolve().parents[1]
k=yaml.safe_load((root/"KERNEL.yaml").read_text())
assert k["experiment"]=="take_4_informed_reconstruction"
assert k["loop"]==["ORIENT","NAVIGATE","RESOLVE","SELECT","EXECUTE","VERIFY","UPDATE","RESELECT"]
assert k["inheritance_rule"]=="inherit_evidence_not_architecture"
assert k["external_corpora"]["reaserch"]=="thytabakman-jpg/Reaserch"
assert k["promoted_runtime_external"]=="IC-2026-09-23-018"
for p in ["project_local_authority","OPEN","INCOMPARABLE","semantic_runtime_authority_separation"]:
    assert p in k["protected"]
print("Take-4 kernel fitness: PASS")
