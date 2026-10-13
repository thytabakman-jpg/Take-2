#!/usr/bin/env python3
"""Read-only verification of native Take-5 authority: no mirror, no runners."""
import argparse
import json
import re
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = ROOT / "source-references/TAKE5_AUTHORITY_PIN.json"
BASE = "https://api.github.com/repos/thytabakman-jpg/Take-5"
CORE = ("integration/CURRENT_HF2.md", "integration/CURRENT_IMPROVEMENT_CORE.md",
        "integration/CURRENT_FULL_TOOL_INVOCATION.md", "runtime/icc_entry.py",
        "projects/tool-system/AUTHORITY_REGISTRY.md",
        "legacy/icc128-legacy/MANIFEST.yaml")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "take2-native-authority-check"})
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def verify(checkout=None):
    pin = json.loads(PIN.read_text(encoding="utf-8"))
    entries = pin["required_files"]
    require(pin["schema"] == "TAKE2_NATIVE_TAKE5_AUTHORITY_PIN/v1", "invalid schema")
    require(pin["source_repository"] == "thytabakman-jpg/Take-5", "invalid source repository")
    require(len(entries) >= 26 and all(p in entries for p in CORE), "required source identities missing")
    require(bool(re.fullmatch("[0-9a-f]{40}", pin["source_commit"])), "invalid commit pin")
    require(bool(re.fullmatch("[0-9a-f]{40}", pin["source_tree"])), "invalid tree pin")
    if checkout:
        def git(*a):
            return subprocess.check_output(["git", "-C", str(checkout), *a], text=True).strip()
        head = git("rev-parse", "HEAD")
        tree_sha = git("rev-parse", "HEAD^{tree}")
        lines = git("ls-tree", "-r", "HEAD").splitlines()
        files = {}
        for line in lines:
            meta, name = line.split("\t", 1)
            mode, typ, sha = meta.split()
            if typ == "blob":
                files[name] = (sha, mode)
        current = head
    else:
        commit = get(BASE + "/commits/" + pin["source_commit"])
        tree_sha = commit["commit"]["tree"]["sha"]
        tree = get(BASE + "/git/trees/" + pin["source_tree"] + "?recursive=1")
        require(tree["truncated"] is False, "truncated source tree")
        require(tree["sha"] == pin["source_tree"], "source tree mismatch")
        files = {x["path"]: (x["sha"], x["mode"]) for x in tree["tree"] if x["type"] == "blob"}
        current = get(BASE + "/commits/main")["sha"]
        head = pin["source_commit"]
    require(head == pin["source_commit"], "checkout is not pinned source commit")
    require(tree_sha == pin["source_tree"], "source tree mismatch")
    mismatches = [p for p, blob in entries.items() if files.get(p) != (blob["sha"], blob["mode"])]
    require(not mismatches, "missing/changed required native blobs: " + repr(mismatches))
    return {"status": "PASS_PINNED_SOURCE", "native_source": pin["source_repository"],
            "pin": head, "required_verified": len(entries), "mirror_required": False,
            "native_main_matches_pin": current == head,
            "runtime_execution_certified": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--take5-checkout", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.take5_checkout), indent=2))
        return 0
    except Exception as error:
        print(json.dumps({"status": "FAIL", "error": str(error), "runtime_execution_certified": False}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
