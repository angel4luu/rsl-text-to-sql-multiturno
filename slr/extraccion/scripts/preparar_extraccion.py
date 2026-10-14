"""Phase 9, step 1 (no model calls) — base table of included studies for extraction.

Joins the full-text inclusions of the main review (cribado/sr_work, id R#####) and of snowballing
(cribado/sr_work_bola, id B#####), and pre-fills from metadata only:
  id_estudio, origen, titulo, autores, anio, venue, doi, foro_tipo, foro_nivel, nivel_previsto, texto
- foro_tipo: PREPRINT (arXiv), TALLER (workshop), REVISTA (journal article), else CONGRESO.
- foro_nivel: CORE rank (fuentes/core_icore_export_*.csv) matched by acronym or full name for congresses;
  journals stay SJR_PENDIENTE until the SJR list is added (fuentes/sjr_*.csv); PREPRINT; SIN_RANKING.
  "Findings of ..." volumes are not ranked by CORE separately -> SIN_RANKING (noted).
- nivel_previsto: from full-text reviewer reasons (MULTITURNO / UN_TURNO); confirmed later by extraction.
- texto: file the extractors will read (full text kept in texto_full*/ when the screening used an excerpt).
Writes extraccion/base_estudios.csv. Usage (from slr/extraccion): python scripts/preparar_extraccion.py
"""
import csv
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
E = os.path.abspath(os.path.join(HERE, ".."))
SLR = os.path.dirname(E)
MT = re.compile(r"multi[- ]?turn|conversational|context[- ]dependent|sparc|cosql|chase|dialog", re.I)
ST = re.compile(r"single[- ]turn", re.I)
ALIAS = {"sigkdd": "KDD", "knowledge discovery and data mining": "KDD", "north american chapter": "NAACL",
         "european chapter of the association for computational linguistics": "EACL",
         "information and knowledge management": "CIKM", "joint conference on artificial intelligence": "IJCAI",
         "joint conference on neural networks": "IJCNN", "naacl": "NAACL", "edbt": "EDBT", "association for computational linguistics": "ACL"}


def core_table():
    f = sorted(glob.glob(os.path.join(E, "fuentes", "core_icore_export_*.csv")))[-1]
    rows = [r for r in csv.reader(open(f, encoding="utf-8")) if len(r) > 4 and r[4] in ("A*", "A", "B", "C")]
    return [(r[2].strip(), r[1].strip().lower(), r[4]) for r in rows]


def nt(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower().replace("&", " and ")).strip()


def sjr_table():
    files = sorted(glob.glob(os.path.join(E, "fuentes", "sjr_*.csv")))
    if not files:
        return {}
    rd = csv.DictReader(open(files[-1], encoding="utf-8"), delimiter=";")
    return {nt(r["Title"]): r["SJR Best Quartile"] for r in rd if r.get("SJR Best Quartile") in ("Q1", "Q2", "Q3", "Q4")}


def foro(venue, doi, core):
    v, low = venue or "", (venue or "").lower()
    if doi.startswith("10.48550/") or low.startswith("arxiv"):
        return "PREPRINT", "PREPRINT"
    if not low.strip():
        return "DESCONOCIDO", "SIN_DATOS"
    if "workshop" in low or re.search(r"\bsemeval\b|shared task", low):
        return "TALLER", "SIN_RANKING"
    if re.search(r"proceedings|conference|symposium|findings|annual meeting|\bacm sig|pacmmod|vldb", low) is None \
            and not any(k in low for k in ALIAS):
        return "REVISTA", "SJR_PENDIENTE"
    if "findings" in low:
        return "CONGRESO", "SIN_RANKING"
    if "pvldb" in low or "vldb endowment" in low:
        return "CONGRESO", next((r for a, _, r in core if a == "VLDB"), "SIN_RANKING")
    if "pacmmod" in low or "management of data" in low:
        return "CONGRESO", next((r for a, _, r in core if a == "SIGMOD"), "SIN_RANKING")
    for key, acr in ALIAS.items():
        if key in low:
            hit = next((r for a, _, r in core if a == acr), None)
            if hit:
                return "CONGRESO", hit
    for acr, name, rank in sorted(core, key=lambda x: -len(x[0])):
        if (len(acr) >= 3 and re.search(rf"\b{re.escape(acr)}\b", v)) or (len(name) > 25 and name in low):
            return "CONGRESO", rank
    return "CONGRESO", "SIN_RANKING"


def load(work, prefix, txt_dirs, levels):
    W = os.path.join(SLR, "cribado", work)
    ft = json.load(open(os.path.join(W, "ft_decisions.json")))
    recs = {r["id"]: r for r in json.load(open(os.path.join(W, "records.json")))["unique"]}
    man = {m["id"]: m["pdf"] for m in json.load(open(os.path.join(W, "ft_manifest.json")))}
    out = []
    for rid, x in sorted(ft.items()):
        if x["final"]["d"] != "include":
            continue
        r = recs[rid]
        whys = " ".join(x[k]["why"] for k in ("A", "B", "ADJ") if x.get(k))
        lvl = levels.get(rid) if levels else ("multi" if MT.search(whys) and not ST.search(whys) else "single")
        text = man[rid]
        for tdir, fdir in txt_dirs:
            full = text.replace(f"/{tdir}/", f"/{fdir}/")
            if full != text and os.path.exists(full):
                text = full
        out.append({"id_estudio": prefix + rid[1:], "origen": "busqueda" if prefix == "R" else "bola_de_nieve",
                    "id_cribado": rid, "titulo": r.get("title") or "", "autores": "; ".join(r.get("authors") or []),
                    "anio": r.get("year") or "", "venue": r.get("journal") or "", "doi": (r.get("doi") or "").lower(),
                    "nivel_previsto": "MULTITURNO" if lvl == "multi" else "UN_TURNO",
                    "texto": os.path.relpath(text, SLR)})
    return out


def main():
    core = core_table()
    levels = json.load(open(os.path.join(SLR, "cribado", "sr_work", "nivel_auto.json")))
    rows = load("sr_work", "R", [("texto", "texto_full")], levels) + \
        load("sr_work_bola", "B", [("texto_bola", "texto_full_bola")], None)
    sjr = sjr_table()
    for r in rows:
        r["foro_tipo"], r["foro_nivel"] = foro(r["venue"], r["doi"], core)
        if r["foro_nivel"] == "SJR_PENDIENTE" and sjr:
            v = re.sub(r"\(including subseries.*", "", r["venue"], flags=re.I)
            r["foro_nivel"] = sjr.get(nt(v), "SIN_RANKING")
    cols = ["id_estudio", "origen", "id_cribado", "titulo", "autores", "anio", "venue", "doi",
            "foro_tipo", "foro_nivel", "nivel_previsto", "texto"]
    with open(os.path.join(E, "base_estudios.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    from collections import Counter
    print(len(rows), Counter(r["nivel_previsto"] for r in rows), Counter(r["foro_tipo"] for r in rows),
          Counter(r["foro_nivel"] for r in rows))


if __name__ == "__main__":
    main()
