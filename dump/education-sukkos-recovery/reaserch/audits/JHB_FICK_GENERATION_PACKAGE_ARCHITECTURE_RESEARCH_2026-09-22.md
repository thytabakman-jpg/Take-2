# Fick Generation Package Architecture Research — 2026-09-22

Status: CURRENT ARCHITECTURE RESEARCH / REPAIR INPUT
Project: Jewish Holiday Booklets
Booklet: Fick / Difference
Target object: JHB:FICK:PRODUCTION-PACKAGE:CANDIDATE:001

## Purpose

Record the wider architecture-discovery result for the four-page generation package
without creating a competing production-control object.

This file does not contain authoritative student-facing copy and does not authorize
rendering. It identifies missing production coordinates that must be integrated into
the current package candidate before that package can be frozen.

## Main finding

The production package is not the render prompt.

The strongest current model is:

AUTHORITATIVE SOURCES
-> EDITABLE GENERATION PACKAGE
-> PREFLIGHT / COMPILATION
-> IMMUTABLE RENDER BUNDLE
-> RENDERER EXECUTION
-> OUTPUT / QA / REPAIR RECORD.

The editable package references authoritative copy, route, artifact, visual, layout,
asset, and acceptance state.

The compiler resolves those references into one immutable execution bundle.

The renderer consumes the compiled bundle.

The prompt is therefore compiler output rather than the maintained source of production
truth.

## PD-derived architecture findings

### 1. Recursive dependency result

A render-ready package requires more than copy, layout, visuals, assets, and acceptance.

Additional load-bearing coordinates discovered:

- stable content IDs;
- content-to-slot binding;
- explicit constraint priority;
- explicit creative/free variables;
- overflow/fallback behavior;
- reference-image roles;
- page structure/wireframe references;
- per-element realization mode;
- renderer capability profile;
- preflight validation;
- compilation into an immutable render bundle;
- run provenance;
- bundle identity/hash.

### 2. Rival architecture result

Models considered:

- giant prompt;
- one giant manifest;
- layered files;
- source package plus compiled render bundle;
- full dependency graph;
- template-first system.

Current strongest architecture:

layered editable source package
+ explicit preflight/compiler
+ immutable render bundle.

A full dependency graph remains useful for audit/reasoning but is too heavy as the
primary authoring interface.

A template/wireframe layer is useful for spatial control but cannot replace semantic,
copy, asset, and acceptance bindings.

## Required architecture repair fronts

### A. Content binding

Current package references page-level copy markers.

It still needs a stable mechanism to bind individual authoritative copy blocks to exact
layout slots without reproducing the wording.

Required coordinates:

- content_id;
- source object identity;
- page_id;
- slot_id;
- required/optional visibility;
- ordering relation where relevant.

### B. Constraint priority

The package needs explicit priority classes.

Working vocabulary:

LOCKED
- exact accepted state that cannot change.

HARD
- required invariant.

FORBIDDEN
- disallowed result.

PREFERRED
- retain when compatible with HARD constraints.

FREE
- explicit renderer design freedom.

Silence is not permission to redesign.

### C. Structure references

Each page can optionally or normally carry a low-fidelity wireframe/structure reference
that controls the spatial relationship among major blocks without becoming the source
of copy.

The four page wireframes can also be combined into a derived four-page proof for
pre-generation inspection of:

- density;
- rhythm;
- hierarchy;
- page distinctness;
- repetition;
- cross-page progression.

The proof is a verification artifact, not an authoritative page set.

### D. Reference roles

Reference images/assets need typed roles rather than one undifferentiated asset list.

Candidate roles:

- EXACT_ASSET;
- STYLE_REFERENCE;
- STRUCTURE_REFERENCE;
- SOURCE_PAGE_REFERENCE;
- SCIENCE_REFERENCE;
- REPAIR_SOURCE;
- OPTIONAL_INSPIRATION.

A reference role does not change artifact authority.

### E. Realization plan

Every material page element needs a realization mode.

Candidate modes:

- GENERATIVE;
- EXACT_TEXT;
- VECTOR_OR_CONTROLLED_DIAGRAM;
- EXACT_ASSET;
- LOCAL_EDIT;
- COMPOSITE;
- LOCKED_EXISTING_REGION.

This prevents "generate the page" from silently becoming one universal realization
method.

### F. Overflow/fallback policy

The package needs an explicit policy for cases where exact copy, required visuals, and
layout cannot all fit.

The renderer is not authorized to resolve overflow by:

- paraphrasing;
- omitting;
- inventing;
- shrinking text below an allowed readability floor;
- collapsing protected whitespace.

A future ordered fallback policy must operate only over coordinates explicitly marked
FREE or PREFERRED and fail closed when HARD constraints cannot be jointly satisfied.

### G. Renderer capability profile

The source package must not assume every renderer supports the same operation.

A renderer adapter/profile needs to declare capabilities relevant to the package, such
as:

- multi-output generation;
- edit/inpaint behavior;
- number/type of image references;
- structure-reference support;
- style-reference support;
- exact-size output;
- transparent/compositing support;
- text reliability assumptions;
- local-edit support.

This profile belongs downstream of booklet truth.

### H. Preflight

Before compilation, preflight must establish at least:

- frozen exact copy exists;
- all source references resolve;
- all required content blocks are intentionally bound;
- no required asset is missing;
- P1/P2/P3/P4 identities are unique;
- no contradictory HARD/LOCKED constraints exist;
- required structure/layout objects exist;
- overflow state is acceptable or explicitly OPEN;
- renderer supports the requested operation;
- page-level and set-level acceptance rules exist.

Failure blocks compilation/render.

### I. Compiler

The maintained package must compile into a renderer-specific execution object.

Compiler responsibilities:

- resolve authoritative references;
- freeze source identities;
- bind content to slots;
- normalize constraints;
- select renderer-compatible realization instructions;
- produce prompt/instruction payloads;
- attach reference assets;
- attach acceptance tests;
- produce bundle identity/hash.

The compiler may transform representation but does not gain authority to rewrite
student-facing content or relax HARD constraints.

### J. Immutable render bundle

A render bundle should record:

- render_bundle_id;
- source production-package version;
- frozen copy identity and blob;
- source artifact IDs;
- style/design profile version;
- resolved P1/P2/P3/P4 instructions;
- resolved structure/style/exact-asset references;
- realization plan;
- renderer/model/profile identity;
- dimensions/format/settings;
- compiled generation instructions;
- acceptance tests;
- bundle hash.

It is execution state, not the editable source package.

### K. Run provenance

Each render episode needs a run record that identifies:

- render bundle;
- renderer/model;
- relevant execution settings;
- output objects;
- page mapping;
- pass/repair-required/fail state;
- regressions;
- accepted survivors;
- repair continuation.

This permits exact reconstruction of what produced a given candidate.

### L. Coherence group

"Generate four pages together" is a production requirement about shared context and
coherence, not necessarily a claim about one particular API-call shape.

Represent the booklet as one coherence group:

FICK:P1..P4

The renderer adapter may realize the group through a native multi-output operation or
another tightly coupled execution path, provided the four pages consume the same frozen
bundle and shared context.

The required output remains four distinct full-size page objects.

## Required architecture layers

### Layer 1 — authoritative upstream state

Owned elsewhere:

- exact copy;
- route / learner architecture;
- exact artifacts;
- product acceptance.

### Layer 2 — editable generation package

Owns:

- target binding;
- coherence/batch contract;
- page contracts;
- content references/bindings;
- layout;
- visual obligations;
- style;
- asset/reference roles;
- constraint/freedom registry;
- realization plan;
- overflow policy;
- render acceptance.

### Layer 3 — preflight/compiler

Owns:

- readiness validation;
- reference resolution;
- compatibility validation;
- compilation.

### Layer 4 — immutable render bundle

Owns:

- exact renderer-ready resolved execution state.

### Layer 5 — run/output state

Owns:

- actual render execution record;
- outputs;
- verification;
- survivor freeze;
- repair continuation.

## Current package assessment

The existing
`generation/PRODUCTION_PACKAGE_CANDIDATE.yaml`
already contains valuable state and remains the correct package candidate.

It must not be replaced by a parallel package.

It is incomplete relative to the architecture above.

Therefore its correct current status is:

ARCHITECTURE_REPAIR_REQUIRED / RENDER_BLOCKED.

## Repair completion condition

The current candidate can return to ordinary assembling/freeze review only after the
missing architecture coordinates above have either:

- been represented directly;
- been delegated by explicit reference to an authoritative shared JHB production
  control; or
- been explicitly rejected as non-result-sensitive with grounds.

No render is authorized merely because copy/layout/style work appears visually complete.
