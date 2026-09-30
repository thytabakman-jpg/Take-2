# Experiment 009 — Actual Map Ingestion

Purpose: satisfy the operational PutIn/RunThrough contract for the current request.

The experiment crosses an actual Take-4 input boundary by cloning the Reaserch corpus during the
Take-4 GitHub Actions run, discovering every tracked text artifact whose filename contains "map"
(case-insensitive), plus the mathematical MASTER_REGISTER, reading/hashing them, and emitting an
observable result.

This is intentionally broader than a hand-curated map list so the user is not the router.

The run proves ingestion/execution/observation for the map corpus. It does not by itself prove that
ICC has semantically understood every map; semantic synthesis remains a separate downstream stage.
