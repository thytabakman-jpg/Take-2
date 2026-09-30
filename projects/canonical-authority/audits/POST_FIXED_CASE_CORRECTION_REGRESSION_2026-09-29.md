# Canonical Authority — Post Fixed-Case Correction Regression

Status: PASS WITH OPEN PUBLICATION GATES  
Date: 2026-09-29  
Branch: `workstream/canonical-authority-draft-20260929`  
Corrected target: `C_S`

## 1. Source identity

Primary-source nucleus:

- Rashi reads `בראשית` in the construct/dependent relation that yields a temporal opening leading to verse 3.
- Rashi supports this with a broader claim about `ראשית` occurring in construct relation.
- Ramban directly challenges that grammatical premise with counterexamples and gives an independent peshat reading.

Corrected verse-level target:

[
C_S = 	ext{Bereishis 1:1 uses bereishis in Rashi's construct/dependent relation.}
]

Rivals:

[
P_R=C_S,qquad P_N=\neg C_S.
]

Result: **PASS**.

## 2. Old-target quarantine

The derivative `I_S` target is absent from the current manuscript.

Any surviving `I_S` references in live control/audit files occur only in explicit historical/supersession discussion.

Result: **PASS**.

## 3. Manuscript propagation

Checked Sections 1–7.

- Section 1 defines C_S and correct polarity.
- Section 2 tests mechanisms against C_S.
- Section 3 source reconstructions refer to C_S only as target application.
- H_R specifically asks whether received creation knowledge supports Ramban's ¬C_S peshat.
- Section 4 TRACE/DISCRIMINATE operate on C_S.
- Section 5 positive control and case test use C_S.
- P23 prevents Funkenstein's subject/object issue from being projected onto C_S.
- P24 states package obstruction relative to C_S.
- Sections 6–7 use C_S only as the corrected fixed target.

Result: **PASS**.

## 4. Logic regression

### Contradiction

[
P_R=C_S,quad P_N=\neg C_S
]

are contradictories under the same verse-level construct/dependent proposition.

Result: **PASS**.

### Old target relation

The old main-predication proposition is a downstream syntactic consequence of the rival parses, not established here as logically identical to C_S in every possible grammar.

Therefore it cannot substitute for C_S without argument.

Result: **DRIFT CORRECTLY REMOVED**.

### Route method

TRACE, DISCRIMINATE, RECOGNIZE, package TRACE, and COMPOSE do not depend on the old target's internal content. They survive target correction.

Result: **PASS**.

### H_R

Received creation knowledge is not currently shown to contain, entail, or truth-support Ramban's ¬C_S peshat.

Result: **TRACE INCOMPLETE**.

### Package result

No current module supplies the missing H_R-to-¬C_S edge; packages without H_R are still less case-proximate.

Result:

[
\forall X\in AdmPkg_A, \neg TRACE(X,C_S)
]

relative to the currently reconstructed corpus.

Status: **PASS / CORPUS-BOUNDED**.

## 5. Other-drift scan

### Fixed target

Confirmed high-severity drift. Repaired.

### Rival polarity

Confirmed inherited polarity tied to old I_S. Repaired.

### “factual” framing

Potential framing inflation. Reader-facing fixed-case language now prefers truth-apt syntactic/exegetical language. Literature titles about factual disagreement remain unchanged where bibliographically accurate.

Status: **REPAIRED WHERE MATERIAL**.

### H_P

No source-identity drift detected in current reconstruction.

### H_M

No source-identity drift detected. `protected reception` remains a project label and must not be presented as Maimonides' own term.

### H_A

No source-identity drift detected.

### H_X

No source-identity drift detected. Positive-control use remains explicitly conditional.

### H_R

No source-identity drift detected after correction. The key proposition-specific bridge remains OPEN.

### H_L

No source-identity drift detected.

### H_G

No source-identity drift detected.

### Target-relative authority

No source drift: this is explicitly a PROJECT_INFERENCE derived from the comparison, not attributed to a Jewish source.

### Novelty

No source drift detected; evidentiary closure remains OPEN.

## 6. Architecture consequence

The theory architecture survives.

The corrected source-level case improves the paper because Section 1 now exposes the actual grammatical argument:

[
	ext{Rashi's construct premise}
	o
	ext{Rashi's dependent peshat}
]

versus

[
	ext{Ramban's counterexamples}
	o
	ext{rejection of the construct/dependent peshat}.
]

The paper's method and bounded result remain unchanged in type, but all case-indexed conclusions are now explicitly indexed to C_S.

## 7. Permanent regression rule

Future fixed-case regression must triangulate:

[
	ext{PRIMARY SOURCE}
leftrightarrow
	ext{FORMAL TARGET}
leftrightarrow
	ext{MANUSCRIPT}.
]

Manuscript ↔ architecture agreement alone is insufficient.

Any primary-source discovery that changes the direct disagreement automatically reopens the formal target.

## Disposition

**CURRENT LIVE MANUSCRIPT: SEMANTIC REGRESSION PASS.**

Remaining OPEN work is publication-facing source/citation closure, H_R acquisition, novelty closure, and reader-level refinement rather than fixed-case identity.
