# Canonical Authority — Architecture on Author Outline Handoff 001

Date: 2026-09-24
Status: EXECUTED
Target: handoff from internal manuscript blueprint to clean review outline to prose manuscript

## Protected set

Preserve CANON:ARCH:001 v1.2.0, the seven-section/twenty-one-movement structure,
the package-level TRACE result, contribution hierarchy, and internal control blueprint.

## Baseline

Current flow uses the internal blueprint as though it were also the clean review outline.

Defect:
the internal blueprint carries control, status, routing, evidence-owner, and reopen machinery
that the user does not need in order to review the paper plan.

## Candidates

A1 Simplify the internal blueprint in place.
Rejected because it destroys the durable owner of internal control information.

A2 Add a separate clean review outline.
Flow:
ResearchState -> InternalBlueprint -> ReviewOutline -> Approval -> ProseManuscript.
This preserves internal controls while giving the user the actual paper plan.

A3 Keep the clean outline only in chat.
Rejected because the durable shared referent disappears and conversation drift returns.

## Minimal review-outline unit

<Heading, Job, MainPoint, Material, Sources, ReaderMove, EarnedClaim, Next>

Exclude by default:
tool IDs, controller states, liveness formalism, registries, readiness taxonomies,
internal routing, and backend OPEN bookkeeping.

## Approval boundary

APPROVE:
use the review outline as the current prose plan.

REVISE:
edit the review outline.
Only re-run research regression when a requested change touches a protected research claim.

## Synchronization

Refresh the review outline when:
- section or movement structure changes;
- result or scope changes;
- contribution hierarchy changes;
- source changes alter planned content.

Do not refresh it merely because backend audits, tool repertoire, or control registries change.

## Strict gain

A2 preserves all current research/control behavior and directly solves the user-facing
completion problem identified by root cause.

Verdict:
A2 = STRICT_GAIN candidate.
