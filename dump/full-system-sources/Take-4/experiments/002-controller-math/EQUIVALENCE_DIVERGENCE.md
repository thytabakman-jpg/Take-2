# Experiment 003 — Minimal Pointed/Autonomous Equivalence and Divergence

## Question

What is the smallest formal change that makes autonomous ICC capable of a result that a pointed ICC cannot obtain while the pointed target remains frozen?

## Model

Let a controller state be z=(G,P,F,O,B,Γ).

- G: governing goal.
- P: licensed candidate subproblems.
- F(p): feasible policies for p after hard authority and protected-capability filters.
- O: observations.
- B: protected capabilities.
- Γ: authority constraints.

A pointed controller D receives frozen p* and may choose only from F(p*).

An autonomous controller A may choose p∈P and then a policy from F(p).

Selection is set-valued over maximal admissible candidates; no scalar Q is assumed.

## E0 — Equivalence base case

Let P={p1}. Let p*=p1. Let both controllers share identical F, observations, comparison relation, stopping rule, B, and Γ. Autonomous problem regeneration is disabled during the episode.

Then:

D(z,p1)=Max F(p1)

and

A(z,G)=Max {(p1,π):π∈F(p1)}.

After projection away from the trivial p1 label, their policy frontiers are identical.

### Result

Pointed and autonomous modes are behaviorally equivalent in this model.

### Sufficient equivalence conditions

EQUIV holds when all of the following remain invariant:

E1 P={p*}.
E2 Same feasible-policy map F(p*).
E3 Same evidence/observation semantics.
E4 Same candidate comparison relation.
E5 Same protected capabilities and authority constraints.
E6 Same local stopping semantics.
E7 No authority to regenerate P during the episode.

This gives a testable baseline rather than assuming "pointed is autonomous with one option."

## D1 — Cardinality divergence

Change only P:

P={p1,p2}.

Suppose every π∈F(p1) leaves G unsatisfied, while some π2∈F(p2) reaches a verified G-satisfying state and preserves B.

Pointed target remains p*=p1.

Then D cannot realize the G-satisfying trajectory. A can select p2 and realize it.

### Minimal changed property

|P| changed from 1 to 2 while problem-selection authority remained available to A.

### Interpretation

The first obvious source of autonomous advantage is licensed alternative problem selection.

But this is not yet the deepest distinction because a pointed controller could have been pointed at p2 externally.

## D2 — Regeneration divergence

Start with P0={p1}; both controllers initially equivalent.

Execute a policy for p1 and receive observation o1. Let a problem-generation operator R produce:

R(G,z1,o1)={p1,p2}.

Pointed authority freezes p1. Autonomous authority permits replacing P0 with R(...).

Suppose p2 now has the only verified G-satisfying trajectory.

### Result

The modes diverge even though they began with the same singleton problem set.

### Minimal changed property

Problem-set regeneration authority after material evidence.

This is stronger than initial candidate-set cardinality.

## D3 — Representation divergence

Keep the external world fixed. Let p1 be a decomposition that makes no feasible G-satisfying policy expressible. Let a reframing operator ρ(p1,O) produce p2, under which such a policy becomes expressible.

A may apply ρ because problem representation is inside its licensed problem-selection authority. D may challenge/clarify p1 but may not replace its frozen target.

### Result

Autonomy can expand reachable behavior by changing the problem representation, not merely by selecting from a pre-enumerated list.

### Important constraint

ρ is not automatically valid. Referent continuity, authority, and protected-goal invariants must establish that p2 remains a licensed child of G rather than goal drift.

## D4 — Information-acquisition divergence

Let P={repair-now, discriminate-first}. Current evidence leaves two causal hypotheses live. Direct repair has different consequences under the hypotheses. An experiment e can distinguish them at bounded cost and without violating B.

A may choose the meta-subproblem discriminate-first. A pointed repair controller cannot abandon its frozen repair target unless experimentation is already admitted as an action inside F(repair-now).

### Result

Whether autonomy adds capability depends on the action/problem typing boundary.

### Discovery

"Autonomous advantage" is representation-relative unless the ontology distinguishes:
- actions within a problem,
- decomposition/reframing of the problem,
- creation of a new subproblem.

This makes the action/problem boundary itself load-bearing.

## D5 — Challenger composition

Joint controller J:

1. A selects p*.
2. D executes a pointed episode.
3. A_challenge observes the result but lacks direct mutation authority over D's target.
4. If a material relevance predicate M(G,p*,O') is false, A_challenge proposes reselection.
5. Authority gate either freezes p* or returns control to A.

This preserves local focus while exposing target error.

### Key property

The autonomous layer need not continuously interfere with pointed execution. Its distinctive capability can be concentrated at explicit reselection boundaries.

## Candidate theorem 1 — Static reduction

Given E1-E7, autonomous control reduces to pointed control up to projection of the singleton problem label.

Status: candidate theorem; proof obligation straightforward under the defined model, but not promoted beyond this model.

## Candidate theorem 2 — Strict autonomy gain

Autonomy has a strict behavioral advantage over pointed control relative to G only when there exists a licensed controller operation outside the pointed episode's admissible closure whose execution enables a verified G-relevant trajectory unavailable inside that closure.

Formally, with Reach_D(z,p*) the states reachable under pointed admissible closure and Reach_A(z,G) under autonomous licensed closure:

AutonomyGain iff there exists x such that

x∈Reach_A(z,G) \ Reach_D(z,p*)

and VerifiedGoal_G(x) and Preserve_B(x).

This defines the gain behaviorally rather than by naming a particular mechanism.

## Candidate theorem 3 — Source taxonomy

Strict gain can arise from at least four sources:

S1 alternative subproblem selection;
S2 post-observation problem-set regeneration;
S3 licensed problem reframing/decomposition;
S4 meta-information acquisition excluded from pointed admissible closure.

These collapse into one deeper property:

AUTONOMOUS DOMAIN EXPANSION

The controller can alter its admissible problem/policy domain in a G-licensed way after receiving evidence.

## Directed ICC verdict

The smallest clean divergence is D2, not D1.

D1 only gives the autonomous controller more preloaded choices. D2 captures the genuinely dynamic capability: evidence can change which problem is being solved.

Provisional discriminator:

A is genuinely autonomous relative to D when it has licensed evidence-sensitive authority over future problem-domain construction that D lacks.

## Autonomous ICC verdict

The autonomous attack selects a different next target.

The deepest unresolved variable is not autonomy itself but ADMISSIBLE CLOSURE.

If every useful reframe, experiment, decomposition, and subproblem change is encoded as an ordinary action inside F(p*), pointed control can simulate much of apparent autonomy. If they are excluded, autonomy appears stronger.

Therefore the next mathematical problem is to define the closure operator Cl_D(z,p*) generated by a pointed controller's admissible transformations and compare it with Cl_A(z,G).

The important quantity is not nominal mode but the difference:

ΔCl = Cl_A(z,G) \ Cl_D(z,p*).

Only elements of ΔCl that enable verified G-relevant trajectories count as genuine additional capability.

## Joint synthesis

The directed run localizes dynamic problem-domain regeneration as the first clean divergence.

The autonomous run finds the hidden dependency: the divergence is only meaningful relative to a formally defined admissible closure.

Together they replace the vague distinction

"pointed solves a given problem; autonomous chooses the problem"

with:

POINTED:
evolves inside a frozen admissible closure, except at externally authorized reselection boundaries.

AUTONOMOUS:
has licensed evidence-sensitive operators that can expand, contract, or reconstruct the admissible closure relative to G.

JOINT:
uses autonomous closure revision at explicit boundaries and pointed optimization inside each temporarily frozen closure.

## Next math attack

1. Define Cl_D and Cl_A as typed closure operators.
2. Determine monotonicity, idempotence, extensivity, and authority sensitivity.
3. Test whether closure revision commutes with evidence update.
4. Define ΔCl capability contribution without scalarizing incomparable outcomes.
5. Derive conditions under which J preserves the focus guarantees of D and the domain-revision capability of A.
6. Connect closure expansion to S≼_B S' so new reachability cannot erase protected behavior.

## Status

The experiment establishes model-relative counterexamples and candidate relations. It does not yet establish a general theorem about all ICC implementations.
