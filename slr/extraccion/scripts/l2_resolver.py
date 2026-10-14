"""Phase 9 — Level 2 resolution, rule-based part (no model calls; amendment A5 (c), pre-specified rules).

Per study (runs_nivel2_ab/A_*.json = Claude, B_*.json = Codex or Claude for R00105/R00123):
  - coded fields: agreement -> value; LIST fields that disagree -> intersection of A and B ("NR" if empty);
    SINGLE-code fields that disagree -> pending (tie-break reading the cited pages, next step).
  - free-text fields (*_resumen, limitaciones_autores): A's text kept (B's kept alongside for the review sheet).
  - quality CQ1-CQ10: agreement -> score; disagreement -> pending.
  - results / contrasts: rows given by both extractors are kept; rows given by only one are kept if their
    number(s) appear verbatim on the page(s) they cite in the study's text (else in the whole text, flagged),
    otherwise flagged for review.
Writes l2_resuelto.json and prints the counts.
Usage (from slr/extraccion): python scripts/l2_resolver.py
"""
import csv
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
E = os.path.abspath(os.path.join(HERE, ".."))
SLR = os.path.dirname(E)
LIST = {"etiquetas", "tipo_contribucion", "paradigmas_secundarios", "modelos_base", "pilares_centrales",
        "pilares_contenidos", "idioma_dataset", "pi1_tecnica", "pi1_insumos_historial", "pi2_representacion",
        "pi2_grafo_nodos", "pi3_tecnica_linking", "pi3_algoritmo", "pi4_mecanismo", "pi4_senal", "coste_reportado"}
FREE = re.compile(r"_resumen$|^limitaciones_autores$")
BLOCK0 = {"id_estudio", "clave_bib", "informes", "titulo", "autores", "anio", "venue", "foro_tipo", "foro_nivel",
          "tipo_pub", "origen", "nivel", "notas_revisora", "extraccion_independiente", "verificado_por"}


def load(path):
    j = json.load(open(path, encoding="utf-8"))
    m = re.search(r'\{\s*"decisions".*\}', j.get("result") or "", re.S)
    return json.loads(m.group(0))["decisions"][0] if m else None


def norm(v):
    v = re.sub(r"\s+", " ", str(v if v is not None else "")).strip().upper()
    return frozenset(x.strip() for x in v.split(";") if x.strip()) if ";" in v else v


def as_set(v):
    v = norm(v)
    return v if isinstance(v, frozenset) else (frozenset() if v in ("", "NR", "NA") else frozenset([v]))


def num(v):
    m = re.search(r"-?\d+(?:[.,]\d+)?", str(v))
    return m.group(0).replace(",", ".") if m else None


def pages_text(path):
    t = open(path, encoding="utf-8").read() if path.endswith(".txt") and os.path.exists(path) else ""
    parts = re.split(r"(?m)^=== página (\d+) ===\n", t)
    return t, {int(parts[i]): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def verify(row, keys, full, pages):
    cited = {int(p) for p in re.findall(r"(?:p\.?|pp?\.?|página|page)\s*(\d+)", str(row.get("ubicacion", "")), re.I)}
    hay = " ".join(pages.get(p, "") for p in cited) if cited else ""
    vals = [num(row.get(k)) for k in keys if num(row.get(k))]
    if not vals:
        return "sin_valor"
    if hay and all(v in hay for v in vals):
        return "verificado_pagina"
    if full and all(v in full for v in vals):
        return "verificado_texto"
    return "no_verificado"


def rkey(r, keys):
    return tuple(norm(r.get(k)) for k in ("benchmark", "particion", "metrica", "turno")) + tuple(num(r.get(k)) for k in keys)


def main():
    base = {r["id_estudio"]: r for r in csv.DictReader(open(os.path.join(E, "base_estudios.csv"), encoding="utf-8"))}
    out, tally = {}, {}
    for fa in sorted(glob.glob(os.path.join(E, "runs_nivel2_ab", "A_*.json"))):
        sid = os.path.basename(fa)[2:-5]
        A, B = load(fa), load(fa.replace("/A_", "/B_"))
        ea, eb = A.get("extraccion", {}), B.get("extraccion", {})
        fields, pend = {}, []
        for k in dict.fromkeys(list(ea) + list(eb)):
            if k.endswith("_ubic") or k in BLOCK0:
                continue
            if FREE.search(k):
                fields[k] = {"valor": ea.get(k), "regla": "texto_A", "B": eb.get(k)}
            elif norm(ea.get(k)) == norm(eb.get(k)):
                fields[k] = {"valor": ea.get(k), "regla": "acuerdo", "ubic": ea.get(k + "_ubic")}
            elif k in LIST:
                inter = as_set(ea.get(k)) & as_set(eb.get(k))
                fields[k] = {"valor": "; ".join(sorted(inter)) or "NR", "regla": "interseccion", "A": ea.get(k), "B": eb.get(k)}
            else:
                fields[k] = {"valor": None, "regla": "pendiente", "A": ea.get(k), "B": eb.get(k),
                             "ubic_A": ea.get(k + "_ubic"), "ubic_B": eb.get(k + "_ubic")}
                pend.append(k)
        qa = {k: v for k, v in (A.get("calidad") or {}).items() if re.fullmatch(r"CQ\d+", k)}
        qb = {k: v for k, v in (B.get("calidad") or {}).items() if re.fullmatch(r"CQ\d+", k)}
        cal = {}
        for q in sorted(set(qa) | set(qb), key=lambda x: int(x[2:])):
            x, y = qa.get(q) or {}, qb.get(q) or {}
            if num(x.get("p")) == num(y.get("p")):
                cal[q] = {"p": float(num(x.get("p"))), "regla": "acuerdo", "justif": x.get("justif"), "ubic": x.get("ubic")}
            else:
                cal[q] = {"p": None, "regla": "pendiente", "A": x, "B": y}
        full, pages = pages_text(os.path.join(SLR, base[sid]["texto"]))
        tables = {}
        for name, keys in (("resultados", ["valor"]), ("contrastes", ["valor_con", "valor_sin"])):
            ra = {rkey(r, keys): r for r in A.get(name) or []}
            rb = {rkey(r, keys): r for r in B.get(name) or []}
            rows = []
            for k, r in ra.items():
                rows.append(dict(r, _regla="ambos" if k in rb else verify(r, keys, full, pages), _fuente="A" if k not in rb else "AB"))
            for k, r in rb.items():
                if k not in ra:
                    rows.append(dict(r, _regla=verify(r, keys, full, pages), _fuente="B"))
            tables[name] = rows
        out[sid] = {"extraccion": fields, "calidad": cal, **tables}
        for f in fields.values():
            tally[f["regla"]] = tally.get(f["regla"], 0) + 1
        for c in cal.values():
            tally["calidad_" + c["regla"]] = tally.get("calidad_" + c["regla"], 0) + 1
        for name in ("resultados", "contrastes"):
            for r in tables[name]:
                tally[f"{name}_{r['_regla']}"] = tally.get(f"{name}_{r['_regla']}", 0) + 1
    json.dump(out, open(os.path.join(E, "l2_resuelto.json"), "w"), indent=1, ensure_ascii=False)
    for k in sorted(tally):
        print(f"{k}: {tally[k]}")


if __name__ == "__main__":
    main()
