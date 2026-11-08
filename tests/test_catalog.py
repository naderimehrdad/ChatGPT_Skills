import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_catalog", ROOT / "scripts/validate_catalog.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def test_valid_catalog(self):
        self.assertEqual(module.validate(self.root), [])

    def test_payload_mutation(self):
        p = self.root / "skills/mt5-backtest-audit/SKILL.md"
        p.write_text(p.read_text() + "\nChanged instructions.\n")
        self.assertTrue(any("hash mismatch" in x for x in module.validate(self.root)))

    def test_missing_payload(self):
        (self.root / "skills/mql5-change-review/references/ACCEPTANCE_PLAN.md").unlink()
        self.assertTrue(any("missing payload file" in x for x in module.validate(self.root)))

    def test_unsafe_manifest_path(self):
        p = self.root / "catalog.json"
        data = json.loads(p.read_text())
        data["skills"][0]["manifest"] = "../outside.json"
        p.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            module.validate(self.root)

    def test_manifest_identity(self):
        p = self.root / "releases/mt5-backtest-audit/1.0.0.json"
        data = json.loads(p.read_text())
        data["version"] = "9.0.0"
        p.write_text(json.dumps(data))
        self.assertTrue(any("identity mismatch" in x for x in module.validate(self.root)))

    def test_broken_document_link(self):
        p = self.root / "docs/CURRENT_STATE.md"
        p.write_text(p.read_text() + "\n[Missing](absent.md)\n")
        self.assertTrue(any("broken/outside" in x for x in module.validate(self.root)))


if __name__ == "__main__":
    unittest.main()
