"""Phase 8 — one-iteration backward/forward snowballing from the Level 2 (multi-turn) included studies
(protocol §11f), through the OpenAlex API.

1. Start set: included studies classified as multi-turn (cribado/sr_work/nivel_auto.json == "multi").
   Each one is resolved in OpenAlex by DOI, else by exact normalised title.
2. Backward: the start study's referenced_works. Forward: works with filter cites:<id>. All pages.
3. Raw results are saved unedited: exports/snowballing/<date>_openalex_raw.jsonl (one work per line, with
   seed and direction) + <date>_openalex_seeds.json (resolution log).
4. Registered filters, in order (counts logged for PRISMA "other methods"):
   a. duplicates among the snowball results (same OpenAlex id);
   b. already in the database-search records (DOI, arXiv id or normalised title; 1,457 records before dedup);
   c. published before 2019 (same date limit as the searches);
   d. block A of search string v4 (task terms) on title + abstract; title only if there is no abstract (rule M4e).
5. Candidates -> exports/snowballing/derived/<date>_snowball_candidates.ris (input for screening) and
   snowball_log.json (all counts).
Usage (from slr/busqueda): python scripts/snowball_openalex.py
"""
import datetime
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.abspath(os.path.join(HERE, ".."))
W = os.path.join(B, "..", "cribado", "sr_work")
OUT = os.path.join(B, "exports", "snowballing")
sys.path.insert(0, HERE)
from v4 import block_a  # noqa: E402

UA = {"User-Agent": "SLR-thesis-UNMSM (mailto:angela.jara@unmsm.edu.pe)"}
API = "https://api.openalex.org/works"
SELECT = "id,doi,title,publication_year,type,abstract_inverted_index,primary_location,authorships,ids,referenced_works"
TODAY = datetime.date.today().isoformat()


def get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 * (k + 1))
    return None


def nt(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def ndoi(d):
    d = (d or "").lower().strip()
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", d)


def abstract(w):
    inv = w.get("abstract_inverted_index") or {}
    return " ".join(x for _, x in sorted((p, k) for k, ps in inv.items() for p in ps))


def arxiv_id(w):
    for v in (w.get("ids") or {}).values():
        m = re.search(r"arxiv\.org/abs/([\d.]+)", str(v)) or re.search(r"10\.48550/arxiv\.([\d.]+)", str(v).lower())
        if m:
            return m.group(1)
    m = re.search(r"10\.48550/arxiv\.([\d.]+)", ndoi(w.get("doi")))
    return m.group(1) if m else ""


def resolve(rec):
    if rec.get("doi"):
        w = get(f"{API}/doi:{urllib.parse.quote(ndoi(rec['doi']))}?select={SELECT}")
        if w:
            return w, "doi"
    q = urllib.parse.quote(re.sub(r"[^\w\s-]", " ", rec.get("title") or "")[:200])
    res = get(f"{API}?filter=title.search:{q}&per-page=10&select={SELECT}") or {}
    for w in res.get("results", []):
        if nt(w.get("title")) == nt(rec.get("title")):
            return w, "title"
    return None, "not_found"


def fetch_ids(ids):
    out = []
    for i in range(0, len(ids), 50):
        chunk = "|".join(x.rsplit("/", 1)[-1] for x in ids[i:i + 50])
        res = get(f"{API}?filter=openalex_id:{chunk}&per-page=50&select={SELECT}") or {}
        out += res.get("results", [])
        time.sleep(0.15)
    return out


def citing(wid):
    out, cursor = [], "*"
    while cursor:
        res = get(f"{API}?filter=cites:{wid.rsplit('/', 1)[-1]}&per-page=200&cursor={cursor}&select={SELECT}")
        if not res:
            break
        out += res.get("results", [])
        cursor = res.get("meta", {}).get("next_cursor")
        time.sleep(0.15)
    return out


def known_index():
    raw = json.load(open(os.path.join(W, "raw_records.json")))
    dois, titles, arx = set(), set(), set()
    for r in raw:
        for d in r.get("DO", []) + r.get("DI", []):
            d = ndoi(d)
            if d:
                dois.add(d)
                m = re.search(r"10\.48550/arxiv\.([\d.]+)", d)
                if m:
                    arx.add(m.group(1))
        for u in r.get("UR", []):
            m = re.search(r"arxiv\.org/(?:abs|pdf)/([\d.]+)", u)
            if m:
                arx.add(m.group(1))
        for t in r.get("TI", []) + r.get("T1", []):
            titles.add(nt(t))
    return dois, titles, arx


def ris(w):
    lines = ["TY  - " + ("JOUR" if w.get("type") == "article" else "CPAPER"), f"TI  - {w.get('title') or ''}"]
    lines += [f"AU  - {a['author']['display_name']}" for a in w.get("authorships", []) if a.get("author")]
    if w.get("publication_year"):
        lines.append(f"PY  - {w['publication_year']}")
    src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name")
    if src:
        lines.append(f"T2  - {src}")
    if w.get("doi"):
        lines.append(f"DO  - {ndoi(w['doi'])}")
    ab = abstract(w)
    if ab:
        lines.append(f"AB  - {ab}")
    lines += [f"M3  - {w.get('type') or ''}", f"UR  - {w['id']}",
              f"N1  - snowballing {w['_dir']} from {', '.join(sorted(w['_seeds']))}", "DB  - OpenAlex (snowballing)", "ER  - "]
    return "\n".join(lines)


def main():
    levels = json.load(open(os.path.join(W, "nivel_auto.json")))
    recs = {r["id"]: r for r in json.load(open(os.path.join(W, "records.json")))["unique"]}
    seeds = sorted(r for r, l in levels.items() if l == "multi")
    os.makedirs(os.path.join(OUT, "derived"), exist_ok=True)
    seed_log, pool = [], {}
    raw_path = os.path.join(OUT, f"{TODAY}_openalex_raw.jsonl")
    with open(raw_path, "w", encoding="utf-8") as raw:
        for n, rid in enumerate(seeds, 1):
            w, how = resolve(recs[rid])
            entry = {"id": rid, "title": recs[rid].get("title"), "resolved": how,
                     "openalex": (w or {}).get("id"), "backward": 0, "forward": 0}
            if w:
                back = fetch_ids(w.get("referenced_works") or [])
                fwd = citing(w["id"])
                entry.update(backward=len(back), forward=len(fwd))
                for direction, works in (("backward", back), ("forward", fwd)):
                    for x in works:
                        raw.write(json.dumps({"seed": rid, "direction": direction, "work": x}, ensure_ascii=False) + "\n")
                        p = pool.setdefault(x["id"], dict(x, _seeds=set(), _dirs=set()))
                        p["_seeds"].add(rid)
                        p["_dirs"].add(direction)
            seed_log.append(entry)
            print(f"[{n}/{len(seeds)}] {rid} {how} back={entry['backward']} fwd={entry['forward']}", flush=True)
    json.dump(seed_log, open(os.path.join(OUT, f"{TODAY}_openalex_seeds.json"), "w"), indent=1, ensure_ascii=False)

    total_links = sum(e["backward"] + e["forward"] for e in seed_log)
    dois, titles, arx = known_index()
    counts = {"seeds": len(seeds), "seeds_resolved": sum(1 for e in seed_log if e["openalex"]),
              "links_retrieved": total_links, "unique_works": len(pool)}
    known, old, off_topic, cands = 0, 0, 0, []
    for w in pool.values():
        if ndoi(w.get("doi")) in dois or nt(w.get("title")) in titles or (arxiv_id(w) and arxiv_id(w) in arx):
            known += 1
            continue
        if (w.get("publication_year") or 0) < 2019:
            old += 1
            continue
        ab = abstract(w)
        if not block_a((w.get("title") or "") + " " + ab):
            off_topic += 1
            continue
        w["_dir"] = "+".join(sorted(w["_dirs"]))
        cands.append(w)
    counts.update(already_in_database_records=known, before_2019=old, not_matching_block_A=off_topic,
                  candidates=len(cands), candidates_without_abstract=sum(1 for w in cands if not abstract(w)))
    ris_path = os.path.join(OUT, "derived", f"{TODAY}_snowball_candidates.ris")
    open(ris_path, "w", encoding="utf-8").write("\n\n".join(ris(w) for w in cands) + "\n")
    log = {"date": TODAY, "source": "OpenAlex API", "counts": counts,
           "raw_file": os.path.relpath(raw_path, B), "candidates_file": os.path.relpath(ris_path, B),
           "seeds_not_resolved": [e["id"] for e in seed_log if not e["openalex"]]}
    json.dump(log, open(os.path.join(OUT, "snowball_log.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps(log, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
