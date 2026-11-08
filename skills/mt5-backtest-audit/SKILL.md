---
name: mt5-backtest-audit
description: Audit MetaTrader 5 Strategy Tester reports and compare EA backtests using actual HTML/XLSX/CSV reports, SET inputs, logs and version identities. Use for Persian or English requests to analyze tester results, compare runs, reconcile trades, investigate SL versus break-even, drawdown or diagnostic mismatches, and decide whether evidence supports a claimed improvement.
---

# MT5 Backtest Audit

Respond in the user's language; default to concise Persian for this user. Lead with whether the supplied evidence supports the comparison, then show important numbers and the next concrete action. Never invent missing performance statistics or execution history.

## Establish scope and provenance

Apply project-documentation-governance when working in a repository; read applicable instructions and preserve protected versions, presets and original evidence. Use existing connected files and the current named artifacts before asking for reuploads. Never mix independent EA projects or import the user's past positions.

Read [evidence protocol](references/EVIDENCE_PROTOCOL.md) for every audit and [reconciliation rules](references/RECONCILIATION.md) for trade-level or P&L questions. Use [report format](references/REPORT_FORMAT.md) to structure findings.

Inventory each supplied report, log, SET, CSV and source/binary with its exact filename and a content hash where feasible. Record run identity separately from artifact identity. A filename/version label alone does not prove which binary generated a report. Redact account identifiers and credentials in shared outputs.

Extract actual tester inputs from the report first. Compare exported SET, source defaults and report inputs as separate evidence; never treat a reconstructed SET as an original export. Read spreadsheets/PDFs with their relevant skills when applicable. Detect encoding, delimiter, decimal and date conventions before parsing; preserve raw values.

## Audit and compare

Build a side-by-side run matrix covering instrument and contract, broker/server, account currency and initial capital, dates, model/history quality, signal and chart timeframes, execution/cost assumptions, EA identity and effective inputs. Mark each field VERIFIED, MISMATCH or UNKNOWN with its source. Call a run matched only for fields actually established; explain how mismatches limit conclusions.

Use MT5 backtests and their outputs as the evidence for trading performance. Parsing/reconciliation scripts may inspect those outputs but must not substitute a Python trading simulation for MT5. Do not require an invented fixed history-quality threshold: use project-approved acceptance gates and report actual quality/gaps.

Extract only supported metrics: net/gross results, PF, trade counts, wins/losses, balance/equity drawdown, exposure and holding times when timestamps exist. Keep report-derived, independently recalculated and unavailable metrics distinct. Inspect large losses, drawdown episodes, long-held positions and missing diagnostic spans when evidence permits.

Explain what changed, what stayed matched and what remains unknown. Do not attribute a performance difference to one input when multiple inputs or conditions changed. Treat a favorable exposed-sample result as a research observation, not proof of robustness, live suitability or permission to promote.

## Close the audit

Separate verified facts, supported inferences and unresolved questions. State whether evidence is sufficient for the specific claim, partially sufficient, or insufficient; these are audit conclusions, not investment ratings. Give the smallest concrete next test or missing artifact that resolves the material uncertainty. Never claim compilation, tester execution or live checks unless observed.

Update only affected project documents and preserve evidence. Do not alter EA source, presets, orders, running terminals or protected artifacts for an audit. Test execution, source changes and publication require authorization within the actual task. Follow existing user authorization rather than adding blanket approval steps.
