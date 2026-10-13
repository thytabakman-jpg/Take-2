# Runner-free mirror cleanup

The default authority gate now verifies pinned source blobs in Take-5. Local mirror file-count thresholds are historical diagnostics.

From a clean Take-2 checkout with a separate clean Take-5 checkout on current main:

```bash
python tools/refresh_take5_authority_pin.py ../Take-5
python tools/compact_verified_mirror.py --take5 ../Take-5 --batch-size 100
python tools/compact_verified_mirror.py --take5 ../Take-5 --batch-size 100 --apply --push
```

Commit any changed authority pin before compaction. The first compaction command is a dry run. The apply command records each 100-file batch, preserves divergent copies, refreshes the derived search index, verifies the remaining source identity and manifest, and uses only non-force Git pushes. GitHub Actions runners are not involved.

The analysis and control changes are recorded in `audits/MIRROR_AUTHORITY_GATE_ROOT_CAUSE_2026_10_13.md`. A verified pinned file is not, by itself, evidence of executed runtime capability.
