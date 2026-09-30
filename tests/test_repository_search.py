import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from repository_search import build_index, check_index, query_index


class RepositorySearchTests(unittest.TestCase):
    def test_content_search_does_not_depend_on_filename(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "notes").mkdir()
            (root / "notes" / "random.md").write_text(
                "# Kernel Note\nImprovement Core routes ASSERT through HF2.\n",
                encoding="utf-8",
            )
            index_dir = root / "search_index"
            build_index(root, index_dir)
            results = query_index("ASSERT HF2", root, index_dir)
            self.assertEqual([r["path"] for r in results], ["notes/random.md"])

    def test_query_intersects_all_tokens(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "a.md").write_text("# A\ncanonical authority alpha\n", encoding="utf-8")
            (root / "b.md").write_text("# B\ncanonical beta\n", encoding="utf-8")
            index_dir = root / "search_index"
            build_index(root, index_dir)
            results = query_index("canonical authority", root, index_dir)
            self.assertEqual([r["path"] for r in results], ["a.md"])

    def test_check_detects_stale_index(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "a.md").write_text("# A\nalpha\n", encoding="utf-8")
            index_dir = root / "search_index"
            build_index(root, index_dir)
            ok, _ = check_index(root, index_dir)
            self.assertTrue(ok)
            (root / "a.md").write_text("# A\nalpha beta\n", encoding="utf-8")
            ok, message = check_index(root, index_dir)
            self.assertFalse(ok)
            self.assertIn("stale", message)


if __name__ == "__main__":
    unittest.main()
