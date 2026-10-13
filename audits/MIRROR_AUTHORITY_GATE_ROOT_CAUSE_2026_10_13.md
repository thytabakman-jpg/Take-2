# Root cause — Take-2 mirror-size authority rule

2026-10-13

## Finding

The legacy authority test used copied-file totals (8,000 Take-5 files and 7,000 tool-system files) as evidence of preservation. These thresholds measured a historical snapshot, not capability availability or runtime verification. An automatic full-mirror consolidation script could recreate files after cleanup. The historical `SYSTEM_AUTHORITY.md` also directed readers to the local copy rather than the current Take-5 repository.

## Executed repairs

- Updated `SYSTEM_AUTHORITY.md` to distinguish source ownership, archival copies and Take-2 enforcement.
- Registered 26 pinned native-source authority blobs at `source-references/TAKE5_AUTHORITY_PIN.json`.
- Added `tools/verify_native_take5.py`, supporting public GitHub-tree or exact local-checkout verification.
- Changed `tools/check_full_system_authority.py` to use source verification by default. The historical snapshot mode remains explicitly selectable for archaeology.
- Made `tools/full_system_consolidate.sh` non-copying by default and prevented its associated workflow from automatically refreshing the mirror.
- Preserved previous deduplication history when rebuilding the manifest, and documented search-index regeneration.
- Added `tests/test_native_take5_authority.py` covering missing/changed identities, truncated trees, and version drift.

## Acceptance boundary

Verified source identity is not executable capability or scientific certainty. A pinned source can be stale relative to main. Historical changed copies remain independent evidence. No physical file deletion is certified by this repair; deletion requires a separate readback-backed exact-match campaign. GitHub runner availability is not assumed.
