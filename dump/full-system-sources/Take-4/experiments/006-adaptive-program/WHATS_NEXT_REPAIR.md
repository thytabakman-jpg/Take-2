# ICC Repair — What's Next Control Semantics

Date: 2026-09-24

## Problem ICC found from the conversation

The protocol correctly added the question "What's next?" but operational use repeatedly converted it into meta-commentary.

Failure pattern:
decision/result -> ask What's next? -> describe candidate frontier -> explain why that frontier is interesting -> stop and return control to user.

That violates the intended autonomy semantics.

The underlying ambiguity was in the charter itself. It said the question "returns control to ICC" but did not require the answer to be an executable selection followed by execution. The output discipline also requested a "next autonomous decision" while the program handoffs sometimes deliberately left candidates unselected. This licensed descriptive answers.

## Repair

Define:

WHY = explanation probe.
WHAT'S NEXT = control-transfer operator.

Operational semantics:

Next(Z_t) -> a_{t+1} | Program_{t+1} | terminal_status.

After Next returns a licensed nonterminal continuation, execution follows immediately:

Z_t --Next--> a_{t+1} --Execute/Verify--> Z_{t+1}.

A list of candidates is not a valid answer unless the selected continuation is itself "run a discriminator over this plural frontier."

"Reconstruct the frontier" is not sufficient as the terminal answer. ICC reconstructs it and then selects/executes.

"Interesting because..." is never the content of What's next. That belongs to Why.

## Why?

Because the earlier wording separated decision autonomy from execution continuity. ICC could make a next-decision-shaped statement without crossing the final boundary into acting on it. The observed conversation repeatedly hit exactly that gap.

## What's next?

Take the current Program 006 Generation-1 handoff, independently reconstruct the live frontier, select the next licensed program slice, and execute it now.
