#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]

BOOKLET_ALIASES = {
    "fick": "fick_difference",
    "fick_difference": "fick_difference",
    "sukkos_fick_difference": "fick_difference",
    "keva": "keva_practice",
    "keva_practice": "keva_practice",
    "sukkos_keva_practice": "keva_practice",
    "conservation": "conservation_boundaries",
    "conservation_boundaries": "conservation_boundaries",
    "sukkos_conservation_boundaries": "conservation_boundaries",
}

OPERATION_SPECS = {
    "show_baseline": {
        "task_function": "accepted_repair_baseline",
        "selector": "baseline",
    },
    "show_current": {
        "task_function": "current_working_set",
        "selector": "current",
    },
    "edit_current": {
        "task_function": "current_working_set",
        "selector": "current",
    },
    "audit_current": {
        "task_function": "current_working_set",
        "selector": "current",
    },
    "package_current": {
        "task_function": "current_working_set",
        "selector": "current",
    },
    "compare_current_to_baseline": {
        "task_function": "current_plus_baseline",
        "selector": "compare",
    },
    "show_accepted_product": {
        "task_function": "accepted_product",
        "selector": "accepted_product",
    },
}


def load(path: str) -> Any:
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def normalize_booklet_alias(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return re.sub(r"_+", "_", normalized)


def resolve_booklet(value: str) -> str:
    key = normalize_booklet_alias(value)
    resolved = BOOKLET_ALIASES.get(key)
    if resolved is None:
        allowed = ", ".join(sorted(BOOKLET_ALIASES))
        raise SystemExit(f"Unknown JHB booklet alias {value!r}. Known aliases: {allowed}")
    return resolved


def compact_object(obj: dict[str, Any]) -> dict[str, Any]:
    return {
        key: obj.get(key)
        for key in (
            "id",
            "name",
            "class",
            "role",
            "page_number",
            "mime_type",
            "source_filename",
            "library_file_id",
            "sha256",
            "dimensions_px",
            "repository_path",
            "repository_bytes_status",
            "acceptance_basis",
            "provenance_note",
        )
        if key in obj
    }


def build_source_set_index(
    booklet_id: str,
    artifacts: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for item in artifacts.get("source_sets", []) or []:
        if not isinstance(item, dict) or not item.get("id"):
            continue
        if item.get("booklet_id") != booklet_id:
            continue
        index[str(item["id"])] = item

    booklet = artifacts.get("booklets", {}).get(booklet_id, {})
    legacy_id = booklet.get("source_set_id")
    legacy_order = booklet.get("page_order") or []
    if legacy_id and legacy_id not in index:
        index[str(legacy_id)] = {
            "id": legacy_id,
            "booklet_id": booklet_id,
            "class": (
                "accepted_source_set"
                if booklet.get("artifact_status") == "accepted_source_set"
                else "unresolved_source_set"
            ),
            "page_order": legacy_order,
            "authority_note": booklet.get("authority"),
        }
    return index


def resolve_source_set(
    booklet_id: str,
    source_set_id: str | None,
    artifacts: dict[str, Any],
) -> dict[str, Any]:
    objects = {
        str(item.get("id")): item
        for item in artifacts.get("objects", [])
        if isinstance(item, dict) and item.get("id")
    }
    sets = build_source_set_index(booklet_id, artifacts)
    source_set = sets.get(str(source_set_id)) if source_set_id else None

    if (
        not source_set_id
        or str(source_set_id).upper() == "OPEN"
        or "UNRESOLVED" in str(source_set_id).upper()
        or not isinstance(source_set, dict)
    ):
        return {
            "outcome": "OPEN",
            "source_set_id": source_set_id,
            "source_set_class": source_set.get("class") if isinstance(source_set, dict) else None,
            "page_order": [],
            "exact_source_objects": [],
            "retrieval_plan": [],
            "artifact_sensitive_gate": "BLOCKED",
            "open_reason": "requested source set is unbound, unresolved, or not registered",
        }

    page_order = source_set.get("page_order") or []
    resolved_objects = [
        compact_object(objects[page_id])
        for page_id in page_order
        if page_id in objects
    ]
    exact = (
        bool(page_order)
        and len(resolved_objects) == len(page_order)
        and all(
            obj.get("sha256")
            and (obj.get("library_file_id") or obj.get("repository_path"))
            for obj in resolved_objects
        )
    )

    retrieval_plan = []
    for obj in resolved_objects:
        retrieval_plan.append(
            {
                "object_id": obj.get("id"),
                "page_number": obj.get("page_number"),
                "object_class": obj.get("class"),
                "preferred_repository_path": (
                    obj.get("repository_path")
                    if obj.get("repository_bytes_status")
                    not in {"pending_binary_transfer", None}
                    else None
                ),
                "library_file_id": obj.get("library_file_id"),
                "source_filename": obj.get("source_filename"),
                "expected_sha256": obj.get("sha256"),
                "rule": (
                    "Use this exact task-bound registered object. Search may retrieve "
                    "its bytes, but search results, recency, filenames, PDFs, composites, "
                    "or generated candidates cannot select the task target or artifact authority."
                ),
            }
        )

    return {
        "outcome": "EXACT" if exact else "OPEN",
        "source_set_id": source_set_id,
        "source_set_class": source_set.get("class"),
        "task_roles": source_set.get("task_roles", []),
        "authority_note": source_set.get("authority_note"),
        "provenance_note": source_set.get("provenance_note"),
        "page_order": page_order,
        "exact_source_objects": resolved_objects,
        "retrieval_plan": retrieval_plan,
        "artifact_sensitive_gate": "CLEAR" if exact else "BLOCKED",
        "open_reason": None if exact else "registered source set is not exactly resolvable",
    }


def get_workstream_binding(
    workstream_id: str,
    booklet_id: str,
    task_function: str,
) -> dict[str, Any] | None:
    registry = load("WORKSTREAMS.yaml")
    for item in registry.get("workstreams", []) if isinstance(registry, dict) else []:
        if not isinstance(item, dict):
            continue
        if item.get("workstream_id") != workstream_id:
            continue
        if item.get("status") == "closed":
            return None
        bindings = item.get("target_bindings", []) or []
        for binding in bindings:
            if not isinstance(binding, dict):
                continue
            if binding.get("project") not in {None, "jewish-holiday-booklets"}:
                continue
            if binding.get("booklet_id") != booklet_id:
                continue
            if binding.get("task_function") != task_function:
                continue
            if binding.get("status") not in {None, "active"}:
                continue
            return binding
        return None
    return None


def current_set_binding(
    *,
    booklet_id: str,
    state: dict[str, Any],
    source_set_id: str | None,
    workstream_id: str | None,
) -> dict[str, Any]:
    if source_set_id:
        return {
            "status": "BOUND",
            "source_set_id": source_set_id,
            "selection_basis": "explicit_current_turn_source_set",
            "workstream_id": workstream_id,
            "authority_effect": "none",
        }

    if workstream_id:
        binding = get_workstream_binding(
            workstream_id,
            booklet_id,
            "current_working_set",
        )
        if binding and binding.get("source_set_id"):
            return {
                "status": "BOUND",
                "source_set_id": binding.get("source_set_id"),
                "selection_basis": "explicit_workstream_continuation",
                "workstream_id": workstream_id,
                "binding_id": binding.get("binding_id"),
                "authority_effect": "none",
            }
        return {
            "status": "OPEN",
            "source_set_id": None,
            "selection_basis": "explicit_workstream_missing_matching_binding",
            "workstream_id": workstream_id,
            "authority_effect": "none",
        }

    continuation = state.get("continuation_bindings", {})
    default_set = continuation.get("default_current_working_set")
    if default_set and str(default_set).upper() != "OPEN":
        return {
            "status": "BOUND",
            "source_set_id": default_set,
            "selection_basis": "promoted_booklet_default_continuation",
            "workstream_id": None,
            "authority_effect": "none",
        }

    return {
        "status": "OPEN",
        "source_set_id": None,
        "selection_basis": "no_current_turn_workstream_or_promoted_default_binding",
        "workstream_id": None,
        "authority_effect": "none",
    }


def resolve_task_binding(
    *,
    booklet_id: str,
    operation: str,
    state: dict[str, Any],
    source_set_id: str | None,
    workstream_id: str | None,
) -> dict[str, Any]:
    spec = OPERATION_SPECS[operation]
    selector = spec["selector"]
    targets: list[dict[str, Any]] = []

    if selector == "baseline":
        baseline = state.get("object_identity", {}).get("accepted_repair_baseline")
        targets.append(
            {
                "task_function": "accepted_repair_baseline",
                "source_set_id": baseline,
                "selection_basis": "booklet_accepted_repair_baseline",
            }
        )
    elif selector == "current":
        current = current_set_binding(
            booklet_id=booklet_id,
            state=state,
            source_set_id=source_set_id,
            workstream_id=workstream_id,
        )
        targets.append(
            {
                "task_function": "current_working_set",
                "source_set_id": current.get("source_set_id"),
                "selection_basis": current.get("selection_basis"),
                "workstream_id": current.get("workstream_id"),
                "binding_id": current.get("binding_id"),
            }
        )
    elif selector == "compare":
        current = current_set_binding(
            booklet_id=booklet_id,
            state=state,
            source_set_id=source_set_id,
            workstream_id=workstream_id,
        )
        targets.append(
            {
                "task_function": "current_working_set",
                "source_set_id": current.get("source_set_id"),
                "selection_basis": current.get("selection_basis"),
                "workstream_id": current.get("workstream_id"),
                "binding_id": current.get("binding_id"),
            }
        )
        targets.append(
            {
                "task_function": "accepted_repair_baseline",
                "source_set_id": state.get("object_identity", {}).get(
                    "accepted_repair_baseline"
                ),
                "selection_basis": "booklet_accepted_repair_baseline",
            }
        )
    elif selector == "accepted_product":
        accepted = state.get("continuation_bindings", {}).get("accepted_product", "OPEN")
        targets.append(
            {
                "task_function": "accepted_product",
                "source_set_id": accepted,
                "selection_basis": "booklet_accepted_product_binding",
            }
        )
    else:
        raise RuntimeError(f"Unhandled selector {selector!r}")

    bound = all(
        target.get("source_set_id")
        and str(target.get("source_set_id")).upper() != "OPEN"
        for target in targets
    )
    return {
        "status": "BOUND" if bound else "OPEN",
        "operation": operation,
        "task_function": spec["task_function"],
        "booklet_id": booklet_id,
        "targets": targets,
        "authority_effect": "none",
        "precedence_rule": [
            "explicit_current_turn_designation",
            "explicit_workstream_continuation",
            "explicitly_promoted_booklet_default",
            "OPEN_targeted_clarification",
        ],
        "forbidden_selectors": [
            "search_ranking",
            "recency",
            "filename_similarity",
            "PDF_convenience",
            "visual_coherence",
        ],
    }


def build(
    booklet_alias: str,
    operation: str = "show_baseline",
    source_set_id: str | None = None,
    workstream_id: str | None = None,
) -> dict[str, Any]:
    if operation not in OPERATION_SPECS:
        allowed = ", ".join(sorted(OPERATION_SPECS))
        raise SystemExit(f"Unknown JHB operation {operation!r}. Known operations: {allowed}")

    booklet_id = resolve_booklet(booklet_alias)
    root_state = load("projects/jewish-holiday-booklets/STATE.yaml")
    artifacts = load("projects/jewish-holiday-booklets/ARTIFACTS.yaml")
    controls = root_state.get("booklet_local_controls", {})
    local = controls.get(booklet_id)
    if not isinstance(local, dict):
        raise SystemExit(f"No booklet-local controls registered for {booklet_id}")

    state_path = local["state"]
    acceptance_path = local["product_acceptance"]
    state = load(state_path)
    acceptance = load(acceptance_path)

    task_binding = resolve_task_binding(
        booklet_id=booklet_id,
        operation=operation,
        state=state,
        source_set_id=source_set_id,
        workstream_id=workstream_id,
    )
    resolutions = [
        resolve_source_set(booklet_id, target.get("source_set_id"), artifacts)
        for target in task_binding["targets"]
    ]
    for target, resolution in zip(task_binding["targets"], resolutions):
        resolution["task_function"] = target.get("task_function")
        resolution["selection_basis"] = target.get("selection_basis")
        resolution["workstream_id"] = target.get("workstream_id")
        resolution["binding_id"] = target.get("binding_id")

    primary = resolutions[0] if resolutions else {
        "outcome": "OPEN",
        "artifact_sensitive_gate": "BLOCKED",
        "source_set_id": None,
        "page_order": [],
        "exact_source_objects": [],
        "retrieval_plan": [],
    }
    all_exact = (
        task_binding["status"] == "BOUND"
        and bool(resolutions)
        and all(r.get("outcome") == "EXACT" for r in resolutions)
    )

    return {
        "authority": "non_authoritative_generated_booklet_workbench",
        "bootstrap_contract_version": "0.3-task-binding",
        "bootstrap_status": (
            "READY_EXACT_ARTIFACT"
            if all_exact
            else "READY_CONTROL_ONLY_ARTIFACT_OPEN"
        ),
        "requested_booklet": booklet_alias,
        "requested_operation": operation,
        "booklet_id": booklet_id,
        "project_id": "jewish-holiday-booklets",
        "entrypoint_rule": (
            "Resolve the execution-local task binding before broad search. "
            "The binding selects a registered task target without changing artifact authority."
        ),
        "sources": {
            "root_state": "projects/jewish-holiday-booklets/STATE.yaml",
            "series_control": "projects/jewish-holiday-booklets/MASTER_CONTROL.md",
            "artifact_registry": "projects/jewish-holiday-booklets/ARTIFACTS.yaml",
            "workstream_registry": "WORKSTREAMS.yaml",
            "local_state": state_path,
            "product_acceptance": acceptance_path,
            "interface_contracts": "INTERFACE_CONTRACTS.yaml",
        },
        "project_mode": root_state.get("project_status", {}).get("current_mode"),
        "task_binding": task_binding,
        "task_target_resolutions": resolutions,
        "object_identity": state.get("object_identity", {}),
        "continuation_bindings": state.get("continuation_bindings", {}),
        "artifact_resolution": primary,
        "lifecycle": state.get("lifecycle", {}),
        "live_findings": state.get("live_findings", {}),
        "learner_route": state.get("learner_route", {}),
        "next_action": state.get("next_action"),
        "acceptance_status": acceptance.get("acceptance_status", {}),
        "acceptance_gates": acceptance.get("gates", []),
        "artifact_registry_entry": artifacts.get("booklets", {}).get(booklet_id, {}),
        "substitution_policy": (
            "Task binding selects the registered target; artifact registry controls identity "
            "and class. Neither search nor task binding can promote candidate authority."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a compact fail-closed JHB task-binding workbench."
    )
    parser.add_argument(
        "--booklet",
        required=True,
        help="Canonical booklet id or controlled alias such as fick, keva, or conservation.",
    )
    parser.add_argument(
        "--operation",
        default="show_baseline",
        choices=sorted(OPERATION_SPECS),
        help="Task predicate used to resolve the task-relative artifact target.",
    )
    parser.add_argument(
        "--source-set-id",
        help=(
            "Explicit current-turn registered source set. This controls only the present "
            "task target and does not change artifact acceptance."
        ),
    )
    parser.add_argument(
        "--workstream-id",
        help="Explicit substantial continuation/workstream whose target binding to use.",
    )
    parser.add_argument(
        "--require-exact-artifact",
        action="store_true",
        help="Exit non-zero unless every task-bound artifact target resolves exactly.",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    view = build(
        args.booklet,
        operation=args.operation,
        source_set_id=args.source_set_id,
        workstream_id=args.workstream_id,
    )
    exact = (
        view["task_binding"]["status"] == "BOUND"
        and all(
            result.get("outcome") == "EXACT"
            for result in view.get("task_target_resolutions", [])
        )
    )
    if args.require_exact_artifact and not exact:
        if args.json:
            print(json.dumps(view, indent=2, ensure_ascii=False))
        else:
            print(
                f"JHB task bootstrap BLOCKED: {view['booklet_id']} "
                f"{view['requested_operation']} target is OPEN or not exactly resolvable."
            )
        return 2

    if args.json:
        print(json.dumps(view, indent=2, ensure_ascii=False))
        return 0

    print(f"JHB booklet bootstrap: {view['booklet_id']}")
    print(f"Operation: {view['requested_operation']}")
    print(f"Task binding: {view['task_binding']['status']}")
    print(f"Bootstrap: {view['bootstrap_status']}")
    print(f"Artifact resolution: {view['artifact_resolution']['outcome']}")
    print(
        f"Artifact-sensitive gate: "
        f"{view['artifact_resolution']['artifact_sensitive_gate']}"
    )
    print(f"Source set: {view['artifact_resolution'].get('source_set_id')}")
    print(f"Lifecycle: {view['lifecycle'].get('status')}")
    print(f"Stage: {view['lifecycle'].get('current_stage')}")
    print(f"Acceptance: {view['acceptance_status'].get('current_result')}")
    print(f"Next action: {view['next_action']}")
    print("Sources:")
    for key, value in view["sources"].items():
        print(f"  {key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
