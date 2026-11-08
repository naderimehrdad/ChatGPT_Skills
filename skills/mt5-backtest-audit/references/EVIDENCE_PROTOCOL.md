# Evidence protocol

## Minimum comparison matrix

| Field | Required distinction |
| --- | --- |
| Run ID and artifacts | Report, CSVs and logs must belong to the same run; timestamps alone are not proof |
| EA identity | Source version/hash, compiled binary/hash, compiler/build when available; source hash does not prove binary provenance |
| Instrument | Exact symbol suffix, contract size, tick size/value, volume constraints and account currency |
| Dates/time | Requested and observed coverage, broker/server timestamps, timezone and DST when known |
| Timeframes | Tester chart timeframe and internal signal/context input timeframes |
| Model/data | Tester mode, reported history quality, tick source/coverage, gaps and warnings |
| Execution | Delay, spread policy, commissions, swap and other explicit tester settings |
| Account | Initial deposit, leverage, account mode/currency and relevant rules |
| Inputs | Effective report inputs versus SET and defaults; declared intended differences |
| Status | Successful completion, failed/aborted execution or unknown |

Do not silently infer contract size, constant tick value, no swap, leverage or currency conversion from the name XAUUSD. Unknown setup fields restrict comparison but do not erase trustworthy report observations.

## Source handling

Keep originals unchanged. Extract archives into a separate location after checking paths; do not execute archive contents. Link reports and diagnostics through recorded run identifiers and evidence. If reports conflict, preserve both and identify the discrepancy rather than picking the nicer outcome. Screenshots support only visible fields, not complete trade reconciliation.

For Persian/RTL screenshots and PDFs, verify numeric order, minus signs and separators against underlying tables when available. Identify calendar conventions explicitly; do not shift broker timestamps to Tehran without knowing their timezone.

Use project-approved thresholds. If none exist, report observations and propose a threshold as a proposal rather than an established rule. Separate data quality, pairing quality, profitability and robustness: one cannot stand in for another.

Do not convert a reported cumulative return to annual return without explicit duration, capital/cash-flow assumptions and a clearly labeled formula. Do not treat in-sample optimization or repeatedly inspected periods as unseen validation.
