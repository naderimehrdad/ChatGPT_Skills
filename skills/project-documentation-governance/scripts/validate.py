import argparse
import re
import sys
from urllib.parse import unquote, urlsplit
from common import project_root, document_paths

def main():
    parser = argparse.ArgumentParser(description="Limited static project-documentation validation")
    parser.add_argument("--project", required=True)
    parser.add_argument("--map", help="JSON mapping of default roles to equivalent paths")
    args = parser.parse_args()
    issues = []
    try:
        root = project_root(args.project)
        for role, path in document_paths(root, args.map).items():
            if not path.is_file():
                issues.append(f"MISSING {role}")
                continue
            content = path.read_text(encoding="utf-8")
            if not content.strip():
                issues.append(f"EMPTY {role}")
            if "GOVERNANCE_BOOTSTRAP_INCOMPLETE" in content:
                issues.append(f"INCOMPLETE {role}")
            # Fenced blocks are examples, not navigational links.
            prose = []
            fence = None
            for line in content.splitlines():
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
            for match in re.finditer(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)[^\n)]*\)", text):
                target = match.group(1).strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                local = unquote(parsed.path)
                # A root-relative URL is ambiguous outside a site build.
                if local.startswith("/"):
                    print(f"MANUAL root-relative link: {role}: {target}")
                    continue
                if not (path.parent / local).exists():
                    issues.append(f"BROKEN_LINK {role}: {target}")
        for issue in issues:
            print(issue)
        print(f"Static validation: {'FAIL' if issues else 'PASS'} ({len(issues)} issue(s))")
        print("Manual review required: semantics, authority, evidence and unsupported link syntax.")
        return 1 if issues else 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
