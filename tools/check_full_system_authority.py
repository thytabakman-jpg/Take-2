#!/usr/bin/env python3
"""Take-2 authority gate: verify native source, not redundant snapshot counts.

TAKE2_AUTHORITY_MODE=snapshot validates a historical archive manifest only.
Neither path constitutes proof of runtime execution.
"""
import os
from verify_native_take5 import main as verify_native
from verify_historical_snapshot import main as verify_historical


if __name__ == "__main__":
    mode = os.environ.get("TAKE2_AUTHORITY_MODE", "native")
    if mode == "native":
        raise SystemExit(verify_native())
    if mode == "snapshot":
        raise SystemExit(verify_historical())
    raise SystemExit("Unknown TAKE2_AUTHORITY_MODE; use native or snapshot")
