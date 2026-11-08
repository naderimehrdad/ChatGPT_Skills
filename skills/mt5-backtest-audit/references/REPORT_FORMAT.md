# Report format

Scale the output to the request; do not force a long report for one factual question.

1. Verdict about the specific evidence claim and main limitation.
2. Run comparison table with actual settings, source references and unknowns.
3. Supported results table; distinguish reported versus recalculated values.
4. Trade discrepancies or root-cause evidence, citing artifact and row/event identifiers.
5. One concrete next action, with the smallest necessary MT5 test/artifact.

For a full audit, keep a reusable evidence manifest containing artifact path, SHA-256 if computed, run association, provenance and limitations. Record input differences and tolerances. If creating a user-facing file, use the available persistence workflow. Do not publish raw account identifiers or credentials.

Suggested Persian opening: «نتیجهٔ این مقایسه ... است؛ محدودیت اصلی ... است.» Avoid claiming all tests passed when only parsing or static checks passed. Missing data is UNKNOWN, not zero.
