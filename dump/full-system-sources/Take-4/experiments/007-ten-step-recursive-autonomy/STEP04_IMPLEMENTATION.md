# Step 04 — Trace oracle implementation

Implemented an evaluator that receives only traces. Mutation identity is absent from its input.

Why? Independent observation is required before ablation can say a distinction is load-bearing.

What's next? Build adversarial traces for the protected failure classes and verify that the oracle catches them without mutation labels.