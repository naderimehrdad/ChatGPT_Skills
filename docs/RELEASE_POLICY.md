# Release policy

## Versions

Give each skill its own semantic version. MAJOR changes break its established workflow/output contract; MINOR adds compatible capabilities; PATCH corrects compatible instructions, links or tools. The initial registration is 1.0.0 for each skill. Repository-wide tooling/docs have their own root changelog and need not bump an unchanged skill.

## Changes and logging

1. Read applicable instructions and current catalog, changelog and manifest.
2. Preserve protected or unrelated files and make the requested change.
3. For a payload change, select a new version and add a dated changelog entry explaining what/why and verification.
4. Create a new releases/<name>/<version>.json with the exact complete payload file set and SHA-256 hashes. Never replace an old release manifest.
5. Update catalog.json to select the new version. Update materially affected repository documents.
6. Run validation, unit tests and relevant skill tests; record observed results and limitations.
7. Commit/publish only under applicable owner authorization. Record the real commit SHA returned by GitHub when reporting a published version; never invent a SHA or prefill an unknown one.

Git history preserves older payloads; manifests establish content identity. A new version does not itself update the user's installed skill. Coordinate any installed-skill update as a separate authorized operation. Git tags/releases can be added when desired, but JSON version records do not claim that tags already exist.
