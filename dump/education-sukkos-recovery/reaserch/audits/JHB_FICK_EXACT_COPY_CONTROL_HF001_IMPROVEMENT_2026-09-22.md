# Fick Exact-Copy Control Audit and Improvement Pass

Date: 2026-09-22
Scope: projects/jewish-holiday-booklets/fick exact-copy control plan
Operation mode: bounded booklet-local control improvement
Repository mutation scope: Fick local copy-control files only

## Target

Create a durable handoff from audited wording to later visual production so the actual
student-facing words are recoverable, version-addressable, and not silently reconstructed
from conversation history or a nearby artifact.

This audit does not reopen the Fick learner architecture or accept a repaired booklet.

## HF-001 old recursive PD audit

### Starting representation

Initial plan:

1. create one EXACT_COPY.md;
2. place the latest wording there;
3. mark it CANDIDATE_EXACT_COPY;
4. later change status to FROZEN_EXACT_COPY;
5. let image production consume the file.

### Hidden dependencies recovered

The plan depends on all of the following:

- exact object identity;
- distinction between candidate and frozen copy;
- explicit freeze authority;
- durable version identity;
- separation of visible student copy from nonvisible production/control notes;
- a downstream consumption rule for visual specification and rendering;
- a reopen rule when wording later changes;
- preservation of the accepted repair baseline and product-acceptance boundary.

Without these, an exact-copy file can still drift while appearing to solve the drift problem.

### Competing interpretations

"Freeze the file" had two materially different readings:

A. keep editing one path while changing its status label;
B. create an immutable approved snapshot with a new stable identity.

These are result-sensitive. Under A, later edits silently alter the object previously
called frozen. Under B, the approved wording remains recoverable and later revisions
become new objects.

### Search-space transformation

The target is not merely "store the words."

The stronger target is:

audited wording
-> exact candidate object
-> explicit approval
-> immutable frozen object
-> visual specification bound to frozen identity
-> render bound to frozen identity.

### Relative convergence result

The smallest robust control architecture is:

COPY_CONTROL.yaml
+
one current exact-copy candidate
+
later immutable versioned frozen snapshots.

Production notes and visual specifications remain separate objects.

## ImprovementCore pass

Relevant capabilities applied manually under the current PracticalCore order:

- I01 live_frontier_localization
- I02 admissible_successor_generation
- I05 behavior_preserving_compression
- I07 subsystem_architecture_improvement
- I09 interface_architecture_improvement
- I10 boundary_decomposition_improvement
- I13 strict_gain_testing
- I14 protected_result_non_regression
- I16 frontier/spine recomputation
- A16 terminal regression verification

### I01 frontier

The strongest live improvement frontier is the wording-to-production interface, not the
booklet's conceptual spine.

### I02 rival successors

Considered:

1. one mixed EXACT_COPY.md containing copy, production notes, source notes, and status;
2. one exact-copy file plus a separate control object;
3. four per-page exact-copy files plus a control object;
4. structured YAML/JSON as the sole copy store.

### I05 / I10 compression and boundary result

Use one exact-copy file for all four pages, not four page files.

Keep control metadata outside that file.

Keep later production notes and visual instructions outside exact-copy control.

This minimizes synchronization surfaces while preserving the material boundary between
student wording and production machinery.

### I09 interface result

Later visual work must reference the frozen exact-copy path and blob identity.

It may arrange and style text but may not obtain student-facing wording from chat
history, an older PDF, a current working image, or a nearby candidate.

### I13 strict gain

The selected architecture adds one small control file while gaining:

- stable candidate identity;
- explicit freeze semantics;
- immutable approved snapshots;
- a recoverable production dependency;
- prevention of mixed visible/nonvisible text;
- a clean reopen path.

The gain is functional, not merely organizational.

### I14 non-regression

The control change does not:

- alter the accepted Fick repair baseline;
- accept a repaired product;
- modify learner-route goals;
- reopen series architecture;
- authorize rendering;
- change empirical-validation status.

### I16 recomputed local state

Current exact-copy state:

- current candidate exists;
- frozen exact copy remains open;
- visual specification remains downstream of explicit copy freeze.

## Implementation

Created:

- projects/jewish-holiday-booklets/fick/copy/EXACT_COPY_CANDIDATE.md
- projects/jewish-holiday-booklets/fick/COPY_CONTROL.yaml

The candidate file contains only the current authorized candidate student copy inside
explicit page markers.

The control file records the candidate path and Git blob identity and defines the later
freeze/promotion contract.

## Next gate

Review the exact-copy candidate itself.

Only explicit user approval of the wording promotes it to an immutable versioned frozen
copy. Visual specification comes after that promotion.
