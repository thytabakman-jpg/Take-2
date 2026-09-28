#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> Any:
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    artifacts = load("projects/jewish-holiday-booklets/ARTIFACTS.yaml")
    state = load("projects/jewish-holiday-booklets/fick/STATE.yaml")
    acceptance = load("projects/jewish-holiday-booklets/fick/ACCEPTANCE.yaml")
    finding_sources = [
        (ROOT / "projects/jewish-holiday-booklets/MASTER_CONTROL.md").read_text(encoding="utf-8"),
        (ROOT / "audits/JHB_AUDIT_FAMILY_COMPARISON_2026-09-21.md").read_text(encoding="utf-8"),
    ]

    objects = {
        str(item.get("id")): item
        for item in artifacts.get("objects", [])
        if isinstance(item, dict) and item.get("id")
    }
    booklet = artifacts.get("booklets", {}).get("fick_difference", {})
    expected_set = "JHB:FICK:ACCEPTED-PAGES:001"
    expected_pages = ["JHB:FICK:P1", "JHB:FICK:P2", "JHB:FICK:P3", "JHB:FICK:P4"]

    source_sets = {
        str(item.get("id")): item
        for item in artifacts.get("source_sets", [])
        if isinstance(item, dict) and item.get("id")
    }
    accepted_set = source_sets.get(expected_set)
    if not accepted_set:
        errors.append("ARTIFACTS missing accepted Fick repair baseline source set")
    else:
        if accepted_set.get("class") != "accepted_source_set":
            errors.append("accepted Fick repair baseline source set has wrong class")
        if accepted_set.get("page_order") != expected_pages:
            errors.append("accepted Fick repair baseline page_order changed")

    if booklet.get("accepted_repair_baseline") != expected_set:
        errors.append("ARTIFACTS Fick accepted_repair_baseline changed")

    ident = state.get("object_identity", {})
    if ident.get("accepted_repair_baseline") != expected_set:
        errors.append("local Fick state baseline does not match ARTIFACTS")
    if ident.get("accepted_pages") != expected_pages:
        errors.append("local Fick state pages do not match ARTIFACTS")

    for page_id in expected_pages:
        obj = objects.get(page_id)
        if not obj:
            errors.append(f"missing accepted page object {page_id}")
        elif obj.get("class") != "accepted_source":
            errors.append(f"{page_id} is not class accepted_source")

    gates = acceptance.get("gates", [])
    gate_ids = {g.get("gate_id") for g in gates if isinstance(g, dict)}
    required = {f"FICK-PA-0{i}" for i in range(1, 7)}
    if gate_ids != required:
        errors.append(f"acceptance gate set mismatch: {sorted(gate_ids)}")

    findings: set[str] = set()
    for gate in gates:
        if isinstance(gate, dict):
            for finding in gate.get("findings", []) or []:
                findings.add(str(finding))
    for finding in findings:
        if not any(finding in source for source in finding_sources):
            errors.append(f"acceptance finding {finding} does not resolve in registered JHB finding evidence")

    result = acceptance.get("acceptance_status", {})
    if result.get("structural_ci_equivalence") != "explicitly_false":
        errors.append("product acceptance must remain distinct from structural CI")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"JHB Fick acceptance: {len(errors)} error(s)")
        return 1

    print("JHB Fick acceptance: PASS (identity + gate wiring; substantive gates remain explicit)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
