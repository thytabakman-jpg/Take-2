# Jewish Holiday Booklet / Curriculum Education Architecture Diagnostic

Date: 2026-09-22  
Mode: READ-ONLY DIAGNOSTIC  
Scope: Jewish Holiday Booklet Program, its four booklet subprojects, and its bounded relationship to Curriculum Design Research.  
Purpose: identify the smallest structural generator that best explains the repeated artifact-identity, image-lineage, audit-target, and "what project are we actually working on?" failures.

## Executive finding

The strongest structural diagnosis is a **missing operational middle layer**.

The repository correctly says that the Jewish Holiday Booklet Program is an **umbrella** with four booklet subprojects, and separately says that Curriculum Design Research is a **support program**. But the four booklet subprojects are only named in `PORTFOLIO.yaml`; they are not instantiated as first-class operational units with their own current state, artifact lineage, working-set identity, accepted/candidate transitions, and local production history.

As a result, the root JHB project is doing too many jobs at once:

- series-level program control;
- shared educational architecture;
- booklet-specific conceptual state;
- artifact authority;
- artifact migration;
- repair governance;
- version recovery;
- candidate selection;
- historical provenance.

That collapse explains why the shared architecture can be audited and converge while the actual booklet objects remain hard to identify.

A second, related problem is that the repository has **two education projects but no explicit common education-program view**:

1. `jewish-holiday-booklets` — active deliverable/production umbrella;
2. `curriculum-design-research` — paused support/research program.

The relation between them is represented by goal-graph constraints, but the user's working concept of "the education project" appears broader than either one. This creates a scope-selection problem before any audit begins.

## Sources and diagnostic machinery used

This diagnostic synthesized the current JHB-specific audit family and the relevant architecture/improvement controls:

- `projects/jewish-holiday-booklets/GOALS.yaml`
- `projects/jewish-holiday-booklets/STATE.yaml`
- `projects/jewish-holiday-booklets/ARTIFACTS.yaml`
- `projects/jewish-holiday-booklets/PROVENANCE.yaml`
- `projects/jewish-holiday-booklets/MASTER_CONTROL.md`
- `projects/curriculum-design-research/GOALS.yaml`
- `projects/curriculum-design-research/PROVENANCE.yaml`
- `PORTFOLIO.yaml`
- `GOAL_GRAPH.yaml`
- `ARCHITECTURE.md`
- `INTENTION_ARCHITECTURE_REGISTRY.yaml`
- `INTENTIONAL_OBJECT_ONTOLOGY.md`
- `RESEARCH_OBJECT_POLICY.md`
- `TRACEABILITY.yaml`
- `projects/pd/practical/PRACTICAL_CORE_MVP_PROTOCOL.md`
- `projects/pd/improvement/IMPROVEMENT_CORE_CAPABILITY_MAP.md`
- `audits/JHB_ARTIFACT_RECONCILIATION_2026-09-21.md`
- `audits/JHB_AUDIT_TARGET_VALIDITY_REVIEW_2026-09-21.md`
- `audits/JHB_AUDIT_FAMILY_COMPARISON_2026-09-21.md`
- `audits/JHB_MASTER_CONTROL_PDAUDIT_PASS1_2026-09-21.md`
- `audits/JHB_MASTER_CONTROL_PDAUDIT_PASS2_2026-09-21.md`
- `audits/JHB_MASTER_CONTROL_PDAUDIT_PASS3_CONFIRMATION_2026-09-21.md`
- `audits/JHB_MASTER_CONTROL_PDAUDIT_PASS4_REPRODUCIBILITY_2026-09-21.md`
- `audits/JHB_MASTER_CONTROL_PDAUDIT_PASS5_POST_ARTIFACT_RECONCILIATION_2026-09-21.md`
- `audits/JHB_CHATGPT_IMAGE_RECOVERY_TOOL_AUDIT_2026-09-22.md`
- `audits/CROSS_GOAL_PD_AUDIT_2026-09-22.md`

No project goals or canonical artifact authority were changed.

## 1. What the repository currently says the projects are

### Jewish Holiday Booklet Program

`PORTFOLIO.yaml` registers `jewish-holiday-booklets` as:

- kind: `umbrella`
- active
- provisional/reconstructed
- with four subprojects:
  - Yom Kippur Booklet
  - Sukkos Fick / Difference
  - Sukkos Keva / Practice
  - Sukkos Conservation / Boundaries

Its root goal is a deliverable objective: finish the four Grade 5–6 holiday booklets.

The current intention-type audit already recognizes that the JHB goal tree is not really one ordinary goal tree:

- JHB:G0 = deliverable objective
- JHB:G1.1 = invariant / benchmark-preservation control
- JHB:G1.2–G1.4 = booklet deliverables
- JHB:G1.5 = maintenance obligation
- JHB:G2.1–G2.4 = constraints/invariants
- JHB:G2.5 = activation gate on broader curriculum research

So even before artifact recovery, JHB is already a mixed program/control graph rather than a simple project tree.

### Curriculum Design Research

`curriculum-design-research` is a separate support program.

Its G0 is epistemic/capability-oriented: recover and test knowledge about curriculum structure and curriculum-development process.

Its goals explicitly include capabilities that are directly relevant to today's failure:

- repeatable authoring and production process;
- change control and convergence;
- preserving provenance and versions;
- preserving upstream pipeline from project definition through candidate generation, discrimination, locking, production, and render QA.

The project is paused and support-only relative to JHB unless separately reactivated.

### Current JHB–CDR relation

The cross-project graph records both directions:

- JHB:G2.5 constrains CDR:G0 through the "only when it materially helps JHB" gate.
- CDR:G0 constrains JHB:G0 through curriculum-structure/authoring/validation knowledge.

This is a real relation, but it is only a goal-level relation. It does not instantiate an operational handoff between CDR process knowledge and JHB booklet production state.

## 2. The key architecture defect

### Finding EDU-ARCH-001 — declared booklet subprojects are not operationally instantiated

Severity: HIGH  
Confidence: HIGH

The repository says the four booklets are subprojects, but they do not have separate project-local control surfaces.

There is one shared:

- `STATE.yaml`
- `ARTIFACTS.yaml`
- `PROVENANCE.yaml`
- `MASTER_CONTROL.md`

for the entire JHB umbrella.

The individual booklet subprojects therefore have no first-class durable place to own:

- current working artifact set;
- historical accepted baseline;
- intended successor;
- image-generation lineage;
- candidate sets;
- rejected branches;
- locked specification;
- current repair frontier;
- local source set;
- local production state;
- local validation state.

This is the immediate structural generator of the image-recovery problem.

The system can answer:

- what the JHB program believes;
- what the shared four-page architecture is;
- what a historical Fick accepted baseline was;

without being able to answer cleanly:

- which four Fick images are the intended current booklet lineage;
- which Keva generation is the active working set;
- which Conservation branch belongs to the same booklet family as the user's anchor.

### Why this matters

Page identity is set-relative.

"Fick Page 3" is not sufficiently identified by content or filename. The real object is:

> Page 3 of a particular four-page Fick booklet lineage.

Without a first-class booklet-level lineage object, the root artifact registry is forced to treat pages as isolated accepted/candidate artifacts rather than as members of evolving booklet versions.

## 3. The missing project-scope layer

### Finding EDU-ARCH-002 — "the education project" has no explicit repository identity

Severity: HIGH FOR HUMAN/ASSISTANT ROUTING  
Confidence: MEDIUM-HIGH

The user's working language contains a broader "education project" that appears to include:

- the booklet production program;
- curriculum-design research;
- educational-method development;
- shared visual/production learning;
- possibly future educational products.

The repository has no registered umbrella with that identity.

Instead, JHB and CDR are peer projects at portfolio level with a typed support relation.

That may be the correct final design, but it creates an ambiguity whenever the user says:

- education project;
- booklet education project;
- curriculum project;
- sub-education project;
- the books;
- the system we learned from the books.

The assistant has to infer whether the target is:

1. JHB program-level shared architecture;
2. one booklet subproject;
3. CDR research;
4. the JHB–CDR interface;
5. a broader education-domain umbrella that is not currently represented.

This is exactly the kind of target ambiguity PracticalCore marks as `goal_or_task_ambiguity` and `representation_open`.

## 4. Cross-layer collapse

### Finding EDU-ARCH-003 — program, control, artifact, and history are too tightly co-located

Severity: HIGH  
Confidence: HIGH

ImprovementCore's ARCH-CROSS-LAYER branch warns against collapsing goal-like, control-like, artifact, evidence, state, and process entities into one architectural layer.

JHB currently centralizes all of the following in its root control system:

- program goal;
- house architecture;
- quality constraints;
- booklet route tables;
- booklet-local findings;
- artifact authority;
- artifact migration status;
- accepted baseline identity;
- production/repair governance;
- provenance coverage;
- empirical validation state.

This is cognitively recoverable in MASTER_CONTROL, but operationally costly.

A shared program control can say "Fick is in constrained repair" while the actual Fick subproject still lacks a durable current working-set lineage. The program-level statement is true but insufficient for production.

## 5. Interface failure between CDR knowledge and JHB execution

### Finding EDU-ARCH-004 — the process research exists, but its outputs are not operationally instantiated in JHB

Severity: HIGH  
Confidence: HIGH

CDR already contains the concepts needed to prevent this failure:

- explicit project definition;
- candidate generation;
- comparison;
- kill tests;
- convergence;
- locking;
- version preservation;
- production handoff;
- render QA.

But JHB does not have concrete booklet-local execution objects that implement those capabilities.

This is an ARCH-INTERFACE defect:

> research knowledge about how to preserve and lock a design exists on one side, but the product project has no per-booklet state machine that receives and operationalizes it.

The support relation is therefore semantically real but operationally lossy.

## 6. Why the prior audits did not solve this

### Finding EDU-ARCH-005 — the audits converged on the representation they were given

Severity: HIGH  
Confidence: HIGH

The controlled MASTER_CONTROL audit target was explicitly:

> Can MASTER_CONTROL function as a stable source-grounded control and repeated-audit bearer without reconstructing the project from chat history?

That target was answered successfully.

Passes 3 and 4 explicitly say:

- the control artifact converged for the current frame;
- project-level openness remained;
- unresolved artifact identities remained legitimate open coordinates;
- do not reopen MASTER_CONTROL merely to search for novelty.

Those were correct conclusions for that target.

But the audit target froze the current project decomposition.

It did not ask:

> Is JHB decomposed into the right projects/subprojects and ownership boundaries?

Nor did it ask:

> Does every booklet have a first-class operational identity sufficient to recover its current visual lineage?

So the audits could converge while the decomposition itself remained defective for the production task.

This is not an audit failure in the narrow sense. It is an audit-target failure relative to the newly observed recurring problem.

## 7. Why the artifact audit found local identity problems instead of the shared generator

The audit family correctly found:

- exact artifact identity matters;
- accepted source images outrank PDFs;
- Fick baseline must be resolved before repair;
- Keva identity is unresolved;
- Conservation render is unresolved;
- audits must identify exact bearer/object.

Those findings were locally correct.

Today's repeated recovery failures add new evidence:

- Fick's historical accepted baseline is not sufficient to identify the user's intended current ideal packet;
- Keva has several plausible complete visual branches;
- Conservation has several complete related branches;
- user-recognized visual lineage outperforms current registry fields for identifying the intended object.

This recurrence across sibling booklet subprojects triggers ImprovementCore's ARCH-BOUNDARY / ARCH-SUBSYSTEM escalation rule.

The common generator is not three independent missing page IDs.

It is the absence of booklet-local lineage/state architecture.

## 8. Rival architectures

### Current effective architecture

Portfolio
- JHB umbrella
  - four named subprojects, mostly metadata-only
  - one shared control/state/artifact/provenance stack
- CDR support program
  - cross-goal support relation to JHB

This is compact, but it makes the JHB root carry local production state for all booklets.

### Stronger candidate architecture

Education domain/program view
- Jewish Holiday Booklet Program
  - shared series architecture and house controls
  - Yom Kippur booklet subproject
  - Fick / Difference booklet subproject
  - Keva / Practice booklet subproject
  - Conservation / Boundaries booklet subproject
- Curriculum Design Research
  - separate research/support program
  - explicit typed outputs into JHB when the activation gate passes

Each booklet subproject would own its own operational lineage/state.

The root JHB program would own only shared constraints, cross-booklet benchmark logic, house architecture, and program-level readiness.

The "Education domain/program view" need not automatically become a new canonical project. It can first be tested as a non-authoritative architectural view. Whether it deserves a registered project identity requires explicit user approval and goal/project governance.

## 9. Minimal repair frontier

This diagnostic does **not** recommend a broad rebuild of the educational content.

The smallest structural repair worth testing is:

### Repair A — instantiate each booklet subproject operationally

For each booklet, create a first-class local control bundle or equivalent logical object containing:

- BOOKLET_ID
- current lifecycle state
- current intended artifact set
- historical accepted baseline(s)
- current working candidate set
- artifact lineage / generation-run grouping
- page order
- supersession/rejection relations
- current repair frontier
- locked student-facing specification
- current validation state

The exact file layout is secondary. The ownership boundary is the important repair.

### Repair B — reduce JHB root responsibility

JHB root retains:

- shared four-page house form;
- series benchmark;
- shared quality constraints;
- cross-booklet source/science/activity rules;
- shared production/repair governance;
- program-level status.

It references booklet-local state rather than storing all local state inline.

### Repair C — make the JHB–CDR interface executable

Define what CDR can hand into JHB, for example:

- validated design distinction;
- authoring-process rule;
- validation protocol;
- provenance/versioning rule;
- production-handoff rule.

Each transfer records:

- source CDR result;
- JHB target control/subproject;
- relation type;
- preserved content;
- operational change;
- acceptance status.

### Repair D — add a project-scope selector to every education task

Before substantive work, resolve:

- EDUCATION_DOMAIN_VIEW?
- JHB_PROGRAM?
- BOOKLET_SUBPROJECT?
- CDR_RESEARCH?
- JHB_CDR_INTERFACE?

Then resolve exact booklet/artifact identity where applicable.

This would have prevented most of the confusion in the image-recovery conversation.

## 10. What not to do

Do not:

- merge CDR into JHB merely because they interact;
- promote a new "Education Project" without explicit user approval;
- rewrite the shared four-page architecture;
- discard MASTER_CONTROL;
- treat the problem as only a missing-image problem;
- treat the problem as only a provenance-storage problem;
- use PDFs as source identity;
- force Keva/Conservation artifact identity closed before evidence supports it.

## 11. ImprovementCore classification

This issue is best classified as:

- ARCH-SYSTEM — whole education/booklet operating architecture;
- ARCH-BOUNDARY — wrong or incomplete project/subproject boundaries;
- ARCH-SUBSYSTEM — booklet-local operating systems are missing;
- ARCH-INTERFACE — CDR process knowledge does not cleanly hand off into JHB production;
- ARCH-CROSS-LAYER — program control, artifact identity, local state, and provenance are collapsed;
- ARCH-INTERFACE — Library image history to GitHub artifact registry handoff is lossy.

It is **not primarily** a content-design problem.

## 12. Key structural issue

The shortest accurate statement is:

> The Jewish Holiday Booklet Program is registered as an umbrella, but its booklet subprojects are not operationally real enough in the backend.

That missing middle layer causes the root project to carry both shared educational architecture and booklet-local artifact/version state. Once several visual branches exist, the system cannot reliably distinguish historical baseline, current intended booklet, candidate successor, and unused/rejected generations.

The possible missing broader "Education" umbrella is a second-order scope problem. The immediately demonstrated production failure comes from the uninstantiated booklet-subproject layer.

## 13. Diagnostic verdict

CONTROL-LAYER CONTENT: largely sound.  
SHARED EDUCATIONAL ARCHITECTURE: no current evidence requires reopening.  
PROJECT DECOMPOSITION: OPEN and now materially suspect.  
BOOKLET SUBPROJECT OPERATIONALIZATION: INADEQUATE.  
JHB–CDR INTERFACE: semantically represented, operationally under-instantiated.  
ARTIFACT LINEAGE: downstream casualty of the missing subproject layer.

Recommended next architecture task, when explicitly authorized:

> Test a booklet-local subproject architecture on Fick first, because Fick now has a recovered family of matching image sets and therefore supplies the best concrete migration case. Preserve the root JHB architecture and compare whether local lineage/state ownership removes the ambiguity without creating duplication or regression.
