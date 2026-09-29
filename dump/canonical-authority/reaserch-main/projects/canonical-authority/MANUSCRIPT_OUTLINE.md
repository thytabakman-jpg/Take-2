# Canonical Authority Manuscript Outline

Status: LIVE WORKING MANUSCRIPT ARTIFACT
Date: 2026-09-24
Authority: derived manuscript-planning object
Research owner: RESEARCH_ARCHITECTURE.yaml
Stable argument identity: SPINE.yaml
Reader dependency control: SPLINE.yaml
Manuscript admission control: MANUSCRIPT_CONTRACT.md

## Purpose

This is the live construction artifact for the article.

The manuscript has two simultaneous jobs:

1. perform the load-bearing argument;
2. move the reader through the epistemic states required to understand, test, and evaluate that argument.

Backend structure is not copied into the article one object per section. A backend distinction earns reader-visible space only when the reader needs that distinction at that point in order to make the next warranted move.

## Protected macro identity

```
A -> Q -> H[F] -> R -> B -> C
```

Current reader-facing method refinement:

```
A -> Q -> PROFILE(H[F]) -> TRACE -> DISCRIMINATE -> RECOGNIZE
  -> [COMPOSE only when several completed grounds materially require it] -> C
```

Current realized fixed-case path:

```
A -> Q -> PROFILE -> package-TRACE obstruction -> bounded C_case
```

The manuscript must not narrate DISCRIMINATE, RECOGNIZE, or COMPOSE as evidential stages successfully traversed by the fixed case while the package-TRACE obstruction remains.

## Reader-unit grammar

Every major section, subsection, and page-sized intellectual unit is evaluated as:

```
U_i =
<Job | ReaderIn | LiveQuestion | Material | Inference | ReaderOut | NextQuestion>
```

A unit passes only when both conditions hold:

```
ArgumentJob(U_i) = satisfied
ReaderTransition(U_i) = satisfied
```

For each unit ask:

1. What job does this unit perform for the paper?
2. What does the reader know or expect on entry?
3. What live question is now active for the reader?
4. What is the minimum material required here?
5. What inference is the reader now licensed to make?
6. What changes in the reader's model?
7. Why does the reader need the next unit?

A unit is defective when it performs a repository or taxonomy job that the reader does not need, when it asks the reader to accept an inference before its basis is visible, or when it repeats setup already completed upstream.

# Current candidate manuscript architecture

## 1. The Disagreement and the Question

### Job

Make the exact disagreement visible and convert it into the paper's truth-directed third-party problem.

### Reader transition

```
"Rashi and Ramban disagree"
->
"I can state the incompatible propositions and see why shared canonical standing
does not answer which claim is true."
```

### Required movements

1. Put Genesis 1:1 and the exact proposition pair in front of the reader.
2. Distinguish factual disagreement from disagreement about practice, legitimacy, provenance, or interpretation generally.
3. State the bounded second-order task.
4. Introduce the later-evaluator question.

### Earned inference

```
Shared canonical standing != proposition-specific truth adjudication.
```

### Exit state

The reader knows exactly what has to be explained and what the paper is not attempting to decide.

### Next live question

How can unlike Jewish authority and knowledge structures be compared without pretending they all do the same thing?

---

## 2. Fixing the Target and Defining the Comparison

### Job

Give the reader a principled comparison frame and explain why these source structures are in the comparison without claiming exhaustive coverage.

### Reader transition

```
"These mechanisms look heterogeneous"
->
"I see the common target that makes comparison possible, the differences the
comparison preserves, and the bounded rule by which the corpus is admitted."
```

### Required movements

#### 2.1 One Fixed Target

Hold the rival proposition pair fixed while allowing the mechanisms to remain heterogeneous in native function.

Earn:

```
common target != common native function.
```

#### 2.2 What Counts as Success?

Distinguish descriptive truth from legitimacy, bindingness, provenance, explanation, authentication, institutional settlement, and other outputs.

Earn:

```
success at one output type does not automatically answer another.
```

#### 2.3 Why These Seven Mechanisms?

Explain the purposive, non-exhaustive admission basis for H.

The reader needs to know:

- what differentiates the admitted mechanism families;
- why each is relevant to the fixed question;
- what coverage is actually claimed;
- what remains outside the present corpus;
- why failure inside H does not license a universal negative.

Corpus admission is a research-scope operation. It is not the same thing as the later admissibility of a multi-source package inside TRACE.

### Contribution earned

Fixed-target heterogeneous comparison.

### Exit state

The reader knows what is being compared, why comparison is legitimate, and how strongly conclusions may generalize from the admitted corpus.

### Next live question

What does each admitted structure actually establish before anyone tries to use it on the Genesis 1:1 target?

---

## 3. What the Sources Actually Do

### Job

Complete PROFILE: reconstruct each relevant structure in native context so that later target-transfer claims cannot trade on vague authority language.

### Reader transition

```
"I know which structures are being compared"
->
"I know what each structure natively supplies and where source content ends."
```

### Required movements

Organize source material by the inferential job it can actually perform rather than by prestige or traditional label alone.

For each relevant structure expose only the reader-needed coordinates:

- source-attributable content;
- bearer where material;
- native domain;
- native function;
- provenance/authenticity where material;
- route-specific commitments.

The source families may include pluralism/determination, protected reception, authority/error, authenticated prophecy, Ramban's creation tradition, loss/reconstruction, and generational hierarchy. Individual modules receive space in proportion to their argumentative role, not equal treatment by default.

### Critical boundary

Complete PROFILE here.

Do not reintroduce PROFILE as an adjudicative stage in Section 4.

### Earned inference

```
NativeSuccess(h) does not entail TargetSuccess(h,tau).
```

The reader can now identify where a source-native claim ends and where a project-level bridge would have to begin.

### Exit state

The reader is ready to inspect source-to-target transfer rather than generic authority status.

### Next live question

What exactly has to happen for one of these typed source structures to give grounds concerning the fixed rivals?

---

## 4. From Source to Ground

### Job

Give the reader the minimal adjudicative engine after typed setup.

### Reader transition

```
"I can see the source outputs"
->
"I can test whether a source package actually yields evaluator-usable grounds
for one rival over the other."
```

### Method sequence

```
TRACE -> DISCRIMINATE -> RECOGNIZE
```

PROFILE is presupposed setup, not another success conjunct.

#### 4.1 TRACE: Does the Source Reach the Target?

Ask whether an independently admissible source package supplies a licensed, source-attributable path from its typed outputs to the fixed truth target.

Several sources may jointly establish one ground. Singleton routes remain the one-member special case.

#### 4.2 DISCRIMINATE: Does the Ground Favor One Rival?

Ask whether the traced relation creates rival-specific truth-directed asymmetry.

Truth relevance without asymmetry is insufficient.

#### 4.3 RECOGNIZE: Can the Evaluator Use It?

Ask whether evaluator e has warranted grounds to identify, authenticate, and rely on the discriminator.

Keep source-side discriminatory support distinct from evaluator uptake.

### Compact formalization

```
SourceGround(X,tau,Delta)
iff TRACE(X,tau,Delta) and DISCRIMINATE(Delta,tau)

Usable_e(Delta,tau)
iff RECOGNIZE_e(Delta,tau)
```

### When Grounds Conflict: The COMPOSE Boundary

Introduce COMPOSE only as the downstream question that arises when several completed grounds exist and materially conflict.

```
package TRACE != COMPOSE
```

Package TRACE uses several source structures to establish one ground.

COMPOSE operates over several already-completed grounds.

Do not give COMPOSE standalone section weight unless actual drafting demonstrates that the reader cannot understand the case-selection boundary without it.

### Contribution earned

TRACE / DISCRIMINATE / RECOGNIZE method, with conditional composition boundary.

### Exit state

The reader has an explicit success test and understands what would count as a source-grounded discriminator.

### Next live question

Can this method succeed in principle, and where does the actual Rashi-Ramban case stop?

---

## 5. Testing the Method: Positive Control and the Rashi-Ramban Case

### Job

Demonstrate that the framework permits success, then apply it to the current corpus and localize the actual obstruction.

### Reader transition

```
"I understand the test"
->
"I see that the test is not rigged against religious authority, and I can see
the exact point at which this case fails."
```

### Required movements

#### 5.1 Can the Method Succeed? Authenticated Prophecy

Use authenticated prophecy to demonstrate in-principle truth-directed success when target coverage, discrimination, and evaluator warrant are actually present.

The point is possibility, not a claim that prophecy resolves the present case.

#### 5.2 Ramban's Creation Tradition: The Strongest Case-Proximate Route

Use Ramban's creation tradition to show why proximity to the topic still does not establish that the received/esoteric content includes the exact proposition I_S.

#### 5.3 Can Incomplete Routes Combine?

Show that the earlier singleton-only obstruction was too strong in general, then use the repaired package-aware analysis.

#### 5.4 Where the Case Stops: Package-Level TRACE

```
For all currently admitted independently admissible packages X,
TRACE(X,I_S,Delta) does not complete.
```

Therefore the realized evidential path is:

```
PROFILE -> TRACE obstruction -> bounded C_case
```

DISCRIMINATE, RECOGNIZE, and COMPOSE remain downstream general-method possibilities rather than successfully realized steps in this case.

### Contribution earned

Bounded Rashi-Ramban result.

### Exit state

The reader understands both the framework's openness to success and the exact reason the current case remains unresolved.

### Next live question

What does this failure pattern reveal about claims of religious authority more generally?

---

## 6. Authority Across Targets

### Job

Derive the broader implication from the worked comparison without turning the case into a universal theory of religious authority.

### Reader transition

```
"I know what happened in this case"
->
"I understand the general transfer problem and why authority is target-relative
and attribution-sensitive."
```

### Required movements

1. Compare the different native outputs exposed in Section 3.
2. Show that status or native success does not itself transfer epistemic force to a distinct truth target.
3. Show that bridge information and selector information must be attributed to the layer that supplies them.
4. Preserve the distinction between source-grounded support and evaluator-indexed usability.
5. Explain the role of conditional composition when several completed grounds exist.
6. Keep etic scholarly analysis distinct from endorsing the emic truth premises being analyzed.

### Earned implication

```
Authority(h,target_1) does not imply Authority(h,target_2)
without a licensed target relation.
```

and

```
Verdict differences generated by added bridge/composition machinery
cannot be attributed to fixed source content alone.
```

### Contribution earned

Target-relative and attribution-sensitive account of authority transfer.

### Exit state

The reader can state the broader payoff and also state exactly what the case does not establish.

### Next live question

What is the final contribution package, how far does it reach, and what remains open?

---

## 7. What the Analysis Establishes

### Job

Compress the paper into the strongest defensible contribution hierarchy and leave the reader with the exact result rather than repository architecture.

### Reader transition

```
"I have traversed the argument"
->
"I can state the paper's problem, method, bounded result, broader implication,
novelty, and limits in the correct dependency order."
```

### What the Paper Contributes

```
CORE METHOD
  fixed-target heterogeneous comparison
    -> TRACE / DISCRIMINATE / RECOGNIZE

WORKED RESULT
  method + current admitted corpus
    -> bounded package-TRACE obstruction

CONDITIONAL LIMIT
  multiple completed conflicting grounds
    -> COMPOSE / defeat requirement

DERIVED SIGNIFICANCE
  native-function differences + transfer/attribution analysis
    -> target-relative, attribution-sensitive authority
```

### What Is New Here

Do not make the conclusion carry the entire novelty burden.

Nearest-neighbor positioning enters earlier where the method or contribution first becomes intelligible. This section consolidates the bounded intersection claim:

the contribution lies in the combined fixed-target source-trace, rival-discrimination, evaluator-uptake, conditional composition, and attribution architecture, not in claiming each component as individually unprecedented.

### Scope and Limits

Preserve explicitly:

- purposive non-exhaustive corpus;
- no universal negative about Jewish tradition;
- fixed worked case rather than representativeness claim;
- first-order grammatical verdict outside current scope;
- future source recovery can revise the bounded case result;
- validation, general method, case result, disciplinary implication, and publication positioning are different evidence layers.

### Final reader state

The reader can recover the argument without repository terminology and can identify both the paper's strongest claim and the precise conditions under which that claim would change.

# Page-sized intellectual movement rule

During drafting, each section is decomposed into page-sized or subsection-sized movements.

For every movement record:

```
JOB
What does this page/unit accomplish for the manuscript?

READER IN
What does the reader currently believe, understand, or still need?

LIVE QUESTION
What question is active now?

MATERIAL
What is the minimum evidence/concept required here?

MOVE
What inference or distinction does the reader make?

READER OUT
What can the reader now understand, reject, or test that they could not before?

PULL
Why does the next unit now matter?
```

A page/unit is cut, merged, or moved when its job duplicates another unit, its material arrives before the reader has a use for it, its inference is not earned, or its exit state does not create a meaningful next dependency.

# Cross-cutting rails

The following remain necessary to manuscript quality but are not serial sections of the substantive argument:

- source and edition control;
- provenance;
- corpus-admission evidence;
- nearest-neighbor literature;
- validation/holdout evidence;
- novelty calibration;
- manuscript clarity/recoverability;
- journal framing.

These rails enter the manuscript at the smallest point where the reader needs them.

# Immediate execution frontier

1. Stress-test this seven-section candidate against SPINE.yaml, SPLINE.yaml, MANUSCRIPT_CONTRACT.md, DISCOVERY_MAP.yaml, and NOVELTY_CONTRIBUTION_MAP.md.
2. Build a section-by-section source/evidence matrix.
3. Decompose Sections 1-7 into page-sized intellectual movements using the reader-unit grammar.
4. Run hostile deletion/merge tests on every movement.
5. Draft the first complete manuscript pass from the surviving movements.
6. Use drafting failures as evidence to reopen architecture only where a missing dependency is demonstrated.

# OPEN

- Exact corpus-admission wording and evidence in Section 2.
- Exact amount of visible source-module detail in Section 3.
- Exact amount of formal notation in Section 4.
- Whether COMPOSE remains a compact subsection or earns more space during drafting.
- Exact location and density of nearest-neighbor literature.
- Journal-facing vocabulary for Section 6.
- Page-level movement architecture, to be determined through the next execution pass.
