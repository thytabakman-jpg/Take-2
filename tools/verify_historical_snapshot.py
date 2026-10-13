#!/usr/bin/env python3
"""Optional validation of a restored historical mirror, not current authority."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIRROR = ROOT / "dump/full-system-sources"
MANIFEST = MIRROR / "PUBLIC_CORPUS_MANIFEST.json"


def main():
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        records = data["records"]
        seen = set()
        counts = {}
        for item in records:
            rel = item["path"]
            root_relative = Path(rel)
            if root_relative.is_absolute() or ".." in root_relative.parts:
                raise ValueError("unsafe record path: " + rel)
            if rel in seen:
                raise ValueError("duplicate manifest path: " + rel)
            seen.add(rel)
            if not rel.startswith("dump/full-system-sources/"):
                raise ValueError("unexpected record path: " + rel)
            path = ROOT / rel
            if not path.is_file():
                raise ValueError("recorded file missing: " + rel)
            blob = path.read_bytes()
            if len(blob) != item["bytes"]:
                raise ValueError("size mismatch: " + rel)
            if hashlib.sha256(blob).hexdigest() != item["sha256"]:
                raise ValueError("content mismatch: " + rel)
            section = rel.split("/")[2]
            counts[section] = counts.get(section, 0) + 1
        if data["total_files"] != len(records) or data["file_counts"] != counts:
            raise ValueError("manifest totals inconsistent")
        actual = {p.relative_to(ROOT).as_posix() for p in MIRROR.rglob("*")
                  if p.is_file() and p.name not in ("PUBLIC_CORPUS_MANIFEST.json", "SOURCE_HEADS.tsv")}
        if actual != seen:
            raise ValueError("unrecorded or absent mirror files: missing=%d extra=%d" %
                             (len(seen - actual), len(actual - seen)))
        print(json.dumps({"status": "PASS_HISTORICAL_ARCHIVE_ONLY",
                          "verified_files": len(records), "authority_certified": False}))
        return 0
    except (OSError, KeyError, ValueError, TypeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc),
                          "authority_certified": False}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
