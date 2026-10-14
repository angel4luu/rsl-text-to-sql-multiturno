"""Phase 2.4 — search sensitivity against the seeds and the independent reference set.

Loads every official export with sr-screener's own parsers (srlib), then matches each
reference-set member and each seed by DOI or normalised title (records from different
databases may carry different DOIs, e.g. arXiv vs. publisher, or wrong DOIs in Scopus).
Writes busqueda/sensibilidad_fase2.json and prints a summary.
"""
import csv
import difflib
import json
import math
import os
import re
import sys

SR = "~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/sr-screener/scripts"
sys.path.insert(0, SR)
import srlib  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "..")
EXPORTS = {
    "Scopus": ["exports/scopus/2026-10-11_scopus_v4.ris"],
    "IEEE": [f"exports/ieee/2026-10-11_ieee{i}_v4.csv" for i in range(1, 5)],
    "ACM": ["exports/acm/derived/2026-10-11_acm1.ris", "exports/acm/derived/2026-10-11_acm2.ris"],
    "ACL": ["exports/acl/derived/2026-10-11_acl_v4.ris"],
    "arXiv": ["exports/arxiv/2026-10-11_arxiv_v4.csv"],
}


def nt(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(c - h, 3), round(c + h, 3))


def load():
    idx = {}
    for db, files in EXPORTS.items():
        recs = []
        for f in files:
            fmt, raw = srlib.load_export(os.path.join(B, f), db)
            for r in raw:
                ti = srlib._first(r, "TI", "T1")
                doi = ""
                for c in r.get("DO", []) + r.get("DI", []):
                    doi = srlib.norm_doi(c)
                    if doi:
                        break
                recs.append((doi, nt(ti)))
        idx[db] = recs
    return idx


def found(member_doi, member_title, recs):
    d = srlib.norm_doi(member_doi)
    t = nt(member_title)
    for doi, ti in recs:
        if d and doi and doi == d:
            return True
        if t and ti and (ti == t or difflib.SequenceMatcher(None, ti, t).ratio() >= 0.93):
            return True
    return False


def main():
    idx = load()
    totals = {db: len(r) for db, r in idx.items()}
    resolved = {r["id"]: r for r in json.load(open(os.path.join(B, "conjunto_referencia_resuelto.json")))}
    members = list(csv.DictReader(open(os.path.join(B, "conjunto_referencia.csv"))))
    rows = []
    for m in members:
        rv = resolved[m["id"]]
        title = rv.get("openalex_titulo") or m["titulo"]
        hits = {db: found(rv.get("doi") or m["doi"], title, recs) for db, recs in idx.items()}
        # also try the candidate's own listed title (e.g. renamed arXiv versions)
        for db, recs in idx.items():
            if not hits[db]:
                hits[db] = found("", m["titulo"].split(" (v1")[0], recs)
        ab = (rv.get("abstract") or "").lower()
        rows.append({"id": m["id"], "arm": m["brazo"], "status": m["estado"].split(" (")[0],
                     "title": title, "hits": hits, "any": any(hits.values()),
                     "no_sparc_cosql": bool(ab) and "sparc" not in ab and "cosql" not in ab,
                     "seed": m.get("semilla", "")})

    def summary(subset):
        n = len(subset)
        k = sum(r["any"] for r in subset)
        per_db = {db: sum(r["hits"][db] for r in subset) for db in idx}
        return {"n": n, "found": k, "recall": round(k / n, 3) if n else None, "wilson95": wilson(k, n), "per_db": per_db}

    out = {"records_per_source": totals, "arms": {}}
    for arm in ("multiturno", "un_turno"):
        el = [r for r in rows if r["arm"] == arm and r["status"] == "Elegible"]
        elp = [r for r in rows if r["arm"] == arm and r["status"] in ("Elegible", "Elegible probable")]
        out["arms"][arm] = {"eligible": summary(el), "eligible_plus_probable": summary(elp),
                            "missed": [(r["id"], r["title"]) for r in elp if not r["any"]]}
        if arm == "multiturno":
            nc = [r for r in el if r["no_sparc_cosql"]]
            out["arms"][arm]["circularity_control_no_SParC_CoSQL_in_abstract"] = summary(nc)
            out["arms"][arm]["eligible_without_seeds"] = summary([r for r in el if not r["seed"]])

    seeds = json.load(open(os.path.join(B, "..", "protocolo", "screening_config.json")))["seeds"]
    out["seeds"] = {s["label"].split()[0]: any(found(s["doi"], s["title"], recs) for recs in idx.values()) for s in seeds}
    out["members"] = rows
    json.dump(out, open(os.path.join(B, "sensibilidad_fase2.json"), "w"), indent=2, ensure_ascii=False)
    print(json.dumps({k: v for k, v in out.items() if k != "members"}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
