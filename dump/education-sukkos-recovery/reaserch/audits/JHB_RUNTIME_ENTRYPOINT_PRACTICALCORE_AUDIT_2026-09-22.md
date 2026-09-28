# JHB Runtime Entrypoint PracticalCore Audit

Date: 2026-09-22  
Workstream: WS:2026-09-22:JHB-RUNTIME-ENTRYPOINT  
Baseline: 57ae13f724ff664170252f6f1f6e6c2028760a8e  
Mode: DEEP_AUDIT + ARCHITECTURE_REVIEW + RAISE_CEILING, semantic-backend execution, then bounded implementation  
Target: Jewish Holiday Booklet runtime bootstrap from conversational task to booklet-local authority and exact artifact identity

## Executive result

The observed friction is confirmed.

The JHB system already contains the correct controlling information:

- root JHB current state;
- booklet-local STATE and ACCEPTANCE controls;
- exact Fick accepted source-set identity;
- exact accepted page IDs, Library locators, hashes, and page order;
- exact-object and semantic preflight rules;
- a generated booklet workbench.

The failure is that these controls were advisory/discoverable rather than an enforced runtime entry path. A conversational request could begin with broad Library or filename search before booklet-local authority and exact-object identity were resolved. That allowed retrieval machinery to participate in authority selection even though authority was already known.

The defect is therefore a control-plane bypass at task bootstrap, not missing artifact identity and not a need to redesign the booklet content architecture.

## Frozen protected result

The repair must preserve:

1. JHB root/series architecture.
2. Booklet-local ownership.
3. Fick accepted baseline JHB:FICK:ACCEPTED-PAGES:001.
4. Fick page order JHB:FICK:P1 through JHB:FICK:P4.
5. Keva and Conservation unresolved artifact identity as OPEN.
6. Exact-object preflight semantics.
7. Product acceptance distinct from repository integrity.
8. No canonical goal change.
9. Search remains available for byte retrieval after authority is resolved.
10. PracticalCore and active-context views remain non-authoritative.

## Observed failure trace

The triggering task was effectively:

user names Sukkos/JHB -> selects Fick -> asks to show current pages -> asks for page-specific repairs.

The actual execution path initially became:

user intent -> Library semantic search -> candidate PDF -> candidate/baseline comparison -> additional image search/materialization -> reconstruction of authority.

The intended path already implied by repository architecture was:

user intent -> JHB project -> booklet-local control -> exact object preflight -> accepted source objects -> retrieval -> task.

The skipped section is the runtime entry gate.

## PracticalCore audit

### A01 object/type analysis

Target object:
JHB task-bootstrap / runtime entry interface.

Not the target:
Fick curriculum content, Fick product acceptance, Library storage, or PDF production.

Result:
PASS. The defect is operational infrastructure inside the JHB project.

### A02 authority and lifecycle analysis

Current authority is distributed correctly:

- root JHB STATE owns program status and local-control references;
- booklet-local STATE owns local lifecycle and repair frontier;
- booklet ACCEPTANCE owns product gates;
- ARTIFACTS owns accepted source-object identity;
- generated workbench is non-authoritative.

Result:
The authority model is adequate. The execution path did not force consultation of it early enough.

### A03 representation sensitivity

Several representations coexist:

- accepted source page objects;
- derived composite/PDFs;
- generated workbench;
- Library search results;
- candidate renders.

Choosing a representation before authority resolution can change the result.

Result:
Representation sensitivity is live. Bootstrap must resolve authority first and fail closed when artifact identity is OPEN.

### A04 hidden-selector analysis

Previously hidden selectors included:

- newest-looking file;
- easiest file to open;
- semantic-search ranking;
- filename similarity;
- generated candidate availability.

These selectors were not licensed authority rules.

Result:
Confirmed defect. They must be demoted to retrieval-only behavior after canonical identity is resolved.

### A05 invariant/challenge analysis

Counterfactual:
Suppose the Library contains a newer coherent four-page PDF.

Protected result:
It must not outrank JHB:FICK:ACCEPTED-PAGES:001.

Counterfactual:
Suppose Keva search returns four visually coherent pages.

Protected result:
Artifact-sensitive work remains blocked while accepted source-set identity is OPEN.

Result:
The proposed fail-closed bootstrap preserves both.

### A06 rival reconstruction

Rival diagnosis 1:
The artifact registry is incomplete.

Rejected for Fick. Exact source-set, page IDs, locators, hashes, and order already exist.

Rival diagnosis 2:
The booklet-local architecture is missing.

Historically true, but repaired before this audit. Fick/Keva/Conservation now have local STATE and ACCEPTANCE controls.

Rival diagnosis 3:
Binary repository transport is the cause.

Rejected as the primary generator. Repository PNG bytes remain transport debt, but exact Library identity is already sufficient to decide authority and begin Fick preservation work.

Rival diagnosis 4:
The generated workbench is sufficient and only assistant discipline failed.

Insufficient. The workbench did not return exact source-object records or fail closed for unresolved artifact identity, and the root runtime instructions did not require it before broad search.

Result:
Diagnosis confirmed as missing enforced runtime bootstrap plus incomplete workbench contract.

### A07 provenance analysis

The Fick artifact registry supplies stable object IDs, Library file IDs, SHA-256 values, source filenames, acceptance basis, and page order.

Result:
No provenance gap blocks this repair.

### A08 authority-alignment analysis

The new bootstrap must remain a derived view.

Result:
Keep specialized source files authoritative; bootstrap may compose but never promote, accept, reject, or supersede objects.

### A09 recurrence/generator analysis

The failure belongs to the same broad family as earlier goal/spine/layer/accepted-versus-derived errors:
a shorthand or nearby representation becomes load-bearing before referent/type/authority resolution.

Local reminder text is therefore weaker than a fail-closed runtime gate.

Result:
Repair the bootstrap generator rather than another Fick-specific retrieval patch.

### A12 spine/dependency reconstruction

Load-bearing execution spine:

task phrase
-> project resolution
-> booklet resolution
-> local state/acceptance resolution
-> exact artifact authority
-> operation gate
-> exact retrieval
-> substantive task.

The demonstrated failure occurred when exact retrieval was attempted before artifact authority was frozen.

### A13 layered-control audit

Layers remain distinct:

- portfolio discovery
- JHB program state
- booklet-local state
- artifact authority
- generated task workbench
- retrieval transport
- product acceptance.

Missing relation:
conversation/task entry -> mandatory JHB bootstrap.

Result:
Add the relation at the repository-wide agent entry surface and enforce its artifact gate in the JHB workbench.

## Raise-the-ceiling pass

### I01 live frontier

The strongest live frontier is not richer JHB content state. It is deterministic use of the state already present.

### I12 dependency leverage

A runtime entry gate is upstream of every later Fick/Keva/Conservation artifact operation. Improving it prevents repeated reconstruction across all three active Sukkos booklets.

### I03 ceiling candidate

Stronger same-task successor:

advisory local workbench
->
root-triggered, alias-resolving, exact-object-aware, fail-closed booklet bootstrap with regression tests.

This raises the ceiling without changing project identity or adding another authority layer.

### I02 rival successor set

Candidate A: instruction-only reminder.

Rejected as too weak. It does not test exact object resolution or unresolved-artifact blocking.

Candidate B: enrich jhb_booklet_context.py only.

Improvement but insufficient. A conversation can still bypass it before path-specific instructions activate.

Candidate C: root AGENTS trigger + enriched fail-closed workbench + CI cold-start regression.

Selected.

Candidate D: build a portfolio-wide universal project bootstrap router.

Deferred. It may later be useful, but no evidence shows the wider portfolio requires this extra layer now. It expands scope and control cost beyond the demonstrated JHB failure.

### I13 strict-gain test

Candidate C strictly improves the protected task by:

- resolving Fick directly from controlled aliases;
- returning the exact accepted source set and ordered page objects;
- exposing stable Library locators and expected hashes;
- preventing search from deciding authority;
- blocking artifact-sensitive Keva/Conservation work while identity is OPEN;
- preserving all existing source-of-truth files.

It is not merely cleaner documentation.

### I14 protected-result non-regression

Required regressions:

- Fick remains EXACT and accepted baseline unchanged.
- Keva remains OPEN.
- Conservation remains OPEN.
- generated view remains non-authoritative.
- product-acceptance controls unchanged.
- no goal changes.
- no search prohibition after exact authority is resolved.

### I15 incomparable-successor preservation

The portfolio-wide bootstrap idea remains a later candidate rather than being falsely rejected. It is not required for the current JHB repair.

### I16 recomputation

After the repair, the JHB execution map becomes:

conversation/task
-> root JHB trigger
-> generated bootstrap/workbench
-> specialized authoritative controls
-> exact-object gate
-> retrieval/substantive work.

## A16 terminal verification criteria

Cold-start regression:

From a fresh execution context, "work on Fick / show the current pages" must resolve:

- booklet_id = fick_difference;
- source_set_id = JHB:FICK:ACCEPTED-PAGES:001;
- ordered objects JHB:FICK:P1..P4;
- each object class = accepted_source;
- each exact source object has Library locator and SHA-256;
- artifact-sensitive gate = CLEAR.

For Keva and Conservation:

- artifact_resolution = OPEN;
- artifact-sensitive gate = BLOCKED;
- no candidate is silently promoted.

Any future change that makes broad search, recency, filename, PDF, composite, or generated candidate select artifact authority is a regression.

## Concurrency and readiness check

Before implementation:

- main baseline: 57ae13f724ff664170252f6f1f6e6c2028760a8e;
- active repository workstreams: none;
- queued GitHub Actions runs: none;
- in-progress GitHub Actions runs: none;
- the immediately preceding JHB structured-YAML closeout merged successfully;
- Portfolio integrity run 35797351250 completed successfully, including structured-YAML mutation regression, JHB Fick acceptance wiring, JHB booklet-local controls, workbench fixtures, and PracticalCore smoke tests.

Readiness classification:
CLEAR.

The runtime-entrypoint repair does not overlap an active writer and does not touch Fick content, artifact acceptance, learner route, or canonical goals.

## Implemented bounded repair

1. Extend tools/jhb_booklet_context.py.
   - controlled booklet aliases;
   - exact source-object resolution;
   - retrieval plan with stable identity and hashes;
   - explicit EXACT/OPEN outcome;
   - fail-closed artifact-sensitive gate;
   - --require-exact-artifact mode.

2. Add root AGENTS JHB runtime-bootstrap trigger.
   - run bootstrap before broad search can influence artifact authority.

3. Strengthen local JHB instructions.
   - same entry rule and fail-closed semantics.

4. Add tools/check_jhb_runtime_entrypoint.py.
   - cold-start alias resolution;
   - exact Fick object contract;
   - OPEN preservation for Keva/Conservation;
   - instruction wiring checks.

5. Wire the regression into Portfolio integrity.

## Non-changes

This work does not:

- alter any canonical goal;
- accept or reject a booklet artifact;
- change Fick's repair baseline;
- close Keva or Conservation artifact identity;
- modify learner-route content;
- perform the Fick booklet repair itself;
- solve the independent accepted-PNG GitHub binary-transport debt.

## Final recommendation

Promote Candidate C only after branch integrity passes.

Reopen this architecture only when:

- the cold-start regression fails;
- another JHB artifact operation bypasses bootstrap despite the root trigger;
- a materially different JHB task requires context the workbench cannot represent; or
- repeated analogous failures outside JHB provide evidence for a portfolio-wide bootstrap router.


## Final concurrency reconciliation

After the pre-closeout validation, main advanced from
`57ae13f724ff664170252f6f1f6e6c2028760a8e` to
`a34ee157dc446e0be3c1465102e282ea7511786d`.

The four intervening main commits changed only:

- `AUDIT_CAMPAIGNS.yaml`;
- `projects/pd/research/OPEN_QUESTIONS.md`;
- `audits/BACKLOG_PREEXECUTION_PD_CONSOLIDATION_CANDIDATE_2026-09-22.md`.

None overlaps the JHB runtime-entrypoint repair's affected objects. The original pull
request was closed without merge, the repair was replayed on the later main baseline,
and the complete integrity suite is required again before promotion.
