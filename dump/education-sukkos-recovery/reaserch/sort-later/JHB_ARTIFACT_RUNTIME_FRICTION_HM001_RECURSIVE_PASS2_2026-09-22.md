# JHB Artifact Runtime Friction — HM-001 Recursive Pass 2

Date: 2026-09-22
Status: DEFERRED ARCHITECTURAL FINDING
Authority: diagnostic / read-only; no JHB canonical state or artifact authority changed
Predecessor: sort-later/JHB_ARTIFACT_RUNTIME_FRICTION_PD_AUDIT_2026-09-22.md

## Audit question

Is the predecessor diagnosis

TASK -> PROJECT -> BOOKLET -> OPERATION/PREDICATE -> ARTIFACT ROLE -> EXACT OBJECT

deep enough, or is artifact-role resolution itself still downstream of a deeper missing dependency?

## Result

The predecessor diagnosis is necessary but not sufficient.

The next deeper generator is:

MISSING DURABLE, SCOPED CONTINUATION BINDING

The system has increasingly strong static authority and exact-object identity, but it does not yet represent strongly enough the relation:

this task / this workstream / this conversational continuation
is operating on
this exact object-set
in this exact role
at this exact branch/state.

A flat booklet-level `active_working_set` would not fully repair this and can create a new concurrency defect.

## HM-001 reconstruction

### Target state

A fresh conversation saying "work on Fick; show me the pages we have now" must continue the actual live work without:

- broad historical reconstruction;
- search deciding authority;
- accepted baseline substituting for current working object;
- a parallel chat's candidate silently replacing this chat's candidate;
- a PDF or preview substituting for page-native objects;
- user confirmations disappearing when the chat ends.

### Starting state

Existing architecture already provides:

- canonical project/booklet state;
- accepted repair-baseline authority;
- exact research-object identity;
- exact-object preflight;
- material-event closure;
- workstream/concurrency infrastructure;
- derived-state freshness controls;
- a JHB runtime bootstrap.

Historical JHB storage audits already stated the stronger target:

- one authoritative home for current semantic state;
- parallel work branches from an accepted base;
- transactional updates;
- conflict detection;
- explicit unresolved alternatives;
- derived human-readable views;
- a new chat continues without reconstruction.

The present failure is evidence that these requirements are not yet composed at the task-to-object interface.

### Epistemic sequence

Observed sequence:

1. user task names Fick/current pages;
2. no durable continuation binding is loaded;
3. retrieval reconstructs likely target from available artifacts;
4. exact-object controls correct authority toward the accepted baseline;
5. task still fails because accepted baseline is not the current conversational working object;
6. user re-supplies the pages;
7. unless this selection is durably and correctly scoped, a later chat repeats the failure.

The key transition failure occurs before artifact-role resolution.

The system is missing the continuation state required to interpret deictic/task-relative terms such as:

- current;
- the one we were working on;
- these pages;
- the version from that zip;
- continue Fick;
- our latest working booklet.

### Hidden premise in predecessor repair

The predecessor proposed a booklet-local field:

`active_working_set = JHB:FICK:WORKING-PAGES:002`

Hidden premise:

there is one globally correct active working set per booklet.

Counterexample:

two concurrent chats branch from the same accepted Fick baseline and test different repair candidates.

Both candidates are active working sets relative to their own workstreams.

A single booklet-level pointer either:

- overwrites one branch;
- silently chooses one branch as global;
- oscillates as chats update it;
- or forces false serialization.

Therefore `active_working_set` is not generally a booklet-global scalar.

### Deeper distinction

At least five coordinates were being collapsed into "artifact role":

1. authority/lifecycle class
   - accepted_source
   - candidate
   - rejected
   - superseded

2. task function
   - repair baseline
   - edit target
   - comparator
   - display target
   - package source
   - final accepted product

3. continuation/workstream scope
   - which branch/chat/workstream owns the current selection

4. representation
   - individual PNG pages
   - PDF
   - composite/contact sheet
   - editable source

5. temporal/version event
   - which exact state after which user confirmation or transition

These are orthogonal enough that one flat `artifact_role` field is unsafe.

## Recursive competing explanations

### Search failure

Real but downstream.
The failure persists after search is removed from authority selection.

### Exact-object failure

Real historically but not sufficient now.
The old baseline has exact identity and can still be the wrong task object.

### Artifact-role failure

Necessary but still too shallow.
Role without workstream/branch scope is not unique.

### State-capture failure

Closer.
A user-confirmed working set was not durably propagated into the operational continuation state.

### General transactional-continuation failure

Best current generator.

The project has static durable state, but the conversation-to-workstream-to-object transition is not fully transactional and typed.

The missing object is a continuation binding, not another artifact.

## Clean reconstruction

The stronger runtime spine is:

USER UTTERANCE
-> TASK CONTRACT
-> PROJECT / BOOKLET
-> CONTINUATION CONTEXT
-> WORKSTREAM / BRANCH
-> OPERATION / PREDICATE
-> TASK FUNCTION
-> AUTHORITY / LIFECYCLE CONSTRAINT
-> REPRESENTATION REQUIREMENT
-> EXACT OBJECT SET + VERSION
-> FRESHNESS / CONFLICT CHECK
-> EXECUTION / PRESENTATION
-> MATERIAL EVENT CAPTURE
-> TRANSACTIONAL STATE PROPAGATION
-> DERIVED VIEW REFRESH.

A compact continuation binding can be represented as a tuple such as:

B = <project, booklet, workstream, branch/base, operation, task_function, representation, exact_object_set, source_event, freshness>

The resolver must return one licensed binding or OPEN.

## Precedence for task referent resolution

For the current task only:

1. explicit current-turn user designation;
2. explicit continuation/workstream binding;
3. promoted booklet/project default binding;
4. OPEN / ask one targeted clarification.

Search recency and filenames are never tie-breakers.

Current-turn designation binds the task target without automatically changing artifact acceptance status.

## Corrected Fick repair

The four supplied pages are now the exact target for this conversation.

Registering them as a source-set candidate is useful.

Do not immediately make them the single booklet-global `active_working_set`.

Instead:

- preserve `JHB:FICK:ACCEPTED-PAGES:001` as accepted repair baseline;
- register the four supplied pages as an exact candidate/working source set;
- bind that set to the current Fick workstream/continuation;
- optionally promote a project-level `default_current_working_set` only through an explicit transition when the user intends this candidate to become the default continuation target;
- keep `accepted_product` separate.

## JHB architecture repair

### Artifact registry

Owns immutable page/set identities, hashes, representation and lineage.

### Booklet STATE

Owns globally meaningful lifecycle and promoted default bindings only:
- accepted repair baseline;
- accepted product;
- production candidate when globally designated;
- default continuation target when explicitly promoted.

It does not own every chat's transient working candidate.

### Workstream / continuation state

Owns:
- exact base;
- exact current working set;
- operation;
- comparison set;
- branch;
- user-confirmation event;
- open conflicts.

### Material-event ledger

Owns the transition:
"user confirmed set S as the continuation target for scope W"
and any later promotion/supersession.

### Generated workbench

Joins booklet state + workstream binding + artifact registry + acceptance controls.
It is freshness-checked and non-authoritative.

## Cross-project transfer

The deeper reusable defect is not JHB-specific:

STATIC STATE WITHOUT SCOPED CONTINUATION SEMANTICS.

Other projects can have the same failure whenever they distinguish:

- accepted baseline vs live branch;
- current manuscript vs comparator;
- canonical model vs experimental successor;
- current analysis object vs historical source;
- branch-local working state vs global project state.

The transferable preflight becomes:

1. resolve the task;
2. resolve continuation/workstream scope;
3. resolve object role/function;
4. resolve exact object/version;
5. verify freshness and conflicts.

A portfolio-wide new router is not yet licensed merely from this finding; existing workstream/intention machinery may be extendable.

## Recursive convergence tests

The repair is not converged until these cases behave correctly:

1. one Fick workstream, one candidate -> "current Fick" resolves that candidate.
2. two parallel Fick workstreams -> each resolves its own candidate.
3. new chat with one promoted default -> resolves the promoted default.
4. new chat with two live unpromoted alternatives -> returns OPEN rather than guessing.
5. user uploads four pages and says "these are the ones" -> current task binds immediately to them without accepting them as final product.
6. "show baseline" -> accepted repair baseline.
7. "compare current to baseline" -> workstream candidate + accepted baseline.
8. "show final accepted product" -> accepted product or OPEN.
9. package_current -> derives from resolved workstream/default set; no independent reselection.
10. derived workbench stale after state transition -> blocks until refreshed.

## Final HM-001 result

The predecessor repair was one layer too shallow.

The missing invariant is not merely:

TASK PREDICATE BEFORE ARTIFACT ROLE BEFORE EXACT OBJECT.

The stronger invariant is:

SCOPED CONTINUATION CONTEXT BEFORE TASK-RELATIVE ROLE BEFORE EXACT OBJECT,
WITH MATERIAL USER DECISIONS CAPTURED AS TRANSACTIONAL STATE TRANSITIONS.

This explains why the same project can possess correct authority rules, exact hashes, exact accepted baselines, and a bootstrap and still repeatedly resume on the wrong thing.
