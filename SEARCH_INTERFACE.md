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

## Refresh behavior

The kernel-fitness workflow rebuilds and verifies the derived index on every run. On pushes
to `main`, a changed index is committed back automatically with the repository Actions
token. Pull requests validate the builder and query behavior without granting the index
authority over source.

## Source-referenced files and runner-free maintenance

The Take-2 search index covers its own present readable working-tree files, not every file ever preserved in its historical migration dump and not the entire Take-5 repository. After exact duplicate removal, stale Take-2 snapshot paths must be removed from this derived index. Run `python tools/repository_search.py build` followed by `python tools/repository_search.py check` in a local checkout; no GitHub Actions runner is required. Never retain a stale generated index as proof that a retired mirror file still exists.

Discover files removed from Take-2's historical mirror through the source-references authority pin and recorded per-file deletion provenance, then consult the **native** Take-5 Git repository. A source reference does not become a local searchable copy or a transfer of authority.

If a current checked-out corpus is inaccessible, mark search coverage OPEN instead of claiming the checked-in index is fresh.
