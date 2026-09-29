# Canonical Authority Phase 2 — Authority / Object Map

Date: 2026-09-23
Status: COMPLETE

## ImprovementCore PRE

Question:
What is each material Canonical Authority object, and where does its current authority live?

## Object-role inventory

### CANONICAL AUTHORITY
- projects/canonical-authority/GOALS.yaml
- projects/canonical-authority/SPINE.yaml
- projects/canonical-authority/STATE.yaml
- projects/canonical-authority/RESEARCH_ARCHITECTURE.yaml
- projects/canonical-authority/CONTROL_MAP.yaml
- projects/canonical-authority/GOAL_SPINES.yaml
- projects/canonical-authority/PROVENANCE.yaml
- projects/canonical-authority/ARTIFACTS.yaml

### RESEARCH SUPPORT
- projects/canonical-authority/research/DISCOVERY_MAP.yaml
- projects/canonical-authority/research/SOURCE_REGISTRY.yaml
- projects/canonical-authority/research/SOURCE_MODULES.yaml
- projects/canonical-authority/research/CEILING_RAISE_REGISTER.yaml
- research analyses/working material

### MANUSCRIPT / READER
- projects/canonical-authority/MANUSCRIPT_CONTRACT.md
- SPLINE.yaml
- reader/manuscript architecture material

### ORIENTATION / DERIVED
- PROJECT_PAGE.md
- PROJECT_PAGE_APPENDIX.md
- PROJECT_LEXICAL_CONTROL.md

These are presentation/control surfaces and do not outrank source authority.

### AUDIT / HISTORY
- audits/*
- historical recovery records

### OPERATIONAL WORK
- current workstream/campaign records
- Sort Later captures routed to Canonical Authority when durable

## Authority map

GOALS → goal identity
STATE → current project/result state
SPINE/SPLINE → stable argument/reader structures
RESEARCH_ARCHITECTURE → integrated research object
SOURCE_REGISTRY → exact source identity
SOURCE_MODULES → typed source analysis
PROVENANCE → history/lineage
ARTIFACTS → accepted project artifact identity
MANUSCRIPT_CONTRACT → manuscript translation control
PROJECT_PAGE → human-facing derived cockpit
GOAL_SPINES → operational goal-spine representation
TRACEABILITY / DERIVED_STATE → portfolio-level derived controls

## Goal-relative dependency result

G0/G1 are load-bearing for:
GOALS, SPINE, RESEARCH_ARCHITECTURE, SOURCE_MODULES, current STATE, and the bounded result.

PROJECT_PAGE is operationally useful but not semantically load-bearing.

Audit history is recoverability infrastructure, not current authority.

## Relational PD result

Critical relations:
- GOALS ↔ GOAL_SPINES = source/derived
- GOALS ↔ SPINE = goal-relative argument dependency
- SPINE ↔ RESEARCH_ARCHITECTURE = stable identity ↔ current integrated method
- RESEARCH_ARCHITECTURE ↔ SOURCE_MODULES = research object ↔ typed evidence analysis
- SOURCE_REGISTRY ↔ SOURCE_MODULES = source identity ↔ source analysis
- PROVENANCE ↔ all historical/current transitions
- ARTIFACTS ↔ accepted representations
- MANUSCRIPT_CONTRACT ↔ RESEARCH_ARCHITECTURE = downstream translation
- PROJECT_PAGE ↔ all = derived human-facing orientation

## RepairCore result

No missing parent authority discovered.
No duplicate canonical authority discovered.
No reason to move a load-bearing authority object solely to make the tree prettier.

## ImprovementCore POST / Phase 2 gate

PASS.

Conclusion:
The organizational problem is primarily representational/taxonomic, not authority ownership.

Movable candidates are primarily non-authoritative support/history/audit objects.
