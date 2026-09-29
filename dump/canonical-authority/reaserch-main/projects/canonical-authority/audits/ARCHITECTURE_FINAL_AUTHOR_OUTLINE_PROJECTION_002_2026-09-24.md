# Canonical Authority — Final Architecture for Clean Review Outline 002

Date: 2026-09-24
Status: EXECUTED / FINAL PROJECTION ARCHITECTURE
Target: clean review outline

## Architecture

ResearchState
-> InternalBlueprint
-> CleanReviewOutline
-> UserApproval
-> ProseManuscript

## Object responsibilities

### InternalBlueprint

Owns:
- readiness;
- claim lifecycle;
- evidence ownership;
- production routing;
- synchronization;
- reopen rules;
- control metadata.

### CleanReviewOutline

Owns:
- paper goal and question;
- exact section order;
- all twenty-one substantive movements;
- what each movement says;
- human-readable source anchors;
- what each movement earns;
- section transitions;
- contribution hierarchy;
- bounded novelty/scope.

It does not own:
- tool/control machinery;
- research authority;
- registry state;
- liveness/runtime semantics.

### ProseManuscript

Owns:
- sentences;
- paragraphs;
- quotations;
- citations;
- stylistic realization.

## Projection rule

The clean outline preserves every content decision that can change what the paper says.

It removes every internal control detail that does not affect the author's decision about
what the paper should say.

## Completion rule

CleanReviewOutline is complete when:
1. all seven sections have fixed jobs;
2. all twenty-one movements have fixed substantive content;
3. evidence/source anchors are allocated;
4. all major contribution locations are fixed;
5. no unresolved planning choice remains that would change argument order or intended claim;
6. remaining work is prose/citation realization or genuinely external evidence closure.

## Sync rule

Refresh CleanReviewOutline only when a material upstream delta changes:
- section/movement structure;
- intended substantive claim;
- source placement;
- scope/result;
- contribution hierarchy.

Backend-only tool/control changes are certified NO_EFFECT.

## User approval

Approval means:
"this is the paper plan to write."

It does not mean:
"the paper is already submission-ready."

## Architecture verdict

The clean review outline is a strict-gain terminal planning surface and fixes the recurrence
identified by whole-chat root cause.

Next:
Improvement Core realizes the object and re-routes current state to it.
