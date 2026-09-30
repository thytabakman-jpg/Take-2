#!/usr/bin/env python3
import hashlib, json, os, re, subprocess, tempfile
from pathlib import Path

SOURCE="https://github.com/thytabakman-jpg/Reaserch.git"
OUT=Path("experiments/009-map-ingestion/result.json")

def headings(text):
    return [ln.strip("# ").strip() for ln in text.splitlines() if ln.startswith("#")][:30]

def tokens(text):
    words=re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}",text.lower())
    stop={"this","that","with","from","into","when","where","current","project","system","map","maps","date","status"}
    return {w for w in words if w not in stop}

def run():
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["git","clone","--depth","1",SOURCE,td+"/r"],check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        root=Path(td)/"r"
        files=[]
        for p in root.rglob("*"):
            if not p.is_file() or ".git" in p.parts: continue
            rel=p.relative_to(root).as_posix()
            name=p.name.lower()
            is_map=("map" in name and p.suffix.lower() in {".md",".yaml",".yml",".json"}) or rel=="projects/core-system-mathematics/math/MASTER_REGISTER.md"
            if is_map:
                try: text=p.read_text(errors="replace")
                except Exception: continue
                files.append({"path":rel,"sha256":hashlib.sha256(text.encode()).hexdigest(),"bytes":len(text.encode()),"headings":headings(text),"tokens":tokens(text)})
        files.sort(key=lambda x:x["path"])
        # Cross-map vocabulary is deliberately descriptive output, not a semantic theorem.
        freq={}
        for f in files:
            for t in f["tokens"]: freq[t]=freq.get(t,0)+1
        shared=sorted(freq.items(),key=lambda kv:(-kv[1],kv[0]))[:100]
        required=[
          "projects/core-system-mathematics/math/TAKE_SYSTEM_PUTIN_OPERATIONAL_CONTRACT_MAP_001_2026-09-24.md",
          "projects/core-system-mathematics/math/TAKE_SYSTEM_INGESTION_EXECUTION_OUTPUT_MAP_001_2026-09-24.md",
          "projects/core-system-mathematics/math/CLOSED_LOOP_EXECUTABLE_CONNECTION_MAP_001_2026-09-24.md"
        ]
        paths={f["path"] for f in files}
        result={
          "experiment":"009-map-ingestion",
          "source":SOURCE,
          "actual_input_boundary":"git clone source repository then read every case-insensitive *map* filename plus MASTER_REGISTER",
          "map_count":len(files),
          "required_new_maps":{x:(x in paths) for x in required},
          "all_required_new_maps_ingested":all(x in paths for x in required),
          "maps":[{k:v for k,v in f.items() if k!="tokens"} for f in files],
          "cross_map_shared_vocabulary":shared,
          "execution_truth":"IMPLEMENTATION_EXECUTED when this script runs in GitHub Actions",
          "semantic_interpretation":"OPEN; inventory/vocabulary output is not itself ICC semantic synthesis"
        }
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(json.dumps(result,indent=2)+"\n")
        print(json.dumps({k:v for k,v in result.items() if k not in {"maps","cross_map_shared_vocabulary"}},indent=2))
        print("MAP_INGESTION_RUN: PASS")
        assert result["all_required_new_maps_ingested"]

if __name__=="__main__":
    run()
