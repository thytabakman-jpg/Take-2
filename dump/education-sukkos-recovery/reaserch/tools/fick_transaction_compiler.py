#!/usr/bin/env python3
"""Compile one approved Fick delta into an immutable transaction or typed blockers."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from fick_authority_resolver import resolve

REQ={"schema_version","delta_id","target","target_identity","operation_type","required_coordinates","basis","authorized_change","affected_scope","protected_state","verification_requirements","approval_authority","status"}

def compile_delta(d:dict)->dict:
    missing=sorted(REQ-set(d))
    if missing: return {"result":"BLOCKED","blockers":[{"type":"MISSING_FIELD","field":x} for x in missing]}
    if d["status"]!="APPROVED": return {"result":"BLOCKED","blockers":[{"type":"DELTA_NOT_APPROVED","status":d["status"]}]}
    for k in ("basis","authorized_change","affected_scope","protected_state","verification_requirements"):
        if not isinstance(d[k],list) or not d[k]:
            return {"result":"BLOCKED","blockers":[{"type":"INVALID_BOUNDED_FIELD","field":k}]}
    if d["affected_scope"]!=[d["target"]]:
        return {"result":"BLOCKED","blockers":[{"type":"OVERSIZED_OR_AMBIGUOUS_SCOPE","scope":d["affected_scope"],"target":d["target"]}]}
    if not isinstance(d["required_coordinates"],list) or not d["required_coordinates"]:
        return {"result":"BLOCKED","blockers":[{"type":"NO_REQUIRED_COORDINATES"}]}
    page=d["target"].split(":")[-1] if d["target"].startswith("JHB:FICK:C3:P") else None
    resolved=[]; blockers=[]
    for c in d["required_coordinates"]:
        r=resolve(c,page if c=="canonical_page_bytes" else None); resolved.append(r)
        if r["status"]!="PASS": blockers.append({"type":"DEPENDENCY_"+r["status"],"coordinate":c,"reason":r.get("reason")})
    src=next((x for x in resolved if x["coordinate"]=="canonical_page_bytes"),None)
    if src and src.get("identity")!=d["target_identity"]:
        blockers.append({"type":"TARGET_IDENTITY_MISMATCH","expected":d["target_identity"],"resolved":src.get("identity")})
    if blockers: return {"result":"BLOCKED","delta_id":d["delta_id"],"blockers":blockers,"resolved":resolved}
    return {"result":"COMPILED_TRANSACTION","transaction":{
      "transaction_id":"TX:"+d["delta_id"],"delta_id":d["delta_id"],"target":d["target"],
      "target_identity":d["target_identity"],"operation_type":d["operation_type"],
      "authorized_change":d["authorized_change"],"affected_scope":d["affected_scope"],
      "protected_state":d["protected_state"],"verification_requirements":d["verification_requirements"],
      "approval_authority":d["approval_authority"],"resolved_authorities":resolved
    }}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("approved_delta")
    a=ap.parse_args(); d=json.loads(Path(a.approved_delta).read_text()); out=compile_delta(d)
    print(json.dumps(out,indent=2)); return 0 if out["result"]=="COMPILED_TRANSACTION" else 2
if __name__=="__main__": raise SystemExit(main())
