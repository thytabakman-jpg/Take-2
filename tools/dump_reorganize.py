#!/usr/bin/env python3
"""Take-2 dump-and-reorganize runner.

Non-destructive by default: source files remain untouched. The runner inventories every
file, hashes it, classifies it, copies it into a stable organized tree, preserves
provenance in a machine-readable receipt, detects duplicates/collisions, and verifies
that every copied byte matches the source.

This is structural organization, not a claim of full semantic understanding.
Ambiguous files remain explicit in OPEN rather than being guessed into a category.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import re
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

TEXT_EXT = {".md",".txt",".rst",".org",".tex",".html",".htm"}
CODE_EXT = {".py",".js",".ts",".tsx",".jsx",".java",".c",".h",".cpp",".hpp",".rs",".go",".rb",".php",".sh",".ps1"}
DATA_EXT = {".json",".jsonl",".csv",".tsv",".xml",".parquet",".sqlite",".db"}
CONFIG_NAMES = {"Dockerfile","Makefile","Procfile"}
CONFIG_EXT = {".yaml",".yml",".toml",".ini",".cfg",".conf",".env"}
IMAGE_EXT = {".png",".jpg",".jpeg",".gif",".webp",".svg",".bmp",".tif",".tiff"}
ARCHIVE_EXT = {".zip",".tar",".gz",".tgz",".bz2",".xz",".7z",".rar"}

@dataclass(frozen=True)
class Record:
    source: str
    sha256: str
    bytes: int
    kind: str
    confidence: str
    destination: str | None
    disposition: str
    duplicate_of: str | None = None
    note: str | None = None

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def is_probably_text(path: Path) -> bool:
    try:
        sample = path.read_bytes()[:8192]
    except OSError:
        return False
    if b"\x00" in sample:
        return False
    try:
        sample.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False

def classify(path: Path) -> tuple[str, str, str | None]:
    name = path.name
    ext = path.suffix.lower()
    if name in CONFIG_NAMES or ext in CONFIG_EXT:
        return "config", "HIGH", None
    if ext in CODE_EXT:
        return "code", "HIGH", None
    if ext in DATA_EXT:
        return "data", "HIGH", None
    if ext in TEXT_EXT:
        return "documents", "HIGH", None
    if ext in IMAGE_EXT:
        return "images", "HIGH", None
    if ext in ARCHIVE_EXT:
        return "archives", "HIGH", None
    mime, _ = mimetypes.guess_type(name)
    if mime and mime.startswith("text/"):
        return "documents", "MEDIUM", f"mime:{mime}"
    if is_probably_text(path):
        return "documents", "MEDIUM", "utf8-text-with-unknown-extension"
    if ext:
        return "binary", "MEDIUM", f"unknown-binary-extension:{ext}"
    return "open", "LOW", "unclassified"

def clean_name(name: str) -> str:
    stem = re.sub(r"\s+", "-", name.strip())
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem)
    stem = re.sub(r"-+", "-", stem).strip("-")
    return stem or "unnamed"

def unique_destination(root: Path, kind: str, source: Path, sha: str) -> Path:
    folder = root / kind
    folder.mkdir(parents=True, exist_ok=True)
    base = clean_name(source.name)
    candidate = folder / base
    if not candidate.exists():
        return candidate
    if digest(candidate) == sha:
        return candidate
    p = Path(base)
    return folder / f"{p.stem}__{sha[:10]}{p.suffix}"

def load_manifest(source_root: Path) -> dict:
    path = source_root / "take2.json"
    if not path.exists():
        return {"id": source_root.name, "job": "organize-corpus", "protected": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        "id": str(data.get("id") or source_root.name),
        "job": str(data.get("job") or "organize-corpus"),
        "protected": list(data.get("protected") or []),
    }

def source_files(source_root: Path, output_root: Path) -> Iterable[Path]:
    output_resolved = output_root.resolve()
    for path in sorted(source_root.rglob("*")):
        if not path.is_file():
            continue
        try:
            path.resolve().relative_to(output_resolved)
            continue
        except ValueError:
            pass
        if path.name == "take2.json":
            continue
        yield path

def run(source_root: Path, output_root: Path) -> dict:
    source_root = source_root.resolve()
    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(source_root)
    records: list[Record] = []
    seen_hash: dict[str, str] = {}

    for src in source_files(source_root, output_root):
        rel = src.relative_to(source_root).as_posix()
        sha = digest(src)
        size = src.stat().st_size
        kind, confidence, note = classify(src)

        if sha in seen_hash:
            records.append(Record(rel, sha, size, kind, confidence, None, "DUPLICATE", seen_hash[sha], note))
            continue

        seen_hash[sha] = rel
        dest = unique_destination(output_root, kind, src, sha)
        if dest.exists() and digest(dest) == sha:
            disposition = "ALREADY_ORGANIZED"
        else:
            shutil.copy2(src, dest)
            disposition = "COPIED"
        if digest(dest) != sha:
            raise RuntimeError(f"verification failed for {rel}")
        records.append(Record(rel, sha, size, kind, confidence, dest.relative_to(output_root).as_posix(), disposition, None, note))

    accounted = {r.source for r in records}
    expected = {p.relative_to(source_root).as_posix() for p in source_files(source_root, output_root)}
    missing = sorted(expected - accounted)
    open_items = [r.source for r in records if r.kind == "open" or r.confidence == "LOW"]
    summary = {
        "schema_version": 1,
        "run_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(source_root),
        "output_root": str(output_root),
        "manifest": manifest,
        "counts": {
            "source_files": len(expected),
            "records": len(records),
            "duplicates": sum(r.disposition == "DUPLICATE" for r in records),
            "open": len(open_items),
        },
        "traversal_complete": not missing and len(records) == len(expected),
        "verification_complete": all(
            r.disposition == "DUPLICATE" or (
                r.destination is not None
                and (output_root / r.destination).exists()
                and digest(output_root / r.destination) == r.sha256
            )
            for r in records
        ),
        "missing": missing,
        "open": open_items,
        "records": [asdict(r) for r in records],
    }
    receipt = output_root / "_take2_receipt.json"
    receipt.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary

def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory, classify, reorganize, and verify a corpus.")
    parser.add_argument("source", type=Path, help="directory containing the material to ingest")
    parser.add_argument("--output", type=Path, default=None, help="organized output directory; default SOURCE/_organized")
    args = parser.parse_args()
    source = args.source
    if not source.is_dir():
        parser.error("source must be a directory")
    output = args.output or (source / "_organized")
    result = run(source, output)
    print(json.dumps({
        "source_files": result["counts"]["source_files"],
        "duplicates": result["counts"]["duplicates"],
        "open": result["counts"]["open"],
        "traversal_complete": result["traversal_complete"],
        "verification_complete": result["verification_complete"],
        "receipt": str((output / "_take2_receipt.json").resolve()),
    }, indent=2))
    return 0 if result["traversal_complete"] and result["verification_complete"] else 2

if __name__ == "__main__":
    raise SystemExit(main())
