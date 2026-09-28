# Education / Sukkos final recovery accounting

Date: 2026-09-28

Status: VERIFIED RECOVERY ACCOUNTING

This record closes the current Education / Sukkos recovery sweep without claiming unavailable historical source objects were recovered.

## Recovered layers

### Archive layer

- 29 root recovery ZIPs were included in the final deterministic sweep.
- Recursive archive traversal found 31 unique ZIP byte objects including nested archives.
- The archive corpus contains 479 unique non-ZIP files after SHA-256 deduplication.
- The final Take-2 archive-layer intake processed all 479 files.
- 86 Markdown files were semantically read.
- Traversal complete: PASS.
- Markdown semantic intake complete: PASS.
- Byte verification complete: PASS.
- 16 ambiguous Markdown files remained OPEN rather than being guessed into a semantic role.

### Reaserch repository layer

- 73 Education/JHB files were copied from the current Reaserch repository with original paths preserved.
- The Take-2 regression gate requires all 73 files to traverse and verify.
- Main CI passed for this recovery layer.

### Take-5 repository layer

- 127 Sukkos/booklet-related files were copied from Take-5 with original paths preserved.
- The recovered set includes the question-booklet projects, frame-resolution project, page scripts, 36 coverage cells, tool runs, candidate states, runtime/test files, source locks, learner model, visual master, and project-management artifacts.
- The Take-2 regression gate requires all 127 files to traverse and verify.
- Main CI passed for this recovery layer.

## Cross-source byte reconciliation

Git blob hashes were compared against the 479 archive-layer files.

- Archive unique files: 479
- Reaserch files: 73
- Take-5 files: 127
- Exact-byte overlap between archive layer and Reaserch: 0
- Exact-byte overlap between archive layer and Take-5: 0
- Exact-byte duplicates inside the two repository recovery layers: 0
- Final exact-byte unique corpus across the three recovered layers: 679 files

Therefore:

```text
479 archive files
+ 73 Reaserch files
+ 127 Take-5 files
= 679 exact-byte-distinct recovered files
```

The three storage layers contain genuinely different evidence rather than merely duplicated copies.

## Known unresolved source-level gaps

Historical curriculum packets 4, 11, 15, 51, 53, 54, 56, 58, and 59 remain unrecovered as original substantive source packets.

These remain explicit gaps. They are not fabricated, reconstructed from titles, or silently treated as recovered.

## Storage rule

Repository-native text/code recovery is stored under:

- `dump/education-sukkos-recovery/reaserch/`
- `dump/education-sukkos-recovery/take5/`

Large binary/archive evidence remains in the recovery archive layer rather than being committed into Git history. Take-2 processes that material through the dump/reorganization path; GitHub is not used as a bulk binary archive.

## Closure

The current recovery job is complete relative to all located recovery ZIPs plus the audited Reaserch and Take-5 repository frontiers.

Future recovery work reopens only when new source evidence appears or one of the nine unresolved historical curriculum packets is located.
