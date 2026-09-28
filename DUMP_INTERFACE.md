# Dump and reorganize interface

Put an arbitrary corpus in a directory and run:

```bash
python tools/dump_reorganize.py PATH_TO_DUMP
```

Default output is `PATH_TO_DUMP/_organized`.

The runner:

1. recursively accounts for every input file;
2. hashes every file before classification;
3. classifies high-confidence structural types automatically;
4. copies into a stable organized tree without deleting the source;
5. deduplicates identical bytes;
6. prevents filename collisions with content hashes;
7. preserves uncertain material in `open/` rather than guessing;
8. verifies every copied file against its source hash;
9. writes `_take2_receipt.json` containing provenance, disposition, OPEN items, and verification state.

An optional `take2.json` can contain `id`, `job`, and `protected`. With no manifest, the runner enters zero-request mode with the job `organize-corpus`.

This runner establishes complete structural traversal and deterministic reorganization. It does not claim full semantic understanding of ambiguous material. Ambiguity remains explicit as OPEN.
