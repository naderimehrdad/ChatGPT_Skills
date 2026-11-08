# Acceptance and reporting

## Finding schema

For each finding record severity, exact source location, concrete triggering sequence, observed or statically derived consequence, applicable requirement, evidence and proposed correction. Severity describes impact, not confidence. State confidence separately. Do not call an intentional policy change a defect solely because it changes results.

For semantic differences use: area | baseline | candidate | trigger | expected consequence | verification status. Track all changed hunks for an exhaustive comparison. When includes or binaries are missing, name the boundary of coverage.

## Focused verification matrix

Select applicable cases rather than mechanically requesting every test:
- Compile the exact candidate plus includes with recorded compiler/build and observed log.
- Run a matched MT5 baseline/candidate comparison for unchanged behavior; define intended differences before evaluation.
- Test admission at zero/one/limit positions, pending/in-flight requests and repeated same-bar events when concurrency changes.
- Test stop transitions in both directions, rejection handling and partial exits when management changes.
- Test calendar boundaries, entry blocking versus existing-position management, and persistent state when risk logic changes.
- Test restart/reattach with open positions only in an authorized isolated tester/demo environment, never by operating an unrelated running terminal.

Record exact symbol/contract, dates, model/data quality, costs, timeframe, effective inputs, source/binary identities and artifacts. Do not choose fixed pass thresholds without approved requirements. Use mt5-backtest-audit for tester evidence and trade reconciliation.

Label each check PASS/FAIL only after actual execution and inspection. Use NOT_RUN/BLOCKED otherwise. Static argument, local unit harness, MT5 tester and broker/demo observation are distinct evidence levels; one cannot silently replace another.

Never use live orders to verify a source review. Do not certify full equivalence from matching headline metrics or counts. Do not certify live readiness or approve promotion from exposed-sample profitability.

## Delivery

Lead with the highest-impact supported finding. If none is established, state reviewed scope and verification limits. Include actual tests and the next smallest useful test. Preserve frozen artifacts and existing edits. Review authorization alone does not authorize fixes, defaults changes, publication or deployment; implementation authorization can include necessary reversible fixes without repeated permission requests.
