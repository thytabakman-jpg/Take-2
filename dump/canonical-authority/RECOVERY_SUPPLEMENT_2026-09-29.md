# Canonical Authority Lost-Idea Recovery Supplement

Date: 2026-09-29
Target: Take-2
Source: thytabakman-jpg/Reaserch

## Purpose

This supplement closes a semantic-preservation gap in the original Canonical Authority import.

The original import correctly preserved:
- 133 project files
- 24 external Canonical Authority audits
- Issue #71 and its comments
- metadata/body records for 19 Canonical Authority-related PRs

However, file/hash completeness does not by itself prove preservation of adjacent control-plane ideas. A second pass found Canonical Authority-relevant material in delegated backend Issue #70 and delegated PD-backend Issue #72. Those records are now preserved verbatim under `github-ledger/adjacent-control/`.

## Recovered ideas

### 1. Conversation-to-repository capture is an observability boundary

A repository validator cannot prove that a material chat event was captured when the event never entered the repository.

Recovered implication:
- capture completeness requires a durable recognition-time receipt or reconciliation boundary;
- repository-only structural validation is insufficient;
- uncaptured material semantic content, decisions, findings, obligations, tool results, and OPEN coordinates must not silently disappear.

This directly explains why a file-perfect migration can still lose thought.

### 2. Three recursion layers are distinct

Recovered distinction:
1. HF-001 recursion: reopen discovery when dependency, representation, or job state changes.
2. Capability-owned feedback: repeat one typed capability over successor states.
3. Multi-Object recursive extension: repeat relation analysis over a transformed relation state.

These are not interchangeable instances of “recursive PD.” Collapsing them loses trigger and responsibility semantics.

### 3. Reusable typed receipts with invalidation conditions

A higher-order result across Task Entry, ImprovementCore, AuditCore, semantic triggering, and verification identified orchestration duplication as a larger compression frontier than deletion of analytic capabilities.

Recovered candidate:
- preserve typed jobs;
- carry reusable semantic, selection, challenge, and verification receipts across boundaries;
- reuse a prior result while its frozen coordinates remain valid;
- rerun only when an authority, representation, dependency, job, or other load-bearing coordinate invalidates it.

Associated removal test:
A downstream PD invocation is removable when the semantic job was already discharged upstream under still-valid coordinates, no new result-sensitive coordinate appears, no relevant state change invalidates the prior result, and ablation preserves downstream behavior.

### 4. Currentness is separate from capability quality

Historical/candidate IC versions can be compared for feature recovery, ancestry, and falsification, but runtime authority cannot be inferred from which version looks strongest or newest.

Current selector/authority remains a separate coordinate.

### 5. Backend architecture repeats four job boundaries

Across Semantic Integrity, Task Entry, ImprovementCore, TransferCore, Capture, and unfinished-work machinery, the recurring pattern is:

detect/type → select/route → semantic operation → authority/verification

Apparent overlap is legitimate when different layers own different jobs. Harmful overlap begins when two layers claim the same selection, semantic adjudication, or authority function.

### 6. Transfer discovery is bidirectional; transfer edges remain directional

Recovered TransferCore result:
- individual source→target transfer relations remain directional;
- source discovery around a need can search inbound;
- verified results can trigger bounded outbound target discovery;
- integration effects feed back into later search/selection evidence.

The missing behavior identified in #72 was systematic bounded discovery and feedback wiring, not basic TransferCore relation semantics.

### 7. Search must stay bounded

The recovered transfer analysis rejects “scan every source against every project.”

Search is localized by:
- explicit goals and dependencies;
- transfer watches;
- source/target type compatibility;
- current frontier or bottleneck;
- bounded relational/Multi-Object analysis.

### 8. Canonical Authority research and backend maintenance have separate owners

Recovered owner split:
- Issue #71 owns substantive Canonical Authority research.
- Issue #70 owns architecture side-effects, maintenance, CI/recovery, capture, reconciliation, and implementation verification.
- Issue #72 owns PD-backend research/recommendation and hands implementation packets to #70.

This prevents the research workstream from silently becoming its own maintenance runtime.

### 9. Red-baseline evidence cannot cleanly attribute candidate failure

A recovered backend lesson states that candidate branch failures cannot be interpreted cleanly when the baseline is already red.

Generalized preservation rule:
- establish a trustworthy baseline before attributing regression;
- separate pre-existing failure from candidate-introduced failure;
- do not interpret attractive semantic design as merge evidence.

## PR discussion recovery check

The discussion timelines for the 19 PRs already listed in `canonical-authority-pr-index.json` were checked using the combined GitHub PR conversation/review timeline.

Checked PRs:
1, 2, 3, 5, 9, 13, 14, 18, 30, 39, 40, 41, 50, 89, 107, 128, 133, 144, 154.

Result:
- no additional issue comments
- no inline review comments
- no review submissions

Therefore no additional PR discussion text was available to recover beyond the preserved PR bodies/index.

## Added source records

- `github-ledger/adjacent-control/issue-70.json`
- `github-ledger/adjacent-control/issue-70-comments.json`
- `github-ledger/adjacent-control/issue-72.json`
- `github-ledger/adjacent-control/issue-72-comments.json`

## Status

RECOVERY PASS COMPLETE for currently discoverable Canonical Authority-specific and directly adjacent control-plane records in Reaserch.

This supplement does not overwrite the imported project authority files. It preserves newly recovered semantic context alongside them so later Take-2 ingestion can distinguish:
- canonical project authority;
- execution/control context;
- recovered ideas;
- candidate architecture;
- OPEN dependencies.
