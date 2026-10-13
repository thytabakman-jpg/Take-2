"""Regression: source authority remains valid without replicated Take-5 files."""
import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import verify_native_take5 as native
import verify_historical_snapshot as historical


class NativeAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.pin = json.loads(native.PIN.read_text(encoding="utf-8"))
        self.tree = {
            "sha": self.pin["source_tree"],
            "truncated": False,
            "tree": [
                {"path": p, "sha": entry["sha"], "mode": entry["mode"], "type": "blob"}
                for p, entry in self.pin["required_files"].items()
            ],
        }

    def fake_get(self, url):
        if "/git/trees/" in url:
            return self.tree
        if "/commits/main" in url:
            return {"sha": self.pin["source_commit"]}
        if "/commits/" in url:
            return {"commit": {"tree": {"sha": self.pin["source_tree"]}}}
        raise AssertionError("unexpected lookup: " + url)

    def test_all_native_sources_pass_without_local_mirror(self):
        with patch.object(native, "get", side_effect=self.fake_get):
            output = native.verify()
        self.assertEqual(output["status"], "PASS_PINNED_SOURCE")
        self.assertEqual(output["required_verified"], 26)
        self.assertFalse(output["mirror_required"])
        self.assertFalse(output["runtime_execution_certified"])

    def test_missing_required_source_fails_closed(self):
        self.tree["tree"].pop()
        with patch.object(native, "get", side_effect=self.fake_get):
            with self.assertRaises(RuntimeError):
                native.verify()

    def test_changed_required_source_fails_closed(self):
        self.tree["tree"][0]["sha"] = "0" * 40
        with patch.object(native, "get", side_effect=self.fake_get):
            with self.assertRaises(RuntimeError):
                native.verify()

    def test_missing_required_pin_fails_closed(self):
        data = dict(self.pin)
        data["required_files"] = dict(self.pin["required_files"])
        data["required_files"].pop(next(iter(data["required_files"])))
        with tempfile.TemporaryDirectory() as td:
            altered = Path(td) / "pin.json"
            altered.write_text(json.dumps(data), encoding="utf-8")
            with patch.object(native, "PIN", altered):
                with self.assertRaises(RuntimeError):
                    native.verify()


class HistoricalManifestTests(unittest.TestCase):
    def test_single_record_validates_without_eight_thousand_files(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            folder = root / "dump/full-system-sources/Take-5"
            folder.mkdir(parents=True)
            content = b"legacy evidence"
            p = folder / "example.md"
            p.write_bytes(content)
            manifest = {
                "records": [{"path": p.relative_to(root).as_posix(),
                             "bytes": len(content),
                             "sha256": hashlib.sha256(content).hexdigest()}],
                "file_counts": {"Take-5": 1},
                "total_files": 1,
            }
            manifest_path = folder.parent / "PUBLIC_CORPUS_MANIFEST.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            with patch.object(historical, "ROOT", root), \
                 patch.object(historical, "MIRROR", folder.parent), \
                 patch.object(historical, "MANIFEST", manifest_path), \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(historical.main(), 0)
                p.write_bytes(b"altered")
                self.assertEqual(historical.main(), 1)


if __name__ == "__main__":
    unittest.main()
