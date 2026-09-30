# Step 09 — Rival representation

Rival R1 explicit: <Q,T,F,E,B;I>.
Rival R2 absorbed: <Q,T*,F*> where T* includes request/ack/post-state/evidence events and F* ranges only over evidence/binding-admissible continuations.

Potential equivalence requires a mapping preserving the protected trace predicates and admissible continuations.

Counterpressure: R2 can encode the behavior, but compression may hide diagnostic cut types. Two systems can have the same successful terminal behavior while differ on whether failure is BINDING, OBSERVABILITY, or EVIDENCE. The governing goal includes diagnosing cuts for autonomous repair, so terminal-only quotient is too coarse.

Result: no reduction admitted. Need quotient indexed to diagnostic job, not only terminal success.

Why? Representation adequacy is job-relative. A compression that preserves success/failure but destroys repair-relevant distinctions loses controller capability.

What's next? Use this to refine the behavioral quotient and then hand the result to the tenth-generation synthesis.