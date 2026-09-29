# Canonical Authority Organizational Repair — Relational PD Phase Comparison

Date: 2026-09-23

## Proposed stages

P1 Authority and object map
P2 Canonical project entry/orientation
P3 Goal / spine / state alignment
P4 Research-object / artifact / source organization
P5 Workstream / open-work routing
P6 Manuscript-facing boundary
P7 Folder implementation + propagation
P8 Closure

## Relational findings

P1 -> P2: GENERATOR / SHARED_DEPENDENCY
The orientation page depends on authoritative source identification.

P1 -> P3: SHARED_DEPENDENCY
Goal/spine/state ownership cannot be presented accurately without P1.

P1 -> P4: SHARED_DEPENDENCY
Artifact/source locations require authority classification first.

P2 -> P3: COMPOSES_WITH
Navigation presents goal/state but does not own it.

P3 -> P4: SHARED_DEPENDENCY
Goal-spine and research-object structure interact but are not the same hierarchy.

P4 -> P5: SHARED_DEPENDENCY
Open work must route to the appropriate source/artifact/object owner.

P4 -> P6: SHARED_DEPENDENCY
The manuscript contract derives from research architecture and source registry, not discovery files.

P5 -> P6: SUPPORTING
Current work informs manuscript execution but does not determine article structure.

P6 -> P7: CONSTRAINS
Folder implementation must preserve manuscript contract and research-object authority.

P7 -> P8: COMPOSES_WITH
Propagation and closure validate the physical result.

## Important separation

The existing project contains three simultaneous structures:

1. research/argument structure;
2. project-control structure;
3. manuscript/reader structure.

They should not be flattened into one folder hierarchy.

## Phase compression result

P4 should contain two explicit passes:
- research object/artifact authority;
- source/evidence authority.

P7 should split into:
- folder move;
- reference/derived propagation.

## Relational PD decision

KEEP all eight stages, but make P1 the deepest prerequisite and P7 the only physical
organization phase.

No physical folder changes before P1-P6 have a passing gate.
