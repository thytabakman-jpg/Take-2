# Canonical Authority Next-Work Priority Selector — Candidate Design

Date: 2026-09-23
Status: CANDIDATE / NON-AUTHORITATIVE

## Purpose

Select the next meaningful Canonical Authority organizational or research-control move from
a set of admissible candidates without inventing an unsupported scalar score.

## Hard admissibility gate

A candidate move m is admissible only if:

- authority is resolved or explicitly OPEN;
- exact object identity is resolved when object-sensitive;
- no protected goal/spine/state invariant is violated;
- current shared state is sufficiently fresh;
- the move has a declared closure/validation condition.

If these fail, m is BLOCKED before priority comparison.

## Core classification

Define:

T_CA(m) ∈ {CORE, ORDINARY}

CORE holds when at least one independently evidenced route applies:

1. AuthorityCore:
   m repairs or protects a load-bearing project authority/control boundary.

2. OrientationCore:
   m materially improves the ability to determine current project purpose, state,
   frontier, authority, or next action across repeated project use.

3. InstrumentCore:
   m materially improves a reusable shared tool/control system that Canonical Authority
   actually depends on.

No CORE status from novelty, convenience, or self-reported importance alone.

## Priority vector

For admissible m:

Π_CA(m) =
⟨
T_CA(m),
D⁺(m),
O(m),
R(m),
H(m),
B(m),
W(m),
I(m),
U(m),
C(m)
⟩

where:

D⁺ = supported downstream and instrumental dependency leverage.
O = set of orientation capabilities materially improved.
R = set of recurring defects/regressions materially addressed.
H = demonstrated human-navigation gain.
B = current blocker/unlock effect.
W = active-work relevance.
I = validated information gain or ambiguity reduction.
U = useful cross-context reuse value.
C = declared execution cost.

## Comparison rule

CORE ≻ ORDINARY.

Within each remaining coordinate, use only its independently justified order.

For set-valued coordinates:
use supported set inclusion.

Do not assign arbitrary weights.

If candidates are incomparable:
preserve the frontier rather than inventing a winner.

## Recalculation rule

Priority is state-relative.

After every meaningful completed move:

state_t → state_{t+1}
→ recompute Π_CA.

A move does not retain priority merely because work has already begun.

## Strict improvement test

A successor state is a strict planning improvement only when:

ProtectedFunctionsPreserved
∧
AtLeastOneAdmittedPriorityCoordinateStrictlyImproved.

## Anti-rescue rules

Do not:
- add a metric after seeing which move it would favor;
- turn human preference into an untyped scalar;
- double-count D⁺, O, and R;
- use cost as an automatic veto when no cost order is licensed;
- call every project-specific improvement "InstrumentCore";
- treat unresolved priority as permission to guess.

## Current Canonical Authority use

Apply this selector only after Phase 6 to:
- choose among remaining organizational defects;
- decide whether Phase 7 active-work setup is needed;
- decide whether Phase 8 physical reorganization is justified;
- choose among bounded migration groups if Phase 8 opens.

## Status

The representation is a priority-control candidate, not yet a canonical repository selector.
It becomes operational only after ImprovementCore validates the variable definitions against
actual Canonical Authority candidate moves.
