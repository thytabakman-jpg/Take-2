# Canonical Authority Import Manifest

Status: COMPLETE IMPORT CANDIDATE
Import date: 2026-09-29
Target repository: thytabakman-jpg/Take-2
Target branch: import/canonical-authority-complete-20260929

## Authoritative source snapshot
- repository: thytabakman-jpg/Reaserch
- branch: main
- source commit: e1f016c4df104b5a7fe9c894a903b78c4894fb95
- project path: projects/canonical-authority
- project tree: 0d3bf90264b7f2b2fd4cd1964c4d70ceb888579b
- project files: 133
- project bytes: 1,099,666

## Additional source material
- top-level Canonical Authority audits from Reaserch/main: 24 files
- GitHub controlling ledger: Issue #71 plus all retrieved comments
- Canonical Authority PR search index: 19 matching PR records

## Preservation rule
All source files were copied byte-for-byte through Git blob transfer. Each transferred source file was verified to produce the identical Git blob SHA in Take-2.

## Imported layout
- source project snapshot: dump/canonical-authority/reaserch-main/projects/canonical-authority/
- external project audits: dump/canonical-authority/reaserch-main/audits/
- GitHub execution ledger: dump/canonical-authority/github-ledger/

## Verification contract
Completion requires:
1. 133/133 project files present at target paths.
2. 24/24 external audit files present at target paths.
3. Source and target blob SHA equality for every transferred source file.
4. Issue #71 snapshot, comment snapshot, and PR index present.
5. Import committed and merged to Take-2 main.
6. Post-merge tree rescan confirms file counts and representative hashes.

This manifest describes an archival/workable migration. It does not replace the authority semantics inside PROJECT_PAGE.md, ARTIFACTS.yaml, STATE.yaml, PROVENANCE.yaml, or the project-local research controls.
