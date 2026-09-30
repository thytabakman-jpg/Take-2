# Generation 2 — ICC adapted plan

Inherited state: runtime witness implementation exists; observable GitHub execution evidence remains OPEN.

## Reassessment

The original Generation 2 plan assumed a runtime baseline for ablation. That assumption is not satisfied.

ICC therefore revises Generation 2 rather than executing invalid ablations.

## Choice

Split ablation into two strata:

A. executable/static fixture ablations that can be encoded now and later run unchanged;
B. runtime-dependent claims held OPEN until an execution observer exists.

Prepare the ablation harness without interpreting unexecuted tests as evidence.

Ablations:
1. remove q_goal lock;
2. remove hidden-constraint observation;
3. allow repair without worker acknowledgement;
4. allow termination without verification;
5. suppress reselection/re-entry;
6. collapse OPEN/INCOMPARABLE representation.

Expected discriminator:
each mutation must produce a detectable protected-behavior violation in at least one fixture for that distinction to earn necessity evidence.

## Why?

This preserves experimental momentum without crossing the semantic/runtime boundary. The blocked runtime observer becomes part of M6/M8 rather than a reason to either stop all work or manufacture evidence.

## What's next?

Build the mutation harness and multi-fixture specification so that the moment execution evidence becomes available, Generations 2 and 3 can run as matched tests. In parallel, treat the inability to observe execution as a real M6 x M8 capability cut requiring its own acquisition path.
