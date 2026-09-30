# Take-3

Take-3 is ICC's clean-room control experiment.

It receives the real operating objective and protected behavior, but it does not inherit the architecture of Take-2 or Reaserch as its starting design.

## Frozen objective

Given a broad task and a corpus boundary, recover the result-sensitive state, preserve authority and provenance, choose the minimum sufficient action, execute only when licensed, verify the result, update represented state, and decide what matters next.

## Experimental rule

Architecture is earned by demonstrated necessity.

Take-3 may consult external corpora to perform a task, but existing system architecture is not evidence that the same architecture belongs here.

## Initial candidate

The smallest current candidate is one recursive episode with four durable record types:

1. Task — frozen goal, corpus boundary, protected behavior.
2. Finding — discovered state/evidence with provenance and epistemic status.
3. Action — proposed or executed operation with authority and baseline.
4. Result — verification, state delta, unresolved coordinates, and reentry decision.

These are experimental representations, not claimed universal primitives.

## Loop

TASK
→ DISCOVER
→ DECIDE
→ ACT
→ VERIFY
→ REENTER

Any missing distinction that changes a benchmark result becomes a candidate addition. Otherwise it remains composition or metadata.

## Status

BOOTSTRAP_CANDIDATE.
No superiority claim.
No production authority.
