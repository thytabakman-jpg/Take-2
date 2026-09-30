#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "dump" / "full-system-sources"
T5 = BASE / "Take-5"

required = [
    "integration/CURRENT_EXECUTION_CLAIM_INTEGRITY.md",
    "integration/CURRENT_FULL_TOOL_INVOCATION.md",
    "integration/CURRENT_HF1.md",
    "integration/CURRENT_HF2.md",
    "integration/CURRENT_ICC128_CONVERSATION_CONTROL.md",
    "integration/CURRENT_ICC128_LEGACY_MATH.md",
    "integration/CURRENT_IMPROVEMENT_CORE.md",
    "integration/CURRENT_MATHEMATICAL_COLORING.md",
    "integration/CURRENT_PROTECTED_TRANSITION_INTEGRITY.md",
    "integration/CURRENT_ROOT_CAUSE.md",
    "integration/CURRENT_SHOW_ME_THE_MATH.md",
    "integration/CURRENT_TOOL_PROJECT_ORGANIZATION.md",
    "integration/CURRENT_TOOL_REALITY.md",
    "architecture/ASSERT_COMPOUND_CONTRACT_055.md",
    "architecture/CAPABILITY_PRESERVATION_INVARIANT_097.md",
    "architecture/EXECUTION_CLAIM_INTEGRITY_117.md",
    "architecture/FULL_CONFIGURED_TOOL_INVOCATION_121.md",
    "architecture/FULL_RUN_DEFAULT_DISPATCH_CONTRACT_066.md",
    "architecture/GLOBAL_TOOL_EXECUTION_CONTRACT_072.md",
    "architecture/IMPROVEMENT_CORE_DEFAULT_HF2_118.md",
    "architecture/TOOL_CONDUCTOR_PORTABLE_MATH_073.md",
    "architecture/WRAPPER_CANONICAL_CONTRACT_053.md",
    "legacy/icc128-legacy/MANIFEST.yaml",
]

missing = [p for p in required if not (T5 / p).is_file()]

counts = {}
for repo in ("Take-3", "Take-4", "Take-5"):
    base = BASE / repo
    counts[repo] = sum(1 for p in base.rglob("*") if p.is_file()) if base.exists() else 0

failures = []
if missing:
    failures.append({"missing_required_authority_files": missing})
if counts["Take-5"] < 8000:
    failures.append({"take5_file_count_too_low": counts["Take-5"]})
if not (T5 / "projects" / "tool-system").is_dir():
    failures.append({"missing_tool_system": True})
else:
    tool_count = sum(1 for p in (T5 / "projects" / "tool-system").rglob("*") if p.is_file())
    if tool_count < 7000:
        failures.append({"tool_system_file_count_too_low": tool_count})

semantic_checks = {
    "hf2_mentions_hf2": "HF2" in (T5 / "integration/CURRENT_HF2.md").read_text(encoding="utf-8", errors="replace") if (T5 / "integration/CURRENT_HF2.md").is_file() else False,
    "full_invocation_mentions_full": "full" in (T5 / "integration/CURRENT_FULL_TOOL_INVOCATION.md").read_text(encoding="utf-8", errors="replace").lower() if (T5 / "integration/CURRENT_FULL_TOOL_INVOCATION.md").is_file() else False,
    "improvecore_mentions_hf2": "HF2" in (T5 / "integration/CURRENT_IMPROVEMENT_CORE.md").read_text(encoding="utf-8", errors="replace") if (T5 / "integration/CURRENT_IMPROVEMENT_CORE.md").is_file() else False,
}
if not all(semantic_checks.values()):
    failures.append({"semantic_checks": semantic_checks})

result = {
    "status": "FAIL" if failures else "PASS",
    "source_counts": counts,
    "required_authority_files": len(required),
    "semantic_checks": semantic_checks,
    "failures": failures,
    "private_source_boundary": "Reaserch remains private and is not copied into public Take-2",
}
print(json.dumps(result, indent=2))
if failures:
    raise SystemExit(1)
