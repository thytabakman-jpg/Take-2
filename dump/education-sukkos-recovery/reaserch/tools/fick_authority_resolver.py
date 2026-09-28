#!/usr/bin/env python3
"""Bounded Fick authority resolver. Routing only; never mutation authority."""
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
MAP=ROOT/"projects/jewish-holiday-booklets/fick/generation/AUTHORITY_MAP.yaml"

def blob(path:Path)->str:
    return subprocess.check_output(["git","hash-object",str(path)],cwd=ROOT,text=True).strip()

def load(rel:str):
    p=(MAP.parent/rel).resolve()
    return p,yaml.safe_load(p.read_text(encoding="utf-8"))

def resolve(coord:str,page:str|None=None)->dict:
    m=yaml.safe_load(MAP.read_text(encoding="utf-8"))
    spec=m["coordinates"].get(coord)
    if not spec:
        return {"coordinate":coord,"status":"OPEN","reason":"coordinate_not_mapped"}
    p,doc=load(spec["owner"])
    out={"coordinate":coord,"owner":str(p.relative_to(ROOT)),"locator":spec["locator_rule"],
         "owner_blob":"blob:"+blob(p),"status":"PASS","identity":None}
    if coord=="current_canonical_set":
        out["identity"]=doc["object_identity"]["current_canonical_source_set"]
    elif coord=="exact_student_wording":
        frozen=doc["frozen_copy"]
        if str(frozen.get("status","")).lower()!="open" and frozen.get("git_blob_sha"):
            out["identity"]="blob:"+frozen["git_blob_sha"]
        else:
            out.update(status="OPEN",reason="frozen_copy_unresolved")
    elif coord=="product_acceptance":
        out["identity"]="acceptance:"+doc["acceptance_status"]["current_result"]
    elif coord=="production_semantics":
        out["identity"]="package:"+doc["package_id"]+"@blob:"+blob(p)
    elif coord=="canonical_page_bytes":
        if page not in {"P1","P2","P3","P4"}:
            out.update(status="OPEN",reason="page_specific_target_required")
        else:
            oid=f"JHB:FICK:C3:{page}"
            obj=next((x for x in doc.get("objects",[]) if x.get("id")==oid),None)
            if not obj or not obj.get("sha256") or not obj.get("library_file_id"):
                out.update(status="OPEN",reason="exact_page_identity_unresolved")
            else:
                out["locator"]=obj["library_file_id"]
                out["identity"]="sha256:"+obj["sha256"]
                out["object_id"]=oid
    elif coord in {"execution_binding","promotion_transition"}:
        out["identity"]="contract@blob:"+blob(p)
    else:
        out.update(status="OPEN",reason="no_resolution_strategy")
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("coordinate"); ap.add_argument("--page")
    a=ap.parse_args(); r=resolve(a.coordinate,a.page); print(json.dumps(r,indent=2))
    return 0 if r["status"]=="PASS" else 2
if __name__=="__main__": raise SystemExit(main())
