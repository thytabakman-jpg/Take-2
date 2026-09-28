#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from jhb_booklet_context import build, resolve_booklet

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors: list[str] = []

    for alias in ("fick", "fick_difference", "sukkos-fick-difference"):
        if resolve_booklet(alias) != "fick_difference":
            errors.append(f"Fick alias did not resolve: {alias}")

    expected_baseline = "JHB:FICK:ACCEPTED-PAGES:001"
    expected_baseline_pages = [
        "JHB:FICK:P1",
        "JHB:FICK:P2",
        "JHB:FICK:P3",
        "JHB:FICK:P4",
    ]
    expected_current = "JHB:FICK:CANONICAL-PAGES:003"
    expected_current_pages = [
        "JHB:FICK:C3:P1",
        "JHB:FICK:C3:P2",
        "JHB:FICK:C3:P3",
        "JHB:FICK:C3:P4",
    ]

    fick_baseline = build("fick")
    resolution = fick_baseline.get("artifact_resolution", {})

    if fick_baseline.get("bootstrap_contract_version") != "0.3-task-binding":
        errors.append("unexpected JHB bootstrap contract version")
    if fick_baseline.get("bootstrap_status") != "READY_EXACT_ARTIFACT":
        errors.append("Fick baseline bootstrap is not exact-artifact ready")
    if fick_baseline.get("task_binding", {}).get("status") != "BOUND":
        errors.append("Fick baseline task binding is not BOUND")
    if resolution.get("outcome") != "EXACT":
        errors.append("Fick baseline artifact resolution is not EXACT")
    if resolution.get("artifact_sensitive_gate") != "CLEAR":
        errors.append("Fick baseline artifact-sensitive gate is not CLEAR")
    if resolution.get("source_set_id") != expected_baseline:
        errors.append("Fick baseline source-set identity changed")
    if resolution.get("page_order") != expected_baseline_pages:
        errors.append("Fick baseline page order changed")

    baseline_objects = resolution.get("exact_source_objects", [])
    if [obj.get("id") for obj in baseline_objects] != expected_baseline_pages:
        errors.append("Fick baseline exact object list does not match accepted page order")
    for obj in baseline_objects:
        if obj.get("class") != "accepted_source":
            errors.append(f"{obj.get('id')}: accepted baseline object class changed")
        if not obj.get("library_file_id"):
            errors.append(f"{obj.get('id')}: missing immutable Library locator")
        if not obj.get("sha256"):
            errors.append(f"{obj.get('id')}: missing SHA-256")

    current = build("fick", operation="show_current")
    current_resolution = current.get("artifact_resolution", {})
    if current.get("task_binding", {}).get("status") != "BOUND":
        errors.append("Fick current task binding is not BOUND")
    if current_resolution.get("source_set_id") != expected_current:
        errors.append("Fick current binding does not resolve CANONICAL-PAGES:003")
    if current_resolution.get("page_order") != expected_current_pages:
        errors.append("Fick current canonical page order mismatch")
    if current_resolution.get("source_set_class") != "canonical_current_source_set":
        errors.append("Fick current set is not canonical_current_source_set")
    if current_resolution.get("outcome") != "EXACT":
        errors.append("Fick current canonical set is not exactly resolvable")
    for obj in current_resolution.get("exact_source_objects", []):
        if obj.get("class") != "canonical_current_source":
            errors.append(f"{obj.get('id')}: current page is not canonical_current_source")
        if not obj.get("library_file_id") or not obj.get("sha256"):
            errors.append(f"{obj.get('id')}: current working page lacks exact identity")

    explicit = build(
        "fick",
        operation="show_current",
        source_set_id=expected_baseline,
    )
    explicit_binding = explicit.get("task_binding", {})
    if explicit_binding.get("targets", [{}])[0].get("selection_basis") != (
        "explicit_current_turn_source_set"
    ):
        errors.append("explicit current-turn designation does not take precedence")
    if explicit.get("artifact_resolution", {}).get("source_set_id") != expected_baseline:
        errors.append("explicit current-turn source set did not control the task target")

    compare = build("fick", operation="compare_current_to_baseline")
    compare_ids = [
        item.get("source_set_id")
        for item in compare.get("task_target_resolutions", [])
    ]
    if compare_ids != [expected_current, expected_baseline]:
        errors.append(f"Fick compare binding mismatch: {compare_ids}")

    accepted = build("fick", operation="show_accepted_product")
    if accepted.get("task_binding", {}).get("status") != "OPEN":
        errors.append("Fick accepted product was silently inferred")
    if accepted.get("artifact_resolution", {}).get("outcome") != "OPEN":
        errors.append("Fick accepted product exact identity was silently closed")

    retrieval = current_resolution.get("retrieval_plan", [])
    if [item.get("object_id") for item in retrieval] != expected_current_pages:
        errors.append("Fick current retrieval plan does not preserve canonical page order")
    for item in retrieval:
        if not item.get("expected_sha256"):
            errors.append(f"{item.get('object_id')}: retrieval plan missing expected SHA-256")
        if "cannot select the task target" not in str(item.get("rule")):
            errors.append(
                f"{item.get('object_id')}: retrieval rule does not block search target selection"
            )

    for alias in ("keva", "conservation"):
        baseline = build(alias)
        result = baseline.get("artifact_resolution", {})
        if result.get("outcome") != "OPEN":
            errors.append(f"{alias}: unresolved baseline identity was silently closed")
        if result.get("artifact_sensitive_gate") != "BLOCKED":
            errors.append(f"{alias}: unresolved baseline work is not fail-closed")

        current_view = build(alias, operation="show_current")
        if current_view.get("task_binding", {}).get("status") != "OPEN":
            errors.append(f"{alias}: current working target was silently inferred")
        if current_view.get("artifact_resolution", {}).get("outcome") != "OPEN":
            errors.append(f"{alias}: current working artifact was silently selected")

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    local_instructions = (
        ROOT / ".github/instructions/jhb.instructions.md"
    ).read_text(encoding="utf-8")
    interface_contracts = (ROOT / "INTERFACE_CONTRACTS.yaml").read_text(encoding="utf-8")
    for label, text in (("AGENTS", agents), ("JHB instructions", local_instructions)):
        if "JHB runtime bootstrap" not in text:
            errors.append(f"{label}: missing JHB runtime bootstrap rule")
        if "jhb_booklet_context.py" not in text:
            errors.append(f"{label}: bootstrap tool not wired")
        if "--operation" not in text:
            errors.append(f"{label}: operation-aware target binding not wired")
        if "search" not in text.lower():
            errors.append(f"{label}: search fallback boundary is not explicit")

    if "IFACE:TASK-CONTINUATION-TO-ARTIFACT" not in interface_contracts:
        errors.append("task-continuation-to-artifact interface contract is missing")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"JHB runtime entrypoint: {len(errors)} error(s)")
        return 1

    print("JHB runtime entrypoint: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
