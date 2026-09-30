#!/usr/bin/env python3
from fixtures import FIXTURES
from mutations import MUTATIONS
from oracle import evaluate

def run():
    n=0
    for fixture in FIXTURES:
        base={k: True for k in ["target_preserved","authority_respected","open_preserved","incomparable_preserved","execution_truth","verified_before_terminate","provenance_preserved"]}
        for mutation,coordinate in MUTATIONS.items():
            test=dict(base)
            test[coordinate]=False
            result=evaluate(test)
            assert result[coordinate] is False, (fixture,mutation,coordinate)
            n+=1
    print("SEMANTIC_ABLATION_HARNESS: PASS")
    print("matched_cases:",n)
    print("runtime_evidence: OPEN")

if __name__=="__main__":
    run()
