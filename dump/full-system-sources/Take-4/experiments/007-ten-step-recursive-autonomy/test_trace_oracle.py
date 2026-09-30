from trace_oracle import evaluate

BASE=[
 {"type":"SELECT","target":"T_CURRENT"},
 {"type":"REQUEST","target":"T_CURRENT"},
 {"type":"ACK"},
 {"type":"POST_STATE"},
 {"type":"OBSERVE"},
 {"type":"VERIFY","pass":True},
 {"type":"TERMINATE"}
]
CASES={
 "target":[{"type":"SELECT","target":"T_OLD"},{"type":"TERMINATE"}],
 "authority":[{"type":"AUTH_DELTA","dimension":"q_goal","value":"CHOOSE"},{"type":"TERMINATE"}],
 "no_ack":[{"type":"POST_STATE"},{"type":"VERIFY","pass":True},{"type":"TERMINATE"}],
 "no_verify":[{"type":"ACK"},{"type":"POST_STATE"},{"type":"TERMINATE"}],
 "collapse_inc":[{"type":"COLLAPSE","from_status":"INCOMPARABLE","evidence":False}],
 "collapse_open":[{"type":"COLLAPSE","from_status":"OPEN","evidence":False}],
 "provenance":[{"type":"OBSERVE","provenance":False}],
}
def run():
    assert all(evaluate(BASE).values())
    expected={"target":"target_preserved","authority":"authority_respected","no_ack":"execution_truth","no_verify":"verified_before_terminate","collapse_inc":"incomparable_preserved","collapse_open":"open_preserved","provenance":"provenance_preserved"}
    for name,tr in CASES.items():
        r=evaluate(tr)
        assert r[expected[name]] is False,(name,r)
    print("TRACE_ORACLE_ADVERSARIAL_SUITE: PASS")
if __name__=="__main__": run()
