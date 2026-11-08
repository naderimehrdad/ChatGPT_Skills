---
name: project-documentation-governance
description: Mandatory documentation lifecycle for every software or research repository task, including implementation, investigation, review, and read-only questions. Read project documentation and applicable policies before action; preserve approved requirements, synchronize affected documents, and validate evidence before responding.
---

# Project Documentation Governance v1.0.0

Use this reconstructed, self-contained edition based on the user's supplied workflow. Its references and scripts are newly authored; do not represent them as recovered originals.

Apply this workflow to every repository request, including small and read-only requests. Follow higher-priority instructions and repository safety boundaries. Never auto-commit, push, or deploy project changes. Explicit existing authorization remains valid.

Before substantive project action:
1. Locate the repository root and approved documentation root. Inspect Git status and applicable ancestor and scoped AGENTS.md instructions; preserve existing edits. Discovery reads are permitted to locate these instructions.
2. Read all four bundled policies: [documentation standard](references/DOCUMENTATION_STANDARD.md), [lifecycle](references/LIFECYCLE_POLICY.md), [conflict resolution](references/CONFLICT_RESOLUTION.md), and [validation rules](references/VALIDATION_RULES.md).
3. Read all seven mandatory project documents defined in the standard, plus conditional policies and relevant source. Report missing files; continue safely where possible without inventing contents. Respect established equivalent paths.
4. Distinguish approved requirements, observed implementation, measured evidence, proposals, and unknowns. Resolve material contradictions with the conflict policy.

After work, before responding:
1. Revisit affected documentation and update only what actually changed. A read-only question normally requires no file changes.
2. Check requirements, source, configuration, version identities, current state and evidence for consistency; preserve historical checkpoints.
3. Inspect final diff/status, verify local documentation links, and run meaningful project checks plus the bundled validator where applicable:
   `python /absolute/skill/path/scripts/validate.py --project PATH`
4. Report actual changes, observed commands/outcomes, and material limitations. Never claim execution, review, publication, or deployment without evidence.

For authorized legacy documentation setup, run the bundled `scripts/bootstrap.py --project PATH --dry-run`, review its plan, then `--apply`. Bootstrap only in the approved writable documentation namespace; do not modify a read-only review or overwrite protected originals. Placeholders require factual completion before they count as complete documents.
