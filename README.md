# Take-2

Take-2 is a clean-room research operating kernel.

It does not copy the legacy Reaserch repository. Capabilities migrate only after they
demonstrate value under an explicit experiment.

Current phase: bootstrap with executable dump/reorganization path.

Core design target:

**Observe -> PD -> Diagnose/Understand -> Decide -> Transition -> Verify -> Observe**

PD is not an add-on audit layer. The demonstrated PD operations are intended to be part
of the kernel's reasoning/control loop. Only capabilities with adequate evidence are
promoted into the stable kernel; experimental capabilities remain explicitly typed.

## Dump and reorganize

A real zero-request intake path now exists.

```bash
python tools/dump_reorganize.py PATH_TO_DUMP
```

It recursively inventories the corpus, hashes and classifies files, creates a stable
organized copy, deduplicates identical bytes, prevents destructive filename collisions,
keeps uncertain material explicit as OPEN, verifies every copied byte, and emits a
machine-readable provenance receipt. See `DUMP_INTERFACE.md`.

The source corpus is never deleted or rewritten by this runner.

The legacy repository remains authoritative for every capability and project not yet
admitted to Take-2.

## Native Take-5 authority and duplicate control (2026-10-13)

Take-2 no longer requires a second local copy of the Take-5 portfolio to recognize its current authority. The source of truth is the public [Take-5 repository](https://github.com/thytabakman-jpg/Take-5). `source-references/TAKE5_AUTHORITY_PIN.json` identifies 26 critical native files by full source revision and Git blob hash.

- `python tools/check_full_system_authority.py` verifies the pinned native-source tree and reports drift from the current Take-5 main branch. This is a source-identity check, **not** evidence that runtime functionality passed.
- `python tools/verify_native_take5.py --take5-checkout /path/to/Take-5` verifies against an exact local checkout instead of making network calls.
- `TAKE2_AUTHORITY_MODE=snapshot python tools/check_full_system_authority.py` runs the older historical full-mirror test for archaeology only; its 8,000/7,000 count thresholds have no bearing on current capability preservation.
- `tools/full_system_consolidate.sh` only verifies by default. `--restore-full-mirror` explicitly reconstructs historical duplicates, and never runs on an ordinary branch push.
- No GitHub Actions runner is required for the native verifier, tests, or the local deduplication workflow. Source mismatches fail closed; historical changed copies are not silently discarded.

The original `dump/full-system-sources/` corpus is historical migration evidence. It may be reduced only through exact-content matching, source-hash receipts, and verification that altered historical copies retain their own provenance. The attached current search index is derived metadata and requires regeneration after actual file deletion.
