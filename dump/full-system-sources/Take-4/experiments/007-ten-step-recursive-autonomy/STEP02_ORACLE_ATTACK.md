# Step 02 — Oracle attack

Finding: the first semantic harness is too weak for necessity evidence. mutations.py maps each mutation directly to the protected coordinate that the harness then forces false. Passing that test establishes wiring, not behavioral discrimination.

Status: useful smoke test, rejected as necessity evidence.

Why? The oracle was partially told the answer by the mutation table.

What's next? Create independent scenario outcomes and derive protected observations from traces, so mutations change controller behavior and the oracle only observes consequences.