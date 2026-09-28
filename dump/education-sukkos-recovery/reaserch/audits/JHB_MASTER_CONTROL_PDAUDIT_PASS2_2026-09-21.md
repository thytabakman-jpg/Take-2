# Jewish Holiday Booklet Master Control — Controlled PDAudit Pass 2

Date: 2026-09-21

## Frozen audit object

Path:
projects/jewish-holiday-booklets/MASTER_CONTROL.md

Blob SHA:
5474b0580edbdb5659b8da7974685533d7fb0222

Containing commit:
7027f667270bb26aac64fc9ead3abbff44d4aea3

Audit target:
Same target as Pass 1.

No historical project reconstruction was added to the audit corpus.

## Pass 1 regression matrix

### JHB-AUD-001 — authority status underspecified

PASS.

The header now states that the file is a source-grounded control artifact and is not yet full canonical project authority.

No goal authority is implied.

### JHB-AUD-002 — stable rule identity missing

PASS.

The repaired artifact contains 20 stable control-invariant IDs.

### JHB-AUD-003 — typed route graph not instantiated

PARTIAL PASS.

The repaired artifact now contains 19 instantiated typed route edges across all four booklets.

However Section 20 requires every cross-domain edge to record:

- source;
- target;
- relation type;
- preserved content;
- new content;
- basis;
- status.

The new edge tables contain all except an explicit basis field.

Several status cells also combine edge state and linked finding text in one free-form field.

This is sufficient for human recovery but weaker than the control's own declared relation schema.

Repair:
Add an explicit basis column and use a small edge-status vocabulary, with linked finding IDs in a separate field.

### JHB-AUD-004 — artifact evidence identity incomplete

PASS AS EXPLICIT OPENNESS.

The repaired artifact now has an artifact/evidence identity register.

Known Library identities are recorded.

Unknown accepted artifact identities are explicitly marked UNRESOLVED rather than guessed.

This does not close the evidence gaps, but it repairs the control defect: missing identity is now represented as state.

### JHB-AUD-005 — unbounded stability wording

PASS.

The artifact now says:

"No currently admitted source-grounded finding requires reopening the shared architecture."

The prior stronger wording is absent.

### JHB-AUD-006 — audit-domain partition missing

PASS.

The artifact now contains eight explicit audit domains and distinguishes domain-specific from whole-artifact convergence.

### JHB-AUD-007 — active findings lack stable identity

PASS WITH ONE NEW ID DEFECT.

The artifact now contains 15 current finding definitions.

However one new finding ID creates a namespace collision described below.

## New finding

### JHB-AUD-008 — finding/provenance namespace collision

Severity:
HIGH FOR TRACEABILITY

Section 25 already uses:

JHB-PROV-001
through
JHB-PROV-008

as provenance record IDs.

Section 30 then reuses:

JHB-PROV-001

as the finding ID for the nine unrecovered curriculum packets.

The same stable ID therefore names two different entity types inside one control artifact.

That defeats the purpose of stable identity and can create false recurrence/provenance matches.

Repair:
Move the finding to a distinct namespace, for example:

JHB-FIND-PROV-001

Do not renumber or rename the existing provenance records merely to fix the collision.

## Structural check

Current repaired object contains:

- 20 stable invariant IDs;
- 15 finding definitions;
- 8 audit domains;
- 19 typed route edges;
- explicit evidence identity register;
- explicit repair-cycle policy;
- bounded stability language.

No educational architecture invariant was lost in the Pass 1 repair.

## Repair-cycle check

No oscillation trigger is met.

There is:

- no reactivation of a previously repaired educational finding;
- no F1 -> F2 -> F1 alternation;
- no return to a materially equivalent prior repair-state signature;
- no repeated preservation conflict;
- no unstable movement of the same defect between neighboring educational nodes.

The two live control defects are:

1. incomplete typed-edge schema repair;
2. newly introduced ID namespace collision.

They share a control/representation level but do not currently form a repair cycle.

Therefore:
repair locally at JHB-D8 / control-representation level.

No escalation above the master-control layer is warranted.

## Pass 2 verdict

REPAIR TWO CONTROL DEFECTS, THEN CONFIRM.

The substantive holiday-booklet architecture still does not require reopening.

Required repairs:

1. separate provenance and finding ID namespaces;
2. complete the typed-edge schema with basis and normalized status/finding fields.

After repair:
freeze the new object and rerun the same audit once more.
