# ImprovementCore Audit — “Borrow Before Build” for Canonical Authority

Target request:
Before rebuilding Canonical Authority's organizational structure, inspect the broader repository
for systems already developed elsewhere, especially PD systems that have demonstrated value,
and determine what should be imported, adapted, or left outside the project.

ImprovementCore result:

1. This is upstream of the existing organizational repair plan.
2. It prevents duplicate-system creation.
3. It protects prior investment in PD, Goal-Spine, project-cockpit, routing, provenance,
   and validation systems.
4. It changes the first phase of the plan.

New protected principle:
DO NOT BUILD A CANONICAL AUTHORITY LOCAL VERSION OF AN EXISTING SYSTEM UNTIL A
BORROW/ADAPT/REJECT TEST HAS BEEN RUN.

Candidate reusable systems already demonstrated in the repository:
- Goal-Spine / HM-001
- project-cockpit/page contract
- relational / multi-level / multi-object PD
- ImprovementCore
- RepairCore / RepairEscalation
- SemanticPreflight
- ExactObjectPreflight
- Workstream / Concurrency
- Traceability
- DerivedStateLiveness
- MigrationContract
- PortfolioHealth
- manuscript/reader architecture controls
- Sort Later routing conventions

Borrow decision classes:
BORROW_AS_IS
ADAPT
REFERENCE_ONLY
PROJECT_SPECIFIC
REJECT / REDUNDANT

ImprovementCore gate:
No new Canonical Authority organizational subsystem is created until its nearest existing
system has been identified and the reuse decision documented.

Plan consequence:
Insert a new Phase 0 before current-state freeze:
SYSTEM INVENTORY + BORROW/ADAPT/REJECT ANALYSIS.

The current cockpit remains preserved.
The research architecture remains protected.
Physical folder changes remain late-stage.
