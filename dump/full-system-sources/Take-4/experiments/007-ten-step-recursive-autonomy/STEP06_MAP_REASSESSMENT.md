# Step 06 — M0-M11 reassessment from trace observability

The trace model gives separate observable signatures to several map regions:
M6 binding: REQUEST/ACK/POST_STATE.
M8 observability: POST_STATE/OBSERVE content.
M9 evidence: evidence-bearing OBSERVE/COLLAPSE transitions.
M5 re-entry: VERIFY failure followed by RESELECT.
M11 collapse discipline: unsupported COLLAPSE of OPEN/INCOMPARABLE.
M4 controller choice: SELECT/RESELECT.
M10 persistence: target/provenance continuity across trace.

Finding: M11 has a candidate independent observable signature: an evidence-unlicensed collapse can fail while selection, binding and observation events still exist. This is not yet proof M11 is an independent primitive; it defeats the claim that it is merely another name for M4 in this observation language.

Why? Behavioral separability is stronger evidence than naming differences.

What's next? Test interaction/noncommutation: whether removing observation or verification changes the meaning/detectability of M11 collapse and M5 re-entry.