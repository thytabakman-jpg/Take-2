# Jewish Holiday Booklet Image-Recovery Conversation Audit

Date: 2026-09-22  
Scope: the full ChatGPT conversation around recovering the Fick / Difference, Keva / Practice, and Conservation / Boundaries booklet images, including the tools used, the repeated ZIP attempts, the GitHub control state, and the user's corrections.

## Executive result

The dominant failure was not image quality. It was target identity.

The user was trying to recover the actual historical image-generation lineages that function as the booklet pages, in the same sense that the Yom Kippur booklet exists as four polished standalone page images. The assistant repeatedly substituted neighboring tasks: generate similar pages, choose the conceptually strongest version, choose the newest coherent version, or choose the GitHub-authoritative baseline. Those selectors can all produce plausible artifacts while still missing the exact lineage the user means.

The correct recovery problem is therefore:

1. freeze the intended booklet-lineage identity;
2. use user-recognized images as anchors;
3. search the ChatGPT image Library around those anchors;
4. reconstruct page families and revision neighborhoods;
5. preserve uncertainty when an exact lineage is not recovered;
6. package only after identity is sufficiently established.

## What the user was actually asking for

The target evolved in wording but was stable in substance:

- recover the actual image files that constitute the three Sukkos booklets;
- do not regenerate replacements;
- do not treat PDFs as source authority;
- treat the Yom Kippur booklet as the model of what kind of object is being recovered: four polished standalone booklet-page images;
- use the image-generation Library as the primary historical corpus;
- distinguish current/intended lineage from merely recent, high quality, conceptually strong, or GitHub-authoritative artifacts;
- when exact identity is unresolved, say that it is unresolved instead of filling the gap;
- keep strong unused image work separately so it is not lost.

The latest user correction adds an important state update:

- the previously packaged Fick Page 3 was wrong;
- Fick Pages 1, 2, and 4 also require confirmation rather than assumption;
- the correct Fick images may already be among the previously labeled high-quality unused images;
- Keva may genuinely lack a recoverable exact set at present;
- Conservation must be recovered by matching the visual/image lineage of the uploaded anchor, not by choosing any conceptually related Conservation branch.

## Tool-by-tool audit

### 1. Image generation

Tool behavior: image generation was invoked after the user uploaded Fick and Conservation pages and said the target images would look like those examples.

Result: failed task selection.

Why it failed:
The uploaded pages were retrieval anchors and visual fingerprints, not requests to make new pages. The assistant interpreted "look kind of like this" as a production specification rather than an identification clue.

Lesson:
When the task is historical artifact recovery, image generation is disallowed by task identity unless the user explicitly asks for replacement production. A reference image can specify what to search for without authorizing generation.

### 2. ChatGPT Library semantic search

Tool behavior: semantic searches were run for page titles, phrases, booklet names, and concepts.

What worked:
- exact or near-exact named assets could often be found;
- known phrases such as Fick titles, Keva headings, and Conservation headings helped surface relevant candidates;
- Library IDs and filenames were sometimes recoverable;
- it was useful for confirming that many candidate branches existed.

What did not work:
- semantic search was not exhaustive enough for image-lineage reconstruction;
- generic image-generation filenames were poorly represented by textual search;
- OCR/indexing on image-heavy artifacts was incomplete;
- semantically related but wrong branches ranked highly because their content was close;
- search result relevance did not establish parent/child revision lineage or booklet membership.

Lesson:
Semantic search is a discovery tool, not an authority or lineage selector.

### 3. Library listing by image type and creation time

Tool behavior: image files were enumerated across narrow date windows and sorted by creation time.

What worked:
This was substantially better for forensic recovery. It exposed clusters of image-generation runs, repeated four-page bursts, and neighboring variants that semantic search missed.

What did not work:
Chronological adjacency is only evidence, not proof. Different branches can be generated close together, and a later image can be a rejected experiment.

Lesson:
Creation time is useful for constructing candidate revision neighborhoods, but it must be combined with visual-family matching and user anchors.

### 4. Reading image-file metadata / extracted text

Tool behavior: image files were read to obtain filenames, timestamps, snippets, and extracted page text.

What worked:
- it identified page titles and some internal wording;
- it helped distinguish Fick, Keva, and Conservation branches;
- it provided lightweight triage before materialization.

What did not work:
- extracted text could not reliably capture visual lineage;
- visual design, layout, iconography, color grammar, and small copy differences are central to this task;
- reading content alone encouraged the assistant to select conceptually correct but visually wrong artifacts.

Lesson:
For a visual-artifact identity task, text extraction is supporting evidence only.

### 5. Materialization of Library assets

Tool behavior: selected Library image assets were materialized as raw files.

What worked:
This was one of the strongest tools in the workflow. It produced exact image bytes rather than reconstructed text, screenshots, or generated approximations. It also enabled later contact sheets, hashing, and ZIP construction.

What did not work:
Materialization faithfully retrieves whatever file was selected. It cannot correct an upstream identity mistake.

Lesson:
Materialization is the right transport tool once candidate identity is sufficiently grounded.

### 6. Direct visual inspection with image opening

Tool behavior: materialized images and contact sheets were visually inspected.

What worked:
This was the most important identification tool after user-provided anchors. It made visible that there were several distinct design families and that images with similar concepts could still belong to different booklet lineages.

What did not work:
Visual inspection was sometimes applied after the assistant had already framed the wrong candidate set. A contact sheet built from a biased candidate pool cannot recover omitted branches.

Lesson:
Visual inspection needs to happen before selection and packaging, not only as a validation after selection.

### 7. Contact sheets / inventories

Tool behavior: many candidate images were compiled into visual inventories.

What worked:
This greatly increased comparison bandwidth. It exposed coherent four-page sequences, repeated revisions, and visually distinct branches.

What did not work:
The contact sheets were not initially organized around explicit lineage hypotheses. They mixed "high quality," chronology, concept, and booklet family. This made it easy to mistake a coherent alternate branch for the intended one.

Lesson:
Contact sheets need grouping keys such as same generation burst, same navigation labels, same typography/layout grammar, same title family, and known anchor proximity.

### 8. GitHub connector and artifact registry

Tool behavior: GitHub files such as ARTIFACTS.yaml, STATE.yaml, MASTER_CONTROL.md, PROVENANCE.yaml, PracticalCore protocol files, and SORT_LATER.yaml were inspected.

What worked:
GitHub clarified several crucial distinctions:
- accepted individual page images outrank derived PDFs;
- PDFs and composites are derived;
- Fick had an exact historically accepted baseline registered;
- Keva exact source-set identity was explicitly unresolved;
- Conservation had no canonical rendered artifact;
- GitHub itself already documented the artifact-identity problem.

This was highly valuable structural information.

What did not work:
The assistant repeatedly treated "GitHub-authoritative historical baseline" as identical to "the exact image lineage the user currently wants." Those are different predicates. The latest user correction demonstrates that even a registered Fick accepted baseline does not automatically identify the current intended booklet lineage.

Lesson:
GitHub authority answers "what does the repository currently classify this as?" It does not automatically answer "which historical image run is the user pointing to now?" The backend needs separate fields for historical accepted baseline, current intended target, candidate successor, and rejected branch.

### 9. PracticalCore

The PracticalCore protocol was well matched to the problem. The task had exactly the conditions its protocol names:
- goal_or_task_ambiguity;
- representation_open;
- provenance_sensitive;
- history_reconstruction_needed;
- demonstrated_defect_with_repair_frontier.

What worked:
Its core principles were useful:
- freeze the target;
- preserve explicit constraints;
- expand only through result-sensitive dependencies;
- preserve OPEN coordinates;
- distinguish recommendation from mutation.

What did not work:
The assistant did not faithfully execute those principles. It repeatedly changed the target from "recover the intended historical booklet lineage" to "select the best/current/authoritative coherent set." It also prematurely closed unresolved coordinates by choosing a plausible Keva or Conservation set instead of returning OPEN.

This is a process failure, not evidence that PracticalCore is ineffective.

Lesson:
For artifact recovery, the TaskContract must explicitly name the identity predicate being recovered. "Ideal version" is too ambiguous unless decomposed into exact historical lineage, current authority, conceptual quality, visual quality, and user-recognized intended version.

### 10. ZIP construction

Tool behavior: Python/container tools built downloadable ZIPs with three or four subfolders.

What worked:
The mechanical packaging was reliable. Folder structures, individual PNG extraction, README files, and download artifacts were created correctly.

What did not work:
The ZIPs faithfully encoded upstream selection errors. Repackaging did not improve identity confidence.

Lesson:
Packaging is terminal. It must occur only after lineage adjudication, not as a way to force adjudication.

## Failure sequence across the conversation

1. The user reported that earlier handoff files contained the wrong images.
2. The assistant misread reference images as generation prompts and invoked image generation.
3. After correction, the assistant correctly reframed the problem as retrieval, but still mixed visual similarity, authority, and currentness.
4. A first Library search recovered many relevant images, but the assistant selected complete/coherent sets rather than first proving lineage identity.
5. PDFs were initially used for Keva despite the user's later explicit statement that PDF-derived artifacts were definitely wrong.
6. GitHub authority was consulted and correctly revealed Fick accepted pages plus unresolved Keva/Conservation states.
7. The assistant then over-weighted GitHub accepted status and under-weighted the user's direct visual recognition.
8. PracticalCore language was invoked, but the task contract was not frozen tightly enough and OPEN coordinates were repeatedly filled with guesses.
9. "High-quality unused" became a misleading category: some images were unused only because the prior selection logic was wrong, not because those images were inferior.
10. The user finally supplied a stricter identity criterion: these are the booklet images equivalent in kind to the Yom Kippur pages, Fick Page 3 is wrong, Pages 1/2/4 still need confirmation, Conservation has a visual anchor, and Keva may remain unrecovered.

## Root problems

### A. Predicate collapse

The conversation used terms such as:
- current;
- accepted;
- best;
- ideal;
- correct;
- high quality;
- latest;
- authoritative.

These were treated as interchangeable. They are not.

At minimum the system needs separate predicates for:
- historically accepted baseline;
- current repository authority;
- current user-intended lineage;
- newest generated artifact;
- strongest conceptual artifact;
- strongest visual artifact;
- candidate successor;
- rejected experiment.

### B. Research-object identity was under-specified

The object being recovered was not just "Fick Page 3." It was "Fick Page 3 belonging to the intended four-page booklet lineage." Page identity depends on set membership.

### C. The backend lacks a real image revision graph

The image Library contains many generated artifacts, generic filenames, timestamps, and partial text indexes, but no reliable parent/child graph connecting:
- generation run;
- revision;
- page number;
- booklet family;
- accepted/rejected state;
- replacement relation.

This forces forensic reconstruction.

### D. User recognition was not treated as highest-value evidence

When the user said an earlier Fick set looked accurate, that evidence needed to constrain subsequent searches. Instead, later backend evidence overrode it.

### E. OPEN was treated as failure rather than a valid result

For Keva especially, the correct result may be "not yet recovered." PracticalCore explicitly licenses OPEN, but the workflow repeatedly guessed to avoid an incomplete package.

### F. Visual evidence was downstream instead of upstream

The task was visual identity recovery, but semantic and architectural reasoning often happened before visual-family matching.

### G. Historical baseline and intended successor were conflated

GitHub's Fick baseline can be perfectly valid as a historical accepted repair baseline while still not being the image set the user now wants to recover. The registry needs both relations.

## What worked best

The strongest combined workflow was:

user-provided visual anchor
-> narrow Library enumeration
-> materialize raw images
-> build same-session / same-family contact sheets
-> direct visual comparison
-> consult GitHub only to understand authority and known uncertainty
-> keep unresolved coordinates open
-> package after confirmation.

The weakest workflow was:

conceptual description
-> semantic search
-> choose coherent/high-quality/latest set
-> package
-> ask whether it looks right.

## Recommended recovery protocol for the next attempt

### Step 1: Freeze the TaskContract

Target:
Recover the exact intended historical four-page image lineage for each Sukkos booklet, equivalent in artifact kind to the Yom Kippur four standalone page images.

Protected constraints:
- image-native source pages;
- no regeneration;
- no PDF-derived substitution;
- same four-page lineage;
- user-recognized visual family;
- do not replace uncertainty with a plausible candidate.

Known anchors:
- Yom Kippur four-page booklet as the artifact-type benchmark;
- user-uploaded Conservation page as a Conservation lineage anchor;
- user correction that prior Fick Page 3 is wrong;
- prior Fick files that the user said looked accurate remain evidence but all pages now require confirmation;
- Keva exact lineage may remain OPEN.

### Step 2: Recover lineages, not isolated pages

For each anchor:
- search exact visible phrases;
- enumerate image-generation assets in the surrounding time window;
- identify same-session bursts;
- materialize all plausible neighbors;
- create contact sheets grouped by generation burst and visual family;
- infer candidate page order only within a family.

### Step 3: Use explicit confidence states

For every page:
- CONFIRMED_BY_USER;
- STRONG_LINEAGE_MATCH;
- CANDIDATE;
- OPEN;
- REJECTED.

Do not ZIP a page as "final" merely because it is strongest among candidates.

### Step 4: Ask the smallest possible confirmation question

When two or more plausible candidates survive, present a numbered contact sheet and ask which family/page is the remembered one. Do not continue with another global scan.

### Step 5: Repair the backend later

Candidate backend changes:
- booklet_lineage_id;
- page_set_id;
- generation_run_id;
- page_number;
- parent_asset_id;
- supersedes;
- derived_from;
- visual_family_id;
- historical_acceptance_status;
- current_user_intended_status;
- current_repository_authority;
- rejection_reason;
- exact Library asset ID;
- timestamp and SHA-256.

The critical architectural repair is to stop using one "authority/status" field to answer several different identity questions.

## PracticalCore finding

The conversation is a direct case where PracticalCore's unresolved-coordinate discipline matters. The correct system behavior is not always "find the best answer"; it is "identify which coordinate is actually unresolved, refuse substitution across predicates, preserve the known-good behavior and user anchors, and narrow the next evidence request."

## Final audit result

The tooling was mostly capable enough. The main failure was semantic control: the assistant repeatedly asked the tools the wrong question.

The image Library, raw-file materialization, direct visual inspection, contact sheets, and GitHub registry together can support recovery. The workflow fails when "recover the user's intended historical image lineage" is replaced by "select a strong/accepted/recent coherent artifact," or when unresolved lineage is silently converted into a selection.
