# Canonical Authority — Affirmative-First Regression Repair

Status: FIXED / REGRESSION GATE ADDED  
Date: 2026-09-30

## Failure observed

The manuscript contained:

> Ramban does not merely offer a different emphasis. He directly attacks that supporting generalization...

This violates the project's affirmative-first prose rule by forcing the reader through a rejected frame before stating the actual claim.

## Why it happened

The affirmative-first rule already existed in `PARAGRAPH_CONTROL_MAP.md`, but it existed as a prose instruction rather than an acceptance condition.

Later manuscript passes protected:

- source fidelity;
- logical validity;
- claim strength;
- boundedness;
- architecture;
- regression of earned claims.

They did not run an explicit sentence-shape check after mutation.

As a result, conventional academic contrast templates such as:

- not merely X; Y;
- not X, but Y;
- does not X. It Y;
- is not X; rather Y

could pass semantic verification even though they violated the project's prose architecture.

This was a **constraint-propagation failure**, not a content failure.

## Repair

The quoted sentence now reads:

> Ramban directly attacks that supporting generalization, citing cases such as Yeshayahu 46:10 and Devarim 33:21 where *reishis* does not function as Rashi's universal premise requires.

Five additional rhetorical negative-first constructions were also rewritten into affirmative-first form.

## Permanent gate

The global prose rule has been promoted to a mandatory acceptance gate.

Every future prose-changing pass must:

1. state the affirmative claim first;
2. scan changed prose for negative-first contrast forms;
3. retain a negative-first form only when the negation itself is the proposition under analysis or otherwise carries load-bearing logical content;
4. fail verification when rhetorical negative-first framing is introduced without such a reason.

The gate applies to:

- section rewrites;
- architecture repairs;
- claim-strength repairs;
- currentness propagation;
- compression passes;
- closure passes;
- and later cut passes.

## Allowed negation

Negation remains allowed when it carries the actual logical content.

Example:

> First, the tradition does not guarantee correctness on the disputed matter.

That sentence states one branch of the correctness-scope trilemma. Recasting it affirmatively would change the proposition being analyzed.

## Final verification

Post-repair scan found no remaining rhetorical negative-first contrast matching the prohibited family.

Remaining automated hits are either:

- ordinary phrase structure such as “one rival rather than the other”;
- logically load-bearing negation;
- or isolated protective negation that is not followed by a positive restatement of the same claim.
