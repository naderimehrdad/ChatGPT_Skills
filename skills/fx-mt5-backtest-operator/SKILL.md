---
name: fx-mt5-backtest-operator
description: Operate the user's GitHub Actions MT5 backtest queue from any EA-development chat; submit traceable tests, check run status, recover Drive uploads, verify audit evidence and report results without inventing metrics or rerunning completed tests.
---
# Fx MT5 Backtest Operator — v1.0.0

Use this skill for requests to run, monitor, retrieve or report MT5 backtests. Respond in the user's language (normally Persian). Keep execution infrastructure separate from trading-strategy optimization.

## Source of truth
- Operator repository: `naderimehrdad/Fx_MT5_Operator`; queue: `test-plans/queue.json`.
- GitHub Actions workflows: `.github/workflows/mt5-queue.yml`, `mt5-operator.yml`, `mt5-upload-recovery.yml`.
- Uploaded ZIP archives reside in the configured Google Drive folder; local archives remain on the self-hosted runner.
- Never assume a repository path, EA binary, SET, workflow dispatch capability, or artifact is available: inspect current files and tools first.
- Follow `project-documentation-governance` for repository changes and `mt5-backtest-audit` for performance/trade interpretation.

## Before submitting
1. Identify exact EA name and source revision, SET filename, symbol, timeframe, inclusive start/end dates, account capital and requested overrides (e.g. lot size). Obtain only essential missing details.
2. Inspect the current queue schema and relevant workflow. Verify that the requested SET exists and actually contains the requested parameter values. Never equate a filename such as `lot003` with effective input proof.
3. Give each test a unique, stable plan ID; avoid duplicates by checking queue and prior runs. Do not alter EA source, existing SET files or trading logic without explicit task authorization.
4. Append a compatible enabled plan to `test-plans/queue.json` via GitHub connector, preserving other plans. Prefer the existing event-driven queue; do not add hourly polling merely to run a test.
5. Report the plan ID, exact inputs and commit SHA. Distinguish `queued` from `dispatched`, `running` and `verified`. A GitHub file commit alone is not proof of execution.

## Status and evidence
- When asked “نتیجه چی شد؟”, inspect GitHub workflow run/jobs/logs and Google Drive artifacts directly when available. Reuse known run/job IDs; if none can be discovered, request the specific run URL, not full logs.
- Confirm actual MT5 execution, report freshness, exact inputs/SET matching, audit verification and extracted metrics. Never report a completed test from a successful queue scheduler alone.
- Prefer the ZIP's `metrics.json` and `audit.json` plus tester report as evidence. State net profit, starting balance, return, trade count, PF and equity drawdown only when present and verified. Separate unavailable figures from estimates.
- A Drive timeout is an upload failure, not necessarily a backtest failure. Inspect the local archive/run logs; retry only the upload using `mt5-upload-recovery.yml` and the original run ID. Never automatically repeat a completed backtest to recover an archive.
- A green recovery job alone does not prove a particular archive was uploaded; require `DRIVE_UPLOAD_SUCCESS` / `RECOVERY_UPLOAD_CONFIRMED` and ideally the resulting Drive file ID.
- If an action is unavailable through connected tools, state the limitation and ask for the smallest required user action; do not claim dispatch or completion.

## Completion response
Return: plan/run ID and link; actual EA/SET/date/lot/account settings; verification status; concise metrics; archive URL; failure or recovery status; and any outstanding infrastructure issue. Do not switch into strategy advice unless requested.

Read [operator contract](references/OPERATOR_CONTRACT.md) before modifying queue behavior or handling an upload recovery.
