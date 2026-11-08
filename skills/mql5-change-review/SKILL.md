---
name: mql5-change-review
description: Review and compare MQL5 Expert Advisor source versions, includes and input settings. Use for Persian or English requests for line-by-line EA comparison, behavioral regression review, entry/exit or concurrency changes, stop-loss/break-even logic, risk controls, restart recovery and a focused MT5 verification plan.
---

# MQL5 Change Review

Respond in the user's language; default to concise Persian for this user. Lead with concrete findings and behavioral consequences. Separate static findings from compiler results and observed MT5 behavior.

Apply project-documentation-governance for repository work. Inspect applicable instructions, approved requirements, protected files and current edits. Resolve named versions from actual files/refs; never infer behavior from a filename or prior chat summary alone.

Read [review checklist](references/REVIEW_CHECKLIST.md) for all reviews and [acceptance plan](references/ACCEPTANCE_PLAN.md) before defining verification. Read relevant local includes, classes, enums and input declarations; report missing dependencies and do not fabricate their behavior.

## Compare actual behavior

Record baseline/candidate identities, exact refs/paths and hashes when feasible. Compare raw text and semantic changes, including source defaults, enum numbering, SET mappings, disabled feature branches and version/build labels. Treat a claim of byte identity as requiring actual byte/hash comparison.

Trace changed inputs through event handlers, helper calls, state transitions and order/position effects. For each meaningful difference, show baseline behavior, candidate behavior, trigger conditions, affected scope and evidence location. If asked line by line, cover all changed hunks and classify cosmetic versus behavioral; do not claim complete coverage after sampling.

Prioritize position ownership and account mode, entry admission/concurrency, closed-bar timing, trade-result handling, initial and moved stops, partial exits, recovery pairs, risk locks and reinitialization. Compare only against this project's approved rules; never import unrelated hedge-cycle or BE requirements.

Find credible defects with a concrete path or counterexample. Label uncertain issues as hypotheses and state what would confirm them. Do not present a generic checklist as discovered bugs. Distinguish a breaking behavior change from an authorized intentional change.

## Verify without overclaiming

Use compiler/static inspection for syntax and structural evidence; use actual MT5 tester outputs for runtime/performance claims. Consult primary MQL5 documentation when API semantics are uncertain. A locally rewritten simulator is not proof of MT5 behavior. Do not launch/connect/restart a trading terminal, attach an EA or alter orders merely to complete a source review.

Provide a targeted verification matrix tied to changed behavior. State what was actually run, result and artifact; mark other checks NOT_RUN or BLOCKED. Source review alone cannot establish profitability or full runtime equivalence.

## Deliver

Present findings by severity with file/line or function evidence, trigger, consequence and suggested correction. Include a compact behavior-difference table, missing dependencies, and concrete next MT5 test when useful. State explicitly when no defect was established within reviewed scope.

Keep review read-only unless fixes are authorized. For authorized fixes, preserve unrelated edits and protected references, update affected documentation and verify the change. Honor existing authorization without repeatedly asking. For this user, provide a complete updated source file when changes exceed five lines; use a patch for five lines or fewer unless the request specifies otherwise. Save user-facing artifacts through the applicable persistence workflow; do not auto-publish project changes.
