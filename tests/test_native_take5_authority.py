import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import verify_native_take5 as native


class NativeTake5AuthorityTests(unittest.TestCase):
    def setUp(self):
        self.pin = json.loads((ROOT / "source-references/TAKE5_AUTHORITY_PIN.json").read_text())
        self.fake_tree = {
            "sha": self.pin["source_tree"], "truncated": False,
            "tree": [
                {"path": path, "sha": info["sha"], "mode": info["mode"], "type": "blob"}
                for path, info in self.pin["required_files"].items()
            ]
        }

    def fake_get(self, url):
        if "/git/trees/" in url:
            return self.fake_tree
        if url.endswith("/commits/main"):
            return {"sha": self.pin["source_commit"]}
        return {"commit": {"tree": {"sha": self.pin["source_tree"]}}}

    def test_pinned_source_identity(self):
        with patch.object(native, "get", self.fake_get):
            result = native.verify()
        self.assertEqual(result["status"], "PASS_PINNED_SOURCE")
        self.assertEqual(result["required_verified"], 26)
        self.assertFalse(result["mirror_required"])
        self.assertFalse(result["runtime_execution_certified"])

    def test_changed_source_blobs_fail(self):
        self.fake_tree["tree"][0]["sha"] = "0" * 40
        with patch.object(native, "get", self.fake_get):
            with self.assertRaises(RuntimeError):
                native.verify()

    def test_missing_native_blob_fails(self):
        self.fake_tree["tree"].pop()
        with patch.object(native, "get", self.fake_get):
            with self.assertRaises(RuntimeError):
                native.verify()

    def test_truncated_tree_fails(self):
        self.fake_tree["truncated"] = True
        with patch.object(native, "get", self.fake_get):
            with self.assertRaises(RuntimeError):
                native.verify()

    def test_changed_main_does_not_misstate_currentness(self):
        def get(url):
            if url.endswith("/commits/main"):
                return {"sha": "1" * 40}
            return self.fake_get(url)
        with patch.object(native, "get", get):
            result = native.verify()
        self.assertFalse(result["native_main_matches_pin"])


if __name__ == "__main__":
    unittest.main()
