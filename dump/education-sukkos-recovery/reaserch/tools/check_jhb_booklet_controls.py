#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]

BOOKLETS = {
    "fick_difference": {
        "dir": "fick",
        "artifact_key": "fick_difference",
        "identity_field": "accepted_repair_baseline",
        "artifact_identity_field": "accepted_repair_baseline",
        "source_set": "JHB:FICK:ACCEPTED-PAGES:001",
        "gate_prefix": "FICK-PA-",
        "gate_count": 6,
    },
    "keva_practice": {
        "dir": "keva",
        "artifact_key": "keva_practice",
        "identity_field": "candidate_source_set",
        "artifact_identity_field": "source_set_id",
        "source_set": "JHB:KEVA:CANDIDATE:UNRESOLVED",
        "gate_prefix": "KEVA-PA-",
        "gate_count": 5,
    },
    "conservation_boundaries": {
        "dir": "conservation",
        "artifact_key": "conservation_boundaries",
        "identity_field": "source_set",
        "artifact_identity_field": "source_set_id",
        "source_set": "JHB:CONS:SOURCE-SET:UNRESOLVED",
        "gate_prefix": "CONS-PA-",
        "gate_count": 6,
    },
}


def load(path: str) -> Any:
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    root_state = load("projects/jewish-holiday-booklets/STATE.yaml")
    artifacts = load("projects/jewish-holiday-booklets/ARTIFACTS.yaml")
    local_controls = root_state.get("booklet_local_controls", {})
    finding_sources = [
        (ROOT / "projects/jewish-holiday-booklets/MASTER_CONTROL.md").read_text(encoding="utf-8"),
        (ROOT / "projects/jewish-holiday-booklets/STATE.yaml").read_text(encoding="utf-8"),
        (ROOT / "audits/JHB_AUDIT_FAMILY_COMPARISON_2026-09-21.md").read_text(encoding="utf-8"),
    ]

    for booklet_id, cfg in BOOKLETS.items():
        directory = cfg["dir"]
        state_path = f"projects/jewish-holiday-booklets/{directory}/STATE.yaml"
        acceptance_path = f"projects/jewish-holiday-booklets/{directory}/ACCEPTANCE.yaml"
        state = load(state_path)
        acceptance = load(acceptance_path)

        root_ref = local_controls.get(booklet_id, {})
        if root_ref.get("state") != state_path:
            errors.append(f"{booklet_id}: root state reference mismatch")
        if root_ref.get("product_acceptance") != acceptance_path:
            errors.append(f"{booklet_id}: root acceptance reference mismatch")

        if state.get("booklet_id") != booklet_id:
            errors.append(f"{booklet_id}: local STATE booklet_id mismatch")
        if state.get("parent_state") != "../STATE.yaml":
            errors.append(f"{booklet_id}: local STATE parent_state mismatch")
        if state.get("series_control") != "../MASTER_CONTROL.md":
            errors.append(f"{booklet_id}: local STATE series_control mismatch")

        ident = state.get("object_identity", {})
        if ident.get(cfg["identity_field"]) != cfg["source_set"]:
            errors.append(f"{booklet_id}: local object identity does not match expected source-set coordinate")

        artifact_booklet = artifacts.get("booklets", {}).get(cfg["artifact_key"], {})
        artifact_identity_field = cfg["artifact_identity_field"]
        if artifact_booklet.get(artifact_identity_field) != cfg["source_set"]:
            errors.append(
                f"{booklet_id}: ARTIFACTS {artifact_identity_field} mismatch"
            )

        if acceptance.get("booklet_id") != booklet_id:
            errors.append(f"{booklet_id}: ACCEPTANCE booklet_id mismatch")
        if acceptance.get("state_ref") != "STATE.yaml":
            errors.append(f"{booklet_id}: ACCEPTANCE state_ref mismatch")
        if acceptance.get("artifact_registry") != "../ARTIFACTS.yaml":
            errors.append(f"{booklet_id}: ACCEPTANCE artifact_registry mismatch")
        if acceptance.get("series_control") != "../MASTER_CONTROL.md":
            errors.append(f"{booklet_id}: ACCEPTANCE series_control mismatch")

        allowed = set(acceptance.get("gate_states", []))
        gates = [g for g in acceptance.get("gates", []) if isinstance(g, dict)]
        expected_ids = {
            f"{cfg['gate_prefix']}{i:02d}"
            for i in range(1, int(cfg["gate_count"]) + 1)
        }
        actual_ids = {str(g.get("gate_id")) for g in gates}
        if actual_ids != expected_ids:
            errors.append(
                f"{booklet_id}: acceptance gate set mismatch "
                f"(expected {sorted(expected_ids)}, got {sorted(actual_ids)})"
            )

        for gate in gates:
            status = gate.get("status")
            if status not in allowed:
                errors.append(f"{booklet_id}: invalid gate status {status!r}")
            for finding in gate.get("findings", []) or []:
                finding = str(finding)
                if not any(finding in source for source in finding_sources):
                    errors.append(
                        f"{booklet_id}: gate finding {finding} is not present in registered JHB evidence"
                    )

        result = acceptance.get("acceptance_status", {})
        if result.get("structural_ci_equivalence") != "explicitly_false":
            errors.append(
                f"{booklet_id}: product acceptance must remain distinct from structural CI"
            )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"JHB booklet-local controls: {len(errors)} error(s)")
        return 1

    print("JHB booklet-local controls: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
