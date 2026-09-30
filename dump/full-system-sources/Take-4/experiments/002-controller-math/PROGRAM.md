# ICC Controller Mathematics Program 001

## Why this exists

The controller currently distinguishes directed and autonomous operation operationally, but the selection mathematics is not yet licensed. This program joins that question to the existing capability-preservation and ICC-over-kernel mathematics.

## Core objects

Let an episode state be

[
z_t = (G, x_t, O_t, H_t, A_t, B, \Gamma)
]

where G is the governing goal, x current system state, O observations, H history, A admissible actions, B protected behaviors/capabilities, and Γ authority and safety constraints.

A controller chooses both a problem/subgoal p and an action or policy a.

## Directed ICC

A directed run receives a frozen target p*. Its admissible choice set is restricted:

[
\Pi_D(z;p^*) = \{\pi : \pi \text{ pursues } p^* \text{ within } A_t, B, \Gamma\}.
]

The informal expression "arg max Q with target fixed" is only a placeholder. The research problem is to define a non-circular, evidence-sensitive selection relation over admissible policies without collapsing incomparable coordinates into a scalar.

Candidate form:

[
\pi_D \in \operatorname{Max}_{\succeq_z}\Pi_D(z;p^*)
]

where ⪰z is a partial preference/dominance relation induced by goal progress, information gain, cost, risk, reversibility, protected behavior, and authority.

## Autonomous ICC

An autonomous run may also choose the next subproblem p from a licensed problem set P(z):

[
(p_A,\pi_A) \in \operatorname{Max}_{\succeq_z}
\{(p,\pi):p\in P(z),\pi\in\Pi(z,p)\}.
]

The informal expression "arg max expected goal gain" is again a placeholder, not an established objective function. The research problem is to define goal gain, expectation under epistemic uncertainty, problem-generation boundaries, and stopping/reselection rules.

## Required connection to capability preservation

Controller selection is invalid when local gain destroys protected system behavior.

For protected capabilities B, candidate changes S→S' require a preservation/refinement witness:

[
S \preceq_B S'.
]

Research must distinguish capability existence, reachability, controller realizability, and witnessed verification.

A candidate Safe Capability Expansion relation remains:

[
S \trianglelefteq_{B,G} S'
]

only when protected behavior is preserved, G-relevant capability is realizable and verified, authority is respected, and the reachable useful behavior set strictly expands on at least one licensed coordinate without an unlicensed regression.

## Joint math questions

M1. What is the correct mathematical object for controller choice when evaluation coordinates are partially ordered or incomparable?

M2. What exactly is Q in directed mode? Is it value, evidence-weighted dominance, information value, progress toward a frozen target, or a family of coordinates?

M3. What exactly is GoalGain in autonomous mode? How is gain measured without Goodharting the controller into proxy optimization?

M4. How are candidate subproblems P(z) generated and bounded?

M5. Under what conditions does autonomous problem selection dominate directed selection, and when does the extra freedom create avoidable search, risk, or drift?

M6. Can directed mode be represented as autonomous mode under the constraint P(z)={p*}, or does target freezing change the semantics of evidence, termination, or authority?

M7. How do uncertainty and information gain affect selection? When is an experiment preferable to a direct repair?

M8. How do preservation constraints S≼_B S' compose across multiple transitions?

M9. What behavioral quotient is sufficient to certify protected capability preservation without exhaustive execution?

M10. What termination predicate establishes completion relative to G without confusing search exhaustion with closure?

M11. What reselection rule prevents both premature stopping and endless "improvement"?

M12. What witness tests establish that a controller can actually realize a registered capability rather than merely containing the required components?

## Two simultaneous ICC attacks

### Track D — pointed/directed

Frozen target: solve M1-M12 as a controller-mathematics problem, prioritizing formal definitions, counterexamples, minimal sufficient conditions, and executable tests. It may decompose the target but not replace it.

### Track A — autonomous

Governing goal: increase the verified ability of the ICC-over-kernel architecture to improve itself and solve user goals without losing protected capabilities. It may choose a different mathematical or architectural subproblem when evidence indicates higher expected goal contribution. It must record why it selected that problem rather than Track D's target.

## Anti-paperclip constraints

No scalar objective is licensed by default.
Protected capabilities and authority are hard admissibility constraints, not tradeable reward terms.
OPEN and INCOMPARABLE remain representable outcomes.
Proxy improvement does not establish goal improvement.
A controller may not self-certify a capability that lacks an independent witness.
Reversible experiments are preferred when competing hypotheses remain materially live.

## Immediate experiments

E1 construct examples where scalar Q chooses a dominated or capability-destroying action.
E2 compare Pareto/maximal-element selection, lexicographic constrained choice, and set-valued choice.
E3 construct a directed/autonomous equivalence case and a case where they diverge.
E4 formalize a minimal capability witness for autonomous project repair.
E5 test whether preservation is compositional under sequential verified transitions.
E6 derive the smallest state sufficient for reselection after observation.

## Status

Research candidate. No claim above promotes a controller, changes production authority, or establishes that the placeholder arg-max formulations are correct.
