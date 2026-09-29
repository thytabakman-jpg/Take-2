# Canonical Authority Spine and Ceiling Integration Audit

Date: 2026-09-21
Workstream: WS:2026-09-21:CANON-SPINE-CEILING-INTEGRATION
Project: canonical-authority

## Objective

Reconcile the current conversation sequence into durable GitHub state without
changing canonical goal identity.

The central operating change is to make the fixed argument spine the project-local
control surface through which discoveries, source modules, PD transfers,
ceiling-raising moves, publication framing, and manuscript planning are routed.

## Baseline finding

The project already had a validated GitHub home with GOALS.yaml, STATE.yaml, and
PROVENANCE.yaml. Those files preserved the fixed Rashi-Ramban case, the typed
source-to-case pathway, bounded no-selector result, and publication objective.

The repository was materially behind the conversation in five ways:

1. the paper spine was not represented as a durable project object;
2. discoveries were not mapped to the smallest spine node they affect;
3. ceiling raising had no explicit admission and anti-bloat control;
4. source modules were not stored in one uniform paper-facing profile registry;
5. research architecture and reader-facing manuscript obligations were not
   durably separated.

## Implemented control layer

Created:

- projects/canonical-authority/SPINE.yaml
- projects/canonical-authority/research/DISCOVERY_MAP.yaml
- projects/canonical-authority/research/CEILING_RAISE_REGISTER.yaml
- projects/canonical-authority/research/SOURCE_MODULES.yaml
- projects/canonical-authority/MANUSCRIPT_CONTRACT.md

The new files are non-goal controls. GOALS.yaml was not changed.

## Spine control

The current controlling argument is represented as:

A -> Q -> H[F] -> R -> B -> C

The spine preserves the fixed case, exact adjudication target, admitted
source-grounded mechanism space, typed source-to-case pathway, adjudicative success
requirement, and bounded comparative result.

The success requirement is sharpened in current research state to:

B** = T + L + I + W

where T is truth or evidential relevance, L is proposition-specific linkage, I is
asymmetric case instantiation, and W is evaluator-available warrant or
recognizability sufficient to rely on the asymmetry.

## Ceiling-raising control

Ceiling raising is represented as a constrained optimization problem over moves that
preserve paper identity and attach to the existing spine.

Current accepted central moves are:

- target-relative religious authority;
- licensed transfer and source attribution;
- third-party warrant or recognizability.

Accepted supporting moves are:

- bearer and representation control;
- indexed pluralism.

The inverse-problem result remains promising support rather than a required central
claim.

Explicit presentation of PD as a second formal framework is rejected for the current
article because it would create a second publication burden and increase scope risk.

## PD transfer

The existing PD diagnostic edge into CANON:G1.3 remains valid.

This integration also identifies a distinct PD:G2A attribution/licensing transfer:
the source-versus-supplementation distinction materially strengthens the
source-to-case pathway without making PD itself the subject of the paper.

A further PD:G2C transfer supports target-indexed determination and bounded
cross-target comparison.

## Manuscript separation

MANUSCRIPT_CONTRACT.md now distinguishes:

- durable research architecture, which maximizes recoverability and auditability;
- reader-facing prose, which contains only the shortest defensible dependency path.

The manuscript is to be derived from the spine rather than from research chronology.

## Readiness

Operational readiness for this integration was CAUTION, not BLOCKED.

Caution basis:

- complete historical conversation coverage remains open;
- complete source/provenance closure remains open.

No blocking condition applied because:

- project identity and goal authority were resolved;
- no canonical goal mutation was required;
- the only overlapping live workstream was read-only;
- affected objects were known.

## Remaining open work

- final full-text nearest-neighbor comparison where access remains incomplete;
- final provenance/source closure for all paper-facing modules;
- sentence-level writing style and reader experience;
- actual manuscript rebuild under MANUSCRIPT_CONTRACT.md;
- continued historical reconciliation beyond the reviewed conversation scope.

## Result

The current conversation produced material durable state and is not merely a chat
summary. Future work can begin from SPINE.yaml plus STATE.yaml and load deeper
registers only as needed.
