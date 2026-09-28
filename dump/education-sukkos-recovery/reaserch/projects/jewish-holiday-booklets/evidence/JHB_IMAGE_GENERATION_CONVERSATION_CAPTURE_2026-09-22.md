# JHB Image Generation Conversation and Findings Capture — 2026-09-22

Status: NON-AUTHORITATIVE PROVENANCE / EVIDENCE CAPTURE
Project: Jewish Holiday Booklets
Immediate application: Fick / Difference booklet
Date captured: 2026-09-22

## Purpose

Preserve the material facts, user observations, corrections, audit results, production lessons, and unresolved architecture decisions from the 2026-09-22 conversations about booklet image generation.

This file is intentionally NOT:
- an authoritative source of student-facing booklet text;
- a replacement for the text-authoring system currently being constructed;
- a product-acceptance record;
- an artifact-identity registry;
- an instantiated Fick generation package.

It exists so later work does not need to reconstruct these findings from chat history.

Authority remains:
- exact artifact identity -> ARTIFACTS.yaml;
- Fick operational state -> fick/STATE.yaml;
- Fick product acceptance -> fick/ACCEPTANCE.yaml;
- shared project interpretation -> MASTER_CONTROL.md;
- generation procedure -> IMAGE_GENERATION_PROTOCOL.md;
- future exact booklet text -> the authoritative text system/objects once their location and IDs are finalized.

## Current Fick object state relevant to generation

Current repository state distinguishes:
- accepted repair baseline: JHB:FICK:ACCEPTED-PAGES:001;
- promoted current working set: JHB:FICK:WORKING-PAGES:002;
- accepted final product: OPEN.

The current working set is the continuation target for present Fick work but is not itself final product acceptance.

Exact target selection must not use filename similarity, recency, PDFs, composites, or visual coherence as substitutes for registered object identity.

## User-observed image-generation failure history

The following recurring failures were identified across booklet work.

### 1. Exact text unreliability

Generated pages can:
- rewrite text;
- shorten text;
- omit text;
- duplicate text;
- misspell text;
- corrupt equations, labels, or technical notation.

Exact wording therefore cannot be left as an implicit prompt preference.

### 2. Local-edit requests can trigger global redesign

A request to alter one image, move one element, remove one box, or repair one region can unexpectedly alter:
- typography;
- hierarchy;
- spacing;
- colors;
- imagery;
- background;
- source treatment;
- other already-correct elements.

### 3. Approved elements do not automatically persist

Previously successful elements can disappear or change during regeneration, including:
- logos;
- equations;
- diagrams;
- color mappings;
- whitespace;
- page hierarchy;
- approved imagery.

### 4. Style drift

Repeated generation can move away from the established booklet language toward:
- generic educational worksheets;
- card-heavy layouts;
- excessive boxes;
- icon clutter;
- overly polished infographic style;
- unrelated decorative visual systems.

The Yom Kippur booklet remains an important visual/structural benchmark because its success came from page-job clarity, strong hierarchy, meaningful visuals, whitespace, emotional movement, and coherent four-page progression rather than mere surface styling.

### 5. Overfilling and density inflation

The generator often treats empty space as unfinished space and adds:
- more images;
- more labels;
- more boxes;
- more icons;
- more scenes.

This can destroy writing space, interaction space, visual hierarchy, and page focus.

### 6. Decorative images can replace functional images

An image can be attractive while failing the instructional job.

Required visual functions include such things as:
- making a mechanism visible;
- showing a relationship;
- embodying a concept;
- supporting a transition;
- producing an intended learner experience.

### 7. Later-page ideas can leak backward

Because the generator sees the whole booklet concept, it can reveal Page 3 or Page 4 ideas on Page 1 or Page 2.

This damages the booklet's discovery sequence.

### 8. Scientific diagrams are fragile

For Fick and other science-driven booklets, plausible-looking diagrams can still be wrong in:
- direction;
- quantity;
- arrow meaning;
- labels;
- gradients;
- membrane relationships;
- equations;
- conceptual mapping.

Visual plausibility is not science fidelity.

### 9. Semantic colors can drift

Color often carries conceptual meaning.

Aesthetic recoloring can therefore change the instructional semantics even when the page looks visually improved.

### 10. Page hierarchy can flatten

The intended hierarchy generally includes:
- one dominant page job;
- one dominant visual or relationship;
- secondary support;
- deliberate whitespace.

Generation often makes too many elements equal in visual weight.

### 11. Writing and interaction space can disappear

Blank space can have an instructional function.

It must be specified as a required object, not left as unused layout area.

### 12. Emotional or experiential mechanism can be polished away

A cleaner page can become less effective when visual polishing turns an experience into information about an experience.

### 13. Wrong ancestor / wrong version problems

"Latest," "best," "accepted," "current working," and "visually coherent" are not interchangeable.

The wrong source set can be repaired successfully and still be the wrong artifact.

This drove the exact-object and task-binding architecture now present in JHB.

### 14. Page correctness and booklet correctness are distinct

A page can be individually attractive and still damage the booklet by:
- duplicating another page's function;
- failing to hand off to the next page;
- revealing later content early;
- embodying a different mechanism;
- breaking shared visual language.

## Critical four-page generation finding

A major empirical finding from prior booklet work is:

COORDINATED FOUR-PAGE GENERATION OFTEN WORKED BETTER WHEN IT WORKED.

The benefit appears in:
- stronger shared visual language;
- more coherent rhythm/density;
- better page-to-page consistency;
- better sense that the pages belong to one booklet;
- better cross-page progression than unrelated independent generations.

This successful behavior must be preserved.

The mistake is to equate "generate four pages together" with "put four pages in one image."

Those are different coordinates.

### Known multi-page failure modes

When asked to generate four pages, the generator has sometimes produced:
- one canvas containing four miniature pages;
- four thin/narrow pages arranged on a single sheet;
- a contact sheet;
- four variants of Page 1;
- duplicated page concepts instead of P1/P2/P3/P4;
- incomplete or ambiguous page identity.

These are output-topology and page-identity failures.

They do NOT establish that coordinated batch generation itself is the wrong mode.

## Critical local-edit finding

Another repeated positive result:

Once a page is mostly useful, targeted removal/replacement/editing of a specific image or region can work well.

Successful repair behavior includes:
- remove one bad object;
- replace one image;
- insert one image;
- repair one bounded region;
- preserve the surrounding page.

This implies two distinct production modes.

### Mode A — coordinated booklet creation / major recomposition

Use shared four-page generation context when booklet-level coherence is part of the target.

### Mode B — local repair / salvage

Once useful pages exist:
- freeze successful pages;
- freeze successful regions;
- repair only the implicated page or region.

Do not reroll successful pages merely because another page failed.

## Corrected production architecture

The working production architecture derived from the conversation is:

CONTENT / ROUTE / VISUAL STATE FROZEN
→ COORDINATED FOUR-PAGE GENERATION
→ SET-LEVEL TOPOLOGY CHECK
→ PAGE-LEVEL CHECK
→ FREEZE SURVIVORS
→ LOCALIZED PAGE/REGION REPAIR
→ FINAL SET VERIFICATION
→ PACKAGE.

A four-page batch is therefore not all-or-nothing.

Example:
- P1 PASS
- P2 PASS
- P3 REPAIR_REQUIRED
- P4 PASS

Then P1/P2/P4 become protected state and P3 enters local repair.

## PD audit correction

An earlier 2026-09-22 audit was described as a "triple PD audit."

That analysis used PD-derived concepts but did NOT faithfully execute the current PracticalCore PD path.

The current PracticalCore execution architecture requires:
1. A18 / HF-001 historical recursive PD bootstrap first;
2. semantic preflight;
3. typed capability routing;
4. ordered capability execution;
5. terminal validation.

The earlier audit also incorrectly created the universal rule:
"one image-generation call = one page."

That rule contradicted the successful coordinated four-page history.

The earlier audit is now explicitly marked superseded as a PD execution record:
- audits/JHB_IMAGE_GENERATION_TRIPLE_PD_AUDIT_2026-09-22.md

The corrected PD record is:
- audits/JHB_IMAGE_GENERATION_PRACTICALCORE_PD_CORRECTION_2026-09-22.md

The corrected analysis used:
- HF-001 recursive discovery;
- representation/coordinate attack;
- result-sensitivity analysis;
- intervention-frontier/preservation analysis.

### Main PD result

The central representation error was collapsing:
- generation episode coupling;
- output topology;
- page identity;
- repair scope;
- shared booklet context.

The desired major-generation configuration is:

- generation episode = coordinated batch;
- output topology = four separate full-size pages;
- page identity = distinct P1/P2/P3/P4;
- booklet context = shared.

A single contact-sheet image is a different object.

Four independent page calls are a different process.

Four variants of Page 1 are not the target booklet.

## Current generation protocol

The corrected reusable production protocol is:
- projects/jewish-holiday-booklets/IMAGE_GENERATION_PROTOCOL.md

Current protocol version at this capture:
- v0.2

The JHB local instructions also require the generation protocol to be loaded before booklet generation/edit work.

## Complete four-page generation package — current design

The conversation established most of the required package architecture.

The package is NOT yet instantiated for Fick.

That is intentional because the project is currently creating the authoritative places where actual booklet text will live.

The generation package must not become a second home for the text.

### Ownership boundary

TEXT SYSTEM
owns:
- exact student-facing wording;
- exact headings;
- exact equations;
- exact labels;
- exact source wording.

GENERATION PACKAGE
owns:
- which authoritative content objects belong on which page;
- where those objects go;
- what visual objects exist;
- what each visual does;
- batch topology;
- shared style/visual grammar;
- page-specific layout;
- render acceptance.

ARTIFACT REGISTRY
owns:
- exact source/render identity;
- hashes;
- lineage;
- object class.

PRODUCT ACCEPTANCE
owns:
- whether the repaired booklet is accepted.

### Critical rule

The generation package references authoritative content IDs/objects.

It does NOT duplicate the actual booklet text once an authoritative text system exists.

Example conceptually:

P2:
  content_ref: FICK:P2:TEXT:...
  layout_ref: ...
  visual_ref: ...

rather than embedding a second independently editable copy of the P2 text.

## Proposed Fick generation-package storage

The conversation proposed the following structure:

projects/jewish-holiday-booklets/fick/
  STATE.yaml
  ACCEPTANCE.yaml
  generation/
    PACKAGE.yaml
    STYLE_CONTRACT.yaml
    ASSET_MANIFEST.yaml
    RENDER_ACCEPTANCE.yaml
    repairs/

Important status:

THIS STRUCTURE HAS NOT YET BEEN INSTANTIATED.

At capture time, the Fick folder still contains only:
- STATE.yaml
- ACCEPTANCE.yaml

No Fick generation package has yet been created.

This avoids colliding with the concurrent work of establishing the authoritative text locations.

## Required components of the future package

### 1. Exact Target Binding

Must identify:
- booklet;
- source/working set where relevant;
- operation mode;
- source refs;
- P1/P2/P3/P4 identities.

### 2. Four-Page Route Map

For every page:
- page job;
- learner entry state;
- new idea/experience;
- handoff;
- forbidden early reveal.

The route map protects against four variants of one page and preserves the booklet's causal sequence.

### 3. Booklet Batch Manifest

This is the set-level control object for coordinated generation.

It must specify:
- output_count = 4;
- output topology = four separate full-size pages;
- page order = P1/P2/P3/P4;
- one unique page contract per PAGE_ID;
- shared visual grammar;
- allowed cross-page motifs;
- forbidden duplication;
- forbidden contact-sheet/composite output;
- set-level acceptance conditions.

### 4. Shared Style Contract

Must specify:
- dimensions/orientation;
- margins;
- hierarchy;
- visual density;
- illustration language;
- footer/source treatment;
- logo treatment;
- whitespace policy;
- semantic colors;
- cross-page motifs.

This exists partly to preserve the demonstrated benefit of coordinated generation.

### 5. Four Page Specifications

Each page requires three conceptually separate coordinates.

#### CONTENT_REF

Points to the authoritative content objects.

It must not become a duplicate text store.

#### LAYOUT_SPEC

Specifies:
- regions;
- relative sizes;
- hierarchy;
- alignment;
- writing space;
- required blank space;
- image/text placement.

#### VISUAL_SPEC

Specifies:
- each image/diagram;
- visual function;
- relative size;
- position;
- semantic role;
- exact asset reference when applicable;
- forbidden decorative additions;
- page-specific visual obligations.

Separating CONTENT_REF / LAYOUT_SPEC / VISUAL_SPEC prevents one overloaded "page blueprint" from silently becoming the authority for everything.

### 6. Asset Manifest

References actual available assets:
- source pages;
- deer logo;
- diagrams;
- approved illustrations;
- references;
- replacement images.

When an exact asset exists, prose recreation is inferior to direct use of that asset.

### 7. Two-Level Render Acceptance

#### Page-level tests

Check:
- correct PAGE_ID;
- full-size page;
- exact content object use;
- science/source fidelity;
- semantic color fidelity;
- hierarchy;
- writing/interaction space;
- page-specific job;
- no unauthorized elements.

#### Set-level tests

Check:
- exactly four distinct outputs;
- P1/P2/P3/P4 once each;
- no composite/contact sheet;
- no miniaturized pages;
- no repeated Page 1 variants;
- shared visual language;
- distinct page jobs;
- cross-page handoffs;
- reveal order;
- coherent density/rhythm.

### 8. Post-generation Preservation Ledger

This belongs primarily to the repair stage.

After successful rendering, record:
- passing pages;
- passing regions;
- locked visual state;
- elements not permitted to change.

### 9. Repair Delta

For each failed page/region:
- exact defect;
- affected PAGE_ID;
- affected region;
- old state;
- intended replacement;
- allowed transformation;
- forbidden collateral changes.

## Important sequencing decision

The generation package can be designed structurally before the text system is finalized.

It must NOT be instantiated in a way that creates duplicate authoritative text while the text-authoring architecture is still being established.

Therefore the safe current state is:
- protocol exists;
- package schema/design exists in this evidence record;
- Fick-specific package files are not yet created;
- generation package later binds to authoritative text IDs/refs.

## Relevant Fick content/route facts from today's work

The Fick conceptual route has been treated as:
difference
→ identify what remains shared
→ coordinate only what the shared activity requires
→ allow unresolved difference to remain
→ continue participation.

Today's Fick repair work also preserved distinctions including:
- coordination is not agreement;
- difference is not automatically a defect;
- sharedness and required coordination are distinct;
- Sukkos-specific surplus remains a live/open issue;
- source content and educational application remain distinct;
- the activity must enact selective coordination rather than merely describe it;
- Page 4 must support transfer beyond the Sukkos activity.

These route facts are relevant to generation because the four page jobs must remain distinct.

This evidence capture intentionally does not reproduce the current exact student-facing text, because the user explicitly identified the need for a separate authoritative place for that text.

## Other relevant 2026-09-22 JHB facts

### Accepted artifacts are images, not PDFs

Earlier today, a PDF was surfaced during Fick retrieval and was rejected as the wrong object class.

The accepted/working booklet objects are individual page images.

A compiled PDF or composite is derived and must not silently substitute for the source pages.

### Current runtime/object repair

Today's JHB runtime work established:
- task target resolution before broad retrieval;
- exact-object retrieval;
- operation-sensitive current/baseline/package resolution;
- Fick continuation binding;
- fail-closed behavior on unresolved targets.

This matters because generation must consume the resolved source set rather than rediscovering "the best/latest" pages.

### Fick baseline versus working set

The accepted repair baseline remains distinct from the current working continuation target.

Do not collapse:
- JHB:FICK:ACCEPTED-PAGES:001
with
- JHB:FICK:WORKING-PAGES:002.

### Product acceptance remains separate

A successful render is not automatically an accepted repaired product.

Fick acceptance gates remain in:
- projects/jewish-holiday-booklets/fick/ACCEPTANCE.yaml

## Reusable lessons

1. Storing authoritative truth and forcing generation to consume it are separate jobs.
2. Exact artifact identity does not by itself define the requested operation.
3. Coordinated generation can provide valuable booklet-level coherence.
4. Output topology must be independently controlled.
5. Page identity must be explicit within a batch.
6. Partial success must be salvageable.
7. Successful pages become protected state.
8. Local editing can outperform full regeneration late in the process.
9. A generation prompt is not a substitute for a production package.
10. The production package must not duplicate authoritative text.
11. Page-level verification and set-level verification are both required.
12. A visually strong render can still fail the instructional mechanism.
13. A new render never becomes accepted merely because it is newer.
14. The four-page generation package is currently designed but not instantiated.

## Current unresolved items

1. Authoritative text storage/IDs are still being established.
2. The Fick-specific generation package has not yet been instantiated.
3. The exact schema/file split for future CONTENT_REF, LAYOUT_SPEC, and VISUAL_SPEC can still be refined once text-object identity is known.
4. Sukkos-specific educational surplus remains open in Fick acceptance.
5. Exact empirical performance of generation modes is tool/model dependent; the preserved evidence is that coordinated four-page generation has repeatedly been valuable when successful and local editing has repeatedly been useful for repair.

## Repository references created/updated during this conversation

- audits/JHB_IMAGE_GENERATION_TRIPLE_PD_AUDIT_2026-09-22.md
  - retained for useful observations;
  - marked superseded as a proper PD execution record.

- audits/JHB_IMAGE_GENERATION_PRACTICALCORE_PD_CORRECTION_2026-09-22.md
  - corrected HF-001-first / PracticalCore-aligned analysis.

- projects/jewish-holiday-booklets/IMAGE_GENERATION_PROTOCOL.md
  - corrected protocol v0.2;
  - coordinated batch plus local repair.

- .github/instructions/jhb.instructions.md
  - generation preflight now preserves coordinated four-page generation and rejects composite/duplicate-page failures.

## Final state of this capture

The project now has:
- a general generation protocol;
- a corrected PD evidence record;
- a comprehensive conversation/provenance capture;
- a clear proposed future generation-package architecture.

The project does NOT yet have:
- an instantiated Fick generation package;
- a second copy of authoritative Fick booklet text.

That absence is intentional until the authoritative text-location work is resolved.

## Later 2026-09-22 state correction

The earlier sections of this capture describe the Fick generation package as not yet
instantiated. That statement was accurate at the time of capture but is no longer
current.

Current package candidate:

- `projects/jewish-holiday-booklets/fick/generation/PRODUCTION_PACKAGE_CANDIDATE.yaml`
- package ID: `JHB:FICK:PRODUCTION-PACKAGE:CANDIDATE:001`

Later architecture research established that the candidate is still incomplete and is
now explicitly marked `architecture_repair_required`.

Controlling architecture-research record:

- `audits/JHB_FICK_GENERATION_PACKAGE_ARCHITECTURE_RESEARCH_2026-09-22.md`

Material additions still required include:

- content-to-slot binding;
- constraint-priority/free-variable representation;
- structure/wireframe references;
- typed reference roles;
- per-element realization modes;
- overflow/fallback policy;
- renderer capability profile;
- preflight/compiler layer;
- immutable render-bundle contract;
- render-run provenance;
- coherence-group representation.

This correction does not alter the earlier historical observations. It updates only the
current package-state claims.
