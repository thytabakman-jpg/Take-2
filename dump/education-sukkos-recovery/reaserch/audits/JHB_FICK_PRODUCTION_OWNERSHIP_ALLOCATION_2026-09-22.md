# Fick Production Architecture Ownership Allocation

Date: 2026-09-22
Project: jewish-holiday-booklets
Immediate target: JHB:FICK:PRODUCTION-PACKAGE:CANDIDATE:001
Authority: analytic allocation record; no mutation authority
Basis:
- audits/JHB_FICK_GENERATION_PACKAGE_ARCHITECTURE_RESEARCH_2026-09-22.md
- audits/JHB_FICK_THREE_OBJECT_PRODUCTION_CLOSURE_PD_2026-09-22.md
- projects/jewish-holiday-booklets/fick/generation/PRODUCTION_PACKAGE_CANDIDATE.yaml

## Allocation rule

For every production coordinate distinguish:

1. SEMANTIC / SCHEMA OWNER
   Where the reusable meaning, allowed values, lifecycle rule, and validation contract
   belong.

2. INSTANCE / VALUE OWNER
   Where the actual booklet-, renderer-, bundle-, or run-specific value belongs.

A reusable schema does not own every instance.
A local instance does not get to redefine the reusable schema.

## Ownership matrix

| Coordinate | Shared/schema owner | Instance/value owner | Current Fick action |
| --- | --- | --- | --- |
| stable content identity fields | JHB shared production substrate | exact-copy authority + Fick package bindings | shared contract defines required identity fields; Fick binds current/frozen copy IDs and blobs |
| content-to-slot binding | JHB shared production substrate | Fick production package | define shared binding shape; Fick supplies P1-P4 block/slot assignments |
| constraint priority classes | JHB shared production substrate | Fick package instantiates constraints | define LOCKED / HARD / FORBIDDEN / PREFERRED / FREE once |
| explicit free variables | JHB shared production substrate | Fick package | shared semantics; Fick enumerates actual allowed freedoms |
| structure / wireframe reference role | JHB shared production substrate | Fick package + referenced structure artifacts | define role and authority boundary once; Fick supplies refs |
| typed reference roles | JHB shared production substrate | Fick package | shared vocabulary; Fick tags actual refs |
| per-element realization modes | JHB shared production substrate | Fick package / compiled bundle | shared vocabulary; Fick selects intended mode, compiler resolves renderer-compatible execution |
| overflow / fallback semantics | JHB shared production substrate | Fick package can narrow allowed local freedoms; compiler executes | shared fail-closed rule plus ordered legal fallback categories |
| coherence-group semantics | JHB shared production substrate | Fick package | shared definition; Fick group is P1-P4 |
| preflight contract | JHB shared production substrate | preflight result for each package/bundle | shared readiness tests; instance records pass/open/fail |
| compiler contract | JHB shared production substrate | compiler execution | shared transformation/authority limits; run-specific compilation downstream |
| immutable render-bundle schema | JHB shared production substrate | each compiled render bundle | schema shared; bundle instance downstream |
| renderer capability-profile schema | JHB shared production substrate | renderer adapter/profile | schema shared; actual capability truth belongs to renderer-specific profile |
| render-run provenance schema | JHB shared production substrate | each render run record | schema shared; actual run/output mapping downstream |
| batch topology vocabulary | JHB shared production substrate | Fick package | shared allowed/forbidden topology semantics; Fick requests coordinated four-page group |
| page/set acceptance framework | JHB shared production substrate | Fick package supplies booklet-specific tests; run records results | shared two-level contract, local criteria |
| preservation/salvage lifecycle | JHB shared production substrate | Fick run/repair state | shared rule; actual surviving pages/regions are run-specific |
| exact student-facing wording | COPY_CONTROL / frozen exact-copy object | exact-copy version | NOT owned by production substrate or package |
| learner route / page jobs | JHB/Fick educational controls | Fick package references/selects production-relevant subset | do not duplicate project authority |
| P1-P4 visual jobs | shared visual-role semantics only | Fick production package | remain Fick-local |
| P1-P4 layouts / eye paths / whitespace | shared layout semantics only | Fick production package | remain Fick-local |
| shared Fick booklet style values | shared house constraints may exist at JHB level | Fick production package unless already inherited | Fick binds actual style values/overrides |
| exact assets | artifact registry owns identity | Fick package references selected assets | no prose recreation when exact asset exists |
| artifact identity / lineage | ARTIFACTS.yaml | rendered output registry entries | outside production substrate authority |
| product acceptance | booklet ACCEPTANCE.yaml | Fick acceptance state | outside production package authority |

## Shared JHB production substrate — minimum justified scope

The shared substrate is justified only for reusable production semantics needed by more
than one booklet or by the source-package -> compiler -> bundle -> run lifecycle.

Minimum shared contract must define:

1. lifecycle layers:
   AUTHORITATIVE_UPSTREAM
   -> EDITABLE_SOURCE_PACKAGE
   -> PREFLIGHT
   -> COMPILE
   -> IMMUTABLE_RENDER_BUNDLE
   -> RENDER_RUN
   -> QA / REPAIR

2. constraint classes:
   LOCKED
   HARD
   FORBIDDEN
   PREFERRED
   FREE

3. reference roles:
   EXACT_ASSET
   STYLE_REFERENCE
   STRUCTURE_REFERENCE
   SOURCE_PAGE_REFERENCE
   SCIENCE_REFERENCE
   REPAIR_SOURCE
   OPTIONAL_INSPIRATION

4. realization modes:
   GENERATIVE
   EXACT_TEXT
   VECTOR_OR_CONTROLLED_DIAGRAM
   EXACT_ASSET
   LOCAL_EDIT
   COMPOSITE
   LOCKED_EXISTING_REGION

5. required source-package interfaces:
   content identity
   content-slot binding
   coherence group
   layout/visual/style constraints
   asset/reference bindings
   acceptance rules
   overflow/fallback rules

6. fail-closed overflow rule:
   HARD/LOCKED content cannot be paraphrased, omitted, or made unreadable to solve fit.
   Fallback can operate only over explicitly PREFERRED/FREE coordinates.

7. preflight contract:
   required refs resolve;
   frozen exact copy exists when required;
   page identities unique;
   no contradictory LOCKED/HARD constraints;
   required local specs present;
   renderer profile supports operation;
   acceptance rules present.

8. compiler authority:
   may resolve and transform representation;
   may not rewrite authoritative copy;
   may not relax LOCKED/HARD constraints;
   must record source identities and produce immutable bundle identity.

9. render-bundle minimum identity:
   source package version/blob;
   frozen copy identity/blob;
   resolved page instructions;
   references/assets;
   realization plan;
   renderer profile;
   dimensions/settings;
   acceptance tests;
   bundle hash/identity.

10. run-record minimum identity:
    bundle identity;
    renderer/model/profile;
    outputs;
    page mapping;
    QA result;
    survivors;
    repair continuation.

## Fick-local responsibilities after shared substrate exists

The existing Fick production package remains responsible for:

- target booklet/source-set binding;
- Fick coherence group P1-P4;
- actual frozen-copy reference;
- P1-P4 production-relevant route/job bindings;
- P1-P4 content-slot assignments;
- P1-P4 visual obligations;
- P1-P4 layout and eye-path decisions;
- Fick style values and semantic colors;
- Fick structure/wireframe references;
- selected asset refs;
- actual free/preferred variables;
- actual realization choices where known;
- Fick-specific page/set acceptance;
- local repair constraints.

## Renderer-specific responsibilities

A renderer profile owns facts about the execution system, such as:

- native multi-output support;
- edit/inpaint support;
- accepted image-reference count/types;
- structure/style-reference support;
- exact-size behavior;
- text reliability assumptions;
- local-edit behavior;
- compositing/transparency support.

These facts must not be asserted by the Fick package merely because they are desired.

## Run-specific responsibilities

A compiled bundle/run layer owns:

- fully resolved execution state;
- actual renderer settings;
- actual outputs;
- exact output-to-PAGE_ID mapping;
- QA;
- protected survivors;
- repair continuation.

## Result

The ownership boundary converges.

The newly discovered production coordinates are neither all Fick-local nor all project-
global.

One small shared JHB production substrate is justified.

The existing Fick package remains the local production source object and must reference
the shared substrate rather than reproduce it.

No separate VISUAL_CONTROL system is justified at this stage.

No universal repository-wide production architecture is justified by this audit.
