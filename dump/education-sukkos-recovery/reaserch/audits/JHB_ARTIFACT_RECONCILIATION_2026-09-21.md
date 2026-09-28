# Jewish Holiday Booklet Artifact Reconciliation

Date: 2026-09-21
Workstream: WS:2026-09-21:JHB-ARTIFACT-MIGRATION-RECONCILIATION
Status: PARTIAL RECONCILIATION

## Reviewed scope

This reconciliation reviewed the currently identified accepted source-image layer for:

- Yom Kippur completed benchmark
- Fick / Difference accepted pre-repair baseline

It also compared those source-object records against:

- projects/jewish-holiday-booklets/MASTER_CONTROL.md
- projects/jewish-holiday-booklets/ARTIFACTS.yaml
- current portfolio registration
- current repository architecture and research-object policy
- relevant Library source/control records used to establish artifact authority

This scope does not claim complete JHB historical reconciliation.

## Frozen repository baseline

Baseline commit:

b20b0101d1c9a5434fd81451f9bd6f8605489cdb

## Reconciled result

### Yom Kippur

Accepted source set:

JHB:YOMKIPPUR:ACCEPTED-PAGES:001

Exact pages:

1. JHB:YOMKIPPUR:P1
2. JHB:YOMKIPPUR:P2
3. JHB:YOMKIPPUR:P3
4. JHB:YOMKIPPUR:P4

Each page has:

- exact Library identity
- source filename
- SHA-256
- dimensions
- page order
- intended repository path

Status:

SOURCE IDENTITY RESOLVED
GITHUB BINARY BYTE TRANSFER PENDING

### Fick / Difference

Accepted source set:

JHB:FICK:ACCEPTED-PAGES:001

Accepted baseline name:

Different People. A Shared Place.

Exact pages:

1. JHB:FICK:P1 — Diffusion Explained: Fick’s Law Infographic.png
2. JHB:FICK:P2 — Difference, Dialogue, and Peace.png
3. JHB:FICK:P3 — Different People, One Sukkah.png
4. JHB:FICK:P4 — Making Room for Each Other.png

Each page now has:

- exact Library identity
- source filename
- SHA-256
- dimensions
- page order
- intended repository path

Verification object:

JHB:FICK:COMPOSITE:001

The composite is derived verification evidence only and does not outrank the four accepted source pages.

Status:

SOURCE IDENTITY RESOLVED
GITHUB BINARY BYTE TRANSFER PENDING

## Repaired repository defects

### JHB-AR-001

Problem:

ARTIFACTS.yaml claimed the Fick source set was resolved and referenced JHB:FICK:P1 through P4, but those object IDs had no object records.

Disposition:

REPAIRED.

### JHB-AR-002

Problem:

MASTER_CONTROL.md still said Fick exact page identities were unresolved after ARTIFACTS.yaml had promoted the source set to resolved.

Disposition:

REPAIRED.

### JHB-AR-003

Problem:

The JHB project lacked project-local STATE.yaml and PROVENANCE.yaml while the portfolio architecture increasingly relied on project state/provenance separation.

Disposition:

REPAIRED.

### JHB-AR-004

Problem:

PORTFOLIO.yaml did not point to the JHB state, provenance, or artifact registry.

Disposition:

REPAIRED without changing migration stage or canonical goal authority.

### JHB-AR-005

Problem:

Accepted source PNG bytes are not physically present at their intended GitHub paths.

Disposition:

OPEN MIGRATION/STORAGE DEBT.

The exact source identity is still recoverable because stable Library IDs and hashes are recorded.

No PDF, preview, composite, or later generated candidate is promoted to fill the storage gap.

## Audit validity result

Earlier education audits divide into:

1. architecture/control findings that remain valid for those targets;
2. candidate/derived-artifact findings that remain evidence about those exact objects;
3. artifact-level findings that require rerun when they did not use the accepted source-page set.

No broad conclusion that earlier education audits were “wasted” is supported.

The missing control was bearer typing.

## Remaining unreviewed scope

- full historical JHB conversation corpus
- full rejected/candidate/derived artifact history
- exact Keva candidate image set
- any future accepted Conservation rendered artifact
- prior booklet audits not yet individually classified by actual audit bearer
- nine unrecovered curriculum-design packets already recorded in MASTER_CONTROL

## Goal effect

No goal changed.

GOALS.yaml was not modified.

## Current closure

This reconciliation is PARTIAL.

The accepted Yom Kippur and Fick source-image identities are reconciled.

The repository is not yet self-contained for those artifacts because raw PNG byte transfer remains pending.
