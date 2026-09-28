# Dump and reorganize interface

Put an arbitrary corpus in a directory and run:

```bash
python tools/dump_reorganize.py PATH_TO_DUMP
```

Default output is `PATH_TO_DUMP/_organized`.

The runner recursively accounts for every input file, hashes it before classification, preserves the source corpus, deduplicates identical bytes, prevents filename collisions, verifies every copied file, and writes a complete `_take2_receipt.json`.

## Markdown semantic intake

Markdown files are read in full. Classification does not rely only on the filename or `.md` extension.

For every Markdown file, Take-2 extracts:

- document title and headings;
- Markdown links and wiki-style links;
- registered system references such as ICC, IC variants, HF1/HF2, PD, ASSERT, GOAL, Jane, Improvement Core, and Take variants;
- content evidence for roles including architecture, project, tool, plan, decision, status, research, and specification;
- role scores, confidence, reasons, and word count.

Markdown is organized under `markdown/<semantic-role>/`.

Weak or conflicting content is routed to `markdown/open/` and recorded as OPEN. The system does not invent a confident semantic category when evidence is insufficient.

The regression suite contains a deliberately misleading filename test: a file named `random-notes.md` whose body defines kernel architecture must be organized as architecture based on its contents.

An optional `take2.json` can contain `id`, `job`, and `protected`. With no manifest, the runner enters zero-request mode with the job `organize-corpus`.

This is deterministic content-aware semantic classification. It does not claim unrestricted human-level interpretation of arbitrary prose; uncertain cases remain explicit instead of being silently misfiled.
