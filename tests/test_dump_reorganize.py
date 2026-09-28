import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from dump_reorganize import run

class DumpReorganizeTests(unittest.TestCase):
    def test_zero_request_reorganizes_preserves_and_verifies(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "dump"
            root.mkdir()
            (root / "notes final.md").write_text("# Notes\nalpha\n", encoding="utf-8")
            (root / "script.py").write_text("print('x')\n", encoding="utf-8")
            (root / "copy.md").write_text("# Notes\nalpha\n", encoding="utf-8")
            (root / "mystery").write_bytes(b"\x00\x01\x02")
            out = root / "_organized"

            result = run(root, out)

            self.assertTrue(result["traversal_complete"])
            self.assertTrue(result["verification_complete"])
            self.assertEqual(result["counts"]["source_files"], 4)
            self.assertEqual(result["counts"]["duplicates"], 1)
            self.assertEqual(result["counts"]["open"], 1)
            self.assertTrue((out / "documents" / "notes-final.md").exists())
            self.assertTrue((out / "code" / "script.py").exists())
            receipt = json.loads((out / "_take2_receipt.json").read_text(encoding="utf-8"))
            self.assertEqual(receipt["manifest"]["job"], "organize-corpus")

if __name__ == "__main__":
    unittest.main()
