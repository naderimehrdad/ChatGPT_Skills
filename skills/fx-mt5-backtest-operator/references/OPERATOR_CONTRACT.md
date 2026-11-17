# Operator contract — v1.1.0

## Queue submission
Repository `naderimehrdad/Fx_MT5_Operator`, file `test-plans/queue.json`, `schema_version: 1`, `plans` array. Each plan requires a unique `id`, `enabled`, `mode: backtest`, `expert`, `set_file`, `symbol`, `period`, `from_date`, `to_date`. Dates use `YYYY.MM.DD`. Confirm fields against the live workflow before submitting; workflow capabilities may change.

The queue scheduler is a dispatch mechanism; success only means the request was submitted. Backtest success requires the downstream MT5 Operator run and its verified audit. A completed plan is not automatically evidence of successful Google Drive delivery.

## Lifecycle
`REQUESTED -> QUEUED -> DISPATCHED -> MT5_EXECUTED -> AUDIT_VERIFIED -> ARCHIVED_LOCAL -> UPLOAD_CONFIRMED`.
If Drive is unreachable, retain `ARCHIVED_LOCAL / UPLOAD_PENDING`. Do not confuse it with `MT5_FAILED`. A run may have multiple upload attempts but only one backtest execution.

## Recovery
Workflow `mt5-upload-recovery.yml` accepts optional `run_id`. Supplying the original run ID targets that archive; omitting it may retry a limited number of pending ZIPs. Verify actual log markers `RECOVERY_ARCHIVE`, `DRIVE_UPLOAD_SUCCESS`, `RECOVERY_UPLOAD_CONFIRMED`, `UPLOAD_QUEUE_EMPTY`. Never infer upload success from green workflow status alone. Keep credentials, token files and account IDs out of logs and shared artifacts.

## Evidence / report
Record exact GitHub run URL, archive filename and Drive file ID. Read `audit.json`, `metrics.json`, and tester outputs. Verify requested lot size against effective inputs, not filename. Report only observed values; do not infer risk or P&L from recovery logs. Treat audit as evidence of matching settings, not proof of live-trading suitability.

## Permissions
GitHub and Drive connector availability differs across chats. If dispatch cannot be invoked directly, committing an enabled plan to the event-driven queue is the supported path when confirmed by the current workflow. Do not invent a workflow dispatch action. Never change or rerun a test solely to recover its ZIP.

## History preflight / real ticks
For real-tick requests (`tick_model: 4`), preserve the requested model. The runner writes `history-preflight.json` with symbol, range, effective model and MT5 tester journal classification. `TESTER_REQUIRED` is not proof of historical coverage; `HISTORY_UNAVAILABLE` is a hard failure. Inspect `tester-history.json` and the original tester journal. Classify missing broker history vs network/synchronization failure only if the log proves which. The isolated terminal must be used for any remediation; never manipulate a live MT5 instance. Do not claim an automatic tick-history download was completed without a verified journal record.

If the MT5 execution fails due to history, keep its ZIP as failure evidence. Do not mark the queue plan completed or report trading performance. A successful Google Drive upload of diagnostic artifacts is not an audited backtest.
