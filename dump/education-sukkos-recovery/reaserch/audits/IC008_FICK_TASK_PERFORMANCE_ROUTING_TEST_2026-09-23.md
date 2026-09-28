# IC-008 Fick Task-Performance Routing Test — 2026-09-23

Status: FORMATIVE REAL-PROJECT TEST
Candidate under test: IC-2026-09-23-008
Project state source: current repository Fick controls
No Fick artifact mutation performed.

## Frozen observed state

Canonical current source set:
JHB:FICK:CANONICAL-PAGES:003.

Targeted existing dry-run repair:
JHB:FICK:C3:P3, activity-enactment repair JHB-FICK-003.

Known transaction blocker:
exact_student_wording -> frozen_copy_unresolved.

Additional execution dependency:
canonical source bytes are SHA-256 verified in Library but repository transport remains pending.

Copy authority:
JHB:FICK:COPY:CANDIDATE:001 exists but is explicitly candidate_reconciliation_required. Frozen copy remains OPEN and requires explicit user approval after reconciliation.

## IC-006 control result

IC-006 correctly identifies:
- exact canonical baseline;
- bounded P3 delta;
- preservation obligations;
- OPEN copy coordinate;
- no mutation authority;
- transaction blocked before execution.

This remains correct inner analysis.

## IC-008 controller result

Disposition:
HOLD / ROUTE, not ITERATE_ANALYSIS.

Current operation sequence:
1. ACQUIRE/OBSERVE canonical P3 visible copy/bytes as needed for reconciliation.
2. DECIDE the exact bounded P3 wording against current canonical artifact and authoritative findings.
3. DECIDE via explicit user wording approval to create frozen copy identity.
4. ACQUIRE canonical source bytes into an execution-accessible path if still unavailable.
5. EXECUTE one bounded source-preserving P3 edit.
6. OBSERVE the actual candidate page.
7. DECIDE human disposition: REJECT / REQUEST_CHANGE / APPROVE_AS_CURRENT.
8. PROMOTE only after candidate-bound explicit approval and predecessor revalidation.
9. VALIDATE continuity by resolving the promoted page as the next current source without chat recency.

## Material result

IC-008 avoids the historical stall:
OPEN project state -> run more architecture/improvement analysis.

The blocker is not another generic analytic defect. It is a typed production frontier containing ACQUIRE and DECIDE before EXECUTE.

This is the expected CAP-028 discrimination.

## Side-route test

PASS.

IC-008 does not absorb Fick artifact authority into generic ImprovementCore semantics. It routes to the existing Fick copy, artifact, execution, acceptance, and promotion controls.

## Task-performance limitation

The test reaches a real external/user decision boundary:
the candidate copy is not frozen and its control explicitly requires reconciliation against the visible canonical pages followed by explicit user wording approval.

Therefore IC-008 correctly stops rather than silently treating the candidate copy as approved.

Actual image execution also requires an accessible exact canonical image target; repository binary transport is still pending.

## Regression comparison

IC-006 advantage retained:
deep frame/baseline/preservation/OPEN/transaction diagnosis.

IC-008 added advantage demonstrated:
the outer controller classifies the next work as ACQUIRE/DECIDE and prevents another unconstrained improvement-analysis loop.

No evidence of IC-006 capability loss appears in this task test.

## Checkpoint

IC-006: BLOCKED FOR EXECUTION, correct.
IC-008: HOLD_AT_AUTHORITY_BOUNDARY, correct.

Next reachable project operation:
reconcile the exact P3 wording against the actual canonical P3 and obtain explicit user approval before freezing wording.

This report does not itself approve wording, freeze copy, execute an image edit, or promote an artifact.
