# Jewish Holiday Booklet Image Generation Protocol

> Architecture status note — 2026-09-22
>
> This v0.2 protocol correctly preserves coordinated four-page generation plus local
> repair, but it is not yet the complete generation-package architecture. Fick research
> subsequently identified additional required source-package, preflight/compiler,
> immutable render-bundle, renderer-capability, realization, overflow, structure-reference,
> constraint-priority, and run-provenance coordinates. See
> `audits/JHB_FICK_GENERATION_PACKAGE_ARCHITECTURE_RESEARCH_2026-09-22.md`.
> Do not treat v0.2 alone as render-readiness proof.
>
> The shared production contract owns reusable production semantics; this protocol owns the
> human execution procedure. Booklet-local packages bind their own values to that contract.


Version: 0.2
Date: 2026-09-22
Immediate target: current Fick / Difference revision
Shared production semantics: `production/PRODUCTION_CONTRACT.yaml` (`JHB:PRODUCTION:CONTRACT:001`)
Applies to: coordinated booklet generation, page generation, image replacement, diagram replacement, and local visual repair.

## Core invariant

Image generation is a rendering operation, not the authority for booklet content, page identity, source lineage, or repair scope.

A booklet can be generated in one coordinated multi-page episode. The output contract, however, must preserve four distinct full-size page objects with explicit page identities.

Do not confuse:
- coordinated four-page generation;
- one composite image containing four pages;
- four miniature pages;
- four variants of one page;
- four independent page-generation episodes.

These are different production objects.

## Production modes

### MODE A — COORDINATED_BATCH

Use for:
- a fresh booklet;
- a major visual recomposition;
- a revision where shared booklet-level visual coherence is a major target.

Desired structure:
- one coordinated generation episode;
- four distinct page outputs;
- P1, P2, P3, P4 each represented exactly once;
- each page full-size;
- shared style and visual grammar;
- page-specific jobs and content.

Forbidden:
- one four-panel/contact-sheet canvas;
- four shrunken pages inside one image;
- four variants of Page 1;
- missing or duplicated PAGE_IDs.

### MODE B — LOCAL_REPAIR

Use after a useful render exists.

Desired structure:
- preserve successful page state;
- alter only the failed page or region;
- do not discard successful pages merely because another page failed.

Preferred repair order:
REGION_EDIT
→ PAGE_EDIT
→ COORDINATED_BATCH_REGENERATION only when the defect is genuinely set-level.

## Required pre-generation bundle

A coordinated generation task is READY only when all required artifacts below exist.

### 1. Exact target binding

Record:
- booklet_id;
- source_set_id where applicable;
- operation mode;
- source references;
- four PAGE_IDs.

For current Fick continuation, resolve the current working target through the JHB runtime before rendering.

### 2. Four-page route map

For every page record:
- page job;
- learner entry state;
- new idea/experience introduced;
- handoff question;
- material forbidden from appearing early.

This prevents four variants of one page and protects the booklet sequence.

### 3. Booklet Batch Manifest

This is the controlling object for coordinated generation.

Record:
- output_count: 4;
- output_topology: FOUR_SEPARATE_FULL_SIZE_PAGES;
- page_order: P1, P2, P3, P4;
- one unique page contract per PAGE_ID;
- shared visual grammar;
- allowed cross-page motifs;
- forbidden duplication;
- forbidden composite/contact-sheet output;
- batch-level acceptance conditions.

### 4. Shared Style Contract

Record once:
- page dimensions and orientation;
- margins;
- type hierarchy;
- visual density;
- illustration language;
- footer/source treatment;
- logo location;
- whitespace policy;
- semantic colors;
- common visual motifs that may persist across pages.

The shared style contract exists to preserve the benefit of coordinated generation.

### 5. Four exact Page Blueprints

For each PAGE_ID record:
- every student-facing string exactly;
- every heading exactly;
- every equation exactly;
- source text exactly;
- region for every text block;
- image/diagram list;
- image function;
- image position;
- image relative size;
- writing/interaction space;
- required blank space;
- dominant visual hierarchy;
- page-specific forbidden content.

Each blueprint answers:
- what exists;
- where it exists;
- what job it performs;
- how this page differs from the other three.

### 6. Preservation Ledger

For any existing source page or successful new render, list every element already correct.

For each protected item record:
- element ID;
- region;
- content;
- reason protected;
- mutation permission.

Once a batch page passes, it enters the preservation ledger.

### 7. Delta Specification

Used during repair.

For each repair record:
- defect;
- affected page;
- affected region;
- old content;
- new content;
- permitted transformation;
- forbidden collateral changes.

No listed delta means no permission to alter that element.

### 8. Asset Pack

Supply actual assets when exact identity matters:
- source pages;
- approved illustrations;
- logo;
- diagrams;
- reference images;
- any image being inserted or replaced.

Do not ask the generator to recreate an existing exact asset from prose when the asset itself is available.

### 9. Acceptance Matrix

Two levels are required.

#### Page-level

- PAGE_ID correct;
- page full-size;
- exact wording preserved;
- equations preserved;
- protected regions preserved;
- licensed delta respected;
- image functions satisfied;
- semantic colors preserved;
- science/source fidelity preserved;
- page job preserved;
- writing/interaction space preserved;
- style contract preserved.

#### Set-level

- exactly four distinct page outputs;
- P1/P2/P3/P4 each represented once;
- no contact sheet;
- no composite four-panel image;
- no duplicate page variants;
- shared visual language coherent;
- page jobs remain distinct;
- cross-page reveal order preserved;
- overall density/rhythm coherent;
- booklet handoffs intact.

## Coordinated batch execution loop

1. Resolve exact booklet target and source set.
2. Freeze the four-page route map.
3. Freeze the Booklet Batch Manifest.
4. Freeze the shared Style Contract.
5. Freeze all four Page Blueprints.
6. Assemble the Asset Pack.
7. Run one coordinated four-page generation episode.
8. Verify set-level topology first.
9. Verify each page individually.
10. Freeze every passing page.
11. Route only failing pages/regions into LOCAL_REPAIR.
12. Rerun the full batch only for a demonstrated set-level defect.
13. Final set verification.
14. Package.

## Partial-success salvage rule

A four-page batch is not all-or-nothing.

Example:
- P1 PASS
- P2 PASS
- P3 REPAIR_REQUIRED
- P4 PASS

Then:
- freeze P1, P2, and P4;
- repair P3 locally;
- do not regenerate P1, P2, or P4 merely to obtain another P3.

This preserves the strongest demonstrated behavior from successful local image editing.

## Reusable coordinated-generation prompt

We are generating one coordinated four-page Jewish Holiday Booklet set.

Booklet:
[BOOKLET_ID]

Source set:
[SOURCE_SET_ID]

Operation:
COORDINATED_BATCH

Output topology:
Return four distinct full-size page outputs.
Return exactly one Page 1, one Page 2, one Page 3, and one Page 4.
Do not create a contact sheet.
Do not place four pages on one canvas.
Do not shrink the four pages into one image.
Do not return four variants of the same page.

Shared booklet contract:
[STYLE_CONTRACT]
[SHARED_VISUAL_GRAMMAR]

Page 1:
[PAGE_1_BLUEPRINT]

Page 2:
[PAGE_2_BLUEPRINT]

Page 3:
[PAGE_3_BLUEPRINT]

Page 4:
[PAGE_4_BLUEPRINT]

Cross-page route:
[ROUTE_MAP]

Exact content:
All supplied student-facing wording, equations, labels, and source text are exact.
Do not rewrite, summarize, paraphrase, duplicate, or invent text.

Assets:
Use supplied exact assets where provided.

Set-level verification:
Confirm that all four PAGE_IDs are distinct, full-size, and follow the shared visual grammar while performing different page jobs.

## Reusable local-repair prompt

We are repairing one existing page from an already generated four-page booklet.

Booklet:
[BOOKLET_ID]

Page:
[PAGE_ID]

Source page:
[SOURCE_PAGE]

Protected state:
[PRESERVATION_LEDGER]

Licensed change:
[DELTA]

Permitted region:
[REGION]

Change only the licensed region.
Preserve everything else.
Do not redesign the page.
Do not alter protected text, images, diagrams, colors, spacing, hierarchy, logo, or blank interaction space.

Return one repaired full-size page.

## Current Fick application

Current Fick state distinguishes:
- accepted repair baseline: JHB:FICK:ACCEPTED-PAGES:001;
- promoted current working set: JHB:FICK:WORKING-PAGES:002;
- accepted final product: OPEN.

For the next Fick revision:

1. bind to JHB:FICK:WORKING-PAGES:002;
2. create/update the four-page route map;
3. create the Booklet Batch Manifest;
4. create the shared Style Contract;
5. create four exact Page Blueprints;
6. assemble the Asset Pack;
7. create the two-level Acceptance Matrix;
8. run one coordinated four-page generation episode;
9. freeze every passing page;
10. locally repair failed pages or regions;
11. rerun the batch only for a set-level defect;
12. perform final set verification;
13. package.

This protocol does not itself accept a repaired product. Fick product acceptance remains controlled by fick/ACCEPTANCE.yaml.
