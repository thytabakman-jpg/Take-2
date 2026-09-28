# Take-2

Take-2 is a clean-room research operating kernel.

It does not copy the legacy Reaserch repository. Capabilities migrate only after they
demonstrate value under an explicit experiment.

Current phase: bootstrap with executable dump/reorganization path.

Core design target:

**Observe -> PD -> Diagnose/Understand -> Decide -> Transition -> Verify -> Observe**

PD is not an add-on audit layer. The demonstrated PD operations are intended to be part
of the kernel's reasoning/control loop. Only capabilities with adequate evidence are
promoted into the stable kernel; experimental capabilities remain explicitly typed.

## Dump and reorganize

A real zero-request intake path now exists.

```bash
python tools/dump_reorganize.py PATH_TO_DUMP
```

It recursively inventories the corpus, hashes and classifies files, creates a stable
organized copy, deduplicates identical bytes, prevents destructive filename collisions,
keeps uncertain material explicit as OPEN, verifies every copied byte, and emits a
machine-readable provenance receipt. See `DUMP_INTERFACE.md`.

The source corpus is never deleted or rewritten by this runner.

The legacy repository remains authoritative for every capability and project not yet
admitted to Take-2.
