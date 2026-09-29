# Canonical Authority Research-Object PD Architecture Audit

Date: 2026-09-21
Workstream: WS:2026-09-21:CANON-RESEARCH-OBJECT-PD-AUDIT
Project: canonical-authority

## Audit target

Pre-repair condition:
The project had durable files but no single registered research object corresponding
to "the paper we have right now."

The effective project state was distributed across:
- GOALS.yaml
- SPINE.yaml
- STATE.yaml
- PROVENANCE.yaml
- MANUSCRIPT_CONTRACT.md
- research/SOURCE_MODULES.yaml
- research/DISCOVERY_MAP.yaml
- research/CEILING_RAISE_REGISTER.yaml

This was a material object-identity vulnerability because audits and ceiling raises
could target different summaries of the project while appearing to target one paper.

## Primary defects found

### 1. No exact integrated research object

The repository's own Research Object Policy requires stable identity for material
research objects and recommends ARTIFACTS.yaml or an equivalent registry.

Canonical Authority had no ARTIFACTS.yaml and no exact object representing the
current pre-manuscript paper architecture.

Risk:
Audits could be performed against chats, summaries, state files, or registers without
a stable answer to which exact object was being audited.

Repair:
Created:
- projects/canonical-authority/RESEARCH_ARCHITECTURE.yaml
- projects/canonical-authority/ARTIFACTS.yaml

Registered stable object:
CANON:ARCH:001

### 2. Competing current-control semantics

SPINE.yaml still contained the older detailed nine-step R pathway and B** as its
active formulation while STATE.yaml and MANUSCRIPT_CONTRACT.md had already moved to
PROFILE -> TRACE -> DISCRIMINATE -> RECOGNIZE.

Risk:
The repository contained multiple plausible current versions of the method.

Repair:
SPINE.yaml now owns only stable A -> Q -> H[F] -> R -> B -> C identity and invariants.
RESEARCH_ARCHITECTURE.yaml owns the current detailed implementation.

### 3. Ceiling insight versus realized architecture was undefined

A ceiling raise could be marked accepted in CEILING_RAISE_REGISTER.yaml without a
formal rule distinguishing "interesting accepted research result" from "part of the
current paper."

Risk:
Chat/register accumulation could be mistaken for a raised actual paper ceiling.

Repair:
A ceiling raise is now realized only when its surviving effect is promoted into
CANON:ARCH:001, passes strict-gain and non-regression controls, updates artifact
version/blob identity, and reconciles dependents.

### 4. Dependency versions were not frozen

The initial integrated architecture pointed to supporting registers by path but did
not freeze their exact versions.

Risk:
Later changes to source modules, discovery, or ceiling registers could silently make
claims about the current architecture stale.

Repair:
Added dependency_snapshot with exact Git blob SHAs and reconciliation rule.

### 5. Realized-ceiling attribution was initially overinclusive

The first architecture realization list incorrectly included moves still classified
as promising, conditional, or manuscript strategy.

Risk:
Candidate support could be retroactively represented as already part of the paper.

Repair:
Separated realized, superseded, and not-yet-realized ceiling moves.

This defect was discovered by applying PD attribution/source-versus-supplementation
logic to the architecture itself.

## Successor ceiling tests

The exact CANON:ARCH:001 v1.0.2 object was then subjected to the full successor
ceiling program recorded in:

audits/CANONICAL_AUTHORITY_SUCCESSOR_CEILING_PROGRAM_2026-09-21.md

That program included:
- deletion tests;
- collapse tests;
- hostile countermodels;
- route-level sufficiency analysis;
- case-level multi-route conflict testing;
- regression over all Jewish modules;
- cross-tradition structural holdouts;
- targeted nearest-neighbor literature review;
- Ramban source-specific investigation;
- explicit strict-gain comparison.

## PD result

The prior four-stage method contained a level-mixing issue.

PROFILE performs a necessary semantic/setup job but is not an independent route-level
success conjunct once TRACE is defined over a typed native output.

The route-level success jobs that survived hostile deletion and collapse tests are:

TRACE
DISCRIMINATE
RECOGNIZE

A new hidden dependency was also exposed:

COMPOSE / DEFEAT

Route-level usable grounds do not guarantee all-things-considered case selection when
multiple successful routes conflict.

## Current exact object

CANON:ARCH:001
Version: 1.1.0
Current Git blob:
ae6fedb7583d839709a7662f387db1e85a7211d5

Current method:

Typed setup:
PROFILE

Route gates:
TRACE -> DISCRIMINATE -> RECOGNIZE

Case-level conditional operation:
COMPOSE / DEFEAT

Current artifact registry:
projects/canonical-authority/ARTIFACTS.yaml

Current manuscript status:
absent_not_yet_drafted

## Non-regression result

The v1.1.0 successor preserves:
- the fixed Rashi-Ramban proposition pair;
- the bounded no-selector result;
- the prophecy positive control;
- open/non-exhaustive source-module status;
- the distinction between explanation and adjudication;
- the source-versus-added-selector attribution rule;
- the no-universal-negative boundary.

H_X stopping-stage representation was refined from DISCRIMINATE to TRACE because
actual target coverage is part of establishing the source-to-target relation. The
case outcome did not change.

H_R remains the strongest case-proximate route but still fails TRACE.

## Architecture verdict

The project is no longer merely a coordinated collection of conceptual files.

It now has:
1. one exact integrated current research object;
2. one stable spine object;
3. one artifact registry;
4. one candidate/decision ceiling register;
5. one detailed source-module registry;
6. one research-to-manuscript contract;
7. explicit version succession and strict-gain semantics.

## Remaining vulnerabilities

### A. Multi-route composition remains open

The v1.1.0 route-level characterization is stronger than the current case-level theory.
A general decisive-adjudication claim requires independently justified aggregation or
defeat semantics.

### B. External holdouts are exploratory

Catholic, Sunni hadith, Pentecostal/charismatic, and Latter-day Saint tests were
structural stress tests performed after the architecture was known. They do not count
as prospective independent validation.

### C. Literature closure remains bounded

The targeted nearest-neighbor search strengthens positioning but some closest
comparators remain incompletely inspected at full-text level.

### D. Manuscript remains absent

The research object is now stronger and cleaner, but publication quality still
depends on translation into a reader-facing manuscript.

## Operating rule going forward

No audit or ceiling claim about "the current paper" is valid unless it identifies:
- CANON:ARCH:001;
- exact version or Git blob;
- the spine link being tested;
- protected prior results;
- strict-gain basis for any promoted successor.

No new field, analogy, distinction, source, or validation case counts as a ceiling
raise merely because it is interesting.

A successor counts only when it yields a stronger same-spine result and is promoted
through the versioned research object with non-regression.
