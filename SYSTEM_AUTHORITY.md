# Take-2 System Authority

Status: consolidation target and execution authority candidate. Take-5 remains the separate current working authority for capabilities not explicitly promoted to Take-2.

## Authority and storage are separate

1. Take-2 local enforcement files and verification gates govern Take-2 transitions.
2. Current Take-5 integration, architecture, runtime, and tool-system authorities are resolved at their native source repository (`thytabakman-jpg/Take-5`), not from a compulsory duplicate under `dump/full-system-sources/Take-5/`.
3. `source-references/TAKE5_AUTHORITY_PIN.json` identifies a particular validated public Take-5 Git tree and hashes of required authority files. It is a reference/provenance index; it does not transfer control authority to Take-2.
4. Any Take-2-local copies are historical evidence. Changed copies are not interchangeable with their current upstream counterparts. Source recovery from Git history is preserved.
5. Take-3 and Take-4 are historical lineage evidence. Reaserch is private and remains outside public Take-2.
6. Experiments remain historical unless a separate, authorized promotion decision is recorded.

A bare tool invocation resolves to the full configured current tool identity. Downgrade to a simplified tool requires an explicit bare/core request. Current HF2 and wrapper obligations remain attached when the current source contracts attach them.

## Fail-closed authority rule

No global consolidation or runtime-completeness claim follows from a copied file count, repository size, inventory symmetry, or a successful reference lookup. `python tools/check_full_system_authority.py` verifies explicit required native-source blobs against the pinned Take-5 tree, reports source revision drift, and distinguishes online verification from structural/offline checks. A PINNED_REFERENCE result does not certify that an executable runtime has been exercised.

The old 8,000-file and 7,000-tool-file local mirror thresholds are retired as invalid capability-preservation proxies. Missing or mismatching required authority source blobs, unavailable provenance, unknown changes, and unverified scientific/runtime claims remain explicit blockers.

## Cleanup and regeneration rule

No process may silently recreate `dump/full-system-sources/Take-5/` or treat deleted exact duplicates as capability loss. Mirror removal requires an exact same-path, same-Git-blob, same-mode check against an identified Take-5 commit, an auditable per-file disposition, and preservation of changed historical copies. An authority pin cannot alone license deletion.

`tools/full_system_consolidate.sh` is legacy restoration only and requires an explicit operator restoration flag. The normal verification route reads the native source reference instead. No GitHub Actions runner is assumed.

## Private source boundary

`thytabakman-jpg/Reaserch` is private while Take-2 is public. Its private contents are not copied into Take-2. Public Take-5 contracts can be referenced but are not automatically re-promoted into Take-2.

## Regression rule

Recognition is not execution. Preservation is not promotion. Promotion is not runtime enforcement. A capability is current only when the native authority is verified, its dependencies exist, and its behavioral/runtime gates pass.
