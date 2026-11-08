from pathlib import Path
import json

DOCUMENTS = {
    "README.md": "Purpose, navigation, prerequisites and verified setup",
    "AGENTS.md": "Working rules and protected boundaries",
    "SOURCE_OF_TRUTH.md": "Approved requirements, conflicts and unknowns",
    "CHANGELOG.md": "Dated material changes",
    "docs/ARCHITECTURE.md": "Components, interfaces and data flow",
    "docs/CURRENT_STATE.md": "Current status, blockers and next work",
    "docs/TESTING.md": "Verification procedures, observed results and limitations",
}

def project_root(value):
    root = Path(value).resolve()
    if not root.is_dir():
        raise ValueError("Project documentation root must be an existing directory")
    return root

def document_paths(root, mapping=None):
    aliases = {} if not mapping else json.loads(Path(mapping).read_text(encoding="utf-8"))
    if not isinstance(aliases, dict) or any(k not in DOCUMENTS for k in aliases):
        raise ValueError("Map must be an object with known default document keys")
    result = {}
    for default in DOCUMENTS:
        value = aliases.get(default, default)
        if not isinstance(value, str) or not value:
            raise ValueError("Mapped paths must be nonempty strings")
        path = (root / value).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Mapped documents must remain inside the documentation root")
        result[default] = path
    if len(set(result.values())) != len(result):
        raise ValueError("Each document role must map to a distinct file")
    return result
