# Canonical Authority — Bloat and Earned-Claim Preservation Audit

Status: PASS after one restoration  
Date: 2026-09-30  
Baseline: manuscript at commit `eb83692ca4d0376cdf3e84765cc99635da775a7d`  
Current branch: `workstream/canonical-authority-draft-20260929`

## Question

Did the subsection passes, closure tools, currentness propagation, and whole-paper equation runs accidentally cut the overfull manuscript or delete previously earned claims?

## Structural comparison

Baseline manuscript:
- 5,605 words
- 29 paragraph-control markers
- 22 numbered subsections

Current manuscript:
- 9,251 words
- 50 paragraph-control markers
- 23 numbered subsections

Net growth:
- +3,646 words
- +65.0%
- +21 paragraph-control objects
- +1 subsection

Original paragraph preservation:
- 29 / 29 baseline paragraph markers remain present.
- No original numbered subsection was removed.
- Section 2.2 was renamed from “Pluralism and Received Tradition” to “Pluralism and Protected Reception.”
- Section 1.4 was added.

## Exact-text versus substantive preservation

Many baseline sentences were rewritten while preserving or sharpening their claims. Therefore the correct claim is not “no sentence was ever deleted.” The correct claim is:

> No baseline section or paragraph object was cut, and after this audit no identified earned substantive claim from the baseline has been lost.

## One issue found and repaired

The baseline P02 explicitly said:

> Shared canonical standing can give both interpreters genuine epistemic weight.

A later rewrite preserved the non-discrimination half of the argument but no longer explicitly stated that affirmative epistemic-weight claim.

That was a real weakening relative to the project's earned-claim preservation rule.

Repair committed:
`772b8bea3f27e8973dc94de78df49bbe6374a876`

The sentence is now restored in Section 1.2.

## Protected earned-claim checks

Current manuscript still explicitly preserves:

- shared canonical standing can give both interpreters genuine epistemic weight while failing to discriminate;
- a genuine counterexample defeats Rashi's universal supporting premise as stated without thereby proving Ramban's full reading;
- under ordinary non-contradiction, preserving P and not-P preserves at least one false proposition;
- if “mesorah” is broad enough to include both rival positions, the same conditional consequence applies to that broad classificatory category;
- successful internal/traditional discriminators count as genuine success rather than being redescribed as failure;
- the current package result remains restricted to (mathcal R_{current});
- failure to recover a selector for one rival is not evidence for the other rival;
- genuinely defeating evidence changes the corresponding paper claim rather than being absorbed by redefining the problem.

## Disposition

The manuscript remains intentionally overfull.

No cut pass has been performed.

Future trimming is still deferred to a later venue-, evidence-, word-budget-, and reader-burden decision stage.

The preservation rule for future editing is:

> Cut only through an explicit cut pass. Do not silently remove an earned claim during architecture, logic, currentness, compression, or prose repair.
