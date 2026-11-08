# Reconciliation rules

## Trades and positions

Identify whether rows are orders, deals, positions, events or summaries. Do not count every deal as a completed trade. Inspect schema and EA accounting before grouping: netting/hedging mode, partial fills, partial closes and reversals can change position aggregation. Use position identifiers and order/deal relationships when present. A ticket match between separate runs is not required; use a documented signature such as symbol, side, entry time, entry volume and price, with explicit tolerances.

Pair trades deterministically and report unmatched or ambiguous cases. Do not silently discard duplicates. Keep open positions, pending orders, canceled orders, forced end-of-test closure and ordinary strategy exit distinct.

## Profit and break-even

Reconcile realized profit, commission, swap and fees exactly once, after confirming each field's meaning and sign. Include entry-side charges when the schema allocates them there. Account for balance operations, deposits/withdrawals and open equity before comparing trade sums to report totals. Display rounding is not full-precision equality; declare a justified tolerance.

An SL exit reason does not distinguish initial stop from a stop moved to BE. Trace entry, stop modifications, exit price, side and available costs. Report price-level BE separately from economic net BE and from the EA's configured BE label. A small loss can be costs/slippage; do not reclassify without evidence. Do not carry a fixed BE offset from another project.

## Drawdown and time

Keep balance/equity, absolute/relative/maximal drawdown and currency/percentage separate. Percentages depend on the relevant peak/base; do not divide every drawdown by initial capital. Closed-trade balance curves cannot reconstruct intratrade equity drawdown. A sampled graph may miss extrema.

Compute holding-time summaries only from verified entry/exit timestamps, handling partially closed positions explicitly. Label units, sample count and missing values. For diagnostics coverage, distinguish absent export, deliberate disabled logging, initialization failure, warmup/filter suppression and no-trade periods; silence alone proves none of them.

## Reproducibility

State source/binary/settings/report provenance separately. Matching headline metrics or trade counts does not prove identical trade paths or diagnostic event ordering. Keep observed equalities and remaining mismatches explicit.
