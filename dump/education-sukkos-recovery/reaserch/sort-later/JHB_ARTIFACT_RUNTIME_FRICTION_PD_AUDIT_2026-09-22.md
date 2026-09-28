# JHB Artifact Runtime Friction — HM-001 PD Audit

Date: 2026-09-22
Status: DEFERRED ARCHITECTURAL REPAIR SPECIFICATION
Authority: diagnostic / read-only analysis; no booklet state or artifact authority changed
Scope: Fick immediate failure, recurring JHB artifact-resolution friction, and transfer to the other booklet lines

## 1. Trigger

The user asked to work on the current Fick booklet and first requested the four current pages.

Observed conversational failure sequence:

1. Broad Library search surfaced `Fick_Sukkos_Corrected_Candidate_v1_1.pdf`.
2. The PDF was treated as the likely target before exact booklet authority was resolved.
3. Repository controls were then consulted and correctly rejected that PDF as the accepted source baseline.
4. The JHB bootstrap / artifact registry then resolved the old accepted Fick repair baseline `JHB:FICK:ACCEPTED-PAGES:001`.
5. Those four PNGs were still not the pages the user meant by the current working booklet.
6. A contact sheet made the wrong resolved set more visible but did not solve target selection.
7. The user supplied the actual four pages directly.

This is not one retrieval error. It exposes two distinct upstream failures plus a presentation handoff defect.

## 2. Exact current Fick working set supplied by the user

These are now the frozen target for the current Fick editing/audit task.

All four are 1103 x 1426 PNG images.

| Page | Current conversation Library ID | SHA-256 |
| --- | --- | --- |
| 1 | `libfile_a01b9dbf0058819188c143c5a2a455c3` | `26cd84ea8660387d32e80b27bdc742e7d2e6731c46a96e12a4053126031c580f` |
| 2 | `libfile_85a1acfd5c7881918bacb3c8da82651d` | `48f766f6caa4e45dbb99ad4066df397f9a6e95231dc6dd5b6c8b61b9d4ebcbfd` |
| 3 | `libfile_857e93667a2c81919f89c4151f6f1449` | `a1cea4e187c9ef9834ddd5da3279370aebb85991dc8d635616ede30f65f464e3` |
| 4 | `libfile_9e58a2cdad2881919469c32f77a59b34` | `d9d0afad51f042e4df1151903782995f79949586e931400e815455d9e69cf3e5` |

This record does not itself promote the set to accepted product status. It records that this is the user-supplied current working target for the present task.

## 3. Same-day evidence of the same defect

Two different archives were generated on 2026-09-22.

### Sukkos_Ideal_Booklets.zip

Created 18:39 UTC Library timestamp.

Its Fick selection notes state that it selected a coherent four-page "Different People. A Shared Place." set because the user had already judged those Fick files to look accurate.

Its Fick pages 2-4 are pixel-identical to the current user-supplied pages 2-4 after normalization. Its page 1 is a nearby earlier variant.

### Sukkos_PracticalCore_Archive.zip

Created 18:47 UTC Library timestamp, later than the ideal-booklets archive.

Its README correctly diagnoses that "current", "best", "latest", "canonical", and "most visually useful" are not the same thing, but then binds Fick to the exact GitHub accepted repair baseline. Its active manifest uses the old `JHB:FICK:ACCEPTED-PAGES:001` hashes.

Therefore a later and more formally controlled packaging pass regressed from the user's current visual work back to the accepted historical repair baseline.

This is decisive evidence that artifact identity alone is not enough. The system also needs task-relative artifact-role resolution.

## 4. Historical recurrence

This failure is continuous with prior JHB and host-system friction:

- wrong images were repeatedly surfaced when the user asked for the current actual booklet pages;
- PDF compilations repeatedly displaced individual image-native pages;
- accepted baseline, active candidate, current working set, visual reference, and final product were repeatedly treated as though one label could cover them all;
- broad search or chat reconstruction repeatedly preceded source-of-truth resolution;
- clean-sheet or newer candidates repeatedly threatened to replace constrained-repair baselines;
- structurally valid repository state was repeatedly overread as semantically sufficient;
- stale or incomplete state transitions forced later conversations to rediscover settled work.

The common form is:

nearby representation or stale role binding becomes load-bearing before the exact referent + task predicate + authority role are jointly resolved.

## 5. HM-001 old recursive audit

### Target-state definition

For a request such as "work on Fick; show me the four pages we have now":

user intent
-> JHB project
-> Fick booklet
-> requested operation/predicate
-> current active working set for that operation
-> exact ordered page objects
-> byte retrieval and hash verification
-> visible presentation
-> substantive audit/editing.

The user must not need to remember internal filenames, Library IDs, accepted-source IDs, or which prior ZIP contained the correct pages.

### Starting-state reconstruction

Current controls already contain:

- project and booklet identity;
- booklet-local STATE and ACCEPTANCE;
- exact-object preflight;
- an artifact registry;
- accepted-source page IDs/hashes;
- a fail-closed JHB bootstrap;
- material-event and capture policies.

But the Fick bootstrap resolves one privileged artifact binding: the accepted repair baseline.

It does not durably represent the active working set the user is presently editing.

### Epistemic sequence reconstruction

The conversation exposed the following transitions:

A. "Fick booklet" -> semantic Library search.
This introduced an unlicensed selector.

B. PDF result -> provisional target.
This collapsed retrieval relevance into artifact authority.

C. Repository audit -> accepted-source baseline.
This repaired authority selection but changed the task predicate from "current pages we are working on" to "accepted repair baseline".

D. Exact old PNGs -> visible contact sheet.
This repaired display but preserved the wrong referent.

E. User-uploaded pages -> exact current target.
The human had to repair the missing task-relative role binding manually.

### Causal transition basis

The first failure came from skipping the already-designed runtime bootstrap.

The second failure remained even after using the bootstrap. The bootstrap asks, in effect, "what is the accepted source set?" It does not first ask "which artifact role is requested by this operation?"

That means the architecture currently distinguishes object identity better than it distinguishes object role-in-task.

### Load-bearing hidden steps

The system silently substituted:

"current booklet"
≈ "accepted source baseline"

That equivalence is false for an active repair project.

The old accepted source baseline is authoritative for preservation and regression.
It is not automatically the current object the user wants to inspect or edit.

A second hidden substitution occurred in packaging:

"generate a useful current archive"
≈ "rerun selection logic now"

That allows two archive passes to choose different Fick sets.

A package must be derived from an already-resolved set ID, not re-select its own source objects.

### Competing interpretations

Rival 1: the problem is bad Library search.
Insufficient. Search caused the first error, but the accepted-baseline resolver still returned the wrong task object.

Rival 2: the problem is missing exact artifact identity.
False for the old Fick baseline. Its identity is exact.

Rival 3: the problem is only stale repository state.
Partly true but incomplete. Updating one "current" pointer without typing its role recreates the same ambiguity later.

Rival 4: the problem is only assistant discipline.
False. The same artifact ambiguity appeared across multiple archives and conversations. This is a missing architecture relation.

Rival 5: the problem is PDF handling.
PDF substitution is one manifestation. The deeper defect is predicate/role collapse before object resolution.

### Static versus dynamic dependency

Static architecture:
project -> artifact registry -> accepted source set.

Dynamic work requires:
project -> operation/predicate -> role binding -> artifact set -> exact objects.

The missing dynamic edge is operation/predicate -> artifact role.

### Clean reconstruction

The minimal stronger architecture is:

TASK
-> PROJECT
-> BOOKLET
-> OPERATION/PREDICATE
-> ARTIFACT ROLE BINDING
-> EXACT SOURCE SET
-> ORDERED OBJECTS
-> VERIFIED RETRIEVAL
-> PRESENTATION
-> AUDIT/EDIT/COMPARE.

Artifact class and task role remain distinct.

Examples of artifact roles:

- accepted_repair_baseline
- active_working_set
- last_user_confirmed_set
- production_candidate
- accepted_product
- visual_reference
- derived_preview

One exact object can occupy more than one role.
One role can transition to a successor.
No role transition occurs merely because an artifact is newer or easier to find.

### Repair propagation

The repair must change Fick, then the booklet-local workbench contract, then all active JHB booklet states, then archive generation and cold-start tests.

It does not require redesigning the shared educational learner architecture.

### Recursive rerun

After adding role-aware resolution, rerun these adversarial tasks:

- "show me the current Fick pages"
- "show me the accepted Fick repair baseline"
- "compare current Fick to its repair baseline"
- "audit the current Fick booklet"
- "package the current Fick booklet"
- "show me the final accepted Fick product"
- same operations for Yom Kippur, Keva, and Conservation.

Convergence requires every phrase to resolve deterministically or return OPEN without search deciding the role.

## 6. Architectural diagnosis

### Defect A — bootstrap bypass

Already diagnosed and repaired in the repository:
broad search was allowed to influence authority before JHB bootstrap.

Current control:
`tools/jhb_booklet_context.py`
+
`EXACT_OBJECT_PREFLIGHT.md`
+
root/local JHB runtime instructions.

This still needs runtime compliance in ChatGPT execution.

### Defect B — operation/role collapse

Still live.

The bootstrap resolves accepted source identity but does not resolve the artifact role demanded by the user's requested operation.

This is the primary remaining architectural defect exposed here.

### Defect C — missing material state transition for user-confirmed working sets

A user-confirmed current set existed strongly enough to generate `Sukkos_Ideal_Booklets.zip`, but no durable Fick local-state transition made that set the active working target.

The later PracticalCore archive therefore reconstructed from accepted-baseline authority and regressed.

This is a material-event closure / capture failure.

### Defect D — package generators re-select rather than derive

A ZIP/archive can independently decide which files are "current" or "best".
That is unsafe.

Packages need a source-set manifest and must derive from that exact set.

### Defect E — presentation handoff

Even after retrieval, the user could not reliably see the images. The response relied on images emitted during tool execution rather than ensuring a user-visible final artifact surface.

Presentation is downstream of identity, but it still needs an explicit contract.

## 7. Fick repair specification

Preserve:

`accepted_repair_baseline = JHB:FICK:ACCEPTED-PAGES:001`

Do not overwrite or silently supersede it.

Add a distinct registered source-set object for the four user-supplied current working pages, provisionally:

`JHB:FICK:WORKING-PAGES:002`

with the four exact Library IDs and hashes listed above.

Then bind booklet-local state:

`active_working_set = JHB:FICK:WORKING-PAGES:002`
`last_user_confirmed_set = JHB:FICK:WORKING-PAGES:002`
`accepted_repair_baseline = JHB:FICK:ACCEPTED-PAGES:001`
`accepted_product = OPEN` unless separately accepted.

Repair/audit jobs that compare change must load both working set and accepted baseline.

"Show/work on current Fick" must load the active working set.
"Show baseline" must load the accepted repair baseline.
"Show final accepted product" must return OPEN until accepted.

## 8. Other booklet repairs

### Yom Kippur

Represent its accepted product and active working set separately even when they currently point to the same set.

This avoids future ambiguity when a revision starts.

### Keva

Keep accepted-source identity OPEN.

Register the exact coherent candidate set already recovered as a candidate/working set when the user selects it.
Do not promote it merely because a complete four-page set exists.

### Conservation

Keep accepted baseline/product OPEN unless separately established.

Register current coherent candidate/repair-reference sets with exact identities and bind only the role actually licensed by the user's selection.

### Future booklet lines

Every booklet starts with the same role slots. Unused slots remain OPEN rather than being inferred.

## 9. Entire JHB system repair

### 9.1 State model

Each booklet-local STATE owns task-relative role bindings.

Artifact registry owns exact object/set identity.

Example:

artifact_bindings:
  accepted_repair_baseline: <set-id or OPEN>
  active_working_set: <set-id or OPEN>
  last_user_confirmed_set: <set-id or OPEN>
  production_candidate: <set-id or OPEN>
  accepted_product: <set-id or OPEN>
  visual_reference: <object/set-id or OPEN>

No duplicate binary metadata belongs in STATE.

### 9.2 Operation-aware resolver

Extend `tools/jhb_booklet_context.py` with an operation/predicate argument.

Minimal operations:

- show_current
- edit_current
- audit_current
- show_baseline
- compare_current_to_baseline
- package_current
- show_accepted_product
- explicit_object

The resolver maps operation -> role(s) -> exact set(s).

Unknown or unbound role -> OPEN/BLOCKED.

### 9.3 Exact set objects

Register booklet source sets as first-class objects, not only a booklet-level page_order list.

Each set records:

- stable set ID;
- role-neutral object identity;
- ordered page IDs;
- set-level hash/manifest hash where useful;
- provenance;
- transition/lineage.

Pages remain independently addressable.

### 9.4 Transition capture

When the user explicitly confirms "these are the right/current pages", that is a material research-object/state event.

Record it through the existing material-event/capture architecture:
- register exact objects/set;
- update active/last-user-confirmed binding when authorized;
- preserve baseline separately;
- propagate derived views;
- verify closure.

A later conversation must not require rediscovery.

### 9.5 Derived-state liveness

Add the JHB bootstrap/workbench to derived-state liveness.

Its freshness depends on:
- JHB root STATE;
- booklet-local STATE;
- booklet ACCEPTANCE;
- ARTIFACTS.

A stale role binding or set reference blocks object-sensitive execution.

### 9.6 Package rule

Every derived ZIP/PDF/contact sheet records:
- exact source-set ID;
- page IDs;
- hashes;
- role used;
- derived_from.

Archive generation receives a resolved set ID.
It never runs "best/current/latest" selection heuristics itself.

### 9.7 Presentation contract

For "show me the pages":
1. resolve exact set;
2. retrieve exact bytes;
3. verify hashes or immutable locators;
4. create/return a visible contact sheet plus individual image links where needed;
5. do not claim the pages are shown unless the final user-visible surface contains them.

## 10. Cross-project transfer

The same host-system pattern appears outside JHB:

representation or reconstructed state becomes load-bearing before the exact target, type, version, or authority relation is frozen.

JHB supplies a concrete reusable lesson:

exact-object preflight needs an operation/predicate layer before object selection.

This can later transfer to other projects that have accepted baseline vs live candidate vs current working result distinctions. It does not justify a portfolio-wide new router until analogous cases are explicitly admitted.

## 11. Regression tests

Required JHB cold-start tests:

### Fick
"show current" -> WORKING-PAGES:002
"show baseline" -> ACCEPTED-PAGES:001
"compare current to baseline" -> both sets
"accepted final" -> OPEN until separately accepted

### Keva
no accepted product inferred from a coherent candidate

### Conservation
no accepted baseline inferred from a coherent candidate

### Yom Kippur
accepted/current can resolve to same set while remaining distinct bindings

### Packaging
two runs of package_current from unchanged state must produce manifests derived from the same exact source set; no independent reselection.

## 12. Core result

The earlier repair solved:

authority before search.

The new failure reveals the next missing invariant:

task predicate before artifact-role binding before exact-object resolution.

The system had the right old artifact and the wrong answer to the user's question because it did not represent what role the requested artifact was supposed to play.

That is why the problem survived multiple attempts to make artifact identity more exact.
