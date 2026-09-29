# Canonical Authority — Architecture Scan Post-MTA Control Surfaces 001

Date: 2026-09-24
Status: EXECUTED / MATERIAL YIELD / RELATIVE CLOSE
Controller: Improvement Core
Analyzer: current Architecture Analysis kernel with HF-001 and Tool Run Closure
Target: post-MTA derived-surface control architecture

## Protected set

No change to:
- CANON:ARCH:001 v1.2.0;
- protected spine;
- fixed case;
- package-TRACE result;
- method;
- contribution claims.

## Baseline architecture A0

Specialized controls are distributed:

- CURRENTNESS_CONTRACT.yaml
- MANUSCRIPT_STATUS_AXES.yaml
- READER_PROJECTION_MAP.yaml
- ABSTRACT_CONTRACT.md
- MANUSCRIPT_CONTRACT.md
- STATE.yaml
- ARTIFACTS.yaml
- PROJECT_PAGE.md
- NOVELTY_CONTRIBUTION_MAP.md

Strength:
local semantics are clear.

Defect:
cross-surface synchronization is implicit and distributed.

## Defect typing

D1 DRIFT:
a source surface changes and a dependent projection remains stale.

D2 LOSS:
a projection removes a protected observable.

D3 AUTHORITY_LEAK:
a derived surface appears to redefine an upstream authoritative object.

D4 CURRENTNESS_CONFUSION:
newness and authority are conflated.

D5 CONSUMER_GAP:
a material upstream delta is persisted but a required downstream surface is not refreshed or reviewed.

D6 OVERMERGE:
a control repair collapses distinct jobs such as currentness, visibility, reader order, and compression into one undifferentiated object.

## Candidate successors

### A1 — keep distributed controls only

Gain:
none beyond current state.

Residual defect:
D1/D5 remain because synchronization topology is not represented centrally.

Disposition:
preserved as baseline but not strict successor.

### A2 — merge controls into one master control object

Gain:
single lookup surface.

Costs:
- collapses distinct semantics;
- increases mutation coupling;
- raises authority ambiguity;
- duplicates specialized details;
- makes local ownership less clear.

Disposition:
rejected as overmerge.

### A3 — thin central surface-control map plus specialized controls

Architecture:

Root authoritative objects
-> typed derived surfaces
-> typed projection edges
-> synchronization triggers/actions
-> verification/consumer requirements

Specialized controls remain owners of their native semantics.

Candidate central object owns only:
1. surface registry;
2. typed derivation/projection edges;
3. protected-observable references;
4. currentness/authority pointers;
5. synchronization matrix;
6. consumer/verification routing.

## Interaction-sensitive evaluation

A3 preserves:
- CURRENTNESS_CONTRACT ownership of currentness semantics;
- MANUSCRIPT_STATUS_AXES ownership of three-axis status typing;
- READER_PROJECTION_MAP ownership of reader refinement;
- ABSTRACT_CONTRACT ownership of abstract compression;
- MANUSCRIPT_CONTRACT ownership of research-to-article translation.

A3 adds:
- a single answer to "what must be reconsidered when X changes?";
- explicit affected-surface closure;
- reduced stale-control risk;
- a durable consumer path for Tool Run Closure.

Therefore A3 is not a replacement architecture.
It is a synchronization/control overlay.

## Reader projection architecture

The reader relation is typed as a refinement graph, not a scalar nesting:

RJ <-> Sections <-> Movements

The existing READER_PROJECTION_MAP data remains usable.
No need to rewrite it merely to change conceptual terminology.

## Surface model

Candidate minimal surface descriptor:

Surface =
<id, source, role, authority, currentness, protected_refs, update_triggers>

Candidate edge:

ProjectionEdge =
<source, target, relation, preserved_refs, allowed_loss, verify>

Candidate synchronization rule:

SyncRule =
<delta_class, affected_surfaces, action, authority, verify, consumer>

Actions:
- NO_EFFECT
- REFRESH
- REVERIFY
- RECONCILE
- REAUTHORIZE
- OPEN

## Strict-gain test

A3 versus A0:

Preservation:
PASS.

New capability:
explicit synchronization/consumer routing.

Reduction in defect exposure:
D1 and D5 materially reduced.

Complexity:
one thin map, not a second theory.

Authority:
derived control only.

Result:
STRICT_GAIN relative to current control/recoverability basis.

## Regression

No fixed-case or method result changes.

No change to:
- package TRACE;
- DISCRIMINATE;
- RECOGNIZE;
- COMPOSE semantics;
- corpus;
- source modules;
- novelty claim;
- contribution hierarchy.

## HF-001 confirmation

Attacks:
- central-map overreach;
- duplicated ownership;
- false source-of-truth status;
- synchronization loops;
- administrative echo;
- derived surface mutating canonical research;
- reader graph forced into hierarchy.

All are handled by keeping A3 thin and pointer-based.

No additional architecture coordinate found after A3 factorization.

## OPEN

O1 automation of synchronization actions.
O2 completeness of delta-class taxonomy.
O3 whether all future manuscript surfaces belong in the same map.
O4 whether surface protection can reuse generic Representation Bridge runtime semantics.
O5 concurrency/multi-editor behavior.

## Verdict

Candidate successor:
A3 THIN CENTRAL SURFACE CONTROL MAP.

Architecture Analysis:
MATERIAL_YIELD_THEN_RELATIVE_CLOSE.

Promotion authority:
Improvement Core.
