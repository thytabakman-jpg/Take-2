import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from dump_reorganize import run
from markdown_semantics import analyze_markdown_text

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
            self.assertTrue(result["semantic_markdown_complete"])
            self.assertEqual(result["counts"]["source_files"], 4)
            self.assertEqual(result["counts"]["duplicates"], 1)
            self.assertEqual(result["counts"]["markdown_semantically_read"], 2)
            self.assertTrue((out / "code" / "script.py").exists())
            receipt = json.loads((out / "_take2_receipt.json").read_text(encoding="utf-8"))
            self.assertEqual(receipt["manifest"]["job"], "organize-corpus")
            self.assertTrue(any(r["disposition"] == "DUPLICATE" for r in receipt["records"]))

    def test_markdown_filename_does_not_control_semantic_role(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "dump"
            root.mkdir()
            body = (
                "# Kernel Architecture\n\n"
                "This document defines the system architecture, kernel primitives, "
                "schema invariants, and interface contract.\n\n"
                "## Primitive model\nObject, Relation, Event, Transition, Observation.\n"
            )
            (root / "random-notes.md").write_text(body, encoding="utf-8")
            out = root / "_organized"

            result = run(root, out)
            record = next(r for r in result["records"] if r["source"] == "random-notes.md")

            self.assertEqual(record["semantic_role"], "architecture")
            self.assertIn(record["semantic_confidence"], {"MEDIUM", "HIGH"})
            self.assertEqual(record["semantic_title"], "Kernel Architecture")
            self.assertTrue((out / "markdown" / "architecture" / "random-notes.md").exists())

    def test_markdown_extracts_links_headings_and_system_references(self):
        text = (
            "# Current Tool Plan\n\n"
            "Improvement Core routes ICC through HF2.\n"
            "## Next step\nSee [architecture](../ARCHITECTURE.md) and [[GOAL]].\n"
        )
        result = analyze_markdown_text(text)
        self.assertEqual(result.title, "Current Tool Plan")
        self.assertIn("Next step", result.headings)
        self.assertIn("../ARCHITECTURE.md", result.links)
        self.assertIn("GOAL", result.links)
        self.assertTrue(any(x.lower().startswith("improvement") for x in result.system_references))
        self.assertTrue(any(x.upper() == "HF2" for x in result.system_references))

    def test_ambiguous_markdown_fails_open(self):
        result = analyze_markdown_text("# Notes\napple orange chair\n")
        self.assertEqual(result.role, "open")
        self.assertEqual(result.confidence, "LOW")

if __name__ == "__main__":
    unittest.main()
