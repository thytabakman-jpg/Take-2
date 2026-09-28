# Fick Production Closure — Three-Object PD Audit

Date: 2026-09-22
Project: jewish-holiday-booklets
Booklet: fick_difference
Scope: generation requirements + exact-copy control + visual-job requirements
Mode: booklet-local architecture diagnosis and bounded control improvement

## Frozen audit targets

### Object A — generation problem

Primary evidence:
- projects/jewish-holiday-booklets/evidence/JHB_IMAGE_GENERATION_CONVERSATION_CAPTURE_2026-09-22.md
  blob: f619a29641d33b1c34b3200715c3749dcb39dc07
- projects/jewish-holiday-booklets/IMAGE_GENERATION_PROTOCOL.md
  blob: 9ab84b530dab34462ccfcfda81b9e4d84ecc696d

Problem represented:
The generator needs an explicit production contract for four distinct full-size pages,
shared booklet context, output topology, page identity, preservation/salvage, assets, and
two-level verification.

### Object B — text problem

Primary controls:
- projects/jewish-holiday-booklets/fick/COPY_CONTROL.yaml
  blob: 55a00c08ace602c1f0a12582b40ea1e43a056066
- projects/jewish-holiday-booklets/fick/copy/EXACT_COPY_CANDIDATE.md
  blob: 2207bf854626c53e675daed70b65d8c33f05a55b

Problem represented:
The exact words need one durable authoritative object, candidate/frozen identity,
immutable promotion, and a rule preventing later rendering from reconstructing or
rewriting the copy.

### Object C — visual-job problem

Primary evidence:
- projects/jewish-holiday-booklets/fick/SESSION_CAPTURE_2026-09-22.md
  blob: 36e23b44370bd52b464076c337ecb3ca550a7889

Problem represented:
Each page needs explicit image function, text-image division of labor, eye path, layout,
whitespace/activity space, cross-page visual continuity, preservation obligations, and
render-specific acceptance.

## Audit 1 — A18 / HF-001 old recursive PD audit

### Initial representation

The project currently describes three apparent problems:

1. how to generate the four pages reliably;
2. where to store and freeze the exact words;
3. where to store and freeze the visual jobs.

The historical sequence made these look like three independent systems because each
failure was discovered at a different time.

### Recursive dependency reconstruction

Generation cannot be made reliable without knowing:
- the exact target booklet and page identities;
- the exact words to render;
- the visual job of each page;
- the layout and hierarchy needed to realize that job;
- the shared booklet style;
- exact assets where identity matters;
- output topology;
- page/set acceptance;
- what survives partial success and how repair is localized.

The text system alone cannot make a page.
The visual system alone cannot make a page.
The generation protocol alone cannot determine what content or visual relations it is
supposed to preserve.

All three therefore converge on the same downstream transition:

AUDITED LEARNING DESIGN
-> CLOSED PRODUCTION INPUT
-> RENDER
-> VERIFIED ARTIFACT

The hidden missing node is CLOSED PRODUCTION INPUT.

### Historical-causation result

The recurring failure family is best explained by incomplete production closure.

When a production coordinate is missing, the render stage silently reconstructs it.

Examples:
- missing exact-copy binding -> rewritten or omitted text;
- missing visual-function binding -> decorative imagery;
- missing layout binding -> hierarchy/whitespace drift;
- missing output-topology binding -> contact sheet / miniatures;
- missing page-identity binding -> repeated Page 1 variants;
- missing style binding -> cross-page drift;
- missing preservation/delta binding -> local edit causes global redesign;
- missing acceptance binding -> attractive but instructionally wrong render survives.

### HF-001 conclusion

The three observed problems are not three peer systems.

They are three views of one missing production-closure object.

The correct parent is a Fick Production Package.

The exact copy remains an upstream authority and is referenced, not duplicated.
Visual/layout/style/generation instructions are production coordinates and belong inside
the package boundary.

## Audit 2 — A03 representation attack + A04 result-sensitivity

### Representation attack

The same work can be represented as three files or as one render function.

The more discriminating representation is:

P = <T, C, R, V, L, S, A, O, Q, X>

where:

T = exact target / source-set / page-identity binding
C = exact-copy reference and immutable identity
R = four-page route and page-job constraints
V = visual-function specification
L = layout / hierarchy / whitespace / interaction-space specification
S = shared style and semantic visual grammar
A = exact asset references
O = generation episode and output-topology contract
Q = page-level and set-level acceptance
X = preservation / salvage / repair contract

A render request is not READY merely because some coordinates exist.

### Result-sensitive coordinates

Critical:
- C exact-copy identity;
- distinct P1/P2/P3/P4 identity;
- V page-specific visual job;
- L hierarchy/space relationships;
- O four-separate-full-size-page topology;
- S shared booklet grammar;
- Q two-level acceptance;
- X partial-success preservation and local-repair scope.

High:
- R page-entry/handoff/forbidden-reveal structure;
- A exact asset identity where an exact asset already exists.

Lower leverage by itself:
- prompt verbosity;
- decorative adjectives;
- repeated natural-language requests to "keep it consistent."

### A03/A04 conclusion

The project does not need three independent control planes.

It needs one atomic production contract whose fields remain typed.

"One piece" is therefore correct at the package level, but wrong if it means flattening
all information into one undifferentiated prompt.

The package must preserve typed coordinates inside one operational object.

## Audit 3 — A13 layered-control-map audit

### Required layers

Layer 1 — learner / booklet architecture
Authority remains in series and Fick state/control.
Job: why the pages exist and what learner transition they create.

Layer 2 — exact copy
Authority remains in COPY_CONTROL + immutable exact-copy snapshots.
Job: exactly what the student reads.

Layer 3 — production package
New parent production object.
Job: bind the frozen copy to route, visuals, layout, style, assets, output topology,
acceptance, and repair behavior.

Layer 4 — rendered artifacts
Authority remains in artifact identity / lineage records.
Job: what was actually produced.

Layer 5 — product acceptance
Authority remains in ACCEPTANCE.yaml.
Job: whether the repaired booklet is accepted.

### Layer-collapse findings

Do not merge exact-copy authority into the generation package.
That would recreate duplicate text authority.

Do not make a separate VISUAL_CONTROL peer unless evidence later shows the visual
specification needs an independent lifecycle outside production.
At present, visual jobs, layout, style, and generation constraints all become meaningful
as a single production contract.

Do not make the rendered artifact itself the source of truth for either text or visual
intent.

### Representation gap found

The project currently has:
- a real exact-copy control;
- a general generation protocol;
- visual-job knowledge in session/evidence captures.

It lacks the one Fick-local object that closes those inputs for rendering.

That is the live representation gap.

## Unified solution

Create one Fick-local Production Package candidate.

Recommended path:

projects/jewish-holiday-booklets/fick/generation/PRODUCTION_PACKAGE_CANDIDATE.yaml

The package owns:
- exact target binding;
- exact-copy REF + blob, never duplicated copy;
- page jobs and route constraints needed for rendering;
- per-page visual jobs;
- per-page layout specs;
- shared style contract;
- asset manifest;
- coordinated-batch topology;
- page/set acceptance;
- post-render survivor preservation;
- local-repair contract.

The package does NOT own:
- the canonical wording itself;
- artifact acceptance;
- product acceptance;
- the full curriculum architecture.

## Lifecycle

Mutable candidate:
PRODUCTION_PACKAGE_CANDIDATE.yaml

When complete and explicitly approved:
create immutable versioned snapshot such as
PRODUCTION_PACKAGE_v1.yaml

Do not convert the candidate path into the frozen object merely by changing a status
label.

## Readiness condition

A Fick generation episode is READY only when:

- exact-copy binding points to a frozen immutable copy;
- all four PAGE_IDs are distinct and bound;
- all four visual-job specs are complete;
- all four layout specs are complete;
- shared style/visual grammar is complete enough for generation;
- required assets are resolved;
- output topology is explicit;
- page-level acceptance is explicit;
- set-level acceptance is explicit;
- operation mode is selected.

Until those conditions hold, the package may be assembled and audited but must not
authorize rendering.

## Consequence for the previously proposed VISUAL_CONTROL

The earlier proposal for:

- visuals/VISUAL_SPEC_CANDIDATE.md
- VISUAL_CONTROL.yaml
- generation/PACKAGE.yaml

is over-decomposed for the current task.

The stronger current design is:

- exact-copy authority remains separate;
- one Fick Production Package contains the visual/layout/style/generation coordinates;
- the package references the frozen copy;
- the package is frozen atomically before rendering.

This reduces synchronization surfaces without collapsing semantic roles.

## Terminal result

The three dumped pieces do have a common parent.

They are not three production problems.

They are missing coordinates of one production-closure object.

Recommended immediate implementation:
1. create the Fick Production Package candidate now;
2. bind it to the current exact-copy candidate while marking render blocked;
3. place the known page visual jobs in the package;
4. leave unresolved layout/style/asset coordinates explicitly OPEN;
5. after wording approval, bind the immutable frozen exact copy;
6. finish visual/layout/style fields;
7. audit and freeze the package;
8. render from the frozen package only.
