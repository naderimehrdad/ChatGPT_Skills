import argparse
import sys
from common import DOCUMENTS, project_root, document_paths

def main():
    parser = argparse.ArgumentParser(description="Create only missing governance documents")
    parser.add_argument("--project", required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    parser.add_argument("--map", help="JSON mapping of default roles to equivalent paths")
    args = parser.parse_args()
    try:
        root = project_root(args.project)
        paths = document_paths(root, args.map)
        for role, path in paths.items():
            if path.exists():
                if not path.is_file():
                    raise ValueError(f"Document target is not a file: {path}")
                print(f"KEEP {path.relative_to(root)}")
                continue
            print(f"{'CREATE' if args.apply else 'WOULD_CREATE'} {path.relative_to(root)}")
            if args.apply:
                path.parent.mkdir(parents=True, exist_ok=True)
                # Resolve again before writing to reject preexisting escaping symlinks.
                if not path.resolve().is_relative_to(root):
                    raise ValueError("Target escapes documentation root")
                with path.open("x", encoding="utf-8") as stream:
                    stream.write(f"# {PathTitle(role)}\n\n<!-- GOVERNANCE_BOOTSTRAP_INCOMPLETE -->\n\nResponsibility: {DOCUMENTS[role]}.\n\nProject facts have not been established. Complete from observed evidence.\n")
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

def PathTitle(role):
    return role.rsplit("/", 1)[-1].removesuffix(".md").replace("_", " ").title()

if __name__ == "__main__":
    sys.exit(main())
