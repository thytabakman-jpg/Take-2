import hashlib, json, os, pathlib, subprocess, tempfile

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/"experiments/010-ic28-corpus/result.json"

with tempfile.TemporaryDirectory() as td:
    corpus=pathlib.Path(td)/"Reaserch"
    subprocess.run(["git","clone","--depth","1","https://github.com/thytabakman-jpg/Reaserch.git",str(corpus)],check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    include=[]
    for p in corpus.rglob("*"):
        if not p.is_file() or ".git" in p.parts: continue
        rel=p.relative_to(corpus).as_posix()
        low=rel.lower()
        if (
            rel.startswith("projects/improvement-core/versions/") or
            rel=="projects/improvement-core/IC026_CANONICAL_CURRENT_STATE.md" or
            rel=="projects/improvement-core/CURRENT_IMPROVEMENT_CORE.md" or
            rel=="projects/improvement-core/CURRENT_UNIFIED_TOOLCHAIN_INDEX.md" or
            rel=="projects/improvement-core/IC_VERSION_REGISTRY.md" or
            rel=="projects/improvement-core/STATE.yaml" or
            rel=="GOAL_SPINE_AUDIT_PROTOCOL.md" or
            rel=="GOAL_SPINE_REGISTRY.yaml" or
            rel.startswith("projects/core-system-mathematics/") or
            rel.startswith("projects/tool-optimization/") or
            ("map" in pathlib.Path(rel).name.lower()) or
            ("register" in pathlib.Path(rel).name.lower())
        ):
            try: data=p.read_bytes(); data.decode("utf-8")
            except Exception: continue
            include.append({"path":rel,"sha256":hashlib.sha256(data).hexdigest(),"bytes":len(data)})
    include=sorted({x["path"]:x for x in include}.values(),key=lambda x:x["path"])
    versions=[x for x in include if x["path"].startswith("projects/improvement-core/versions/IC-")]
    maps=[x for x in include if "map" in pathlib.Path(x["path"]).name.lower()]
    math=[x for x in include if x["path"].startswith("projects/core-system-mathematics/")]
    result={
      "experiment":"010-ic28-corpus",
      "job":None,
      "request_semantics":"NO_SUBSTANTIVE_JOB",
      "boundary":"actual Reaserch clone into Take-4 execution",
      "counts":{"total":len(include),"ic_versions":len(versions),"maps":len(maps),"math_artifacts":len(math)},
      "contains_ic026":any(x["path"].endswith("IC-2026-09-24-026.yaml") for x in include),
      "contains_canonical_ic026":any(x["path"].endswith("IC026_CANONICAL_CURRENT_STATE.md") for x in include),
      "artifacts":include,
      "status":"INGESTED"
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result["counts"],indent=2))
    print("IC28_CORPUS_INGESTION: PASS")
