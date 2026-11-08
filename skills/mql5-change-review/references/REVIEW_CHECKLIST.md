# Review checklist

Use these as inspection prompts, not presumed defects or universal strategy requirements.

## Identity and inputs
Check version labels, dependencies, input defaults/types/units, enum ordinal changes, SET compatibility, feature flags and disabled paths. Distinguish chart timeframe from internal signal/context timeframe. Include external modules and configuration differences in scope.

## Entry and event flow
Trace OnInit/OnTick/OnTimer/OnTradeTransaction/OnDeinit only where actually present. Check data-ready guards, indicator buffer reads, candle indexing, first-tick behavior, repeated callbacks, new-bar detection and event timestamps. Establish whether decisions intentionally use open or closed bars. Identify timing limits: every tick, each bar, cooldown and rolling/session windows.

Trace position counting and pending-order counting by symbol, magic, side, strategy and cycle as intended. Check admission order when multiple candidates arrive on one tick, partial fills or requests in flight. Do not assume synchronous execution or that request submission guarantees a filled position.

## Execution and ownership
Inspect account netting/hedging assumptions and how ticket/symbol selection affects owned versus external positions. Trace API returns, trade-server result codes, retries, rejected modifications, stale selections and volume/price normalization. Verify semantics against current primary documentation when needed; do not assert one universal accepted result code for all operations.

## Stops and exits
Check side-aware bid/ask handling, price/tick units, stops/freeze constraints, initial SL/TP, BE arming versus moving, offset interpretation, stop monotonicity if required, trailing activation, partial-close residual volume and exit ordering. Verify cost treatment before equating stop price with economic BE.

For a project with recovery/hedge cycles, derive pairing and closure rules from its approved documents; inspect identifiers, orphan positions and exactly when a cycle is considered closed. Do not assume every EA has such a cycle.

## Risk and state
Trace risk bases (initial capital, balance, equity or peak), realized/floating components, deposit handling, daily/weekly/monthly reset timezone and boundary logic. Confirm whether a lock blocks entries, modifies management or closes positions according to approved policy.

Inspect restart/reattach/recompile/input-change persistence: reconstruct positions, pending requests, BE state, last signal time, cooldowns, locks and cycle associations as applicable. A missing persistence mechanism is a defect only when the required behavior needs it.

## Diagnostics
Check that logging flags do not change decisions, that events identify run/version/position, and that file or logging failures have the documented effect. Check array bounds, resource/handle release, blocking operations, full-history scans and per-tick cost where code supports a concern.
