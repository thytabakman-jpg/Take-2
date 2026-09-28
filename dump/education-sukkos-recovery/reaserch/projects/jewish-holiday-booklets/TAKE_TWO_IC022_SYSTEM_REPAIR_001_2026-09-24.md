# Jewish Holiday Booklet — Take Two / IC-022 System Repair
Date: 2026-09-24
Controller: IC-022
Status: active repair architecture

## Goal

Reliably move from the current Jewish Holiday Booklet project state to the exact lesson that is intended to be taught, while preserving the approved curriculum, limiting repairs to authorized deltas, and preventing candidate/rejected artifacts from reaching teaching.

## IC-022 diagnosis

The project has already accumulated strong curriculum architecture, audits, source controls, booklet-local state, and production constraints.

The dominant remaining failure class is control continuity:

CURRENT STATE
→ TARGET LESSON
→ AUTHORITATIVE ARTIFACT
→ APPROVED DELTA
→ RENDERED ARTIFACT
→ RELEASE
→ TEACHING
→ POST-TEACHING EVIDENCE

The historical failure occurred because these were treated as related records rather than one result-sensitive execution chain.

## Take Two application

Take Two becomes the control envelope for every substantive booklet-production episode.

### Frozen entry packet

Before work begins, freeze:

- exact lesson target;
- exact booklet;
- current authoritative state;
- exact baseline artifact;
- intended production delta;
- protected functions;
- open findings;
- excluded changes;
- release destination;
- teaching date/use when known.

No history reconstruction is allowed after the packet is frozen except through an explicit OPEN/recovery route.

## Five distinct object states

Every booklet must distinguish:

1. CONCEPT
2. ARTIFACT SPECIFICATION
3. RENDERED CANDIDATE
4. RELEASED TEACHING ARTIFACT
5. CLASSROOM-VALIDATED ARTIFACT

No state inherits authority merely because it is newer.

## Production transaction

Production follows:

BASELINE LOCK
→ PRESERVATION LEDGER
→ AUTHORIZED DELTA
→ CONSTRAINED PRODUCTION
→ WHOLE-OBJECT RENDER QA
→ ARTIFACT AUDIT
→ RELEASE TRANSACTION
→ TEACHING PRE-FLIGHT
→ TEACHING
→ RESULT CAPTURE

A failed gate reopens only the smallest implicated stage.

## Required distinctions

### Architecture versus artifact

A correct route does not establish a correct PDF.

### Artifact audit versus render QA

Artifact audit asks whether the student-facing object is conceptually, source-wise, structurally, emotionally, and functionally correct.

Render QA asks whether production faithfully implemented the approved object.

### Teaching outcome versus causal proof

A successful learner response demonstrates an outcome. It does not by itself establish that the intended curricular mechanism caused it.

### Candidate versus release

A candidate is evidence.

A release is an authorized teaching object.

## Current routing

### Yom Kippur

BENCHMARK.

No Sukkos problem reopens it.

### Fick / Difference

CONSTRAINED REPAIR.

Baseline and repair delta remain separate.

The project must not return to whole-booklet redesign unless a protected-function regression or explicit reopen condition is demonstrated.

### Keva / Practice

CURRENT NEXT LESSON.

Exact released artifact:
Sukkos_Keva_Next_Week_RELEASE.pdf

The release record identifies the lesson, exact file, four-page identity, Page 1 and Page 4 titles, activity, and non-substitution rule.

Operational status:
READY FOR TEACHING PREPARATION after visual release QA.

### Conservation / Boundaries

NOT RELEASED.

Remain at architecture/text candidate until the cross-domain bridge is closed and an artifact specification plus canonical render exists.

## IC-022 package selection for booklet work

The booklet workflow does not need every analytic capability on every turn.

Use the smallest package that can change the live result:

- exact-state/object discovery;
- target-specific diagnosis;
- delta specification;
- production;
- render QA;
- release verification;
- empirical validation.

Add broader PD/audit capabilities only when a named failure or OPEN coordinate makes them result-sensitive.

## Hard gates

### Gate 1 — TARGET

Exactly one lesson is named for the current teaching operation.

### Gate 2 — BASELINE

Exactly one operative baseline is named, or the absence is explicitly OPEN.

### Gate 3 — DELTA

Every proposed change is inside an authorized closure.

### Gate 4 — ARTIFACT

The rendered result matches the approved artifact specification.

### Gate 5 — RELEASE

Exactly one teaching artifact occupies the NEXT LESSON slot.

### Gate 6 — PRE-FLIGHT

The file opened for teaching matches the release object by lesson identity, page count, and first/last page identity.

### Gate 7 — POST-CLASS

Observed failures route back only to the earliest implicated stage.

## Known project failures reclassified

### Wrong booklet taught

Type:
RELEASE CONTROL FAILURE

Control:
exact release object + NEXT LESSON singleton + pre-teaching identity test.

### Repeated rebuilding

Type:
SCOPE / AUTHORIZATION FAILURE

Control:
frozen baseline + approved delta + excluded-change list + smallest implicated stage.

### Artifact authority confusion

Type:
IDENTITY / PROVENANCE FAILURE

Control:
exact artifact identity and release status.

### Architecture treated as production readiness

Type:
STATE-TYPE CONFUSION

Control:
five-state artifact lifecycle.

### Page vocabulary mistaken for conceptual dependency

Type:
SEMANTIC BRIDGE FAILURE

Control:
explicit handoff contract:
learner has → unresolved → why next page → unique contribution.

### Activity treated as causal proof

Type:
EVIDENCE-TYPE CONFUSION

Control:
separate outcome evidence from mechanism evidence.

### One booklet reopening another

Type:
DEPENDENCY / WORKSTREAM FAILURE

Control:
booklet-local workstreams with explicit cross-booklet dependencies only.

### Endless auditing

Type:
ROUTING / STOP-RULE FAILURE

Control:
audit only when a live uncertainty, failure, contradiction, or reopen condition makes it result-sensitive.

## Most important operational change

The system no longer asks:

'What booklet should we work on next?'

It asks:

'What is the exact next teaching operation, what object is authorized to realize it, and what is the smallest remaining result-sensitive obstacle?'

That changes the optimization target from research completeness to operational closure.

## First live Take Two test

The next real-world test is the Keva release.

Use only:
Sukkos_Keva_Next_Week_RELEASE.pdf

Before teaching, perform the release-card identity check.

Do not run another whole-project audit unless the release check fails or a new result-sensitive problem appears.

After teaching, record actual classroom evidence separately from conceptual correctness.

## Expected Take Two gain

A successful run demonstrates:

- zero artifact ambiguity at teaching time;
- no substitution of newer candidates;
- no unrelated booklet reopening;
- no broad audit between release and teaching;
- exact traceability from current state to teaching artifact;
- demonstrated post-teaching routing to the smallest implicated stage.

## Promotion boundary

This is a project-local application of Take Two.

It does not promote IC-022 to runtime authority.
It does not replace the repository's existing governance controls.
It does make the Jewish Holiday Booklet project a direct empirical test of the Take Two architecture.


## Sort Later integration

SORT_LATER is a conditional unresolved-intake path inside IC-022 routing.

Use it only when a potentially useful or material side finding cannot yet be safely classified or routed, or when focus-preserving deferral is licensed and the finding is nonblocking.

Routing order:

1. exact known destination;
2. immediate specialized routing when result-sensitive;
3. SORT_LATER capture when destination/classification remains genuinely unresolved and deferral is safe;
4. return to the active objective;
5. drain at the review trigger;
6. remove from SORT_LATER after definitive routing.

Current Fick, Keva, Conservation, release, and provenance findings remain in their existing specialized destinations. They are not moved into SORT_LATER merely because they remain open.

SORT_LATER never becomes authoritative state, backlog, open-question register, debt register, or release state.
