> STATUS: SUPERSEDED AS A PD EXECUTION RECORD on 2026-09-22.
>
> The analysis below contains useful observations, but it did not faithfully execute the current PracticalCore HF-001-first PD path and it encoded an incorrect universal one-page-per-call rule. See `audits/JHB_IMAGE_GENERATION_PRACTICALCORE_PD_CORRECTION_2026-09-22.md` and `projects/jewish-holiday-booklets/IMAGE_GENERATION_PROTOCOL.md` v0.2 for the corrected result.

# JHB Image Generation Triple PD Audit

Date: 2026-09-22
Scope: Jewish Holiday Booklet image-generation workflow, with immediate application to the current Fick / Difference revision.
Frozen target: produce the intended four-page booklet revision while preserving exact page identity, exact source lineage, exact student-facing content, cross-page sequence, and already-correct visual state.

## Audit 1 — Old recursive discovery audit

### Target result

A successful production run yields four distinct full-size pages, each performing its assigned booklet job, with only licensed changes applied to the current source pages and no silent regressions elsewhere.

### Recursive dependency chain

Reliable final page
→ correct page identity
→ correct source artifact
→ correct operation type
→ complete page specification
→ explicit protected state
→ explicit licensed delta
→ bounded generation unit
→ verification against invariants
→ acceptance or rejection before advancing.

### Deepest load-bearing findings

1. Too much required state has historically remained implicit in conversation.
   The generator receives prose describing intent, while exact text, layout, protected regions, semantic color mappings, page job, and source lineage remain only partially externalized.

2. The operation type has often been wrong.
   A local repair has been attempted through whole-page regeneration. This converts a bounded edit problem into a fresh sampling problem and reopens already-settled decisions.

3. The generation unit has not always been frozen.
   "Four-page booklet" has been interpreted as one four-page sheet, four miniature pages, or four variants of one page. Page identity and object cardinality need explicit representation.

4. Page correctness and booklet correctness are distinct.
   A locally attractive page can still violate the cross-page reveal sequence, duplicate another page's job, or leak a later concept early.

5. Verification has often occurred visually and informally after generation.
   Without an explicit acceptance matrix, attractive but semantically wrong renders can survive longer than they ought to.

### Recursive root cause

The recurring generator is not merely weak prompting. It is unrepresented production state.

The workflow has often relied on the model to reconstruct the authoritative source, infer what is protected, infer the requested delta, infer page identity, infer layout, and infer acceptance criteria at generation time.

That gives the generator unnecessary degrees of freedom exactly where the booklet requires preservation.

### Repair implied by Audit 1

Externalize the state before generation. No generation call occurs until the target page, page specification, protected elements, licensed delta, cross-page job, and acceptance conditions exist as explicit artifacts.

## Audit 2 — Five-lens orthogonal audit

### Lens 1 — Information loss

Natural-language prompts compress a large amount of page state.

Lost or weakened coordinates have included:
- exact wording;
- exact relative placement;
- image function;
- protected regions;
- page identity;
- cross-page handoff;
- color semantics;
- source lineage;
- acceptance conditions.

Control:
Use a structured page blueprint plus a preservation ledger and delta specification.

### Lens 2 — Inverse problem

A prompt such as "make this page about Fick's law and connection" admits many visually plausible solutions.

The user target is one narrow member of that solution space.

Control:
Reduce the admissible output space by anchoring to an exact source page, exact page blueprint, actual reference assets, and a list of forbidden changes.

### Lens 3 — Coordinate failure

Several distinct coordinates have repeatedly been collapsed:
- one page vs four pages;
- four sequential pages vs four variants;
- page image vs contact sheet;
- booklet revision vs fresh booklet;
- visual edit vs semantic redesign;
- local repair vs whole-page regeneration.

This explains the repeated "four pages on one page," "four thin pages," and "four versions of Page 1" failures.

Control:
Every call declares exactly one PAGE_ID and exactly one output page. Multi-page packaging occurs only after all four pages are independently accepted.

### Lens 4 — Selection effect

Visually polished renders can be selected even when they violate the teaching mechanism.

Common false positives:
- attractive decorative imagery with no instructional function;
- clean layouts that erase writing space;
- visually strong pages that leak later concepts;
- plausible scientific diagrams with incorrect semantic relationships;
- appealing color changes that break established mappings.

Control:
Acceptance is specification-relative, not beauty-relative.

### Lens 5 — Counterfactual history

Each regeneration can erase knowledge of how the current page was reached.

Without lineage, the system can:
- repair the wrong ancestor;
- reintroduce rejected elements;
- mistake a newer render for an accepted render;
- forget which regions were already approved.

Control:
Every production run binds to a registered source set and records its delta and result status.

## Audit 3 — PDAudit 1.1 result-sensitivity pass

### Result classes

PASS
- correct PAGE_ID;
- one full-size page;
- all protected elements preserved;
- licensed delta applied;
- exact text preserved or deterministically composited;
- page job and booklet handoff intact.

REPAIR_REQUIRED
- correct page exists but one or more invariants fail.

FAIL
- wrong source, wrong page, wrong generation unit, collapsed page sequence, substantial unlicensed redesign, or irrecoverable semantic loss.

### Coordinates tested

| Coordinate | Result sensitivity | Finding |
| --- | --- | --- |
| exact source identity | very high | wrong ancestor changes the entire repair result |
| page identity | very high | Page 1/2/3/4 confusion changes booklet structure |
| output cardinality/unit | very high | one page vs four-page sheet changes object class |
| operation mode | very high | local edit vs regeneration changes preservation risk |
| protected-elements ledger | very high | absence reopens settled decisions |
| licensed delta | very high | vague delta permits global redesign |
| exact text/layout specification | high | variation changes instructional content and readability |
| cross-page job/handoff | high | variation changes booklet causal sequence |
| semantic color/image mapping | high | variation can change meaning without obvious visual failure |
| acceptance matrix | high | absence allows false positives to survive |
| aesthetic adjectives | low to medium | affects style but rarely resolves the core failure |
| prompt length | low | longer prompts do not compensate for missing state |
| decorative detail | low | often increases noise rather than reliability |

### PDAudit result

The highest-sensitivity coordinates are structural controls, not prompt rhetoric.

The minimum useful intervention is not "write a much better prompt."

It is:
exact target + exact page unit + operation mode + page blueprint + preservation ledger + licensed delta + acceptance matrix.

## Combined conclusion

The recurring booklet-generation failure is a state-control problem expressed through an image generator.

A reliable workflow must separate:
1. what the booklet is;
2. what this page is;
3. what is already correct;
4. what is allowed to change;
5. how the change is rendered;
6. how the result is tested.

For the current Fick revision, the preferred mode is local editing of the registered current working pages whenever a usable page already exists. Full-page regeneration is reserved for a page whose whole visual solution is rejected.

## Required pre-generation artifacts

1. Exact Target Binding
   - booklet ID;
   - source-set ID;
   - PAGE_ID;
   - operation mode;
   - source locator/reference.

2. Booklet Route Map
   - one job per page;
   - what the learner knows entering each page;
   - what that page adds;
   - bottom question/handoff;
   - concepts forbidden from appearing early.

3. Series Style Contract
   - page dimensions/aspect;
   - margins;
   - type hierarchy;
   - illustration language;
   - source treatment;
   - logo treatment;
   - whitespace rules;
   - semantic color mappings.

4. Page Blueprint
   - every exact text string;
   - text hierarchy;
   - approximate region/bounding area for every text block;
   - every image/diagram;
   - image function;
   - image position and relative size;
   - writing/interaction space;
   - required empty space;
   - page-specific visual hierarchy.

5. Preservation Ledger
   - elements that are already correct;
   - regions that are locked;
   - text that cannot change;
   - colors/mappings that cannot change;
   - source/diagram relationships that cannot change.

6. Licensed Delta Specification
   - exact defects being repaired;
   - exact region each repair may touch;
   - replacement asset/content;
   - explicit "everything else unchanged" boundary.

7. Asset Pack
   - current source page;
   - approved reference images;
   - diagrams;
   - logo;
   - icons/illustrations actually intended for use;
   - no reliance on the generator to invent a substitute when an exact asset exists.

8. Acceptance Matrix
   - PAGE_ID correct;
   - exactly one full-size page;
   - exact text check;
   - locked-region check;
   - licensed-delta check;
   - science/source fidelity check;
   - page-job check;
   - cross-page handoff check;
   - color-semantic check;
   - whitespace/interaction-space check;
   - style-contract check.

9. Render Record
   - source set;
   - source page;
   - operation used;
   - delta applied;
   - accepted/rejected;
   - identified regressions;
   - next authorized move.

## Production rule

Do not generate the four-page booklet in one image-generation call.

Generate or edit exactly one identified full-size page at a time.

For an existing page with valuable correct content:
source page + bounded local edit + verification.

For a completely rejected page:
page blueprint + style contract + asset pack → fresh visual layer, followed by deterministic placement of critical text where exact typography matters.

After all four pages pass independently, package them into the four-page booklet.
