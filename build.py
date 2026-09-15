#!/usr/bin/env python3
"""Bygger index.html från template.html + data/*.json.

Kör:  python3 build.py
Datan bakas in i sidan så att index.html är en enda fristående fil.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
DATA_DIR = ROOT / "data"
FILES = {
    "parts": ["del1.json", "del2.json", "del3.json"],
    "objections": "skeptiker.json",
    "explainers": "forklarare.json",
    "swedish": "svenskt.json",
    "method": "metod.json",
}

def load(name):
    p = DATA_DIR / name
    if not p.exists():
        print(f"varning: saknar {p}", file=sys.stderr)
        return None
    with p.open(encoding="utf-8") as f:
        return json.load(f)

def main():
    data = {
        "parts": [d for d in (load(n) for n in FILES["parts"]) if d],
        "objections": load(FILES["objections"]) or {"items": []},
        "explainers": load(FILES["explainers"]) or {"items": []},
        "swedish": load(FILES["swedish"]) or {},
        "method": load(FILES["method"]) or {},
    }
    # Sortera svar efter score, fallande, och sätt rank
    for part in data["parts"]:
        for q in part.get("questions", []):
            q["answers"] = sorted(q.get("answers", []), key=lambda a: -float(a.get("score", 0)))
            for i, a in enumerate(q["answers"], 1):
                a["rank"] = i
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    # Skydda mot </script> i datan
    blob = blob.replace("</", "<\\/")
    tpl = (ROOT / "template.html").read_text(encoding="utf-8")
    out = tpl.replace("/*__DATA__*/null", blob)
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    n_answers = sum(len(q["answers"]) for p in data["parts"] for q in p.get("questions", []))
    print(f"index.html byggd: {len(data['parts'])} delar, {n_answers} svar, {len(data['objections'].get('items', []))} invändningar, {len(out)//1024} kB")

if __name__ == "__main__":
    main()
