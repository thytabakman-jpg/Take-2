# Step 03 — Independent trace model

ICC changes the experimental unit from coordinate-labelled mutation to event trace.

Events: SELECT, AUTH_DELTA, REQUEST, ACK, POST_STATE, OBSERVE, VERIFY, RESELECT, TERMINATE.
The oracle sees events/state only. It does not receive the mutation name or expected failed coordinate.

Protected properties are derived from trace predicates.

Why? This removes the direct answer channel between mutation generator and evaluator.

What's next? Implement the trace-derived oracle and adversarially test mutations against it.