# Architecture

- skills/<name>/ contains each complete installable payload, unchanged at initial export.
- catalog.json maps skill names to their current versions, paths, changelogs and manifests.
- releases/<name>/<version>.json is an immutable per-release payload checksum record.
- changelogs/<name>.md records each skill's independent version history.
- scripts/validate_catalog.py validates current catalog identities, paths, manifest hashes, local Markdown links and required assets.
- tests/ exercises the catalog validator on valid and corrupted temporary copies.
- docs/ records governance, status, verification and release procedures.

The catalog validator uses Python's standard library and does not write payloads or access the network. The included governance tools remain inside their original skill payload. Historical manifests are not verified against the current payload when their versions are no longer current; inspect the corresponding historical Git revision.
