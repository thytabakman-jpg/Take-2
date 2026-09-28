---
applyTo: "projects/jewish-holiday-booklets/**"
---

# Jewish Holiday Booklet local instructions

Keep root booklet architecture, booklet-local state, task binding, artifact identity,
and product acceptance distinct.

## JHB runtime bootstrap

Resolve the task target before broad file/history search.

Use:

```
python tools/jhb_booklet_context.py --booklet <booklet-or-alias> --operation <operation> --json
```

Operation mapping:

- "show/work on the current pages" -> `show_current`
- "edit the current pages" -> `edit_current`
- "audit the current pages" -> `audit_current`
- "package the current pages" -> `package_current`
- "show the repair baseline" -> `show_baseline`
- "compare current to baseline" -> `compare_current_to_baseline`
- "show the accepted final product" -> `show_accepted_product`

For an explicit current-turn designation of a registered source set, add
`--source-set-id <set-id>`. For a substantial branch continuation, add
`--workstream-id <workstream-id>`.

For artifact-sensitive work, add `--require-exact-artifact`.

The generated `task_binding` is execution-local and non-authoritative. It selects the
registered target for this request without changing acceptance. Durable continuation
belongs to WORKSTREAMS when a substantial branch exists; explicitly promoted defaults
belong to booklet/project state; exact identity/class/lineage remain in ARTIFACTS.

Precedence:

1. explicit current-turn designation;
2. explicit workstream binding;
3. explicitly promoted booklet/project default;
4. OPEN / one targeted clarification.

Never use search ranking, filename similarity, recency, PDFs, composites, or visual
coherence as a target selector.

When resolution is EXACT, retrieve only the returned registered objects and verify their
locators/hashes. When resolution is OPEN/BLOCKED, fail closed.

For Fick / Difference:

- accepted repair baseline: `JHB:FICK:ACCEPTED-PAGES:001`
- promoted default current working set: `JHB:FICK:WORKING-PAGES:002`
- accepted final product: OPEN

The current working set is a candidate target, not a product-acceptance transition.

For Keva and Conservation, preserve unresolved artifact/continuation identities as OPEN
until a registered set and licensed binding exist.

Treat product acceptance separately from structural/runtime integrity.

Do not change canonical goals without the repository goal-approval procedure.

## Image-generation and visual-edit preflight

For any request to generate, regenerate, visually redesign, or locally edit a booklet page,
read and apply:

`projects/jewish-holiday-booklets/IMAGE_GENERATION_PROTOCOL.md`

before invoking image generation.

Hard generation invariants:

- resolve the exact booklet task target first;
- preserve the distinction between a coordinated four-page generation episode and a one-canvas composite;
- for major booklet creation/recomposition, coordinated batch generation is permitted and preferred when booklet-level coherence is part of the target;
- a coordinated batch must return four distinct full-size PAGE_ID outputs, exactly P1/P2/P3/P4 once each;
- never accept a four-page contact sheet, four miniature pages on one canvas, or four variants of one page as the booklet output;
- after a useful batch exists, freeze passing pages and default failed pages/regions to bounded local editing;
- rerun the full batch only for a demonstrated set-level defect;
- freeze the route map, Booklet Batch Manifest, shared style contract, four page blueprints, asset pack, and two-level acceptance matrix before coordinated generation;
- freeze preservation ledgers and licensed deltas before local repair;
- verify both page-level and set-level invariants before packaging.

For Fick, preserve the distinction between `JHB:FICK:WORKING-PAGES:002`,
`JHB:FICK:ACCEPTED-PAGES:001`, and accepted product OPEN.
