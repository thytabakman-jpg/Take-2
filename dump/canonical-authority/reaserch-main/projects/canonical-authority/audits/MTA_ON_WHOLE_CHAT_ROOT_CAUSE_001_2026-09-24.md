# Canonical Authority — MTA on Whole-Chat Root Cause 001

Date: 2026-09-24
Status: EXECUTED / MATERIAL YIELD / RELATIVE CLOSE
Target: WHOLE_CHAT_ROOT_CAUSE_001

## Frozen job

Reconstruct the minimal object model needed to prevent internal scaffolding from being
mistaken for the user-requested final paper outline.

## Round 1 — object factorization

The current workflow has at least three distinct manuscript-adjacent objects:

B = INTERNAL_BLUEPRINT
A = AUTHOR_FACING_OUTLINE
M = PROSE_MANUSCRIPT

They are not synonyms.

B owns:
- control status;
- evidence ownership;
- readiness;
- reopen rules;
- synchronization;
- production routing.

A owns:
- paper goal/question;
- section/subsection sequence;
- substantive claim/content plan;
- source placement at author-decision resolution;
- reader movement;
- what each unit earns;
- final planned contribution.

M owns:
- sentences;
- paragraphs;
- transitions;
- quotations/citations;
- stylistic realization.

Material delta M1:
B, A, and M require separate object identities.

## Round 2 — projection semantics

A is not independently invented after B.

It is a controlled projection:

pi_A : B x ResearchState -> A

Protected observables:
- root paper goal;
- exact fixed case;
- scope;
- bounded result;
- seven-section order;
- twenty-one intellectual movements;
- source/function distinctions;
- method sequence;
- contribution hierarchy;
- bounded novelty;
- architecture reopen triggers only where author-facing relevance exists.

Allowed loss:
- tool names;
- tool-run history;
- controller state;
- artifact registry data;
- liveness formalism;
- synchronization mechanics;
- most readiness taxonomy;
- backend provenance bookkeeping.

Material delta M2:
the author outline is a lossy but preservation-constrained projection of the internal
blueprint/research system.

## Round 3 — author-level terminality

Architecture closure and author-outline completion are different predicates.

Define:

BlueprintClosed(B)
AuthorOutlineReady(A)

AuthorOutlineReady requires:
1. every section/subsection has one clear manuscript job;
2. every unit states the substantive point to make;
3. required source/evidence placement is decided at outline resolution;
4. section transitions are explicit;
5. no hidden planning decision remains that would change what the section is trying to say;
6. remaining work is sentence/paragraph realization, citation formatting, or genuinely new evidence.

Material delta M3:
"frozen architecture" does not entail "author outline ready."

## Round 4 — unresolved decisions attack

The current internal blueprint still marks local packets for:
- M06-M09 source allocation;
- M15-M16 evidence presentation;
- M21 novelty wording.

At author-outline resolution, these can be resolved now from current admitted research:
- H_P/H_M grouped first;
- H_A/H_L/H_G compressed next;
- H_X/H_R receive strongest dedicated treatment;
- M15/M16 use H_R then package-level result;
- M21 uses bounded intersection novelty language already admitted by the novelty map.

Material delta M4:
these are not architecture blockers for A and need not remain as open planning decisions.

## Round 5 — approval boundary

User approval is not research admission.

It is an authoring transition:

AUTHOR_REVIEW(A)
-> APPROVE | REVISE

APPROVE licenses prose population under A.
REVISE changes A and only propagates upstream when the requested revision violates protected
research constraints.

Material delta M5:
the author-approval gate belongs between A and M, not inside research architecture.

## Round 6 — closure attack

A clean author outline can still become stale if B/research changes materially.

Therefore A needs a lightweight sync rule:
- refresh on section/movement change;
- refresh on result/scope/contribution change;
- refresh on source change only when it alters planned content;
- no refresh for backend-only control changes.

Material delta M6:
author-outline synchronization should be content-sensitive, not all-control-sensitive.

## Reconstructed model

ResearchState
-> InternalBlueprint B
-> author projection pi_A
-> AuthorOutline A
-> user approval/revision
-> ProseManuscript M

with:
- B preserving control complexity;
- A preserving author-relevant content structure;
- M realizing A in prose.

## OPEN

O1 exact minimal author-outline contract fields.
O2 whether A should encode all 21 movements explicitly or group them under subsection headings.
O3 synchronization rule detail.

## Verdict

MTA_MATERIAL_YIELD_THEN_RELATIVE_CLOSE.

Next:
Architecture Analysis on the B -> A -> M handoff.
