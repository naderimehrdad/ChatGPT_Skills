# Testing

Run from the repository root with Python 3.10+:

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
python3 skills/project-documentation-governance/scripts/validate.py --project .
```

The catalog validator checks all current payload hashes, version/name consistency, local Markdown link targets and declared icons. Unit tests cover payload mutation, missing files, unsafe paths and metadata mismatch on temporary repository copies.

Observed outcomes of the initial local registration are recorded in validation/initial-registration.json after executing these commands. These are static/catalog checks, not MT5 trading tests, compiler tests or proof of agent policy compliance.

## Imported skill evidence

Prior conversation checks exercised the governance bootstrap/validator and a synthetic MT5/MQL5 review scenario. Those earlier outputs are not fabricated as new test runs here. Initial-registration checks independently rerun the bundled governance scripts on temporary fixtures.

No exact binary/EA performance claims are associated with this repository.
