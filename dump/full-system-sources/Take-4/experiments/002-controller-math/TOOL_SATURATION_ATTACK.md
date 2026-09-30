# Tool-Saturation Attack — Pointed ICC, Autonomous ICC, and Joint Controller

## Goal

Attack the newly exposed controller distinction with the cumulative demonstrated toolset, not with one favored architecture.

Targets:

- P: pointed/directed ICC, where the problem target is frozen.
- A: autonomous ICC, where problem/subgoal selection is licensed inside a governing goal and authority boundary.
- J: joint controller, where pointed and autonomous modes can compose, switch, challenge, or supervise one another.

No scalar objective is assumed.

## Tool order

The first substantive discovery operation is HF-001 recursive PD. Then use semantic/type admission, dependency/spine reconstruction, orthogonal/rival attacks, PDAudit sensitivity, robust localization, Multi-Object, Factorization/Quotient, Diagnosis, TransferCore, Raise-the-Ceiling, ImprovementCore, hostile/non-regression verification, and HF-001 re-entry. Use ablation, noncommutation/order tests, metamorphic/invariant tests, recurrence analysis, fixed-point/cycle analysis, and capability witnesses where triggered.

The same tools attack P, A, and J separately. Results are then compared relationally rather than collapsed into one score.

## Attack 1 — Pointed ICC

### HF-001 descent

Frozen target p* does not by itself determine controller behavior. Load-bearing unresolved objects:

1. target identity and referent continuity;
2. admissible policy set Π_D(z;p*);
3. evaluation relation over policies;
4. evidence update;
5. protected-capability constraints;
6. termination relative to p*;
7. re-entry after material observation;
8. authority for target modification.

The expression argmax Q | p=p* is underdefined until 2-7 are fixed.

### Orthogonal/rival attack

Rival formulations:
- scalar utility Q;
- lexicographic constrained optimization;
- Pareto/maximal-element choice;
- satisficing with proof obligations;
- set-valued admissible frontier followed by discriminating experiment.

Scalar Q loses OPEN/INCOMPARABLE unless a justified commensuration map exists. Therefore scalarization is not admitted as the default representation.

### PDAudit/result sensitivity

Result-sensitive coordinates include target interpretation, admissibility constraints, preservation constraints, evidence state, cost/risk treatment, and stopping rule. Changing any can change the selected policy while leaving p* textually unchanged.

### Factorization

Pointed control factors into:
FREEZE → TYPE → GENERATE admissible policies → FILTER hard constraints → COMPARE remaining candidates → EXPERIMENT when unresolved → SELECT → EXECUTE → VERIFY → REENTER/STOP.

### Provisional mathematical object

[
D(z,p^*) = \operatorname{Max}_{\succeq_{z,p^*}} F(z,p^*)
]

where F is the feasible policy set after hard authority/preservation filters and Max returns a set of nondominated/maximal candidates, not necessarily one action.

Pointedness is therefore primarily a restriction on problem-selection authority, not necessarily a different optimization algebra.

## Attack 2 — Autonomous ICC

### HF-001 descent

Autonomy adds unresolved load-bearing objects:
1. licensed problem-generation set P(z);
2. relation between governing goal G and candidate subproblem p;
3. expected effect of solving p on G;
4. value of information and experimentation;
5. drift/Goodhart controls;
6. opportunity cost of choosing p rather than q;
7. problem reselection after observations;
8. termination at both subproblem and governing-goal levels.

Thus argmax ExpectedGoalGain is underdefined and potentially unsafe.

### Diagnosis

The central additional burden is not merely a larger action space. It is endogenous construction of the optimization domain. A controller that generates its own candidate problems can alter what is compared.

### Rival reconstruction

Candidate autonomous choice forms:
- maximize scalar expected goal gain;
- constrained multiobjective frontier;
- choose the experiment with maximal expected discrimination among live controller hypotheses;
- hierarchical control: goal → frontier of subproblems → local pointed episode → global reselection;
- adversarial dual-controller: proposer and challenger.

The hierarchical formulation survives more invariants than direct scalar maximization.

### Provisional mathematical object

Let P_G(z) be licensed candidate subproblems grounded in G. For each p define a pointed feasible frontier D(z,p). Then:

[
A(z,G)=\operatorname{Max}_{\trianglerighteq_{z,G}}
\{(p,\pi):p\in P_G(z),\pi\in D(z,p)\}.
]

This preserves the distinction between choosing a problem and choosing how to solve it.

## Attack 3 — Joint pointed/autonomous controller

### Multi-Object and relation ontology

P and A are not simple competitors. P can be a subroutine of A:

[
A: G \mapsto p^*; \qquad D: (z,p^*) \mapsto \pi.
]

But the reverse relation is also useful: a pointed episode can invoke an autonomous challenger whose authority is restricted to proposing alternative decompositions or detecting target failure, without authorizing target replacement.

### Noncommutation

In general:

[
D(A(z,G)) \neq A(D(z,p),G).
]

Choosing a subproblem before local optimization and locally optimizing before reconsidering the problem can produce different trajectories. Order is therefore result-sensitive.

### Candidate joint architecture

GLOBAL AUTONOMOUS FRONTIER
→ freeze selected p*
→ POINTED ICC episode
→ verify local result
→ AUTONOMOUS CHALLENGER checks whether p* remains goal-relevant
→ global reselection.

The challenger can reopen the target only under an explicit material-delta/authority rule.

### Combination theorem candidate

Directed mode is a special case of autonomous mode only under all of:

[
P_G(z)=\{p^*\},
]

identical feasibility/preservation constraints, identical evidence semantics, identical local stopping semantics, and no autonomous authority to regenerate the problem set during the episode.

Without these conditions, "directed = constrained autonomous" is false or incomplete.

## Cross-tool findings

### Recursive/dependency

The deepest shared dependency is a typed choice relation under changing evidence, not Q itself.

### Semantic admission

"Q", "goal gain", "problem", "progress", "expected", "done", and "autonomy" are not admitted primitives yet. Each requires operational semantics or decomposition.

### Orthogonal/rival

Scalar maximization is one rival, not the default. Partial orders and set-valued frontiers preserve incomparability.

### PDAudit

Controller output is sensitive to representation of the candidate set itself. This makes problem-generation a first-class result-sensitive operation.

### Multi-Object

State, goal, problem, policy, capability, evidence, authority, and observation must remain distinct typed objects.

### Factorization/Quotient

A minimal controller quotient appears to require:
[
Q_C(z)=\langle G,P,F,\succeq,B,\Gamma,O,H,Done\rangle
]
up to distinctions that can change selection, preservation, or termination.

### Diagnosis

The earlier loss of Take-2's autonomous repair behavior is an instance of controller-level behavior not being represented as a protected capability.

### TransferCore

The preservation/refinement mathematics transfers directly: controller improvement is licensed only when protected capabilities remain witnessed. The bridge is explicit because controller selection changes reachability of system behavior.

### Raise the Ceiling

The new ceiling is not "better Q". It is a controller that can change its own problem decomposition while retaining proof/witness obligations and protected behavior.

### ImprovementCore

Highest-information next experiments:
1. construct minimal counterexample where scalar Q selects a capability-destroying action that a constrained partial order rejects;
2. construct P/A equivalence and divergence models;
3. test hierarchical A→P versus monolithic autonomous choice;
4. test noncommutation under evidence updates;
5. derive sufficient conditions for preservation to compose over a controller trajectory;
6. derive termination/reselection fixed-point conditions.

### Dynamics/fixed points

Let R be one full controller cycle including observation and reselection. Desired termination is not merely R(z)=z. Need a goal-relative verified fixed point:

[
Done_G(z) \land R(z) \sim_G z
]

where ~_G ignores changes irrelevant to G and protected behavior. Cycles with unresolved relevant deltas are not closure.

### Metamorphic/invariant tests

Required invariants include:
- renaming irrelevant internal identifiers cannot change choice;
- adding a dominated candidate cannot remove an existing maximal candidate absent resource interaction;
- reordering independent evidence cannot change the final frontier;
- equivalent representations of p* cannot change pointed behavior;
- narrowing autonomy to singleton P_G must converge to pointed behavior under the equivalence conditions above.

## New mathematical frontier

The combined attack localizes five coupled problems:

C1 Choice algebra under partial order/incomparability.
C2 Endogenous problem-generation semantics.
C3 Hierarchical composition and noncommutation of problem selection with policy selection.
C4 Dynamic reselection/termination under evidence updates.
C5 Compositional capability preservation across controller trajectories.

These belong inside the broader unified transition calculus, not as isolated controller equations.

## Status

No scalar Q, ExpectedGoalGain functional, equivalence theorem, or preservation theorem is established yet. The attacks above narrow the objects and generate falsifiable next experiments.
