import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from dump_reorganize import run

class RecoveredEducationDumpTests(unittest.TestCase):
    def test_reaserch_recovery_dump_is_complete_and_processable(self):
        source = ROOT / "dump" / "education-sukkos-recovery" / "reaserch"
        with tempfile.TemporaryDirectory() as td:
            result = run(source, Path(td) / "organized")
        self.assertEqual(result["counts"]["source_files"], 73)
        self.assertTrue(result["traversal_complete"])
        self.assertTrue(result["semantic_markdown_complete"])
        self.assertTrue(result["verification_complete"])

if __name__ == "__main__":
    unittest.main()
