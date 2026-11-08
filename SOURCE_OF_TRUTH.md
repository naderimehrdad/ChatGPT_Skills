# Source of truth

The owner requested versioned registration of their three installed personal skills in naderimehrdad/ChatGPT_Skills.

## Authority and identity

The initial payloads are byte-for-byte copies of the installed skill files at export time. catalog.json selects each current version; releases/<name>/<version>.json records payload paths and hashes. Changelogs explain changes. Historical payloads are recovered from Git history rather than from the current skills/ directory.

Version 1.0.0 is the first repository release for all three skills, dated 2026-11-08. The governance workflow already labels itself v1.0.0; the other two receive external release metadata without changing their installed SKILL.md. This adds version tracking, not new runtime capabilities.

The installed governance edition is reconstructed from a user-supplied outline; its supporting references/scripts are authored additions, not recovered originals. The other two are custom workflows authored in this conversation.

## Limits

Repository publication does not update ChatGPT-installed skills automatically. No backtests, trading orders, deployment or EA compilation are performed by registering these files. Static validation does not prove semantic correctness or policy compliance. No software license has been selected by the owner; do not infer a license from public visibility.
