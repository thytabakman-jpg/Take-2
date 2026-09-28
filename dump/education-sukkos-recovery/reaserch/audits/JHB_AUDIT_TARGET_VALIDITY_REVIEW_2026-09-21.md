# Jewish Holiday Booklet Audit Target Validity Review

Date: 2026-09-21

## Purpose

Determine which prior education audits remain informative after distinguishing:

- project architecture;
- control artifact;
- accepted source page images;
- candidate renders;
- derived PDFs;
- historical reconstructions.

## Governing rule

An audit establishes properties only of the object it actually audited.

Similarity of content does not transfer artifact-level conclusions automatically.

## Validity classes

### V1 — Still valid for its actual target

These audits remain useful without rerun when their target was:

- learner-route architecture;
- four-page structure;
- source/application boundaries;
- project control logic;
- repair governance;
- state/provenance architecture;
- cross-page dependency architecture.

Reason:

Those claims are about the project/control representation rather than exact rendered page bytes.

Examples include:

- the controlled MASTER_CONTROL PDAudit passes, for the exact frozen blobs they named;
- route-level recursive and orthogonal audits;
- repair-escalation/governance audits;
- source/bridge architecture work.

### V2 — Valid as candidate/derived-artifact evidence only

An audit remains evidence about the exact candidate or PDF it inspected but does not automatically validate the accepted source pages.

Examples include:

- audits of generated PDF compilations;
- audits of programmatic full-booklet replacements;
- audits of later candidate renders.

Disposition:

Preserve them as regression/comparison evidence.

Do not treat them as accepted-artifact validation.

### V3 — Requires rerun against accepted source objects

Rerun any audit whose conclusion depended on:

- exact layout;
- exact wording as rendered;
- text legibility;
- cropping;
- visual hierarchy;
- image choice;
- page composition;
- actual page-to-page visual continuity;
- exact source framing visible to students;
- physical artifact usability;

when the audit did not use the exact accepted source page-image set.

## Current booklet consequences

### Yom Kippur

The exact accepted source set is now identified in:

projects/jewish-holiday-booklets/ARTIFACTS.yaml

Artifact-level audits can now be rerun against the four exact page PNGs.

Architecture/control audits remain useful.

### Fick / Difference

The accepted pre-repair baseline is established as a project fact:

“Different People. A Shared Place.”

But exact accepted individual page-image identity is still unresolved.

Therefore:

- architecture/route findings remain usable;
- candidate/PDF findings remain candidate/PDF findings;
- no new artifact repair is executable until exact baseline images are recovered;
- artifact-level claims about the accepted baseline remain pending exact-object recovery.

### Keva / Practice

A current artifact candidate exists.

It is not yet registered as an accepted source artifact.

Audits can characterize the candidate, but cannot promote it by auditing it.

### Conservation / Boundaries

No canonical rendered artifact is currently established.

Route/control audits remain relevant.

Artifact-level validation is premature.

## Prior convergence clarification

The Pass 3 and Pass 4 MASTER_CONTROL convergence result remains valid for the exact frozen blob:

a77f240b6ea269ac22b82dfb983d71841436c42f

MASTER_CONTROL has since changed to add explicit research-object authority and artifact-target rules.

Therefore the old convergence certificate does not automatically certify the newer blob.

A fresh controlled rerun is required after the current migration edits stabilize.

## Are the earlier education audits wasted?

No.

Their value separates into three buckets:

1. reusable architecture/governance findings;
2. candidate/derived-artifact regression evidence;
3. artifact-specific conclusions that need rerun against the accepted source images.

The mistake was not necessarily the reasoning inside each audit.

The mistake was insufficient typing of the audit bearer.

## New audit requirement

Every future JHB audit begins with:

AUDIT_OBJECT_ID
ARTIFACT_CLASS
IMMUTABLE_IDENTITY
AUDIT_TARGET
OPERATION_MODE

For source-artifact audits, immutable identity means exact artifact ID plus hash or equivalent immutable version.

## Current status

TARGET-TYPING REPAIRED.

Artifact validation remains open booklet by booklet.
