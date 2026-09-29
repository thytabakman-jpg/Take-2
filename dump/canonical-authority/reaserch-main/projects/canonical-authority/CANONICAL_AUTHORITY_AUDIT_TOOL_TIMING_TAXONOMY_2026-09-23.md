# Canonical Authority Audit / Tool Timing Taxonomy

Date: 2026-09-23
Status: ACTIVE CONTROL

## Purpose

Select the smallest adequate audit/tool set for each stage of the Canonical Authority
organizational repair without turning every step into every audit.

## Work-mode taxonomy

### A — READ_ONLY_ARCHITECTURE
Use when:
- determining what exists;
- reconstructing dependencies;
- comparing systems;
- identifying authority;
- testing taxonomy hypotheses.

Permitted:
read-only inspection and durable audit records.

Preferred tools:
ImprovementCore, HM-001, Goal-Spine, Relational PD, SemanticPreflight, ExactObjectPreflight.

### B — CONTROL_SURFACE_REPAIR
Use when:
- fixing project-page/state/traceability/derived-control inconsistencies;
- no physical research-object relocation occurs.

Preferred tools:
ImprovementCore, RepairCore, Goal-Spine, Traceability, DerivedStateLiveness.

### C — MIGRATION_PREPARATION
Use when:
- exact destination/identity/rollback must be established;
- physical mutation is approaching.

Required:
ImprovementCore, ExactObjectPreflight, MigrationContract, Workstream/Concurrency,
PortfolioHealth, Relational PD where dependencies cross objects.

### D — PHYSICAL_MUTATION
Use only in Phase 8.

Required:
ImprovementCore PRE
→ ExactObjectPreflight
→ Workstream/Concurrency
→ PortfolioHealth
→ MigrationContract
→ mutation
→ RepairCore
→ local regression
→ ImprovementCore CHECKPOINT.

### E — POST_MUTATION_VALIDATION
Use after every meaningful physical mutation group.

Required:
targeted validator
→ Traceability
→ DerivedStateLiveness
→ relevant Goal-Spine regression
→ RepairCore
→ ImprovementCore FINAL.

### F — CLOSURE
Use only at the end of the project.

Required:
full integrity suite
→ Relational PD
→ HM-001 coverage pass
→ RepairCore convergence
→ ImprovementCore CLOSE.

## Tool-trigger matrix

| Tool | Before stage | Before step | After step | Final gate | Trigger |
|---|---|---|---|---|---|
| ImprovementCore | YES | YES for meaningful steps | YES | YES | every phase and meaningful step |
| Goal-Spine/HM-001 | when goals/spine/frontier involved | when a step changes/reads dependency semantics | regression | phase gate | target/dependency semantics |
| Relational PD | before cross-object design | before relational mutation | after relation changes | phase gate | >=2 interacting structures |
| RepairCore | when repairing known defect | before a repair loop | after repair | convergence | regression/oscillation/repair |
| SemanticPreflight | before semantic classification | whenever type/scope affects result | when classification changes | no | result-sensitive identity |
| ExactObjectPreflight | before object-sensitive work | before move/replace/delete | after | yes for mutation | exact artifact/version |
| Traceability | after source/derived changes | before propagation | after | yes | derived claims |
| DerivedStateLiveness | after source changes | before/after derived changes | yes | yes | freshness-dependent views |
| Workstream/Concurrency | before mutation | before each mutation group | after | yes | shared repository work |
| PortfolioHealth | before mutation | before each mutation group | after | yes | consequential write |
| MigrationContract | before move | each migration row | after | yes | physical relocation |
| Project-page audit | Phase 3/9 | when orientation changes | after | yes | human navigation |
| Multi-object PD | Phase 0/3/5/7/9 | when >2 objects interact | after | when needed | higher-order relation |
| Prompt PD | only for user-prompt ambiguity | before ambiguous action | not routine | no | hidden selector/target ambiguity |

## Old recursive PD rule

The historical HM-001 recursive PD audit runs:
1. once across the whole organizational repair problem before Phase 1;
2. again whenever a shared upstream generator is discovered;
3. again before Phase 8 if the taxonomy decision materially changes;
4. at closure for audit coverage.

The full internal findings need not be surfaced to the user unless they change the plan,
produce a material repair, or expose an OPEN decision.

## ImprovementCore cadence rule

ImprovementCore is not merely a phase-gate tool.

It runs:
- before every phase;
- before every meaningful step;
- after every meaningful step;
- when a specialist audit produces a material new finding;
- immediately after a repair;
- before any physical mutation;
- after each physical mutation group;
- at closure.

Tiny mechanical substeps can be grouped under one meaningful-step gate.

## Safe phase rule

Phases 0-6 are normally safe to perform while other repository work continues.

Phase 7 can involve small control-surface writes and requires concurrency awareness.

Phase 8 contains the first potentially material physical repository reorganization.

Phases 9-10 are validation/closure.

"No physical reorganization" does not mean "no GitHub writes":
audit records, plan records, and small control-surface repairs can still be written when
authorized and independently recoverable.

## Anti-overaudit rule

Do not run every tool on every tiny step.

The taxonomy selects the smallest adequate combination.
ImprovementCore and the specialist tool for that step are mandatory; additional tools trigger
only when their result can change the decision.

## Current recommendation

Before implementing Phase 1:
- run the whole-project HM-001 recursive PD audit;
- run ImprovementCore on that audit;
- use the taxonomy to determine which specialist audits are actually required for Phase 1;
- do not yet perform any folder mutation.
