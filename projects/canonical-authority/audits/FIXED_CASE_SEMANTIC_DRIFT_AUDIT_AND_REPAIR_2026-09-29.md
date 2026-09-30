# Canonical Authority — Fixed-Case Semantic Drift Audit and Repair

Status: HIGH-SEVERITY DRIFT CONFIRMED / REPAIR AUTHORIZED  
Date: 2026-09-29  
Branch: `workstream/canonical-authority-draft-20260929`

## Executive finding

The live paper inherited a semantic drift in the fixed Rashi–Ramban target.

The primary-source disagreement centers on the grammatical/dependent status of `בראשית / ראשית` in Bereishis 1:1. Rashi's peshat treats the opening as dependent: `בראשית` is read in the construct/dependent relation that yields “at the beginning of [God's] creating ...,” and Rashi supports that move with the broader claim that `ראשית` in Scripture occurs in construct relation. Ramban explicitly attacks that grammatical premise with counterexamples and then gives an independent peshat reading of the verse.

The project instead canonized a downstream consequence as its formal target:

> `I_S`: `bara Elohim` is the main predication rather than part of a temporal subordinate construction leading to verse 3.

That proposition tracks a consequence of the rival parses, but it is not the most source-faithful statement of the textual disagreement being argued between Rashi and Ramban.

Severity: **HIGH** because the target proposition is the comparison coordinate for the entire paper.

## Corrected case object

### Rashi's broader supporting premise

`G_R`:

> Rashi argues that `ראשית` is used in construct/dependent relation in Scripture.

Ramban directly challenges this generalization by citing counterexamples.

`G_R` is important evidence about the disagreement, but it is not the best fixed target because it is a broader lexical/grammatical generalization rather than the verse-specific peshat claim the paper wants to test.

### Corrected fixed target

`C_S`:

> On the peshat of Bereishis 1:1, `בראשית` functions in the construct/dependent relation Rashi assigns to it, so the opening forms the temporal setting that leads to the main clause in verse 3.

Rashi:

[
P_R = C_S.
]

Ramban:

[
P_N = \neg C_S.
]

Ramban's independent creation-statement reading is a consequence of his rejection of the Rashi construct/dependent parse.

This preserves the same verse-level truth conflict while restoring the linguistic nucleus of the source disagreement.

## Why the old target was tempting

The old `I_S` target was:

- binary;
- easy to formalize;
- sufficient to distinguish the two resulting parses;
- convenient for downstream TRACE analysis.

But it compressed:

[
	ext{grammatical premise / construct relation}
	o
	ext{clause dependency}
	o
	ext{main-predication consequence}
]

into the final consequence and then treated that consequence as though it were the source-level disagreement itself.

This is **compression substitution**.

## Drift lineage

### 1. Drift already present at first recovered spine formalization

The earliest recovered `SPINE.yaml` commit inspected is:

`f76d4c06ca1001cf15c4379a6cc8c24b02bd74fb`  
2026-09-22 01:15:48Z  
Commit message: `Add Canonical Authority argument spine control`.

That first recovered formal spine already defines `I_S` as the main-predication/temporal-subordination proposition.

Therefore the recent manuscript rewrite did not originate the drift. It inherited it.

### 2. Canonicalization converted a compression into a protected identity

Once `I_S` entered SPINE, STATE, GOALS, RESEARCH_ARCHITECTURE, outline, and manuscript controls, later work treated preservation of `I_S` as a correctness condition.

### 3. Later source work actually exposed the mismatch

The later Ramban target-edge acquisition work explicitly records:

- Ramban “directly disputing Rashi's construct/temporal peshat”;
- Ramban discussing “Rashi's construct-state objection”;
- Ramban adducing counterexamples;
- Ramban then giving the independent/simple peshat.

That evidence should have triggered revalidation of the fixed target.

Instead it was used only to ask whether Ramban's received/esoteric material supported the already-fixed `I_S`.

### 4. Regression tests checked internal consistency instead of source identity

The Section 1 regression required:

- `I_S`;
- `P_R = not I_S`;
- `P_N = I_S`.

It verified that the prose matched the formal architecture, but did not independently ask whether the formal architecture still matched the primary-source disagreement.

This is **reference-lock regression**.

## Root cause

The defect requires all four conditions:

1. **Source-to-model compression:** a downstream consequence was chosen as the formal proposition.
2. **Missing claim-type distinction:** the architecture did not mark whether the target was a direct source proposition, close paraphrase, or analyst-derived consequence.
3. **Fixed-case authority:** once formalized, the target became protected and later source evidence was interpreted through it.
4. **Regression circularity:** checks compared manuscript ↔ architecture rather than manuscript ↔ architecture ↔ primary source.

## Propagation

The drift propagated into:

- SPINE / STATE / RESEARCH_ARCHITECTURE in the archived source project;
- GOALS and goal spines;
- source-module `required_bridge` language;
- author-facing outline and blueprint;
- old manuscript;
- current live manuscript;
- paragraph control map;
- package-TRACE wording;
- H_R acquisition questions;
- whole-paper and paragraph audit artifacts.

The archived `dump/` tree remains immutable historical evidence. Live artifacts must use the corrected target and explicitly mark older audits as pre-correction.

## Corrected target regression across the seven mechanism families

The change from `I_S` to `C_S` requires re-testing the current bounded result.

### H_P — pluralism/determination

Native output still does not supply a proposition-specific relation to whether `בראשית` has Rashi's construct/dependent function.

Result: **TRACE incomplete**.

### H_M — protected reception

The source can classify provenance, but current evidence does not place `C_S` or `¬C_S` inside protected received content asymmetrically.

Result: **TRACE incomplete**.

### H_A — authority/error

Institutional authority does not itself supply a truth-directed relation to the construct/dependent parse.

Result: **TRACE incomplete**.

### H_X — authenticated prophecy

Still a valid positive control: authenticated privileged access that explicitly covered `C_S` and favored one rival could satisfy the architecture.

Current case: target coverage absent.

Result: **success in principle / not instantiated**.

### H_R — Ramban creation tradition

This is the crucial re-test.

Ramban invokes received knowledge about creation, but current evidence does not identify his rejection of Rashi's construct/dependent parse (`¬C_S`) as itself received content or as truth-supported by that received content.

The Funkenstein/ Berger material about an esoteric subject/object reversal does not repair this edge. A different esoteric syntax does not establish either Rashi's construct/dependent peshat or Ramban's verse-level anti-construct peshat as received.

Result: **TRACE incomplete**.

### H_L — loss/reconstruction

No current proposition-specific bridge to `C_S`.

Result: **TRACE incomplete**.

### H_G — generational hierarchy

No current relation from comparative stature to reliability on the construct/dependent question.

Result: **TRACE incomplete**.

### Package result

The package-level obstruction survives the corrected target:

> Relative to the currently reconstructed seven-module corpus and independently licensed source use, no current package completes TRACE to `C_S`.

This is a fresh regression result indexed to the corrected target, not an automatic carryover from `I_S`.

## Other semantic-drift scan

### Confirmed additional framing drift: “factual claims”

The manuscript sometimes describes the rival exegetical/syntactic claims as “factual.”

That wording is broader than necessary and risks importing an unnecessary classification.

Repair:

> “incompatible truth-apt syntactic claims”

or equivalent source-specific language.

### No second target-identity drift confirmed in the seven source modules

The reviewed module claims remain aligned with their current source controls:

- H_P: legitimacy / practical determination;
- H_M: provenance / reception classification;
- H_A: authoritative procedure compatible with represented error;
- H_X: authentication of prophetic access plus legal constraints;
- H_R: received creation knowledge, with proposition-specific linkage open;
- H_L: loss and reconstruction;
- H_G: generational asymmetry.

These labels are project-level analytical types, not quotations from the sources. The manuscript must continue to make that ownership clear.

### Watch-list rather than confirmed drift

1. `protected reception` is a project label and must not be made to sound like Maimonides' own technical term.
2. `authenticated prophecy` is a project compression of the Yesodei HaTorah material and must remain tied to the actual authentication conditions.
3. `target-relative authority` is the paper's derived claim, not a recovered Jewish source doctrine.
4. `source-grounded` must distinguish direct source content from source content plus an explicitly licensed bridge.

No additional defect in this watch-list currently requires changing the argument result.

## Permanent prevention rule

Every load-bearing source-facing claim now receives a claim-lineage type:

- **DIRECT** — explicit source assertion;
- **CLOSE_PARAPHRASE** — faithful semantic paraphrase;
- **DERIVED_CONSEQUENCE** — follows from source material but is not itself the source's stated issue;
- **PROJECT_INFERENCE** — analytic conclusion introduced by the paper;
- **CONDITIONAL_CONTROL** — counterfactual/positive-control construction.

A fixed-case target may be a derived proposition only when the paper explicitly says so and demonstrates that it preserves the source disagreement relevant to the research question.

### Source-fidelity reentry trigger

Any new primary-source recovery that changes:

- the linguistic nucleus of the dispute;
- the relation between premise and conclusion;
- the level at which two rivals directly contradict;
- the ownership of a proposition;

automatically reopens the fixed target before downstream regression may continue.

## Disposition

1. Replace live `I_S` with corrected `C_S`.
2. Reverse the rival orientation: `P_R=C_S`, `P_N=¬C_S`.
3. Rewrite Section 1.1 around the construct/dependent dispute and Ramban's explicit attack on Rashi's “reshit” premise.
4. Propagate `C_S` through Sections 2–7.
5. Re-state H_R as requiring a bridge from received creation knowledge to Ramban's `¬C_S`.
6. Mark pre-correction audit artifacts as superseded for fixed-case semantics.
7. Add the claim-lineage/source-fidelity gate to the live paragraph control map.
