# Canonical Authority Roadmap — Multi-Object PD Result

Date: 2026-09-23
Method: METHOD:MULTI_OBJECT_PD_RECURSIVE
Objects: roadmap phases P0-P10

## Frozen objects

P0 cockpit/control surface
P1 source/corpus/provenance closure
P2 novelty/comparator closure
P3 open theory/ceiling raising
P4 integrated manuscript architecture
P5 drafting
P6 hostile/referee review
P7 citation/provenance/reproducibility closure
P8 venue/framing
P9 external researcher handoff
P10 post-review revision/submission

## Pairwise isolation summary

All 55 unordered pairs were tested for dependency, support, constraint, feedback, overlap, or no licensed relation.

### Strong directed dependencies

P0 -> P1,P2,P3,P4,P5,P6,P7,P8,P9,P10 only as orientation/control, not substantive evidence.
P1 -> P4,P5,P6,P7,P8,P9,P10 through source/corpus closure.
P2 -> P4,P5,P6,P8,P9,P10 through novelty/literature placement.
P3 -> P4,P5,P6,P8,P9,P10 through accepted ceiling changes.
P4 -> P5,P6,P7,P8,P9,P10 through manuscript structure.
P5 -> P6,P7,P8,P9,P10 because whole-manuscript operations require a manuscript.
P6 -> P7,P8,P9,P10 because hostile findings can reopen claims, sources, architecture, or prose.
P7 -> P9,P10 as external-review/submission readiness.
P8 -> P9,P10 as framing/venue constraints.
P9 -> P10 through external feedback.

### Important bidirectional feedback relations

P1 <-> P5: drafting can expose missing source gates; source changes can force redrafting.
P2 <-> P5: drafting can expose novelty ambiguity; literature changes can alter framing.
P3 <-> P5: drafting is a discovery environment; accepted theory changes can alter prose/architecture.
P4 <-> P5: drafting can falsify an outline decomposition.
P6 <-> P1/P2/P3/P4/P5: hostile review can reopen any earlier branch.
P7 <-> P1/P5: claim audit can expose source or wording defects.
P8 <-> P4/P5: venue constraints can compress/reorder presentation but cannot silently change protected identity.
P9 <-> all earlier substantive phases through typed external feedback routed in P10.

### Overlap relations that require boundary control

P1 and P7 both touch provenance, but P1 closes research evidence while P7 verifies manuscript claim-to-source execution.
P2 and P8 both touch literature/framing, but P2 establishes novelty while P8 adapts presentation to a venue.
P3 and P6 both attack the ceiling, but P3 proactively generates stronger theory while P6 adversarially attacks a complete manuscript.
P4 and P5 both shape exposition, but P4 plans dependency architecture while P5 tests it in prose.
P6 and P9 both involve reviewers, but P6 is internal simulation while P9 is actual external handoff.

## Pair synthesis

The roadmap is not a ten-step chain. It is a dependency graph with four macro-states:

A. ORIENT
P0

B. RESEARCH-CLOSURE / CEILING FRONTIER
P1 || P2 || P3

C. MANUSCRIPT CONSTRUCTION AND INTERNAL VALIDATION
P4 -> P5 -> P6 -> P7
with feedback edges back to P1-P5

D. EXTERNALIZATION
P8 -> P9 -> P10
with venue framing P8 permitted to begin once a stable manuscript center exists.

## Joint n-ary finding

The higher-order structure is a gated feedback network, not a waterfall.

The central joint relation is:

(P1 + P2 + P3) do not each need global completion before P4/P5.
Instead, each must reach DRAFT-SAFE status for the particular manuscript dependency it feeds.

This creates a new readiness predicate:

DRAFT_SAFE(x) iff the unresolved coordinates in branch x are explicitly represented and none can silently invalidate the manuscript architecture currently being drafted.

This is not recoverable from any single pair alone because it concerns simultaneous partial closure across the three research branches plus their shared consumer P4/P5.

Second higher-order finding:

P6 hostile review and P7 reproducibility are not merely late phases. They are convergence tests on the entire P1-P5 subgraph. A material failure reopens the earliest causal phase rather than being patched locally.

Third higher-order finding:

P0 is not a substantive publication phase. It is a persistent control service. Treating it as a normal once-only phase overstates its importance and risks backend delay. Build the minimum live cockpit, then keep it updated by checkpoints.

## Irreducibility

- DRAFT_SAFE is HIGHER_ORDER_CANDIDATE: removal of any of P1/P2/P3 changes what can count as safe architecture input.
- P6/P7 as convergence gates is HIGHER_ORDER_CANDIDATE at program level.
- P0 as persistent service is a REFINEMENT of pairwise orientation relations.

## Reconciliation with prior roadmap

Prior roadmap correctly identified partial parallelism of P1-P3 but still visually privileged a phase sequence.

Successor representation:

SERVICE S0: live cockpit/orientation
WORKSTREAM W1: sources/corpus/provenance
WORKSTREAM W2: novelty/comparators
WORKSTREAM W3: theory/ceiling
GATE G1: DRAFT_SAFE across W1-W3
BUILD B1: integrated manuscript architecture
BUILD B2: drafting
GATE G2: hostile review
GATE G3: reproducibility/claim audit
EXTERNAL E1: venue/framing
EXTERNAL E2: researcher handoff
FEEDBACK E3: revision/submission

S0 persists across all states rather than being completed and left behind.

## Order sensitivity

Material order sensitivity exists:
- P3 before P4 can change architecture.
- P2 before final introduction/conclusion reduces novelty rewrite.
- P1 before source-heavy sections reduces provenance rewrite.
- P8 too early risks venue-driven scope distortion.
- P6 requires enough of P5 to attack an integrated object.
- P7 before P6 can waste claim-audit effort on prose later rewritten.

No need to enumerate all 11! permutations. The discriminating constraints above establish the partial order.

## OPEN

1. Exact threshold for DRAFT_SAFE per branch.
2. Whether P8 venue work begins after P4 or after P6.
3. Whether source-heavy manuscript subsections can begin before global G1.
4. How much S0 cockpit construction is minimum sufficient before W1-W3 begin.

## Disposition

Replace the simple phase-zero-first waterfall with a persistent cockpit service plus three research workstreams and explicit DRAFT_SAFE gate. Use the Universal Operating Loop at every state transition and re-run Multi-Object PD after any phase/workstream changes object type or dependency topology.
