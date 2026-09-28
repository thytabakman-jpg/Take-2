# Fick Adaptive Production-Architecture Run — PD + ImprovementCore

Date: 2026-09-22
Project: jewish-holiday-booklets
Immediate target: Fick / Difference production architecture
Method: HF-001 recursive PD + manual/theoretical ImprovementCore checkpoint loop
Mutation scope: JHB shared production controls and Fick production-package controls only

## Method note

The executable PracticalCore/ImprovementCore path is currently in a transitional
architecture and is not treated here as a mechanically authoritative runtime. This run
therefore applies the demonstrated semantic ImprovementCore sequence manually:

PROTECT
-> LOCALIZE
-> SELECT
-> GENERATE
-> EVALUATE
-> DISPOSE
-> RECOMPUTE

Every durable state-changing checkpoint is followed by:
1. HF-001 recursive dependency/representation rerun;
2. ImprovementCore recomputation of the strongest remaining frontier;
3. non-regression check;
4. decision whether the next planned step still survives.

A "step" means a durable mutation or architectural conclusion that changes the remaining
plan. It does not mean every sentence or tool invocation, which would create infinite
self-audit recursion.

Stop condition:
- a rerun produces no new higher-leverage upstream change;
- remaining work is local execution under settled ownership, or depends on explicit user
  approval/external evidence.

## Checkpoint 0 — PD audit of the user's prompt

### Frozen prompt target

User request:
- use PD to determine the best next step;
- audit the recommendation itself before execution;
- after every meaningful step, rerun PD + ImprovementCore because the plan may change;
- use the strongest currently available theoretical understanding of ImprovementCore.

### HF-001 result

The prompt is not merely requesting repeated validation.

Its functional requirement is adaptive planning under state mutation.

Hidden dependency:
A plan selected at state S0 is not automatically licensed at S1 after the first repair.
Therefore later steps must not be treated as pre-authorized simply because they were in
the initial plan.

Correct process:

STATE_n
-> audit current bottleneck
-> select one bounded step
-> execute
-> STATE_n+1
-> recompute plan.

### ImprovementCore result

PROTECT:
- actual booklet completion remains governing goal;
- Fick exact-copy authority remains separate;
- current Fick package remains the package candidate;
- no duplicate production-control family;
- no broad project rewrite unless demanded by dependency leverage.

LOCALIZE:
- current live uncertainty is ownership of newly discovered production coordinates.

SELECT:
- first step remains ownership allocation, but only as an analytic record; do not yet
  create shared infrastructure.

GENERATE:
Candidate process options:
A. execute the whole previous six-step recommendation without recomputation;
B. audit every micro-action;
C. use bounded adaptive checkpoints.

EVALUATE:
C strictly dominates for this task: it preserves adaptivity without infinite recursion.

DISPOSE:
Reject A and B.

RECOMPUTE:
Next target is the previous recommendation itself.

## Checkpoint 0 result

The adaptive checkpoint method is accepted.

No production architecture mutated at this checkpoint.


## Checkpoint 1 — PD audit of the previous recommendation

Previous recommendation:
1. allocate every missing production coordinate to its correct owner;
2. create only the minimum shared JHB production substrate justified by that allocation;
3. repair the existing Fick package to reference the shared substrate;
4. recompute;
5. return to local Fick completion.

### HF-001 rerun

Question:
Does ownership allocation remain the earliest dependency after Checkpoint 0?

Yes.

Trying to create shared controls before allocation would require guessing which coordinates
are genuinely reusable.

Trying to continue Fick-local repair first would duplicate generic machinery.

Trying to repair the whole JHB architecture first would exceed the demonstrated
dependency frontier.

One refinement was discovered:

Ownership must be typed at two levels:
- schema/semantics owner;
- instance/value owner.

Example:
"content-to-slot binding" has a shared schema but Fick-specific values.
"renderer capability profile" has a shared interface schema but renderer-specific
instance data.

Without this distinction, an ownership audit could incorrectly move local values upward
or leave generic semantics duplicated locally.

### ImprovementCore rerun

PROTECT:
- JHB G0 remains completion of the four booklets;
- exact-copy authority remains separate;
- Fick package identity remains fixed;
- current package is repaired, not replaced.

LOCALIZE:
The highest-leverage uncertainty is now specifically:
schema owner vs instance owner for each missing coordinate.

SELECT:
Run one read-only ownership-allocation audit.

GENERATE:
Candidate next steps:
A. create shared production files immediately;
B. fill Fick package immediately;
C. create a typed ownership allocation matrix first.

EVALUATE:
C has strict gain because it reduces the permissible mutation frontier before any
architecture write.

DISPOSE:
A and B are deferred.

RECOMPUTE:
If the allocation converges, create only the shared contracts actually supported by the
matrix.

## Checkpoint 1 result

The previous recommendation survives with one refinement:
first produce a schema-owner / instance-owner allocation matrix.

Next step authorized:
read-only ownership allocation.


## Checkpoint 2 — ownership allocation completed; plan recomputation

Durable new state:
- audits/JHB_FICK_PRODUCTION_OWNERSHIP_ALLOCATION_2026-09-22.md now classifies
  schema owners and instance owners for every newly discovered production coordinate.

### HF-001 rerun

Question:
Does the ownership allocation reveal a different upstream repair than "create minimal
shared substrate"?

No.

It does reveal a representation choice that was previously under-specified:

Should shared semantics live only inside IMAGE_GENERATION_PROTOCOL.md, or in a typed
shared production contract?

The existing image protocol is procedural prose and already has a status note saying it
is incomplete relative to the newly discovered architecture.

The missing coordinates include reusable enums, lifecycle states, required interface
fields, authority boundaries, and fail-closed contracts that the Fick source package
needs to reference precisely.

Therefore merely expanding prose would preserve an ambiguous source->consumer relation.

### ImprovementCore rerun

PROTECT:
- IMAGE_GENERATION_PROTOCOL.md remains the human procedure for generation;
- do not replace it;
- do not create several new shared files;
- no new universal repository production system.

LOCALIZE:
One missing shared typed contract is the minimal reusable object.

SELECT:
Create exactly one shared JHB production contract.

GENERATE:
A. extend IMAGE_GENERATION_PROTOCOL.md only;
B. create several shared schema/control files;
C. create one typed production contract and later make the prose protocol reference it.

EVALUATE:
C provides the smallest strict gain:
- typed reusable semantics;
- one reference target for Fick;
- no duplication of procedural prose;
- no multi-file shared-control explosion.

DISPOSE:
A is too representation-weak for exact package conformance.
B is over-decomposed.

RECOMPUTE:
Next authorized step:
create one shared JHB production contract containing only the reusable semantics in the
ownership allocation.

Do not yet modify the Fick package in the same step.

## Checkpoint 2 result

Plan changed slightly:
the shared substrate will be exactly one typed shared contract, not a new family of
controls and not a prose-only expansion.


## Checkpoint 3 — shared production contract created; plan recomputation

Durable new state:
- projects/jewish-holiday-booklets/production/PRODUCTION_CONTRACT.yaml
- object: JHB:PRODUCTION:CONTRACT:001
- blob: 152e45c11e5dfd325a4105a6e50cc388d3eb59bf

### HF-001 rerun

Question:
Can the next step now be only "repair the Fick package to reference the new contract"?

A new upstream issue appears.

The shared production contract is now a load-bearing view, but nothing yet declares the
relation:

shared production contract
-> human generation protocol
-> booklet-local production package.

This resembles the broader representation-boundary failure class recently surfaced in
the PracticalCore architecture audit: a new load-bearing view can exist without an
explicit consumer/conformance relation.

Within JHB, the smallest repair is not a new interface framework.

It is to bind the existing IMAGE_GENERATION_PROTOCOL.md and root JHB state to the shared
contract before treating the contract as current production semantics.

### ImprovementCore rerun

PROTECT:
- one shared contract only;
- IMAGE_GENERATION_PROTOCOL remains the procedure;
- no repository-wide interface architecture work;
- Fick package remains untouched until upstream binding is explicit.

LOCALIZE:
The current frontier is shared-contract admission, not Fick-local instantiation.

SELECT:
Bind the shared production contract into the existing JHB production entry points.

GENERATE:
A. immediately update Fick;
B. update only IMAGE_GENERATION_PROTOCOL;
C. register the shared contract in root JHB state and point IMAGE_GENERATION_PROTOCOL to it.

EVALUATE:
C gives the smallest complete upstream join:
- root state identifies the current shared contract;
- procedural protocol names the contract it implements;
- Fick can then safely consume the same object.

DISPOSE:
A risks an orphan/shared-contract ambiguity.
B leaves current shared state implicit.

RECOMPUTE:
Next step changes:
before repairing Fick, register the shared production contract in JHB root state and add
a short conformance pointer in IMAGE_GENERATION_PROTOCOL.md.

## Checkpoint 3 result

The plan changed.

Next authorized step:
bind the new shared contract into existing JHB root production state and generation
procedure. Do not add another control object.


## Checkpoint 4 — shared contract admitted into JHB; plan recomputation

Durable new state:
- root JHB STATE.yaml registers JHB:PRODUCTION:CONTRACT:001;
- IMAGE_GENERATION_PROTOCOL.md explicitly identifies that contract as the owner of
  reusable production semantics;
- the protocol remains the human procedure rather than the semantic schema;
- terminal verification found an incorrect contract blob binding in root state;
- that binding was corrected to the actual GitHub blob identity before this rerun.

### HF-001 rerun

Question:
Has the highest-leverage frontier moved from shared architecture to Fick-local repair?

Yes.

The reusable meanings now have one shared owner and one explicit procedural consumer.

The remaining Fick architecture-research findings split into two classes:

A. architecture representation problems now solvable by reference:
- constraint vocabulary;
- reference roles;
- realization-mode vocabulary;
- overflow semantics;
- preflight contract;
- compiler contract;
- render-bundle schema;
- renderer-profile schema;
- run-provenance schema;
- coherence-group semantics.

B. Fick-local values still genuinely incomplete:
- stable internal content block IDs / content-slot assignments;
- actual wireframe/layout values;
- actual visual/style values;
- exact asset bindings;
- actual element realization choices;
- actual renderer profile selection;
- frozen exact-copy binding.

Therefore "architecture repair required" is no longer the right status once the Fick
package explicitly binds/delegates class A and represents class B as OPEN local values.

### ImprovementCore rerun

PROTECT:
- do not create another shared control;
- do not move Fick-specific values upward;
- do not mark render ready;
- do not freeze candidate copy without explicit user approval.

LOCALIZE:
The frontier is the existing Fick production-package representation.

SELECT:
Repair the existing package in place to:
1. bind the shared production contract by exact identity;
2. explicitly delegate generic semantics;
3. add typed local placeholders/registries for Fick values;
4. close architecture-repair status as a representation issue only;
5. keep render blocked on incomplete local values and frozen-copy approval.

GENERATE:
A. replace the package with a new v2 package;
B. create a separate visual control and renderer control;
C. repair the existing package by reference.

EVALUATE:
C preserves object identity, minimizes synchronization surfaces, and satisfies the
architecture-research completion rule.

DISPOSE:
A and B rejected.

RECOMPUTE:
Next authorized step:
repair JHB:FICK:PRODUCTION-PACKAGE:CANDIDATE:001 in place and update Fick STATE.yaml to
distinguish "architecture represented" from "production values complete."

## Checkpoint 4 result

The plan survives but narrows.

Next step is Fick package repair-by-reference, not further shared architecture work.


## Checkpoint 5 — Fick package architecture representation closed; plan recomputation

Durable new state:
- JHB:FICK:PRODUCTION-PACKAGE:CANDIDATE:001 now binds
  JHB:PRODUCTION:CONTRACT:001 by exact identity;
- generic production semantics are delegated rather than duplicated;
- local registries now explicitly represent content binding, coherence group,
  constraints, references, structure refs, realization, overflow, renderer profile,
  preflight, compiler, bundle, and run state;
- architecture_repair is closed at the representation/ownership level;
- render remains blocked on local values and explicit copy freeze.

### HF-001 rerun

Question:
Is the next highest-leverage task now stable content-block/slot binding?

Almost, but terminal state comparison reveals one stale-control defect first.

Fick STATE.yaml still reports:
lifecycle.current_stage = preservation_ledger.

Root JHB STATE.yaml still includes an explicit next action to construct the Fick
preservation ledger.

Those descriptions no longer represent the active frontier.

The local state itself now says the next action is production-package completion.

Therefore the system has a source/consumer liveness mismatch:
current local production state changed, but higher-level/current-stage projections did
not fully follow it.

This is small, but advancing while state is stale would recreate the exact architecture
failure family being repaired elsewhere.

### ImprovementCore rerun

PROTECT:
- do not reopen architecture;
- do not modify goals;
- do not change product-acceptance findings.

LOCALIZE:
state synchronization only.

SELECT:
repair the stale stage/next-action projections.

GENERATE:
A. ignore stale metadata and continue;
B. rewrite broad root architecture;
C. update only the stale Fick stage and the obsolete root Fick next-action line.

EVALUATE:
C is the smallest supported repair.

DISPOSE:
A risks future incorrect task routing.
B exceeds the frontier.

RECOMPUTE:
After synchronization, rerun before choosing between:
- content-block/slot binding;
- copy approval/freeze;
- layout/visual production completion.

## Checkpoint 5 result

Plan changed again:
perform one bounded state-synchronization repair before the next production task.


## Checkpoint 6 — state synchronization completed; final plan recomputation

Durable new state:
- Fick lifecycle.current_stage now reports production_package_completion;
- root JHB next action now routes Fick through booklet-local production-package
  completion rather than the obsolete preservation-ledger step.

### HF-001 rerun

Current remaining blockers:
- exact copy not frozen;
- stable content-block/slot binding incomplete;
- layouts/structure incomplete;
- shared style values incomplete;
- exact assets incomplete;
- element realization plan incomplete;
- renderer profile unbound;
- preflight not run;
- package not frozen.

Question:
Which remaining dependency has the highest leverage and is actually licensed now?

The exact-copy freeze is upstream of the detailed visual/layout production work.

COPY_CONTROL already requires a frozen copy before visual-spec production.

Stable content-block/slot work could technically be started against the mutable candidate,
but doing so before approval creates avoidable churn if wording or segmentation changes.

Detailed layout/visual work before freeze would violate the current production gate.

Therefore the next step is not another architecture mutation.

It is explicit user review/approval of the current exact-copy candidate, followed by
immutable promotion.

### ImprovementCore rerun

PROTECT:
- do not silently approve wording;
- do not freeze candidate without explicit user approval;
- do not start downstream visual/layout production against an unfrozen copy.

LOCALIZE:
highest-leverage blocker = exact-copy approval/freeze gate.

SELECT:
request explicit approval of JHB:FICK:COPY:CANDIDATE:001.

GENERATE:
A. assign block IDs before approval;
B. start layouts/visuals before approval;
C. stop at approval gate.

EVALUATE:
C preserves the designed dependency order and avoids downstream rework.

DISPOSE:
A is possible but lower leverage and creates version churn.
B violates the current gate.

RECOMPUTE:
After explicit approval:
1. create immutable exact-copy snapshot;
2. update COPY_CONTROL and Fick/package bindings;
3. rerun HF-001 + ImprovementCore before selecting the next local production step.

## Checkpoint 6 result — relative convergence

The adaptive loop has reached a real user-controlled gate.

No further autonomous architecture mutation is currently justified.

Next action:
explicitly approve or revise the exact-copy candidate.

Stop condition satisfied:
- no new higher-leverage upstream architecture change emerged;
- the strongest remaining dependency requires explicit user approval.
