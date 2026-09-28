# Fick Exact-Copy Adaptive Wording Run — PD + ImprovementCore

Date: 2026-09-22
Project: jewish-holiday-booklets
Target: JHB:FICK:COPY:CANDIDATE:001
Target path: projects/jewish-holiday-booklets/fick/copy/EXACT_COPY_CANDIDATE.md
Initial target blob: 2207bf854626c53e675daed70b65d8c33f05a55b
Method: HF-001 recursive PD + orthogonal/result-sensitivity + source-boundary/non-regression + manual ImprovementCore
Mutation scope: exact-copy candidate and its identity bindings only until wording converges

## Step 1 — lock the exact stored wording object as the sole wording audit target

The wording audit target is the GitHub object at the path above, not chat history, a PDF,
a rendered page, a session capture, or the production package.

All wording findings must identify a defect in this stored object.

### Post-step PD + ImprovementCore rerun

HF-001:
The target identity is now explicit and recoverable. The prior failure mode of auditing
an informal reconstruction is removed.

ImprovementCore:
PROTECT
- exact-copy candidate remains editable;
- accepted repair baseline remains separate;
- production package may reference but not duplicate wording;
- no visual/layout work is authorized by this step.

LOCALIZE
The live frontier is wording quality inside the exact stored object.

SELECT
Run the strongest bounded wording audits against this exact blob.

RECOMPUTE
Step 2 survives unchanged.


## Step 2 — strongest wording audits on the stored object

Audits applied:
1. HF-001 learner-state / inferential-causation audit
2. A03/A04 orthogonal misreading + result-sensitivity audit
3. source-boundary + non-regression audit
4. ImprovementCore compression / strict-gain pass

### Page 1

Result: structurally sound.

The science wording preserves the needed distinction:
- Fick's First Law gives flux from the concentration gradient;
- the time-evolution sentence is framed as a simple setup rather than as a direct
  definition of Fick's First Law;
- the physics/human-domain boundary is explicit.

No wording repair is currently justified.

### Page 2

Defect P2-W1 — coordination collapses toward agreement/decision.

Current:
"WHAT DO WE ACTUALLY NEED TO DECIDE TOGETHER?"

This is result-sensitive because the booklet's central operation distinguishes agreement
from coordination.

Repair:
"WHAT DO WE ACTUALLY NEED TO COORDINATE?"
"What decision or action has to work together?"

Defect P2-W2 — source/application boundary is accurate but student-facing wording is
needlessly technical.

Current:
"Paraphrase. The tool below is our classroom application."

Repair:
"That is Rav Kook's idea. The questions below are our classroom tool."

The Rav Kook paraphrase itself remains within the source-supported claim that genuine
peace does not require uniformity and that different sides/opinions have their place.
The classroom coordination procedure remains explicitly ours.

Defect P2-W3 — redundant/over-broad closing sentence.

Current:
"A real difference can stay real without becoming distance."

This can be read as saying no real disagreement need ever affect relational distance.
That is stronger than the booklet establishes and duplicates the preceding relational
sentence.

Repair:
remove it.

Compression repair:
combine the two sentences beginning "Sometimes the hardest part..." without changing
the learner move.

### Page 3

Defect P3-W1 — the live prompts return to "shared decision" language and weaken the
coordination distinction.

Repair:
"DO WE NEED TO COORDINATE HERE?"
"CAN THIS STAY DIFFERENT?"

Debrief repair:
"WHERE DID WE HAVE TO COORDINATE?"

Transfer handoff:
"WHERE ELSE DO WE NEED TO COORDINATE, AND WHERE CAN WE STAY DIFFERENT?"

Defect P3-W2 — classroom-model rules are more verbose than their instructional load
requires.

Repair:
compress five rules to four while preserving:
- one shared structure;
- walls/opening/roof area representing schach;
- one shared material set;
- one completed shared model.

Source/application boundary remains unchanged.

### Page 4

Defect P4-W1 — different kinds of disagreement still need an explicit scope guard at
the point of independent transfer.

Repair:
add:
"Different disagreements can affect what people can do together in different ways."

Defect P4-W2 — "one decision or coordinated next step" is awkward and again treats
coordination as a near-synonym for a decision.

Repair:
"WHERE DO YOU ACTUALLY NEED TO COORDINATE A DECISION OR NEXT STEP?"

The dissolving-paper target survives unchanged because it correctly removes the demand
for total agreement rather than erasing either viewpoint.

### Source-boundary verification

External source verification during this audit supports:
- Fick's First Law as flux proportional to the negative concentration gradient;
- Sukkah 27b as the source of "all Israel are fit to sit/reside in one sukkah";
- Rav Kook, Olat Re'iyah I pp. 330-331 on Berakhot 64a, as rejecting uniformity as the
  necessary form of peace and describing different sides/opinions as having their place.

No source verification licenses attributing the four-question coordination tool to Rav
Kook or a conflict-resolution theory to Sukkah 27b.

### Post-step PD + ImprovementCore rerun

PROTECT
- Page 1 wording;
- Page 2 emotional hinge and pineapple discriminator;
- Page 3 source/application boundary and discovery-first debrief;
- Page 4 dissolving-paper mechanism;
- all four page handoffs.

LOCALIZE
The repairs are concentrated in one protected distinction:
coordination must not collapse back into agreement/decision language.

SELECT
Apply only P2-W1/W2/W3, P3-W1/W2, and P4-W1/W2 plus the stated compression.

EVALUATE
These repairs improve semantic precision and reduce text while preserving the learner
route and accepted emotional functions.

DISPOSE
Do not rewrite Page 1.
Do not perform a broad stylistic rewrite.
Do not add new examples or sources.

RECOMPUTE
Step 3 survives: edit the same exact-copy candidate in place, then rerun against the new
Git blob before touching identity bindings.


## Step 3 — apply justified wording repairs to the same stored candidate

Updated target blob:
d5e422c0e6b31509d71a827376898794708c4a7b

Applied only the repairs licensed in Step 2.

### Post-step PD + ImprovementCore rerun

HF-001 learner-state check:
- Page 1 still earns the human convergence question without answering it.
- Page 2 now names coordination directly rather than treating shared decision as the
  master category.
- Page 3 uses the same coordination operation during enactment and debrief.
- Page 4 now carries an explicit scope guard for materially different disagreements.
- The four-page route remains continuous.

A03/A04 misreading/result-sensitivity check:
- agreement and coordination are now less likely to collapse;
- Page 2 no longer implies that every real disagreement can remain without relational
  distance;
- Page 4 does not imply that all disagreement types have identical practical effects;
- no new source/application confusion was introduced.

ImprovementCore:
PROTECT
- the revised wording object itself;
- Page 1 unchanged;
- all source boundaries;
- the pineapple contrast;
- Page 3 discovery-first structure;
- Page 4 dissolving-paper target.

LOCALIZE
The next defect is not wording content. It is stale identity references: COPY_CONTROL,
Fick STATE, and the production package still point to the previous copy blob.

SELECT
Synchronize only those exact-copy identity bindings.

RECOMPUTE
Step 4 changes from "general identity update" to a bounded three-consumer blob update.
No further wording edit is licensed before synchronization.


## Step 4 — synchronize exact-copy identity consumers

Current exact-copy candidate blob:
d5e422c0e6b31509d71a827376898794708c4a7b

Updated exact-copy identity references in:
- projects/jewish-holiday-booklets/fick/COPY_CONTROL.yaml
- projects/jewish-holiday-booklets/fick/STATE.yaml
- projects/jewish-holiday-booklets/fick/generation/PRODUCTION_PACKAGE_CANDIDATE.yaml

Verification:
all three consumers now point to the current candidate blob.

Current visible-copy size:
- P1: 126 words
- P2: 238 words
- P3: 189 words
- P4: 168 words

### Post-step PD + ImprovementCore rerun

HF-001:
The source object and all known immediate consumers are now synchronized. The audit
target remains exact and recoverable.

No new identity or authority defect appears.

ImprovementCore:
PROTECT
- current synchronized candidate and bindings;
- no downstream production work yet.

LOCALIZE
The frontier returns to the revised wording itself and whether another audit cycle
produces a material repair.

SELECT
Run a fresh full wording audit on the new blob rather than assuming Step 2 findings
still exhaust the state.

RECOMPUTE
Step 5 survives exactly as intended.


## Step 5 — fresh full wording audit on the revised synchronized blob

Target blob:
d5e422c0e6b31509d71a827376898794708c4a7b

### HF-001 rerun

The learner-state sequence remains intact and no page now requires a structural rewrite.

Three small wording coordinates remain result-sensitive:

1. Page 2 heading "A BETTER WAY FORWARD" does not name the operation and introduces an
   unnecessary evaluative claim.
   Better functional heading:
   "TRY FOUR QUESTIONS"

2. Page 2 coordination subtext:
   "What decision or action has to work together?"
   remains grammatically awkward and can still pull the learner toward "decision" as the
   central category.
   Better:
   "What has to work together for the shared thing to happen?"

3. Page 4 transfer prompt:
   "WHERE DO YOU ACTUALLY NEED TO COORDINATE A DECISION OR NEXT STEP?"
   over-specifies the answer form and is less clean than the operation learned on
   Pages 2-3.
   Better:
   "WHAT DO YOU ACTUALLY NEED TO COORDINATE?"

No other wording defect currently changes the intended learner result.

### Orthogonal misreading check

The revised copy now protects:
- coordination != agreement;
- nonuniformity != equal truth of every view;
- sharedness has a concrete bearer;
- disagreement types can have different consequences;
- Sukkah 27b is not presented as a conflict-resolution theory;
- Rav Kook is not presented as author of the classroom procedure;
- diffusion is not presented as a normative human law.

### Compression / non-regression check

P2 remains the densest page because it performs the emotional problem, Jewish concept,
operational tool, and worked discriminator. Removing any of those functions would damage
the route.

The three edits above reduce friction without removing a load-bearing function.

### Post-step ImprovementCore

PROTECT
All current content except the three identified phrases.

LOCALIZE
Only three wording coordinates remain.

SELECT
Make those three edits.

EVALUATE
Strict gain:
- clearer operation naming;
- less agreement/decision slippage;
- cleaner transfer;
- no source or emotional loss.

DISPOSE
No further compression is licensed at this stage.

RECOMPUTE
Step 6 becomes one final micro-repair cycle followed by another full convergence audit.


## Step 6A — apply final micro-repairs

Updated candidate blob:
10547ab377d3855a85f6fafc0b2dbb96a192d5c0

Applied:
- "A BETTER WAY FORWARD" -> "TRY FOUR QUESTIONS"
- Page 2 coordination subtext -> "What has to work together for the shared thing to happen?"
- Page 4 transfer prompt -> "WHAT DO YOU ACTUALLY NEED TO COORDINATE?"

### Immediate post-edit PD + ImprovementCore rerun

HF-001:
The learner-state path remains unchanged.
The Page 2 tool now names coordination more cleanly.
The Page 4 transfer prompt now asks the learner to retrieve the learned operation rather
than a narrower decision-shaped version of it.

No new wording defect emerges from these changes.

ImprovementCore:
PROTECT
- current wording content;
- no additional stylistic optimization.

LOCALIZE
Known stale-copy identity consumers now point to the prior blob.

SELECT
Synchronize the three exact-copy identity consumers before declaring convergence.

RECOMPUTE
No further wording edit is authorized before identity synchronization.


## Step 6B — identity resync and full convergence audit

Current exact-copy candidate blob:
10547ab377d3855a85f6fafc0b2dbb96a192d5c0

Verified current candidate identity in:
- COPY_CONTROL.yaml
- Fick STATE.yaml
- PRODUCTION_PACKAGE_CANDIDATE.yaml

Current visible-copy size:
- P1: 126 words
- P2: 240 words
- P3: 189 words
- P4: 163 words

### Full HF-001 convergence rerun

Page 1:
No unresolved wording defect changes the learner transition.

Page 2:
The emotional problem, Rav Kook source boundary, coordination operation, and worked
discriminator are all present. Removing another major block would remove a distinct
load-bearing function. The page is text-dense, but the remaining density is a layout
problem unless later visual preflight demonstrates fit failure.

Page 3:
The source/application boundary is explicit. The activity instructions create one shared
structure with real decision pressure. The live prompts use coordination rather than
agreement. The debrief still requires student inference rather than supplying the answer.

Page 4:
The disagreement-type scope guard is explicit. The scaffold is reduced. The transfer
prompt retrieves the coordination operation. The dissolving-paper action removes the
demand for total agreement rather than either position.

Cross-page:
- P1 question is earned;
- P2 supplies the operation;
- P3 enacts it;
- P4 transfers it;
- coordination no longer collapses into agreement/decision language;
- no later-page conclusion leaks materially backward;
- source claims and educational applications remain separated.

### ImprovementCore convergence rerun

PROTECT
All current wording.

LOCALIZE
No demonstrated wording defect remains whose repair has a strict gain without opening a
new content/design question.

SELECT
Stop wording mutation.

GENERATE
Candidate successors:
A. continue polishing copy;
B. freeze immediately without user seeing the revised copy;
C. declare wording candidate converged and route to explicit wording-approval gate.

EVALUATE
A risks optimization drift.
B violates COPY_CONTROL's explicit wording-approval rule because the current wording was
modified after the user's last approval of the workflow.
C preserves both convergence and authority.

DISPOSE
A and B rejected.

RECOMPUTE
Step 7 is now an explicit approval gate, not an autonomous mutation.

## Step 6 result — wording convergence

JHB:FICK:COPY:CANDIDATE:001 is converged for the current analytic frame.

This means:
- no further wording edit is currently licensed by the audits;
- it remains editable if a later audit or user review finds a defect;
- it is not yet frozen.

## Step 7 — freeze gate

Status: WAITING_FOR_EXPLICIT_WORDING_APPROVAL

Reason:
The exact wording changed during Steps 3 and 6. Agreement to run this seven-step process
does not by itself establish approval of wording that did not yet exist at the time of
that agreement.

On explicit approval of the current exact wording:
1. create immutable copy/EXACT_COPY_v1.md from the exact current candidate bytes;
2. record its immutable Git blob in COPY_CONTROL.yaml;
3. bind Fick STATE and the production package to the frozen object;
4. rerun HF-001 + ImprovementCore before selecting the next production step.
