REQUIRED = ["target_preserved","authority_respected","open_preserved","incomparable_preserved","execution_truth","verified_before_terminate","provenance_preserved"]

def evaluate(trace):
    return {k: bool(trace.get(k, False)) for k in REQUIRED}

def passes(trace):
    r=evaluate(trace)
    return all(r.values()), r
