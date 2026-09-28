# JHB Structured-YAML Mutation Boundary Repair

Date: 2026-09-22
Workstream: WS:2026-09-22:JHB-STRUCTURED-YAML-SAFETY
Mode: bounded infrastructure repair before further Sukkos structural work

## Result

The immediate structured-control dependency for Sukkos/JHB work is repaired without
redesigning the JHB project or splitting the portfolio control files.

The repair adds one transactional mutation boundary for consequential YAML state and
tests it against the actual JHB control shapes used by the current Sukkos work.

## Implemented boundary

`tools/structured_yaml_mutate.py` now requires or enforces:

1. parse the current YAML object;
2. resolve the exact structural target, including list selectors that must match exactly once;
3. verify the expected current value before set/delete;
4. optionally verify the full file SHA-256 read at transaction start;
5. mutate the parsed object rather than raw YAML text;
6. serialize a candidate with round-trip YAML handling;
7. reparse the candidate independently with ruamel.yaml and PyYAML;
8. reject semantic changes outside the declared target paths;
9. compare the current file hash again immediately before write;
10. use atomic local replacement and reparse after transport.

The engine also rejects ambiguous selectors, stale value preconditions, stale file hashes,
unsupported operations, missing exact targets, and duplicate append identities when an
absence precondition is supplied.

## Sukkos/JHB coverage

`tools/check_structured_yaml_mutation.py` runs mutation probes on temporary copies of:

- JHB root STATE;
- Fick STATE and ACCEPTANCE;
- Keva STATE and ACCEPTANCE;
- Conservation STATE and ACCEPTANCE;
- JHB ARTIFACTS;
- JHB PROVENANCE;
- WORKSTREAMS using exact workstream-ID selection;
- PORTFOLIO_EVENT_LEDGER using exact event-ID selection.

The existing JHB booklet-local control validator remains separately active. The new
regression is about mutation safety, not booklet truth or product acceptance.

## CI and policy integration

The portfolio workflow now installs `requirements.txt`, including the round-trip YAML
dependency, and runs the new structured-mutation regression.

`WORKSTREAM_POLICY.md` now prohibits raw append, indentation-sensitive insertion, and
broad textual replacement for consequential load-bearing YAML changes. A transport that
cannot execute the utility before write must use an isolated candidate branch or
equivalent surface, verify the exact semantic delta and full integrity suite, and only
then advance authoritative state.

## Verification

Commit 74801fbcc5de34a4251a15cb3d7fc38095bdef0b passed Portfolio integrity run 35795923618.

The run included:

- all existing portfolio structural checks;
- JHB Fick product-acceptance wiring;
- JHB booklet-local control checks;
- the new structured-YAML mutation regression;
- the remaining PD/portfolio regression suite.

Result: PASS.

## Scope deliberately not expanded

This repair does not decide whether WORKSTREAMS.yaml is too large, whether it later
needs hot/warm/cold partitioning, or whether run-to-terminal execution needs a separate
controller. Those are distinct architecture questions.

No JHB content architecture, learner route, artifact acceptance, or canonical goal was
changed.

## Operational consequence

Further Sukkos structural work can proceed after this closeout. The immediate dependency
is no longer “do not touch YAML until the architecture is redesigned.” It is “use the
transaction boundary or isolated-candidate equivalent whenever consequential structured
state is changed.”
