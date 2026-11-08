"""Validate the current skill catalog and exact release payloads. No network or writes."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
VERSION = re.compile(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)")
HASH = re.compile(r"[0-9a-f]{64}")


def inside(root, value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError("Expected a nonempty relative path")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Path escapes the allowed root: " + value)
    return path


def validate(root):
    root = Path(root).resolve()
    issues = []
    catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("skills"), list) or not catalog["skills"]:
        raise ValueError("Invalid catalog schema or empty skill list")
    seen = set()
    for entry in catalog["skills"]:
        name, version = entry["name"], entry["version"]
        if not isinstance(name, str) or not NAME.fullmatch(name) or name in seen:
            raise ValueError("Invalid or duplicate skill name")
        if not isinstance(version, str) or not VERSION.fullmatch(version):
            raise ValueError("Invalid stable semantic version")
        seen.add(name)
        folder = inside(root, entry["path"])
        if entry["path"] != "skills/" + name:
            raise ValueError("Skill payload must use skills/<name>")
        manifest_path = inside(root, entry["manifest"])
        if entry["manifest"] != f"releases/{name}/{version}.json":
            raise ValueError("Manifest path does not match current version")
        changelog = inside(root, entry["changelog"])
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("schema_version") != 1 or manifest.get("name") != name or manifest.get("version") != version:
            issues.append(f"{name}: manifest identity mismatch")
        hashes = manifest.get("files")
        if not isinstance(hashes, dict) or not hashes:
            raise ValueError("Manifest must list payload files")
        for rel, digest in hashes.items():
            path = inside(folder, rel)
            if not isinstance(digest, str) or not HASH.fullmatch(digest):
                raise ValueError("Invalid SHA-256")
            if not path.is_file():
                issues.append(f"{name}: missing payload file {rel}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                issues.append(f"{name}: hash mismatch {rel}")
        actual = set()
        for path in folder.rglob("*"):
            if path.is_symlink():
                issues.append(f"{name}: payload symlink {path.relative_to(folder)}")
            elif path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                actual.add(path.relative_to(folder).as_posix())
        if actual != set(hashes):
            issues.append(f"{name}: payload file set differs from manifest")
        skill = folder / "SKILL.md"
        text = skill.read_text(encoding="utf-8")
        header = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
        if not header:
            issues.append(f"{name}: missing SKILL.md frontmatter")
        else:
            fields = header.group(1)
            if not re.search(r"^name:\s*" + re.escape(name) + r"\s*$", fields, re.M):
                issues.append(f"{name}: SKILL.md name mismatch")
            if not re.search(r"^description:\s*\S", fields, re.M):
                issues.append(f"{name}: empty description")
        if not re.search(r"^## \[" + re.escape(version) + r"\]", changelog.read_text(encoding="utf-8"), re.M):
            issues.append(f"{name}: version missing from changelog")
        metadata = (folder / "agents/openai.yaml").read_text(encoding="utf-8")
        if "$" + name not in metadata:
            issues.append(f"{name}: invocation missing from interface metadata")
        for icon in re.findall(r"^\s*icon_(?:small|large):\s*(.+)$", metadata, re.M):
            if not inside(folder, icon.strip().strip("'\"")).is_file():
                issues.append(f"{name}: declared icon is missing")
    # Limited static Markdown navigation check; no external URL or anchor validation.
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        prose, fence = [], None
        for line in text.splitlines():
            marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
            if marker:
                token = marker.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
                continue
            if fence is None:
                prose.append(line)
        text = re.sub(r"`[^`\n]*`", "", "\n".join(prose))
        for target in re.findall(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)[^\n)]*\)", text):
            parsed = urlsplit(target.strip("<>"))
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root) or not destination.exists():
                issues.append(f"{path.relative_to(root)}: broken/outside local link {target}")
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        issues = validate(args.project)
        for issue in issues:
            print("FAIL:", issue)
        print(f"Catalog validation: {'FAIL' if issues else 'PASS'} ({len(issues)} issue(s))")
        return 1 if issues else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("ERROR:", error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
