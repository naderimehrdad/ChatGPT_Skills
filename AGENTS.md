# Repository working rules

Read README.md, SOURCE_OF_TRUTH.md, CHANGELOG.md, docs/ARCHITECTURE.md, docs/CURRENT_STATE.md and docs/TESTING.md before project work. Apply the project-documentation-governance lifecycle.

- Keep each skill self-contained under skills/<name>/; keep catalog, release metadata and changelogs outside those installable folders.
- Preserve existing user edits. Do not silently change installed copies when editing this repository, or vice versa.
- Follow docs/RELEASE_POLICY.md. Never rewrite historical release manifests or assign changed payloads the same version.
- Run the three documented validation commands; record actual outcomes only.
- Keep account identifiers, credentials, local absolute paths and trading account details out of published artifacts.
- User authorization covers initial registration and publication of all three skills in this repository. Future commits/pushes/deployments require applicable user authorization.
- The repository contains workflows, not proof that an EA was compiled, backtested or certified.
