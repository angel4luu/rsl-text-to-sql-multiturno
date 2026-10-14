"""Pre-deduplication of report versions (protocol: version rules and EX9), before sr-screener.

sr-screener merges records by DOI and by title+year, but never merges two records whose DOIs
differ. That leaves two kinds of same-study duplicates, both handled here on DERIVED copies
of the exports (raw exports stay unedited):

  1. arXiv preprint vs. published version (DOI 10.48550/arXiv.* vs. publisher DOI), same title:
     the arXiv record is dropped; the published record is kept as the primary report.
  2. Scopus record whose DOI conflicts with the ACL Anthology DOI for the same ACL paper
     (Scopus assigns wrong DOIs to some Findings papers, e.g. CQR-SQL): the Scopus record is dropped.

Pairs that match on title but fit neither rule are only listed for full-text review (EX9).
Same title = normalised titles with similarity >= 0.95 and |year difference| <= 2.
Writes: busqueda/exports/_dedup/<files> and busqueda/dedup_versiones_log.csv
"""
import csv
import difflib
import os
import re
import sys

SR = "~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/sr-screener/scripts"
sys.path.insert(0, SR)
import srlib  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "..")
OUT = os.path.join(B, "exports", "_dedup")
FILES = {
    "exports/scopus/2026-10-11_scopus_v4.ris": "Scopus",
    "exports/ieee/2026-10-11_ieee1_v4.csv": "IEEE Xplore",
    "exports/ieee/2026-10-11_ieee2_v4.csv": "IEEE Xplore",
    "exports/ieee/2026-10-11_ieee3_v4.csv": "IEEE Xplore",
    "exports/ieee/2026-10-11_ieee4_v4.csv": "IEEE Xplore",
    "exports/acm/derived/2026-10-11_acm1.ris": "ACM DL",
    "exports/acm/derived/2026-10-11_acm2.ris": "ACM DL",
    "exports/acl/derived/2026-10-11_acl_v4.ris": "ACL Anthology",
    "exports/arxiv/2026-10-11_arxiv_v4.csv": "arXiv",
}


def nt(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def year(r):
    m = re.search(r"(19|20)\d\d", srlib._first(r, "PY", "Y1", "DA") or "")
    return int(m.group(0)) if m else None


def doi(r):
    for c in r.get("DO", []) + r.get("DI", []):
        d = srlib.norm_doi(c)
        if d:
            return d
    return ""


def main():
    recs = []  # (file, index, db, title_norm, year, doi)
    for f, db in FILES.items():
        _, raw = srlib.load_export(os.path.join(B, f), db)
        for i, r in enumerate(raw):
            recs.append({"file": f, "i": i, "db": db, "t": nt(srlib._first(r, "TI", "T1")),
                         "title": srlib._first(r, "TI", "T1"), "y": year(r), "doi": doi(r)})
    by_prefix = {}
    for k, r in enumerate(recs):
        by_prefix.setdefault(r["t"][:30], []).append(k)

    drop, log = set(), []
    for ks in by_prefix.values():
        for a in ks:
            for b in ks:
                if a >= b:
                    continue
                ra, rb = recs[a], recs[b]
                if not ra["doi"] or not rb["doi"] or ra["doi"] == rb["doi"]:
                    continue  # already handled (or not handled) by sr-screener's own rules
                if difflib.SequenceMatcher(None, ra["t"], rb["t"]).ratio() < 0.95:
                    continue
                if ra["y"] and rb["y"] and abs(ra["y"] - rb["y"]) > 2:
                    continue
                ax = [x for x in (ra, rb) if x["doi"].startswith("10.48550/")]
                if len(ax) == 1:
                    pre = ax[0]
                    pub = rb if pre is ra else ra
                    k = a if pre is ra else b
                    drop.add(k)
                    log.append(["preprint_de_version_publicada", pre["db"], pre["doi"], pub["db"], pub["doi"], pre["title"]])
                elif {ra["db"], rb["db"]} == {"Scopus", "ACL Anthology"} and all(x["doi"].startswith("10.18653/") for x in (ra, rb)):
                    sc = ra if ra["db"] == "Scopus" else rb
                    acl = rb if sc is ra else ra
                    drop.add(a if sc is ra else b)
                    log.append(["doi_erroneo_scopus", "Scopus", sc["doi"], "ACL Anthology", acl["doi"], sc["title"]])
                else:
                    log.append(["solo_listado_revisar_EX9", ra["db"], ra["doi"], rb["db"], rb["doi"], ra["title"]])

    os.makedirs(OUT, exist_ok=True)
    dropped_by_file = {}
    for f, db in FILES.items():
        idxs = {recs_k["i"] for k, recs_k in enumerate(recs) if recs_k["file"] == f and k in drop}
        dropped_by_file[f] = len(idxs)
        src = os.path.join(B, f)
        dst = os.path.join(OUT, os.path.basename(f))
        if f.endswith(".csv"):
            text = srlib.read_text(src)
            rows = list(csv.reader(text.splitlines()))
            # csv.reader on splitlines breaks multi-line fields: use DictReader on the full text instead
            import io
            rd = csv.DictReader(io.StringIO(text))
            data = list(rd)
            with open(dst, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=rd.fieldnames)
                w.writeheader()
                for i, row in enumerate(data):
                    if i not in idxs:
                        w.writerow(row)
        else:
            blocks = re.split(r"(?m)^ER  -.*$", srlib.read_text(src))
            blocks = [b.strip("\n") for b in blocks if "TY  - " in b]
            with open(dst, "w", encoding="utf-8") as fh:
                for i, b in enumerate(blocks):
                    if i not in idxs:
                        fh.write(b.strip() + "\nER  - \n\n")
    with open(os.path.join(B, "dedup_versiones_log.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["regla", "base_descartada", "doi_descartado", "base_conservada", "doi_conservado", "titulo"])
        w.writerows(log)
    from collections import Counter
    print("rules:", Counter(r[0] for r in log))
    print("dropped per file:", {os.path.basename(k): v for k, v in dropped_by_file.items()})
    print("total dropped:", len(drop))


if __name__ == "__main__":
    main()
