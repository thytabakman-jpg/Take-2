
# Goal / Project Page Architecture Retrospective

Date: 2026-09-23

Status: SORT LATER — research and architecture candidate. Not promoted into canonical portfolio architecture.

## Purpose

This report reconstructs the work done on the Canonical Authority project page and identifies what that work discovered about the function of a project-facing goal page.

The actual discovery is that a project page is an architectural interface between authoritative project state and the human or AI entering the project. It has to orient work without becoming a second source of truth, and it has to expose enough structure that the next action can be selected without reconstructing the project from chat history.

The Canonical Authority work therefore appears to reveal a general project-level control pattern that every substantial project can instantiate, with project-specific contents but a common semantic contract.

## 1. What the Canonical Authority work discovered

The project page evolved from a status summary into an opening cockpit and then into a structured orientation interface.

The major discoveries were:

1. The page must distinguish what the project ultimately wants from what the research must establish.
2. The page must distinguish research architecture from reader-facing manuscript architecture.
3. The page must expose the protected load-bearing spine without turning the page into a second source of truth.
4. The page must show the live frontier, not merely a list of unresolved questions.
5. The next operation needs a visible selection basis, not merely a task name.
6. The page needs dependency and propagation information so downstream staleness can be understood.
7. The page must preserve unresolved coordinates instead of silently collapsing OPEN into an answer.
8. Goal-spine coverage is not equivalent to active work.
9. Hierarchical position does not determine semantic type.
10. The page is derived state and therefore needs freshness and source mapping.

## 2. The crucial distinction: goal is not the project

The Canonical Authority work exposed several objects that need to remain distinct.

### Project goal

What the project is ultimately trying to make or accomplish.

For Canonical Authority this is publication of the rigorous peer-reviewed paper.

### Epistemic or substantive target

What the research has to establish for the goal to succeed.

For Canonical Authority this is the substantive result concerning the fixed Rashi-Ramban case.

### Deliverable

The artifact through which the result is communicated and evaluated.

For Canonical Authority this is the manuscript / paper.

### Objectives

The major jobs needed to move from current state toward the goal.

### Constraints

Conditions limiting admissible moves.

### Invariants

Conditions that ordinary improvement cannot silently violate.

### Spine

The load-bearing dependency structure connecting the major parts of the project.

### Current result

What the current evidence establishes.

### Current frontier

The currently live unresolved point that controls the next operation.

### Reader architecture

How the completed argument or artifact is meant to be understood.

The page becomes unstable when any one of these silently substitutes for another.

## 3. The project page is a cockpit, not a summary

The page evolved from asking:

"What is in this project?"

toward asking:

"Where am I, what is protected, what has been established, what is open, what is live now, and what is the next consequential move?"

This is a different job.

A project page is therefore an operating cockpit for project entry.

Its primary function is rapid, reliable orientation.

## 4. The page is a derived interface, not an authority source

The current project-page contract makes the page non-authoritative.

The authoritative objects remain separate:

- GOALS controls goal identity and success conditions.
- SPINE controls substantive argument identity and invariants.
- STATE controls current operational state.
- RESEARCH_ARCHITECTURE controls the integrated research object.
- specialized registries control sources, artifacts, provenance, workstreams, and audits.

The project page assembles selected information from those sources.

When the page conflicts with an authoritative source, the source wins and the page is stale.

This rule is critical because otherwise the project page gradually becomes an informal shadow database.

## 5. The project page is a progressive-disclosure layer

The project page solves a practical context problem.

The AI should not need to reconstruct a large project from historical chat every time the project is reopened.

The intended path is:

project page
-> identify the current project object and frontier
-> descend only into the authoritative sources needed for the task
-> perform the requested work
-> refresh the page when displayed orientation becomes materially stale

This makes the page an AI-context optimization layer as well as a human-facing orientation layer.

## 6. Stable spine versus reader-level refinement

The Canonical Authority work produced a particularly useful separation.

The protected research spine is the substantive architecture.

A reader-level refinement is a more granular representation of the dependencies the reader needs to understand.

The manuscript then implements that refinement.

So the intended transformation is:

Spine
-> reader-level refinement
-> reader journey
-> manuscript section architecture
-> prose

The manuscript outline is therefore not allowed to silently become the research architecture.

This distinction is likely generalizable to research papers, engineering projects, curriculum projects, software projects, and other complex deliverables.

## 7. The reader journey is a distinct object

The Canonical Authority page now explicitly tracks the intended change in reader state.

That journey can be thought of as:

1. encounter the actual problem;
2. understand what kind of question it is;
3. see the relevant heterogeneous response structures;
4. understand what accepting each route commits the argument to;
5. understand what bridge is required to connect native output to the target;
6. distinguish genuine target-specific support from nearby but non-adjudicative authority;
7. understand the present bounded result;
8. understand the broader contribution.

This is not the same thing as a chapter outline.

It is a cognitive dependency structure.

## 8. Roads and route commitments need their own representation

The Canonical Authority work also showed that route names are insufficient.

Each admitted road has at least:

- native content;
- native domain;
- native function;
- commitments introduced by granting the route;
- licensed transfer requirements;
- target-specific consequence.

This means route labels cannot be treated as interchangeable categories.

A project page needs route structure when route-specific commitments materially affect the project's current state or next operation.

## 9. The project page needs a live frontier

A project can have many OPEN coordinates without all of them being active work.

The page therefore needs to distinguish:

- open coordinates;
- dependency frontiers;
- current live frontier;
- next activated operation.

This prevents the page from becoming a flat backlog.

The frontier is a dependency concept.

It identifies the unresolved point with the highest current operational relevance under the project's accepted selection regime.

## 10. The next-work recommendation needs an explicit basis

The repository's project-page contract identifies a common decision record for recommended next work:

- target;
- goal reference;
- spine reference;
- expected gain;
- dependency unlock;
- evidence readiness;
- cost;
- regression risk;
- reversibility;
- blocking status;
- selection basis;
- invalidation set.

This does not imply one universal numerical priority equation.

Different projects can use different legitimate selectors.

The common contract is that the page exposes why the recommendation is next and what would invalidate it.

## 11. Propagation and freshness became part of the architecture

The Canonical Authority appendix makes propagation explicit.

Goal changes can affect:

GOALS
-> intentional-object interpretation
-> goal-spine interpretation
-> page orientation

Spine changes can affect:

SPINE
-> reader spline
-> dependency/frontier display

Research-architecture changes can affect:

RESEARCH_ARCHITECTURE
-> method/result/contribution display

Operational-state changes can affect:

STATE
-> current result / blockers / frontier

Source/provenance changes can affect:

SOURCE_REGISTRY / SOURCE_MODULES / PROVENANCE
-> evidence and closure display

Publication changes can affect:

MANUSCRIPT_CONTRACT / manuscript state
-> deliverable readiness

This implies that a project page needs a freshness model and a propagation map.

## 12. Goal-spine coverage is not active work

The later portfolio goal-architecture work exposed another important distinction.

A registry can contain complete coverage of project goals and their potential spines while many rows remain dormant.

Therefore:

coverage != activation

A represented goal-spine entry becomes unfinished work only when separate activation evidence exists, such as:

- an active workstream;
- an audit campaign;
- a current blocker or next action;
- a material-event route;
- accepted debt work;
- explicit user instruction.

This prevents complete registry coverage from generating synthetic backlog.

## 13. Hierarchy position does not determine semantic type

The goal-architecture work also showed that entries can occupy hierarchy positions while functioning as different intentional/control species.

Possible types include:

- ordinary goal;
- constraint;
- invariant;
- validation task;
- standing mandate;
- maintenance obligation;
- routing/watch function;
- composite object.

This matters because type affects:

- completion;
- maintenance;
- lifecycle;
- priority;
- dependencies;
- permitted mutation.

The project page therefore cannot infer semantic type merely from G0/G1/G2 labels or tree position.

## 14. General project-page contract

A reusable project orientation page can expose:

1. PROJECT ID / STATUS
2. PROJECT GOAL
3. SUCCESS CONDITION / SUBSTANTIVE TARGET
4. PROTECTED SPINE
5. ACTIVE FRONTIER
6. CURRENT RESULT
7. PROTECTED INVARIANTS
8. OPEN COORDINATES
9. NEXT WORK
10. WHY THIS NEXT
11. DEPENDENCY / PROPAGATION NOTES
12. SOURCE MAP
13. REFRESH / FRESHNESS STATE

This is the general interface contract suggested by the Canonical Authority experiment.

The content remains project-specific.

## 15. What belongs in every project versus what remains project-specific

A common interface should standardize the jobs the page performs, not force identical substantive schemas.

Common interface jobs:

- identify;
- orient;
- distinguish authority from derived state;
- show current result;
- show current frontier;
- preserve OPEN;
- explain next action;
- expose propagation;
- expose provenance;
- expose freshness.

Project-specific content can include:

- argument spine;
- engineering architecture;
- experimental design;
- manuscript architecture;
- production artifact;
- source map;
- domain-specific success conditions;
- specialized route systems.

## 16. The project page is itself part of the control architecture

The deepest finding is:

The project page is not an authority source, but it is part of the project's operational control architecture.

Bad orientation can create downstream semantic errors even when the underlying authoritative files are correct.

Therefore project-page defects can be operationally important without being substantive research defects.

The project page deserves its own audit and freshness contract.

## 17. Proposed audit for every substantial project

A project page can be tested using a common battery.

### Identity test

Can a new reader identify the project and distinguish it from neighboring projects?

### Goal test

Can the reader state the highest-level goal without confusing it with the research target?

### Success test

Can the reader identify what result or deliverable constitutes success?

### Spine test

Can the reader identify the protected load-bearing structure?

### State test

Can the reader distinguish current state from history?

### Frontier test

Can the reader identify what is live now rather than treating all OPEN items as backlog?

### Next-work test

Is the next operation explicit?

### Selection-basis test

Can the reader see why that operation is next?

### Propagation test

Can a material source change be traced to every dependent page field?

### Source test

Can every substantive page claim be traced to its authoritative source?

### OPEN test

Does the page preserve unresolved coordinates?

### Type test

Are goal-like, control-like, validation, maintenance, routing, and composite objects distinguished where that distinction changes behavior?

### Non-authority test

Can the page be refreshed without silently mutating the project's authoritative state?

## 18. What this suggests for PD

There are two plausible PD connections.

### A. PD as an evaluator of project-orientation architecture

PD can audit whether a page preserves distinctions required for correct project entry and downstream action.

Candidate targets include:

- goal versus substantive target;
- current result versus next work;
- open coordinate versus backlog;
- canonical source versus derived summary;
- dormant coverage versus activated work;
- research architecture versus reader architecture.

### B. Project orientation as a PD research object

A deeper question is:

What is the minimum task-faithful representation of a project that lets a human or AI identify the correct active objective, constraints, state, and next operation without reconstructing the project from history?

Potential measures include:

- orientation accuracy;
- source traceability;
- semantic loss;
- downstream action accuracy;
- stale-state exposure;
- goal-drift exposure;
- hidden-selector exposure;
- propagation completeness.

This can become a falsifiable research program rather than an undocumented design intuition.

## 19. Connection to existing PD work

The discovery maps naturally onto current PD directions.

PD:G2A
-> source/attribution integrity of displayed information

PD:G2D
-> construction of faithful project-orientation representations

PD:G2R
-> architecture and preservation relations for orientation interfaces

PD:G2U
-> which page capabilities are useful for which project tasks

PD:G3-SPINE
-> representation and preservation of task-relative project spines

PD:G4
-> transfer of the orientation architecture to other active projects

It also connects to the formal fidelity work because a project page can be treated as a representation whose adequacy depends on which task-relevant distinctions it preserves.

## 20. Proposed comparative validation sequence

Do not impose the full Canonical Authority design on every project immediately.

A better sequence is:

1. Select several substantially different projects.
2. Inspect their current entry points.
3. Construct candidate project-orientation pages using the common interface.
4. Run destructive removal tests on individual page fields.
5. Determine which fields are actually load-bearing for each project.
6. Compare common versus project-specific requirements.
7. Test downstream task selection with and without the page.
8. Record which properties are invariant across projects.
9. Promote only the independently supported common contract.

This is also the cleanest way to distinguish genuine architecture from a page style that merely happened to work for Canonical Authority.

## 21. Potential future research question

The strongest candidate question is:

What is the minimum task-faithful orientation representation that lets a user or agent enter a project, identify the correct active objective and constraints, and select the appropriate next operation without reconstructing the project from history?

That question is narrower and more testable than:

"What should every project page contain?"

## 22. Relationship to the other PD retrospective

The recent novel-PD-use retrospective identifies PD expanding into:

- multi-object relation discovery;
- heterogeneous typed connections;
- independent route comparison;
- order robustness;
- prompt semantic preflight;
- architecture discovery;
- information-loss detection;
- OPEN-preserving outputs;
- cross-project transfer;
- experiment design.

The project-page discovery fits that expansion as a new object class:

**project orientation interface**

This means the two reports likely belong together eventually.

The current best hypothesis is:

PD is becoming a general method for auditing and discovering result-sensitive structure across objects, representations, relations, routes, prompts, and architectures.

Project pages are one new test domain for that behavior.

## 23. What belongs in Sort Later now

The following should remain deferred rather than promoted immediately:

- universal project-page schema;
- universal priority formula;
- assumption that every project needs the exact Canonical Authority fields;
- claim that page architecture improves downstream performance;
- claim that the project page is itself a PD primitive;
- claim that all page fields are equally important.

The strongest current claim is narrower:

Canonical Authority exposed a repeatable project-orientation architecture with distinct semantic objects, explicit authority separation, frontier/state separation, propagation requirements, and a source/freshness contract. Its cross-project generality is a testable hypothesis.

## Primary source set

- PROJECT_PAGE_CONTRACT.md
- projects/canonical-authority/PROJECT_PAGE.md
- projects/canonical-authority/PROJECT_PAGE_APPENDIX.md
- ARCHITECTURE.md
- audits/GOAL_ARCHITECTURE_BACKLOG_LEVERAGE_AUDIT_2026-09-22.md
- Canonical Authority project-page evolution commits from 2026-09-23
- goal-architecture workstream and closure records from 2026-09-22
