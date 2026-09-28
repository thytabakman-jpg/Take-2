# Project Entry Binding Regression Pack — Fick

Date: 2026-09-23
Status: frozen regression specification
Target: projects/jewish-holiday-booklets/fick/PROJECT_ENTRY.yaml

## Positive resume cases

Each utterance must bind to RESUME_PROJECT and require SHOW_CURRENT_FOUR_PAGES before ordinary substantive project discussion.

1. "Let's work on Fick."
2. "Continue Fick."
3. "Go back to the Fick booklet."
4. "Let's pick up where we left off on Fick."
5. "Work on the booklet." when Fick is the active/referenced booklet.

Expected authority chain:
Fick PROJECT_ENTRY.yaml
-> Fick STATE.yaml continuation_bindings.current_canonical_set
-> JHB:FICK:CANONICAL-PAGES:003
-> ARTIFACTS.yaml source set
-> C3 P1, P2, P3, P4
-> exact current page-image acquisition
-> display in page order.

## Negative/control cases

6. "What is Fick's First Law?"
Expected: DISCUSS_PROJECT/general factual answer; do not force booklet display merely because the word Fick occurs.

7. "Audit the current Fick booklet."
Expected: AUDIT_CURRENT; bind canonical set 003 as audit target. Display only when the audit requires visual observation.

8. "Edit Page 3 of Fick."
Expected: EDIT_CURRENT; resolve canonical set 003 and current P3 edit source before proposing/executing mutation.

## Fail-closed cases

9. Canonical source-set record missing.
Expected: authority-resolution blocker. No W2/baseline/chat fallback.

10. Canonical page bytes unavailable.
Expected: identify exact acquisition blocker/page objects. Do not replace required images with prose reconstruction.

## Regression target

The original observed failure is closed only when case 1 produces the declared entry action rather than a prose explanation of what the current frontier is.

This pack tests entry binding. It does not by itself establish that a given chat runtime has automatic access to Library image bytes; byte acquisition remains a separate execution dependency.
