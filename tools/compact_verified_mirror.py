#!/usr/bin/env python3
"""Runner-free, 100-file batch cleanup of exact historical Take-5 mirrors."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

PREFIX = "dump/full-system-sources/Take-5/"
MANIFEST = "dump/full-system-sources/PUBLIC_CORPUS_MANIFEST.json"


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def tree(root):
    result = {}
    for entry in git(root, "ls-tree", "-rz", "HEAD").split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        mode, kind, sha = metadata.decode().split()
        if kind == "blob":
            result[name.decode()] = (mode, sha)
    return result


def run(take2, take5, batch_size=100, max_batches=100, apply=False, push=False):
    take2, take5 = Path(take2).resolve(), Path(take5).resolve()
    if take2 == take5 or not (take2 / ".git").exists() or not (take5 / ".git").exists():
        raise RuntimeError("Separate local Take-2 and Take-5 clones required")
    if batch_size < 1 or max_batches < 1:
        raise ValueError("Batch counts must be positive")
    if git(take2, "status", "--porcelain") or git(take5, "status", "--porcelain"):
        raise RuntimeError("Both Git checkouts must be clean")
    if git(take2, "branch", "--show-current").strip() != b"main":
        raise RuntimeError("Take-2 must be checked out on main")
    for root in (take2, take5):
        if push:
            git(root, "fetch", "origin", "main")
            if git(root, "rev-parse", "HEAD") != git(root, "rev-parse", "refs/remotes/origin/main"):
                raise RuntimeError("Repository is behind origin/main; no deletion permitted")

    donor_commit = git(take5, "rev-parse", "HEAD").decode().strip()
    starting_commit = git(take2, "rev-parse", "HEAD").decode().strip()
    subprocess.run([sys.executable, str(take2 / "tools/verify_native_take5.py"),
                    "--take5-checkout", str(take5)], check=True)
    importer = (take2 / "tools/full_system_consolidate.sh").read_text()
    if "--restore-full-mirror" not in importer:
        raise RuntimeError("Mirror regeneration is not guarded")
    removed = 0
    receipts = []
    for batch in range(1, max_batches + 1):
        if git(take5, "rev-parse", "HEAD").decode().strip() != donor_commit:
            raise RuntimeError("Native Take-5 changed; stop")
        local, native = tree(take2), tree(take5)
        matched = [p for p, item in sorted(local.items()) if p.startswith(PREFIX)
                   and item[0] in ("100644", "100755")
                   and native.get(p[len(PREFIX):]) == item]
        selected = matched[:batch_size]
        if not selected:
            break
        data = json.loads((take2 / MANIFEST).read_text())
        records = {x["path"] for x in data["records"]}
        if not set(selected).issubset(records):
            raise RuntimeError("Cannot reconcile selected paths with historical manifest")
        if not apply:
            print(json.dumps({"mode": "DRY_RUN", "eligible": len(matched),
                              "first_batch": selected, "donor": donor_commit}, indent=2))
            return
        details = {p: {"mode": local[p][0], "sha": local[p][1]} for p in selected}
        subprocess.run(["git", "-C", str(take2), "rm", "--", *selected], check=True,
                       stdout=subprocess.DEVNULL)
        data["records"] = [x for x in data["records"] if x["path"] not in details]
        data["file_counts"]["Take-5"] -= len(selected)
        data["total_files"] -= len(selected)
        provenance = data.setdefault("mirror_deduplication", {
            "source_repo": "thytabakman-jpg/Take-5",
            "donor_commit": donor_commit,
            "original_take2_commit": starting_commit,
            "comparison": "exact path, Git blob hash, and mode",
            "removed_paths": [], "removed_blobs": {},
        })
        if provenance["donor_commit"] != donor_commit:
            raise RuntimeError("Donor pin changed; stop")
        provenance["removed_paths"].extend(selected)
        provenance["removed_blobs"].update(details)
        (take2 / MANIFEST).write_text(json.dumps(data, indent=2) + "\n")
        git(take2, "add", "--", MANIFEST)
        git(take2, "commit", "-m",
            "chore(take2): retire %d exact mirror files batch %d" % (len(selected), batch))
        receipts.append({"batch": batch, "removed": len(selected)})
        removed += len(selected)

    if apply and removed:
        subprocess.run([sys.executable, str(take2 / "tools/repository_search.py"), "build"],
                       cwd=take2, check=True)
        git(take2, "add", "--", "search_index")
        if git(take2, "diff", "--cached", "--name-only").strip():
            git(take2, "commit", "-m", "chore(take2): refresh derived search index")
        subprocess.run([sys.executable, str(take2 / "tools/repository_search.py"), "check"],
                       cwd=take2, check=True)
        subprocess.run([sys.executable, str(take2 / "tools/verify_native_take5.py"),
                        "--take5-checkout", str(take5)], check=True)
        manifest = json.loads((take2 / MANIFEST).read_text())
        after = tree(take2)
        if manifest["total_files"] != len(manifest["records"]) or any(
                item["path"] not in after for item in manifest["records"]):
            raise RuntimeError("Post-deletion manifest failed to reconcile")
        if push:
            git(take2, "push", "origin", "main")  # never force push
    print(json.dumps({"removed": removed, "batches": receipts,
                      "changed_or_missing_donor_copies_untouched": True,
                      "pushed": bool(push and apply and removed)}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--take5", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--max-batches", type=int, default=100)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--push", action="store_true")
    args = parser.parse_args()
    try:
        run(Path(__file__).resolve().parents[1], args.take5, args.batch_size,
            args.max_batches, args.apply, args.push)
    except (RuntimeError, ValueError, OSError, subprocess.CalledProcessError) as e:
        print("FAIL CLOSED:", e, file=sys.stderr)
        sys.exit(2)
