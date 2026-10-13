# Repository search interface

## Problem

GitHub code search is not currently a reliable discovery dependency for this repository.
On 2026-09-30, GitHub's code-search endpoint returned zero results with
`incomplete_results: true` for known-present terms, and repository index metadata reported
the Take repository family as not code-search indexed.

This file defines the repository-owned fallback. It does not claim to repair GitHub's
external index. It removes that external index as a single point of failure.

## Architectural status

`search_index/` is a derived view, not authority.

Repository source files remain authoritative. The index can always be deleted and rebuilt.
No decision, project state, tool definition, or research claim becomes authoritative merely
because it appears in the search view.

## Mathematical invariant

For readable source files S and normalized token t:

I(t) = { p in S : t is in Tok(p) }

For a multi-token query Q:

C(Q) = intersection over t in Q of I(t)

The completeness obligation is:

for every p in S, if Q is a subset of Tok(p), then p is in C(Q).

The committed manifest also stores a deterministic source fingerprint. An index is fresh
only when its fingerprint equals a rebuild from the current repository source set.

## Local use

Build:

```bash
python tools/repository_search.py build
```

Query:

```bash
python tools/repository_search.py query "ASSERT HF2"
python tools/repository_search.py query "canonical authority" --limit 50
```

Verify freshness:

```bash
python tools/repository_search.py check
```

## Connector fallback use

When native GitHub code search is unavailable:

1. Fetch `search_index/manifest.json`.
2. Normalize the query into lowercase tokens using the same token rule.
3. Fetch one shard per query token from `search_index/<first-character>.json`.
4. Intersect the document-id postings for all query tokens.
5. Resolve document ids through `manifest.json`.
6. Fetch the resulting repository files directly by path.

This path uses exact GitHub file fetches and therefore does not depend on GitHub code-search
index availability.

## Refresh behavior without GitHub runners

The search index is derived metadata, not a source of authority. File deletion, source editing, or compacting the historical Take-5 mirror invalidates its recorded source fingerprint. Do not claim that the committed index is fresh merely because a workflow file exists.

From a complete local Take-2 checkout run:

```bash
python tools/repository_search.py build
python tools/repository_search.py check
```

The native Take-5 authority verifier does not need the duplicated snapshot or a search index. `tools/compact_verified_mirror.py` rebuilds and verifies this index after actual local batch deletions. A remote GitHub workflow may provide additional verification when runners are available, but it is not the completion route for this campaign.

Until a verified rebuild is committed, any previously saved search index is a historical snapshot and cannot certify coverage of current tracked source files.
