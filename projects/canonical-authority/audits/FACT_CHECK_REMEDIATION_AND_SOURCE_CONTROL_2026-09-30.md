# Canonical Authority — Fact-Check Remediation and Source Control

Status: COMPLETE REMEDIATION PASS / PUBLICATION SOURCE CLOSURE STILL OPEN  
Date: 2026-09-30  
Branch: workstream/canonical-authority-draft-20260929

## Input

The full source-facing fact check already existed as:

- audits/FULL_MANUSCRIPT_FACT_CHECK_2026-09-30.md

That audit deliberately left the manuscript unchanged. This remediation pass applies the factual/source-identity corrections and creates permanent source-control artifacts.

## Main result

The fixed Rashi–Ramban case survives fact check.

The source collision remains:

\[
P_R=C_S,
\qquad
P_N=\neg C_S.
\]

The important drift was in the narrative representation of the opening case, not in the formal target.

## Drift found at the front of the paper

The prior P01 compressed the source exchange into:

1. Rashi states a universal construct premise.
2. Ramban gives Yeshayahu 46:10 and Devarim 33:21 as counterexamples.

That representation omitted a load-bearing fact:

> Extant Rashi himself already discusses Yeshayahu 46:10 and treats it through ellipsis.

Ramban's surviving objection then does more than merely name an untouched counterexample. He says Yeshayahu uses non-construct reishis and argues that, even if an omitted noun is supplied there, an omitted kol can likewise be supplied in Bereishis 1:1. That means the ellipsis license does not uniquely force Rashi's dependent parse.

Re'em then creates a second distinction: the logical relation among the extant texts is not identical to the historical claim that Ramban actually saw Rashi's extant Yeshayahu sentence.

## Manuscript repairs applied

Commit:
- 7451b09be96a24f157fad246eeda98a6e2ba1075

Repairs:
1. P01 now includes Rashi's extant Yeshayahu ellipsis treatment.
2. P01 now includes Ramban's omitted-kol argument.
3. P01 distinguishes defeat of Rashi's universal premise from the weaker point that ellipsis still does not uniquely yield Rashi's dependent reading.
4. P30 now distinguishes extant-text logical relation from historical direct response.
5. R. Yishmael's date changed from 90–135 CE to c. 50–c. 135 CE.
6. P21 now makes explicit that Berger reports Funkenstein while challenging Funkenstein's broader account.

## Permanent source-control artifacts

### Citation ledger
- CITATION_LEDGER.md
- stable numeric IDs [1]–[56]
- verified / yellow / open / project-record status
- one source ID can support many claim units
- open slots remain open rather than being filled with weak substitutes

Creation/extension commits:
- d7ce368403243b4071062c97390c32f909fa8194
- bd6b8d00d9117ce352cfaa137b8e918f3097ba0a

### Argument/evidence map
- ARGUMENT_EVIDENCE_MAP.md
- covers every paragraph in the manuscript
- splits source-heavy paragraphs into sentence-sized or two-sentence claim units
- distinguishes primary-source fact, scholarship attribution, analytic inference, definition, project-history claim, and bounded research negative
- records exact citation IDs and source-closure status

Creation commit:
- 13e6d4cd8c8312909ad7c2f51dbba1bc0fce62ee

## Propagation controls

PARAGRAPH_CONTROL_MAP.md was updated so future prose passes cannot silently return to the flattened case.

Commit:
- 62a8922b296404cd0b5f3194126722d2daf2891f

Protected P01 controls now require:
- Rashi's construct/dependent peshat;
- Rashi's universal reishis premise;
- Rashi's extant Yeshayahu 46:10 ellipsis treatment;
- Ramban's attack on the premise;
- Ramban's omitted-kol response to the ellipsis move;
- the distinction between supporting premise and fixed target;
- P30/Re'em control over historical direct-response claims.

PUBLICATION_READINESS_CHECKLIST.md now recognizes the fact-check, citation ledger, and evidence map.

Commit:
- 78c33bb782a44b758fa2f94c6f287b72484064ed

## Current date audit

### Corrected
- R. Yishmael: c. 50–c. 135 CE.

### Verified enough for current draft
- Rashi: 1040–1105.
- Ramban: 1194–c. 1270.
- R. Akiva: c. 50–135 CE.
- R. Yochanan: c. 180–c. 279 CE.
- Reish Lakish: c. 200–c. 275 CE.
- Rambam: 1138–1204.
- Chatam Sofer: 1762–1839.
- David Berger: b. 1943.
- Amos Funkenstein: 1937–1995.
- Moshe Halbertal: b. 1958.

### Yellow / calibrate before submission
- Eliyahu Mizrahi: manuscript c. 1450–1526; stronger reference gives about 1455–1525/1526.
- Ritva: manuscript c. 1250–1330; life dates vary significantly by reference.
- Judah Halevi: manuscript c. 1075–1141; newest Stanford Encyclopedia entry says birth year is unknown and places it only within a broader numerical window.
- David Shatz: manuscript b. 1948; authoritative institutional/CV support for the birth year still needs recovery.

The numeric-year-only rule remains protected. No century-label substitution is permitted.

## Fact-check disposition by source family

### Rashi/Ramban/Re'em
Verified and repaired for source fidelity.

### Cross-strata recurrence
Akiva/Yishmael and Yochanan/Reish Lakish verified. Geonic Endor claim has secondary confirmation but exact primary Geonic sources remain OPEN.

### Pluralism / protected reception
Eruvin 13b, Ritva, Rambam Mamrim, and Kuzari III:24 source claims verified. Modern pluralism-scholarship framing still needs a named scholarly citation.

### Authority / error / loss / hierarchy
Horayot, Rambam Shegagos, Temurah, Shabbos 112b, and Eruvin 53a source claims verified. The paper's transfer/reliability conclusions are analytic applications rather than source quotations.

### Prophecy / Ruach HaKodesh
Rambam prophetic authentication/legal limits verified. Ramban Bava Batra 12a verified. Exact Chatam Sofer primary passage remains OPEN.

### Ramban creation tradition and modern scholarship
Ramban's received-creation statement verified. Berger verified, including his adversarial context toward Funkenstein's broader thesis. Shatz supported. Funkenstein full-text inspection and exact Halbertal target pages remain OPEN.

### Epistemology / interdisciplinary positioning
No contradiction was found, but several article-visible field-positioning sentences still need named literature. These are citation debts, not current factual corrections.

## Submission-blocking OPEN items

Highest priority:
1. primary Geonic Endor passages;
2. exact Chatam Sofer passage;
3. Funkenstein full article;
4. Halbertal exact target pages;
5. expertise/epistemic-authority literature;
6. testimony literature;
7. collective/institutional epistemology;
8. jurisprudence comparator;
9. canon/cultural-memory comparator;
10. sociology of religious knowledge;
11. provenance/authenticity comparator;
12. modern rabbinic pluralism scholarship;
13. comparative-methodology / tertium comparationis;
14. multi-premise/aggregation background;
15. emic/etic religious-studies methodology;
16. Ritva/Halevi/Shatz date calibration if those dates remain in the final text.

## Acceptance rule

A future source-facing manuscript edit is accepted only when:

\[
\text{PRIMARY / SCHOLARLY SOURCE}
\leftrightarrow
\text{ARGUMENT EVIDENCE UNIT}
\leftrightarrow
\text{MANUSCRIPT CLAIM}
\]

remain aligned.

Agreement between manuscript and architecture alone is insufficient.

## Final disposition

- Full-document source audit: COMPLETE for the current development-draft state.
- Clear factual/source-narrative defects found: REPAIRED.
- Fixed case: PRESERVED and source-faithfully strengthened.
- Citation infrastructure: CREATED.
- Claim-by-claim evidence infrastructure: CREATED.
- Publication citation closure: OPEN.
- Cut pass: NOT AUTHORIZED and NOT PERFORMED.
