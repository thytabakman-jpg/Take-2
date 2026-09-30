# Matched Controller Traces

Date: 2026-09-24
Execution truth: SYNTHETIC TRACE TEST. This is not a live runtime execution.

## Trace A — incumbent pointed closure

1. Freeze T_CURRENT.
2. Local frame omits HC1.
3. Pointed controller proposes repair using the incomplete frame.
4. Verification checks represented obligations only.
5. No closure challenger is licensed to reconstruct the frame.
6. Result cannot establish preservation of HC1.

Observation:
P1 PASS
P2 FAIL
P3 PASS
P4 FAIL
P5 OPEN
P6 OPEN
P7 FAIL
P8 OPEN
P9 PASS
P10 FAIL

Terminal disposition: OPEN/NOT VERIFIED. A correct evaluator must reject apparent completion.

## Trace B — closure-aware candidate

1. Freeze G1/T_CURRENT and protected observations.
2. Recover current pointed closure and local frame.
3. Pointed attempt exposes that HC1 is absent from the represented obligations.
4. Challenger classifies RD1 as a representation cut.
5. Construct closure-revision witness tied to G1.
6. Raise q_repr only. Keep q_goal/q_object locked.
7. Reconstruct frame with HC1.
8. Reject ADJ1 as target-displacing.
9. Delegate licensed repair to W1.
10. Require worker acknowledgement and observed post-state.
11. Verify against G1, HC1 and P1-P10.
12. On simulated first verification failure, re-enter rather than stop.
13. Apply corrected repair through W1.
14. Verify post-state.
15. De-escalate representation freedom and terminate.

Observation:
P1 PASS
P2 PASS
P3 PASS
P4 PASS
P5 PASS
P6 PASS
P7 PASS
P8 PASS
P9 PASS
P10 PASS

Terminal disposition: VERIFIED_GOAL_RELATIVE_FIXED_POINT.

## Discriminator

The candidate's gain comes from evidence-sensitive revision of the represented admissible closure while preserving target authority, followed by executable-binding evidence and re-entry.

This trace does not prove the candidate implementation exists. It establishes a falsifiable behavioral contract for an implementation.
