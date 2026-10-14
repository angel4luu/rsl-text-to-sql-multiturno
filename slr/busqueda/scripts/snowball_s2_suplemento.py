"""Phase 8 supplement (amendment A5) — backward snowballing through Semantic Scholar for the Level 2 start
studies whose reference list is missing in OpenAlex (backward = 0 in <date>_openalex_seeds.json).

Raw responses are saved unedited to exports/snowballing/<date>_s2_raw.jsonl. The same registered filters are
applied, in the same order, plus one more de-duplication: against the OpenAlex snowball pool (so a work found
by both sources is counted once). New candidates -> exports/snowballing/derived/<date>_snowball_candidates_s2.ris;
counts -> snowball_log_s2.json.
Usage (from slr/busqueda): python scripts/snowball_s2_suplemento.py
"""
import datetime
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.abspath(os.path.join(HERE, ".."))
W = os.path.join(B, "..", "cribado", "sr_work")
OUT = os.path.join(B, "exports", "snowballing")
sys.path.insert(0, HERE)
from v4 import block_a  # noqa: E402
from snowball_openalex import abstract, arxiv_id, known_index, ndoi, nt  # noqa: E402

UA = {"User-Agent": "SLR-thesis-UNMSM (mailto:angela.jara@unmsm.edu.pe)"}
FIELDS = "title,year,abstract,externalIds,venue,publicationTypes,authors"
TODAY = datetime.date.today().isoformat()


def get(url):
    for k in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(5 * (k + 1))
        except Exception:
            time.sleep(5 * (k + 1))
    return None


def ris(p, seeds):
    ext = p.get("externalIds") or {}
    lines = ["TY  - CPAPER", f"TI  - {p.get('title') or ''}"]
    lines += [f"AU  - {a.get('name')}" for a in p.get("authors") or [] if a.get("name")]
    if p.get("year"):
        lines.append(f"PY  - {p['year']}")
    if p.get("venue"):
        lines.append(f"T2  - {p['venue']}")
    if ext.get("DOI"):
        lines.append(f"DO  - {ext['DOI'].lower()}")
    elif ext.get("ArXiv"):
        lines.append(f"DO  - 10.48550/arxiv.{ext['ArXiv']}")
    if p.get("abstract"):
        lines.append(f"AB  - {p['abstract']}")
    lines += [f"N1  - snowballing backward (Semantic Scholar supplement) from {', '.join(sorted(seeds))}",
              "DB  - Semantic Scholar (snowballing supplement)", "ER  - "]
    return "\n".join(lines)


def main():
    seeds_file = sorted(glob.glob(os.path.join(OUT, "*_openalex_seeds.json")))[-1]
    seeds = [e for e in json.load(open(seeds_file)) if e["backward"] == 0]
    recs = {r["id"]: r for r in json.load(open(os.path.join(W, "records.json")))["unique"]}
    # OpenAlex pool, to count a work found by both sources once
    pool_titles, pool_dois = set(), set()
    for line in open(sorted(glob.glob(os.path.join(OUT, "*_openalex_raw.jsonl")))[-1], encoding="utf-8"):
        w = json.loads(line)["work"]
        pool_titles.add(nt(w.get("title")))
        if w.get("doi"):
            pool_dois.add(ndoi(w["doi"]))
    dois, titles, arx = known_index()
    found, log_seeds = {}, []
    with open(os.path.join(OUT, f"{TODAY}_s2_raw.jsonl"), "w", encoding="utf-8") as raw:
        for n, e in enumerate(seeds, 1):
            r = recs[e["id"]]
            key = f"DOI:{ndoi(r['doi'])}" if r.get("doi") else None
            if key and key.startswith("DOI:10.48550/arxiv."):
                key = "ARXIV:" + key.split("arxiv.", 1)[1]
            refs = []
            if key:
                res = get(f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(key)}/references?fields={FIELDS}&limit=1000")
                refs = [x["citedPaper"] for x in ((res or {}).get("data") or []) if (x.get("citedPaper") or {}).get("title")]
            for p in refs:
                raw.write(json.dumps({"seed": e["id"], "direction": "backward", "paper": p}, ensure_ascii=False) + "\n")
                k = (p.get("externalIds") or {}).get("DOI", "").lower() or nt(p["title"])
                found.setdefault(k, (p, set()))[1].add(e["id"])
            log_seeds.append({"id": e["id"], "s2_key": key, "references": len(refs)})
            print(f"[{n}/{len(seeds)}] {e['id']} refs={len(refs)}", flush=True)
            time.sleep(1.2)
    c = {"seeds_without_openalex_references": len(seeds), "seeds_with_s2_references": sum(1 for s in log_seeds if s["references"]),
         "links_retrieved": sum(s["references"] for s in log_seeds), "unique_works": len(found)}
    in_db = in_oa = old = off = 0
    cands = []
    for p, sd in found.values():
        ext = p.get("externalIds") or {}
        d, ax = (ext.get("DOI") or "").lower(), ext.get("ArXiv") or ""
        if d in dois or nt(p["title"]) in titles or (ax and ax in arx):
            in_db += 1
        elif d in pool_dois or nt(p["title"]) in pool_titles:
            in_oa += 1
        elif (p.get("year") or 0) < 2019:
            old += 1
        elif not block_a(p["title"] + " " + (p.get("abstract") or "")):
            off += 1
        else:
            cands.append((p, sd))
    c.update(already_in_database_records=in_db, already_in_openalex_snowball=in_oa, before_2019=old,
             not_matching_block_A=off, candidates=len(cands),
             candidates_without_abstract=sum(1 for p, _ in cands if not p.get("abstract")))
    path = os.path.join(OUT, "derived", f"{TODAY}_snowball_candidates_s2.ris")
    open(path, "w", encoding="utf-8").write("\n\n".join(ris(p, sd) for p, sd in cands) + "\n")
    log = {"date": TODAY, "source": "Semantic Scholar Graph API (supplement, amendment A5)", "counts": c,
           "seeds": log_seeds, "candidates_file": os.path.relpath(path, B)}
    json.dump(log, open(os.path.join(OUT, "snowball_log_s2.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps(c, indent=1))


if __name__ == "__main__":
    main()
