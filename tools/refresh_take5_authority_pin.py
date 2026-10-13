#!/usr/bin/env python3
"""Refresh Take-2's source-reference identities from a local native Take-5 checkout."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = ROOT / "source-references/TAKE5_AUTHORITY_PIN.json"


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def main(donor):
    donor = Path(donor).resolve()
    if not (donor / ".git").exists():
        raise RuntimeError("Supply a real Take-5 Git checkout")
    if git(donor, "status", "--porcelain"):
        raise RuntimeError("Take-5 is dirty; source pin cannot be refreshed")
    if git(donor, "branch", "--show-current") != "main":
        raise RuntimeError("Take-5 is not on main")
    if git(donor, "rev-parse", "HEAD") != git(donor, "rev-parse", "refs/remotes/origin/main"):
        raise RuntimeError("Fetch and synchronize Take-5 to origin/main before refreshing")
    pin = json.loads(PIN.read_text(encoding="utf-8"))
    assert pin["schema"] == "TAKE2_NATIVE_TAKE5_AUTHORITY_PIN/v1"
    required = set(pin["required_files"])
    if len(required) < 26:
        raise RuntimeError("Authority source register unexpectedly shrank")
    files = {}
    for line in git(donor, "ls-tree", "-r", "HEAD").splitlines():
        meta, path = line.split("\t", 1)
        mode, kind, sha = meta.split()
        if kind == "blob":
            files[path] = {"mode": mode, "sha": sha}
    missing = sorted(required - files.keys())
    if missing:
        raise RuntimeError("Required native authority files disappeared: " + repr(missing))
    pin["required_files"] = {name: files[name] for name in sorted(required)}
    pin["source_commit"] = git(donor, "rev-parse", "HEAD")
    pin["source_tree"] = git(donor, "rev-parse", "HEAD^{tree}")
    PIN.write_text(json.dumps(pin, indent=2) + "\n", encoding="utf-8")
    from verify_native_take5 import verify
    result = verify(donor)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise RuntimeError("Usage: python tools/refresh_take5_authority_pin.py /path/to/Take-5")
        main(sys.argv[1])
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print("FAIL CLOSED:", exc, file=sys.stderr)
        sys.exit(2)
