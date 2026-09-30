# Canonical Authority — ROOT CAUSE + HF2: Affirmative-First Regression

Status: RELATIVE_CLOSE / ROOT ADMITTED LOCALLY  
Date: 2026-09-30  
Execution truth: HOST_BOUND_CONFIGURED  
Tool: RootCause  
Profile: full configured D36_C + HF2 recurrence

## Frozen failure class

The failure class is not only the bad sentence. It contains the full recurrence:

1. the affirmative-first rule existed in the control map before the mutation;
2. the Section 1.1 prose mutation introduced a prohibited negative-first frame;
3. ARCHITECT did not reject the constraint-violating realization;
4. the later full 36D + HF2 review did not catch the violation;
5. VERIFY accepted a semantically correct but prose-invalid successor;
6. the same rhetorical family survived in multiple manuscript locations.

## Evidence

The parent of commit `eb83692ca4d0376cdf3e84765cc99635da775a7d` contained:

> Ramban directly attacks that grammatical premise...

Commit `eb83692ca4d0376cdf3e84765cc99635da775a7d`
(`Canonical Authority: restructure Section 1.1 around exact collision`) introduced:

> Ramban does not merely offer a different emphasis. He directly attacks...

The affirmative-first rule was already present in `PARAGRAPH_CONTROL_MAP.md` before that commit:

> State the affirmative claim first. Use negation only when the distinction itself requires it.

Therefore the regression did not arise because the rule was added later.

## RootCause round 1

Candidate classes tested:

- academic negative-first language prior;
- local SOLUTION prose mutation defect;
- ARCHITECT prose-constraint omission;
- VERIFY semantic-only acceptance;
- protected constraint not promoted to an executable acceptance invariant;
- general protected-transition-integrity failure.

The local prose prior and SOLUTION defect explain introduction but not escape.

The ARCHITECT omission explains one failed checkpoint but not the later VERIFY/HF2 escape.

The VERIFY gap explains escape but not introduction.

The general protected-transition-integrity candidate is too broad for this frozen failure class.

Round-1 nondominated admissible candidate:

[
	exttt{PROTECTED_CONSTRAINT_NOT_PROMOTED_TO_EXECUTABLE_ACCEPTANCE_INVARIANT}.
]

## HF2 smaller-generator challenge

HF2 re-applied RootCause to a finer representation of the surviving candidate.

Rivals:

- prose rule was document-only;
- no final negative-first linter;
- ARCHITECT treated reader-first framing as nonarchitectural;
- protected basis was dropped at the prose-mutation acceptance boundary.

The smaller stable generator is:

[
oxed{
	exttt{PROTECTED_BASIS_DROPPED_AT_PROSE_MUTATION_BOUNDARY}
}
]

Meaning:

> The affirmative-first constraint existed in the project control plane but was not carried as a mandatory acceptance invariant through prose mutation and successor acceptance. Therefore SOLUTION could generate a violating realization, ARCHITECT could fail to reject it, and VERIFY/HF2 could certify the successor because they were evaluating semantic and structural validity without owning this protected prose constraint as a failure condition.

## Why this is the root rather than the nearest cause

### SOLUTION

SOLUTION introduced the actual sentence.

That is the local mechanism, not the root.

Replacing only the sentence generator would not prevent another mutator from producing the same rhetorical structure.

### ARCHITECT

ARCHITECT failed to protect the constraint.

That is a real failure and must be repaired.

It is still not the smallest root because the same constraint was also absent from later acceptance/verification behavior.

### VERIFY / later full-stack run

These allowed the regression to escape.

Adding only a final linter would catch the symptom later but would leave the protected constraint absent from upstream architecture and mutation ownership.

### Root

When the protected basis is bound to every prose-changing transition as an acceptance invariant:

- SOLUTION cannot admit the violating mutation;
- ARCHITECT must reject a realization whose reader-first structure violates the basis;
- VERIFY must fail the successor;
- HF2 re-entry cannot close over the violating state.

Removing this generator therefore breaks the entire recurrence class.

## D36_C result

The root survived the configured Scope × ModeFace representation changes:

- SYSTEM
- SUBSYSTEM
- COMPONENT
- INTERFACE
- BOUNDARY_DECOMPOSITION
- CROSS_LAYER

across:

- EXPAND
- CONTRACT
- INWARD
- OUTWARD
- ISOLATE
- COUPLE.

The diagnosis remains the same at each scale:

> protected prose constraints lacked transition ownership at mutation/acceptance.

This is why the issue appeared simultaneously as a sentence defect, an ARCHITECT miss, a VERIFY miss, and a later closure miss.

## Accountability

Introduction:
- SOLUTION / prose mutation.

Missed prevention:
- ARCHITECT.

Missed escape detection:
- VERIFY and later configured review.

Root generator:
- protected-basis propagation failure at the prose-mutation acceptance boundary.

GOAL is not the root and did not introduce the sentence.

## Repair implication

The paper-level negative-first gate is a valid local containment repair.

The system-level repair implied by RootCause is stronger:

> Every protected prose constraint must be promoted into the protected transition basis for any prose-changing tool and must be checked both before mutation admission and before successor-state acceptance.

ARCHITECT must therefore treat reader-first framing as architecture when the project marks it protected.

SOLUTION must preserve it during realization.

VERIFY must reject violations.

HF2 must re-enter rather than close when the protected prose invariant fails.

## RootCause local closure

Local status: RELATIVE_CLOSE.

RootCause does not own global completion. Per the current RootCause contract, the proper parent handoff is:

[
	ext{ImprovementCore}
ightarrow
	exttt{ADMIT_ROOT_CAUSE_AND_REPLAN}.
]

No global tool-system mutation is claimed by this audit.
