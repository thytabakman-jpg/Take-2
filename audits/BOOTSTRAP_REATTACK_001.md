# Bootstrap reattack 001

Baseline: bootstrap/kernel-v0 after initial architecture files.

Tools/lenses applied: HF-001 recursive discovery, object typing, hidden-dependency search,
representation attack, result-sensitivity compression, rival clean-sheet reconstruction,
recurrence analysis, spine reconstruction, layered-control challenge, A16 regression,
IC-018/RTC v2, Multi-Object relation challenge, strict-gain and non-regression.

## Findings

1. Initial PD admission was too permissive. A06 had only supported-profile evidence and A08
documented/portfolio support, while the declared stable threshold was repeated or controlled
behavior. Both were demoted to experimental. This is exactly the evidence-status discipline
Take-2 is intended to enforce.

2. Five primitives do not require five registries. A single ledger can preserve their types
while testing whether separate stores are actually needed. Adopted.

3. The plan lacked an executable architectural fitness check. A policy-only kernel would repeat
the legacy control-exists/control-optional pattern. Added a validator at bootstrap.

4. Event and Observation remain potentially reducible. They are retained provisionally because
event = occurrence and observation = evidence about an occurrence/object. The first vertical
slice must test whether this distinction changes behavior. If not, compress them.

5. PD belongs in the kernel, but PD output must not own mutation. This boundary survived all
reattacks.

RTC successor: minimal typed ledger + evidence-tiered PD + executable fitness check dominates
the prose-only bootstrap. Further architecture expansion is blocked pending vertical-slice data.
