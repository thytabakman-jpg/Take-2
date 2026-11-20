# Take-2

Take-2 is a clean-room research operating kernel.

The kernel does not treat the legacy Reaserch architecture as automatically admitted. It does, however, preserve selected historical Reaserch source snapshots under `dump/`; those archives are evidence, not a claim of current Take-2 authority. Capabilities migrate only after they demonstrate value under an explicit experiment.

Current phase: bootstrap with executable dump/reorganization path.

Core design target:

**Observe -> PD -> Diagnose/Understand -> Decide -> Transition -> Verify -> Observe**

PD is not an add-on audit layer. The demonstrated PD operations are intended to be part
of the kernel's reasoning/control loop. Only capabilities with adequate evidence are
promoted into the stable kernel; experimental capabilities remain explicitly typed.

## Approved-source precedence and deferred migration

[Research-System](https://github.com/thytabakman-jpg/Research-System) and [ICC-System](https://github.com/thytabakman-jpg/ICC-System) are the two user-approved destination repositories. Each file placed in either has the user's explicit approval and is authoritative for the subject and responsibility it actually governs. Where an approved file conflicts with an older file on the same responsibility, the approved file controls; an older `canonical`, `current`, or `locked` label does not reverse that precedence. The two destination repositories govern their respective research and ICC subjects, not each other's unrelated responsibilities.

This does not mean the migration is complete. Legacy repositories retain historical evidence, experiments, and responsibility for work not yet represented by an approved replacement. In particular, Take-5 remains the current working ICC runtime until an independently authorized and verified cutover. Migration and legacy cleanup are deferred, not prerequisites to using the approved files. This README does not authorize moving, deleting, promoting, or importing any file; new admission to either approved repository requires explicit user approval.

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

Where no approved destination file governs the responsibility, the existing source owner retains it. Take-2 experiments and archival copies do not override approved Research-System or ICC-System files and do not independently transfer legacy authority.

## Native Take-5 authority and duplicate control (2026-10-13)

Take-2 no longer requires a second local copy of the Take-5 portfolio to recognize its current authority. For working ICC runtime and tool responsibilities not yet transferred to an approved ICC-System file, the native source remains the public [Take-5 repository](https://github.com/thytabakman-jpg/Take-5). `source-references/TAKE5_AUTHORITY_PIN.json` identifies 26 critical native files by full source revision and Git blob hash.

- `python tools/check_full_system_authority.py` verifies the pinned native-source tree and reports drift from the current Take-5 main branch. This is a source-identity check, **not** evidence that runtime functionality passed.
- `python tools/verify_native_take5.py --take5-checkout /path/to/Take-5` verifies against an exact local checkout instead of making network calls.
- `TAKE2_AUTHORITY_MODE=snapshot python tools/check_full_system_authority.py` runs the older historical full-mirror test for archaeology only; its 8,000/7,000 count thresholds have no bearing on current capability preservation.
- `tools/full_system_consolidate.sh` only verifies by default. `--restore-full-mirror` explicitly reconstructs historical duplicates, and never runs on an ordinary branch push.
- No GitHub Actions runner is required for the native verifier, tests, or the local deduplication workflow. Source mismatches fail closed; historical changed copies are not silently discarded.

The original `dump/full-system-sources/` corpus is historical migration evidence. It may be reduced only through exact-content matching, source-hash receipts, and verification that altered historical copies retain their own provenance. The attached current search index is derived metadata and requires regeneration after actual file deletion.

## Retained historical inputs

Reaserch hosts the [education recovery collection](https://github.com/thytabakman-jpg/Reaserch/tree/main/System-Wide%20Experiments/System%20Recovery%20and%20Successor%20Studies/Take-2%20Education%20Recovery) and [PD records](https://github.com/thytabakman-jpg/Reaserch/tree/main/System-Wide%20Experiments/Kernel%20and%20Controller%20Experiments/Take-2/pd). The Take-2 kernel check and recovery tests read their original inputs from this repository's pinned Git history. Use a full Git checkout to run them.
