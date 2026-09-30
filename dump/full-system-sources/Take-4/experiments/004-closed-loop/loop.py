#!/usr/bin/env python3
from dataclasses import dataclass, asdict
import json

@dataclass
class Receipt:
    request_id: str
    authority: dict
    pre_state: dict
    action: str
    worker_ack: bool
    post_state: dict
    observation: dict
    verification: dict
    provenance: list

def worker(state, action, authority):
    new=dict(state)
    if action=="recover_constraint" and authority.get("q_repr")=="CHOOSE":
        new["hidden_constraint"]=True
    elif action=="repair" and state.get("hidden_constraint"):
        new["repaired"]=True
    return new, True

def verify(state):
    checks={
      "target": state.get("target")=="T_CURRENT",
      "constraint": state.get("hidden_constraint") is True,
      "repair": state.get("repaired") is True,
      "adjacent_not_target": state.get("target")!="ADJ1",
    }
    return {"checks":checks,"pass":all(checks.values())}

def run():
    authority={"q_goal":"LOCKED","q_object":"LOCKED","q_repr":"LOCKED"}
    state={"target":"T_CURRENT","hidden_constraint":False,"repaired":False}
    trace=[]
    cycle=0
    while cycle<4:
        cycle+=1
        v=verify(state)
        if v["pass"]:
            trace.append({"phase":"TERMINATE","cycle":cycle,"state":state,"verification":v})
            break
        if not state["hidden_constraint"]:
            cut="REPRESENTATION"
            authority=dict(authority); authority["q_repr"]="CHOOSE"
            action="recover_constraint"
        else:
            cut="BIND_EXECUTE"
            action="repair"
        pre=dict(state)
        post,ack=worker(state,action,authority)
        obs={"changed":{k:post[k] for k in post if post[k]!=pre.get(k)},"cut":cut}
        vv=verify(post)
        receipt=Receipt(f"R{cycle}",dict(authority),pre,action,ack,post,obs,vv,["T_CURRENT","HC1"])
        trace.append({"phase":"CYCLE","cycle":cycle,"receipt":asdict(receipt)})
        state=post
        if action=="recover_constraint":
            authority=dict(authority); authority["q_repr"]="LOCKED"
    return trace

if __name__=="__main__":
    trace=run()
    print(json.dumps(trace,indent=2))
    assert trace[-1]["phase"]=="TERMINATE"
    assert trace[-1]["verification"]["pass"]
    cycles=[x for x in trace if x["phase"]=="CYCLE"]
    assert cycles[0]["receipt"]["authority"]["q_goal"]=="LOCKED"
    assert cycles[0]["receipt"]["authority"]["q_object"]=="LOCKED"
    assert cycles[0]["receipt"]["observation"]["cut"]=="REPRESENTATION"
    assert cycles[0]["receipt"]["worker_ack"]
    assert cycles[1]["receipt"]["worker_ack"]
    print("CLOSED_LOOP_WITNESS: PASS")
