#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "dump" / "full-system-sources"
OUT = DEST / "PUBLIC_CORPUS_MANIFEST.json"

records = []
counts = {}
for repo in ("Take-3", "Take-4", "Take-5"):
    base = DEST / repo
    repo_records = []
    for p in sorted(base.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        data = p.read_bytes()
        repo_records.append({
            "path": rel,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        })
    counts[repo] = len(repo_records)
    records.extend(repo_records)

heads = {}
heads_file = DEST / "SOURCE_HEADS.tsv"
if heads_file.exists():
    for line in heads_file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        name, sha = line.split("\t", 1)
        heads[name] = sha

payload = {
    "schema": "TAKE2_FULL_SYSTEM_PUBLIC_CORPUS/v1",
    "source_heads": heads,
    "file_counts": counts,
    "total_files": len(records),
    "records": records,
    "private_source_boundary": {
        "repository": "Reaserch",
        "content_copied": False,
        "reason": "source is private while Take-2 is public; no private content is published by this consolidation",
    },
}
OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(json.dumps({"manifest": str(OUT.relative_to(ROOT)), "file_counts": counts, "total_files": len(records)}))
