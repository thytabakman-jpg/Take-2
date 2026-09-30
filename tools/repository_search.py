#!/usr/bin/env python3
"""Deterministic repository search fallback for Take-2.

GitHub code search can temporarily report a repository as unindexed. This tool builds a
derived, non-authoritative inverted index from the checked-out repository so discovery
does not depend on GitHub's external code-search index.

The index is deterministic, sharded, and freshness-checked against a content fingerprint.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = ROOT / "search_index"
SCHEMA_VERSION = 1

TEXT_EXTENSIONS = {
    ".md", ".txt", ".rst", ".org", ".tex", ".html", ".htm",
    ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".c", ".h", ".cpp", ".hpp",
    ".rs", ".go", ".rb", ".php", ".sh", ".ps1",
    ".json", ".jsonl", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env",
    ".csv", ".tsv", ".xml",
}
TEXT_NAMES = {"Dockerfile", "Makefile", "Procfile"}
SKIP_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "venv"}
TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{1,63}")
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def shard_for(token: str) -> str:
    first = token[0].lower()
    return first if first.isalnum() else "_"


def tokenize(text: str) -> set[str]:
    return {m.group(0).lower() for m in TOKEN_RE.finditer(text)}


def source_files(root: Path) -> list[Path]:
    out = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel.parts and rel.parts[0] == "search_index":
            continue
        if any(part in SKIP_PARTS for part in rel.parts):
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS or path.name in TEXT_NAMES:
            out.append(path)
    return out


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8-sig")
    except (UnicodeDecodeError, OSError):
        return None


def title_for(path: Path, text: str) -> str | None:
    if path.suffix.lower() == ".md":
        match = HEADING_RE.search(text)
        if match:
            return match.group(1).strip()[:200]
    return None


def content_fingerprint(records: list[tuple[str, str]]) -> str:
    h = hashlib.sha256()
    for rel, digest in records:
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(digest.encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def build_index(root: Path = ROOT, index_dir: Path | None = None) -> dict:
    root = root.resolve()
    index_dir = (index_dir or (root / "search_index")).resolve()

    docs: list[dict] = []
    postings: dict[str, set[int]] = {}
    fingerprints: list[tuple[str, str]] = []
    unreadable: list[str] = []

    for path in source_files(root):
        rel = path.relative_to(root).as_posix()
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        fingerprints.append((rel, digest))
        text = read_text(path)
        if text is None:
            unreadable.append(rel)
            continue

        doc_id = len(docs)
        tokens = tokenize(text)
        tokens.update(tokenize(rel))
        title = title_for(path, text)
        if title:
            tokens.update(tokenize(title))

        docs.append({
            "id": doc_id,
            "path": rel,
            "sha256": digest,
            "bytes": len(raw),
            "title": title,
        })
        for token in tokens:
            postings.setdefault(token, set()).add(doc_id)

    shards: dict[str, dict[str, list[int]]] = {}
    for token, ids in postings.items():
        shards.setdefault(shard_for(token), {})[token] = sorted(ids)

    if index_dir.exists():
        shutil.rmtree(index_dir)
    index_dir.mkdir(parents=True)

    shard_names = sorted(shards)
    for shard in shard_names:
        payload = {
            "schema_version": SCHEMA_VERSION,
            "shard": shard,
            "terms": {k: shards[shard][k] for k in sorted(shards[shard])},
        }
        (index_dir / f"{shard}.json").write_text(
            json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "kind": "derived_repository_search_view",
        "authoritative": False,
        "source_fingerprint": content_fingerprint(fingerprints),
        "source_file_count": len(fingerprints),
        "indexed_text_file_count": len(docs),
        "unreadable_text_candidates": unreadable,
        "shards": shard_names,
        "documents": docs,
    }
    (index_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return manifest


def load_manifest(index_dir: Path) -> dict:
    return json.loads((index_dir / "manifest.json").read_text(encoding="utf-8"))


def query_index(query: str, root: Path = ROOT, index_dir: Path | None = None, limit: int = 20) -> list[dict]:
    index_dir = (index_dir or (root / "search_index")).resolve()
    manifest = load_manifest(index_dir)
    query_tokens = sorted(tokenize(query))
    if not query_tokens:
        return []

    candidate_ids: set[int] | None = None
    matched_tokens: list[str] = []
    for token in query_tokens:
        shard_path = index_dir / f"{shard_for(token)}.json"
        if not shard_path.exists():
            return []
        shard = json.loads(shard_path.read_text(encoding="utf-8"))
        ids = set(shard["terms"].get(token, []))
        if not ids:
            return []
        matched_tokens.append(token)
        candidate_ids = ids if candidate_ids is None else candidate_ids & ids
        if not candidate_ids:
            return []

    docs = {int(d["id"]): d for d in manifest["documents"]}
    q = query.lower()
    results = []
    for doc_id in sorted(candidate_ids or set()):
        doc = docs[doc_id]
        path_l = doc["path"].lower()
        title_l = (doc.get("title") or "").lower()
        score = len(matched_tokens)
        if q in path_l:
            score += 4
        if q and q in title_l:
            score += 3
        score += sum(1 for token in matched_tokens if token in path_l)
        score += sum(1 for token in matched_tokens if token in title_l)
        results.append({**doc, "score": score, "matched_tokens": matched_tokens})

    results.sort(key=lambda d: (-d["score"], d["path"]))
    return results[:limit]


def check_index(root: Path = ROOT, index_dir: Path | None = None) -> tuple[bool, str]:
    index_dir = (index_dir or (root / "search_index")).resolve()
    if not (index_dir / "manifest.json").exists():
        return False, "search index missing"

    with tempfile.TemporaryDirectory() as td:
        expected_dir = Path(td) / "search_index"
        expected = build_index(root, expected_dir)
        current = load_manifest(index_dir)
        if current.get("source_fingerprint") != expected.get("source_fingerprint"):
            return False, "search index source fingerprint is stale"

        current_files = sorted(p.name for p in index_dir.glob("*.json"))
        expected_files = sorted(p.name for p in expected_dir.glob("*.json"))
        if current_files != expected_files:
            return False, "search index shard set is stale"

        for name in expected_files:
            if (index_dir / name).read_bytes() != (expected_dir / name).read_bytes():
                return False, f"search index differs: {name}"

    return True, "search index fresh"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build, query, or verify the Take-2 repository search fallback.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("build", help="rebuild search_index from repository text files")
    sub.add_parser("check", help="verify committed search_index is fresh")
    query = sub.add_parser("query", help="query the committed search_index")
    query.add_argument("text")
    query.add_argument("--limit", type=int, default=20)

    args = parser.parse_args()
    if args.command == "build":
        manifest = build_index()
        print(json.dumps({
            "source_file_count": manifest["source_file_count"],
            "indexed_text_file_count": manifest["indexed_text_file_count"],
            "source_fingerprint": manifest["source_fingerprint"],
            "shards": manifest["shards"],
        }, indent=2))
        return 0

    if args.command == "check":
        ok, message = check_index()
        print(message)
        return 0 if ok else 2

    results = query_index(args.text, limit=args.limit)
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
