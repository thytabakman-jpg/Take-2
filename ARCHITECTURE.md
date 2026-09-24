# Take-2 kernel architecture v0

## Design rule

Represent semantic distinctions without automatically creating independent operating
surfaces for each distinction.

## Five primitives

### Object
A stable identified thing with kind, state, authority, evidence references, and version.

### Relation
A typed directed claim between objects with provenance and authority. Relations are
first-class; duplicated prose is not a substitute.

### Event
An immutable record that something material occurred. Events record facts about change;
they do not become authority merely by existing.

### Transition
The only ordinary path for consequential state change. A transition declares baseline,
target, authority, evidence, expected effects, protected behavior, validators, and
result.

### Observation
Structured evidence emitted by operations and transitions. Observations include timing
when available, tool/capability identity, result, failure, boundary crossed, and objects
read/changed.

## Kernel loop

OBSERVE
-> FREEZE/TYPE
-> PD DISCOVER/CHALLENGE
-> DIAGNOSE when causal explanation is the job
-> DECIDE under authority
-> TRANSITION
-> VERIFY
-> OBSERVE
-> REENTER when material state changed

## PD at the heart

PD is the kernel's epistemic control layer, not a project-specific plugin.

Stable PD jobs admitted initially:
- task/object typing;
- hidden dependency discovery;
- representation attack;
- result-sensitivity compression;
- robust localization;
- rival clean-sheet reconstruction;
- provenance/attribution disentanglement;
- referent continuity;
- recurrence escalation;
- historical reconciliation;
- dependency/spine reconstruction;
- regression/post-candidate verification;
- HF-001 recursive discovery.

Candidate/experimental jobs remain callable but cannot silently become stable kernel
requirements. Their evidence class travels with their output.

PD never owns mutation authority. It changes what is known, typed, OPEN, or licensed;
Transition performs state change under the relevant authority.

## Views, not registries by default

Backlog, debt, sort-later, workstreams, audit campaigns, execution receipts, diagnosis
lists, transfer queues, and lifecycle dashboards begin as queries/views over kernel
objects, relations, events, transitions, and observations.

A dedicated durable surface is admitted only when a view cannot preserve required
semantics or authority.

## Authority

Authority is explicit and typed. Evidence, diagnosis, priority, and tool output do not
self-authorize mutation. No control may promote its own output solely from local
success.

## Observability

Every consequential transition must emit enough structured observation to answer:
what ran, on what baseline, why, under what authority, what changed, what was checked,
what failed, how long observable portions took, and what remains OPEN.

Missing telemetry is represented as missing telemetry, not converted into a causal claim.

## Evolution

Architecture changes by small transitions guarded by executable fitness checks.
A new abstraction must demonstrate strict gain over a view/composition of existing
primitives before becoming a primitive or dedicated subsystem.
