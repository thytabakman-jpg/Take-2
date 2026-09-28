# Fick Adaptive Image-Spec Run — PD + ImprovementCore

Date: 2026-09-22
Project: jewish-holiday-booklets
Target package: JHB:FICK:PRODUCTION-PACKAGE:CANDIDATE:001
Method: HF-001 recursive PD + crossed-structure/orthogonal audit + manual ImprovementCore
Mutation scope: Fick production-package image/layout/style/asset coordinates and immediate state bindings

## Checkpoint 0 — prompt audit

The image task is not a linear P1 -> P2 -> P3 -> P4 sequence.

It is a crossed structure in which at least these coordinates intersect:

- page-specific learner job
- page-specific visual job
- text/image division of labor
- eye path and layout space
- cross-page visual grammar
- exact/source/style asset roles
- generation topology and repair constraints

The correct object is therefore a matrix:

PAGE JOB
x VISUAL JOB
x LAYOUT / SPACE
x SHARED STYLE
x ASSET / REFERENCE ROLE
x PRODUCTION CONSTRAINT

HF-001 result:
The live missing object is not another visual-control system. It is the incomplete image
and layout portion of the existing Fick production package.

ImprovementCore result:
1. formalize page-level image specifications;
2. rerun;
3. formalize shared cross-page visual grammar;
4. rerun;
5. formalize exact/typed asset and production-facing image constraints;
6. rerun;
7. stop when the remaining coordinates are exact wireframe/style/asset choices rather
   than missing architecture.

No rendering is authorized by this run.


## Checkpoint 1 — page-level image specifications formalized

Package blob after write:
9c2a95c342ef3a2af17f6f365dad6566d71d42f4

Added for each P1-P4:
- supporting visual jobs
- must-notice relations
- text-inside-visual rules
- text-outside-visual divisions
- eye path
- space requirements
- page-specific visual failure conditions

Layout status now distinguishes:
STRUCTURAL_REGIONS_SPECIFIED_EXACT_WIREFRAME_OPEN

### Post-step HF-001 / crossed-structure audit

The page-level image jobs are now materially specified, but the write exposed one
representation defect:

Each page already owned a top-level central_visual_job.
The new image_spec block duplicated that same central visual job text.

That duplication is unnecessary and creates a future synchronization surface.

The stronger representation is:
page.central_visual_job = authoritative local statement
image_spec.central_visual_job_ref = page.central_visual_job

No other page-level image-spec conflict was found.

Cross-page risk confirmed:
P2 and P4 require different visual states.
- P2 = pre-tool relational discomfort
- P4 = post-tool independent transfer

That distinction is already protected in their separate failure conditions.

### ImprovementCore recomputation

PROTECT:
- all new page-level image obligations;
- top-level central_visual_job as the single local authority.

LOCALIZE:
remove duplicated central-visual wording before adding shared grammar.

SELECT:
replace only the four nested duplicates with local references.

RECOMPUTE:
After that micro-repair, proceed to the shared cross-page visual grammar.


## Checkpoint 1B — page-level deduplication completed

The four image_spec blocks now reference each page's existing central_visual_job rather
than duplicating it.

### Post-step PD + ImprovementCore rerun

HF-001:
The page-level representation is now cleaner:
- one local authority for the central visual job;
- supporting visual logic lives in image_spec;
- exact wireframe remains OPEN rather than being silently invented.

No higher-level dependency appeared.

ImprovementCore:
PROTECT page-level image specs.
LOCALIZE next frontier = shared cross-page visual grammar.
SELECT formalize the shared visual grammar inside the existing shared_style_contract.
RECOMPUTE next step survives.
