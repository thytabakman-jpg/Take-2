# IC-008 Fick Ten-Test Campaign — First Pass Results

Date: 2026-09-23
Campaign: audits/IC008_FICK_TEN_TEST_CAMPAIGN_2026-09-23.md
Mode: real-project diagnostic + bounded repair routing
No user approval or image mutation inferred.

## T1 Artifact identity and continuation — PASS

Observed:
- current canonical set = JHB:FICK:CANONICAL-PAGES:003;
- accepted baseline 001 is explicitly regression/preservation only;
- W2 is historical and explicitly superseded;
- exact hashes exist for C3 P1-P4.

Tension resolved by existing controls. No new architecture needed.
IC-008 next operation: VALIDATE only.

## T2 Copy authority and wording drift — PARTIAL / DECIDE

Observed:
- one candidate exact-copy object exists;
- frozen copy remains OPEN;
- control correctly forbids rendering authority from the mutable candidate;
- current candidate predates designation of canonical set 003 and must be reconciled against its visible wording.

Actual tension:
the project knows where copy belongs but has not completed the ordinary content decision needed to freeze it.

IC-008 classification:
DECIDE, not ANALYZE.

Repair possible now:
preserve candidate as the sole editable wording proposal and prohibit reconstruction from chat.
Repair requiring external/user boundary:
page-by-page reconciliation against the actual canonical images followed by explicit wording approval.

## T3 Science/source fidelity — PARTIAL / ANALYZE->DECIDE

Current candidate already contains two strong repairs:
- Fick explanation explicitly distinguishes random motion both ways from net diffusive flux toward lower concentration and says the difference becomes smaller over time in the simple setup;
- P2 attributes the peace/unity idea to Rav Kook/Olat Re'iyah on Berakhot 64a rather than presenting the classroom four-question tool as a quotation.

However ACCEPTANCE still carries JHB-FICK-001/002 as repair_required. This is stale/unfinished closure unless those findings identify further defects not represented in the current candidate.

Repair:
do not mark the acceptance gate passed from candidate prose alone. Resolve the original finding records/evidence before changing gate status.

IC-008 result:
the next operation is targeted evidence resolution, not booklet-wide redesign.

## T4 Learner-route architecture — PASS WITH ONE DEPENDENCY

Route is coherent in the exact-copy candidate:
P1: physical difference persists during diffusion -> asks whether people need sameness.
P2: introduces selective coordination tool -> asks what happens when one thing must be built together.
P3: one sukkah build -> asks where else coordination/difference applies.
P4: transfers to a safe disagreement.

The route itself no longer appears to be the dominant bottleneck.
Dependency:
T5/T6 determine whether P3 genuinely earns its place rather than merely occupying it.

## T5 Sukkos-specific surplus — OPEN / ANALYZE

Current P3 uses Sukkah 27b and one shared sukkah, but the current acceptance test asks a harder question:
would replacing it with a generic collaborative build lose something educationally important?

Current evidence does not yet establish that result.
Therefore H1-FICK-001 correctly remains OPEN.

This is a genuine conceptual tension point, not production plumbing.

IC-008 classification:
ANALYZE the specific surplus. Do not globally redesign the booklet and do not falsely close the gate.

## T6 Activity enactment — PASS AT COPY LEVEL, ARTIFACT VERIFICATION OPEN

The candidate now requires:
- each person chooses one design preference;
- one shared material set and one shared structure;
- during build students repeatedly ask "Do we need to coordinate here?" and "Can this stay different?";
- after build they identify what stayed different and where coordination was required.

That is materially stronger than merely talking about difference. It operationalizes selective coordination.

Repair conclusion:
JHB-FICK-003 appears resolved in the candidate copy at the semantic/activity level.
Do not change product acceptance until exact canonical reconciliation/freeze and actual-page verification occur.

IC-008 classification:
OBSERVE/VALIDATE next, not more activity architecture.

## T7 Independent transfer — PASS AT COPY LEVEL, ARTIFACT VERIFICATION OPEN

P4 supplies a new disagreement, requires the learner to identify:
- what differs;
- what remains shared;
- what actually requires coordination;
- what can remain unresolved;
- what joint next action remains possible.

It therefore performs independent transfer rather than simply repeating the sukkah activity.

Potential tension:
the dissolving-paper statement is a strong slogan and must not replace the boundary-analysis task. In the candidate it follows the boundary questions, so the transfer mechanism remains primary.

JHB-FICK-004/005 appear semantically repaired in candidate copy.
Artifact/product closure remains blocked until reconciliation and verification.

## T8 Production closure and readiness — PASS ROUTING / BLOCKED EXECUTION

The typed readiness architecture correctly separates analytic, execution, promotion, product, and empirical readiness.

Current execution blockers are concrete:
- frozen exact copy unresolved;
- canonical PNG bytes verified in Library but repository execution transport pending.

IC-008 correctly routes:
DECIDE copy -> ACQUIRE bytes -> EXECUTE.
Another generic architecture audit is not licensed.

No new production-control layer is warranted by this test.

## T9 Local-edit preservation and promotion — SPECIFICATION PASS / EXECUTION OPEN

Existing dry-run binds:
- exact P3 predecessor hash;
- one bounded P3 delta;
- P1/P2/P4 protected;
- unaffected P3 regions protected;
- no collateral visual drift;
- candidate-bound verification before promotion.

This directly addresses the historical local-defect -> global-redesign failure.

Execution remains OPEN because T2/T8 prerequisites are unresolved.
No image mutation attempted.

## T10 Continuation after promotion — NOT YET EXECUTABLE

The desired invariant is represented:
a promoted successor must become the next canonical source without chat recency.

It cannot be empirically tested before one actual promotion occurs.

IC-008 classification:
HOLD until T9 has a real promoted candidate; then VALIDATE continuity.

## Cross-test relational challenge

The ten apparent problems compress into four current tension families:

A. CONTENT CLOSURE
T2 + unresolved part of T3.
The words/sources need final reconciliation and authority closure.

B. HOLIDAY/LEARNING SURPLUS
T5 plus the residual product-level part of T6/T7.
The key conceptual question is what specifically Sukkos adds beyond generic selective coordination.

C. PRODUCTION BRIDGE
T8 + T9.
The project must turn an approved bounded repair into pixels without reconstructing or redesigning the rest.

D. CONTINUITY
T10.
Once promoted, the new artifact must automatically become the next source.

T1 and T4 are substantially stable.
T6 and T7 are semantically strong in the candidate and now need artifact-level observation rather than more conceptual invention.

## Dominant current sequence

1. resolve T3's original finding evidence enough to know whether candidate science/source copy closes JHB-FICK-001/002;
2. solve T5 Sukkos-specific surplus;
3. reconcile/finalize exact copy across P1-P4;
4. obtain explicit user wording approval and freeze copy;
5. acquire canonical image bytes for execution;
6. execute the smallest P3/P4/P1/P2 deltas actually required by the frozen copy;
7. visually inspect each changed page;
8. candidate-bound approval/promotion;
9. rerun product gates;
10. test fresh continuation from the promoted set.

## ImprovementCore test result

IC-008 adds value on this campaign because it prevents three recurring category errors:
- OPEN -> automatically run more ImprovementCore;
- semantic repair -> pretend artifact repair is complete;
- local defect -> regenerate the whole booklet.

No tested Fick tension currently requires another general ImprovementCore architecture change.
