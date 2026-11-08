import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/project-documentation-governance/scripts"


class GovernanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_tool(self, name, *args):
        return subprocess.run([sys.executable, str(SCRIPTS/name), "--project", str(self.root), *args], capture_output=True, text=True)

    def test_dry_run_writes_nothing(self):
        result = self.run_tool("bootstrap.py", "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_bootstrap_is_non_destructive(self):
        original = self.root/"README.md"
        original.write_text("# Existing owner content\n")
        result = self.run_tool("bootstrap.py", "--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(original.read_text(), "# Existing owner content\n")
        self.assertEqual(len(list(self.root.rglob("*.md"))), 7)

    def test_bootstrap_placeholders_fail_validation(self):
        self.assertEqual(self.run_tool("bootstrap.py", "--apply").returncode, 0)
        self.assertEqual(self.run_tool("validate.py").returncode, 1)

    def test_complete_documents_pass_validation(self):
        self.assertEqual(self.run_tool("bootstrap.py", "--apply").returncode, 0)
        for p in self.root.rglob("*.md"):
            p.write_text("# Fixture\n\nObserved test fixture content.\n")
        self.assertEqual(self.run_tool("validate.py").returncode, 0)


if __name__ == "__main__":
    unittest.main()
