def evaluate(trace):
    events=[e["type"] for e in trace]
    terminal=trace[-1] if trace else {}
    targets=[e.get("target") for e in trace if "target" in e]
    auth_bad=any(e["type"]=="AUTH_DELTA" and e.get("dimension") in ("q_goal","q_object") and e.get("value")!="LOCKED" for e in trace)
    ack=("ACK" in events)
    post=("POST_STATE" in events)
    verified=any(e["type"]=="VERIFY" and e.get("pass") for e in trace)
    terminated=("TERMINATE" in events)
    incomparable_ok=not any(e["type"]=="COLLAPSE" and e.get("from_status")=="INCOMPARABLE" and not e.get("evidence") for e in trace)
    open_ok=not any(e["type"]=="COLLAPSE" and e.get("from_status")=="OPEN" and not e.get("evidence") for e in trace)
    return {
      "target_preserved": all(t=="T_CURRENT" for t in targets) if targets else True,
      "authority_respected": not auth_bad,
      "open_preserved": open_ok,
      "incomparable_preserved": incomparable_ok,
      "execution_truth": (not terminated) or (ack and post),
      "verified_before_terminate": (not terminated) or verified,
      "provenance_preserved": all(bool(e.get("provenance",True)) for e in trace),
    }
