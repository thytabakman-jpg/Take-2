# Canonical Authority Article-Facing Source Closure Audit

## Objective

Increase publication rigor by testing whether every article-visible Jewish source
module has an exact primary-source registry anchor matching the module actually used.

This audit does not expand the admitted source-module corpus.

## Fixed case

### Rashi Genesis 1:1

Registry status: verified primary edition.

Current role: fixed P_R rival.

No closure defect identified in this pass.

### Ramban Genesis 1:1

Registry status: verified primary edition:
*Mikraot Gedolot HaKeter: Genesis*, ed. Menachem Cohen.

Current role: fixed P_N rival and H_R.

Independent online cross-check confirms that Ramban explicitly characterizes creation
as a deep mystery knowable through Mosaic tradition while the same comment also
contains his peshat discussion.

No core identity defect identified.

## H_P pluralism and determination

SOURCE_MODULES anchors:
- Eruvin 13b
- Ritva on Eruvin 13b

SOURCE_REGISTRY status:
neither exact anchor is currently registered by name.

Independent verification:
- Eruvin 13b contains elu ve-elu and the determination of halakha like Beit Hillel.
- Ritva on Eruvin 13b explicitly discusses how opposed rulings can both be divrei
  Elohim hayyim and reports the model in which multiple reasons are entrusted to the
  sages of each generation for determination.

Closure status: GAP.

Required repair after repository reconciliation:
1. add Eruvin 13b as exact verified primary anchor for H_P;
2. add an exact publication/edition locator for Ritva on Eruvin 13b, not merely a
   generic web locator;
3. keep legitimacy/pluralism and legal determination distinct from descriptive-truth
   selection.

## H_M protected reception

Registry anchors:
- Maimonides, Mishneh Torah, Hilkhot Mamrim 1:3
- Maimonides, Introduction to the Mishnah

Status: verified primary.

Closure status: PASS for current architecture.

## H_A authority and error

SOURCE_MODULES anchor:
- Horayot 2b

SOURCE_REGISTRY currently contains:
- Mishnah Horayot 1
- Maimonides, Hilkhot Shegagot 12

These support the authority/error module, but the exact article-facing module anchor
Horayot 2b is not registered.

Independent verification:
Horayot 2b explicitly discusses cases in which a court erred and cases in which a
qualified judge or scholar knows the court is mistaken, including the distinction
between following the court and knowing the ruling is wrong.

Closure status: PARTIAL GAP.

Required repair:
register Horayot 2b directly so module anchor and source registry agree.

## H_X authenticated prophecy

SOURCE_MODULES anchors:
- Maimonides, Yesodei HaTorah 9
- Maimonides, Yesodei HaTorah 10

SOURCE_REGISTRY:
no matching source record located.

Independent verification:
- Yesodei HaTorah 9 limits prophetic authority to add, subtract, or permanently
  reinterpret Torah law.
- Yesodei HaTorah 10 provides an authentication procedure based on repeated successful
  prophecy and describes when an established prophet is no longer continuously
  retested.

This is the paper's positive control and therefore article-visible.

Closure status: HIGH-PRIORITY GAP.

Required repair:
register both chapters as verified primary anchors for H_X with exact edition/locator.

## H_R Ramban creation tradition

Registry:
verified primary edition for Ramban Genesis 1:1.

Independent cross-check:
the text supports received/esoteric creation knowledge but does not, by itself,
identify the fixed syntactic proposition I_S as the received item.

Closure status: PASS for current bounded result.

## H_L loss and reconstruction

Registry:
Babylonian Talmud, Temurah 16a, verified primary.

Independent verification:
the text reports forgotten halakhot after Moses and reconstruction through Othniel's
reasoning while rejecting reacquisition by heavenly inquiry.

Closure status: PASS.

## H_G generational hierarchy

Registry:
- Eruvin 53a, verified primary;
- Shabbat 112b, verified primary.

Independent verification:
Shabbat 112b supplies the generational-stature comparison used by the module.

Closure status: PASS for the current limited claim.

## Source-closure priority

Priority 1:
H_X exact registration because it is the article-visible positive control.

Priority 2:
H_P exact Eruvin/Ritva registration because pluralism is central and has a substantial
secondary literature.

Priority 3:
H_A Horayot 2b anchor alignment.

Priority 4:
final page/section-level citation normalization for all article-visible quotations and
paraphrases in the eventual manuscript.


## Branch execution status

The verifiable registry repairs identified above have now been executed on this
isolated workstream branch:

- CANON:SRC:046 registers Eruvin 13b for H_P;
- CANON:SRC:047 registers the exact Ritva on Eruvin 13b locus for H_P;
- CANON:SRC:048 registers Horayot 2b for H_A;
- CANON:SRC:049 registers Yesodei HaTorah 9 for H_X;
- CANON:SRC:050 registers Yesodei HaTorah 10 for H_X.

One narrow gate remains:
final print-edition bibliographic normalization for Ritva on Eruvin 13b.

These branch records remain non-promoted relative to main until the overlapping
backend-recovery workstream is reconciled.

## Publication-value result

The source layer is stronger than an undifferentiated "needs more primary sources"
diagnosis suggests.

The current architecture already has strong primary grounding for the fixed case,
reception, Ramban creation tradition, loss/reconstruction, and generational hierarchy.

The main rigor gain is targeted registry closure for three article-facing modules, not
corpus expansion.

This raises evidential defensibility without increasing manuscript scope.
