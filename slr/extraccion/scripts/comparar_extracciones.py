"""Phase 9 — compares the two independent AI extractions (A, B) of each study and builds the review sheet.

Field agreement: values normalised (case, spaces; ";" lists compared as sets). Quality: per CQ item.
Results tables: compared as sets of (benchmark, metrica, turno, sistema, valor) rows.
Writes <runs>/_comparacion.json (per-field status) and a Spanish review sheet (--sheet) showing, per study,
the disagreements with both values and locations, then the agreed values compactly.
Usage (from slr/extraccion): python scripts/comparar_extracciones.py runs_piloto --sheet revision_piloto_extraccion.md
"""
import argparse
import glob
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
E = os.path.abspath(os.path.join(HERE, ".."))


def load(path):
    j = json.load(open(path, encoding="utf-8"))
    txt = j.get("result") or ""
    m = re.search(r'\{\s*"decisions".*\}', txt, re.S)
    return json.loads(m.group(0))["decisions"][0] if m else None


def norm(v):
    v = re.sub(r"\s+", " ", str(v if v is not None else "")).strip().upper()
    return frozenset(x.strip() for x in v.split(";")) if ";" in v else v


FREE = re.compile(r"_resumen$|^limitaciones_autores$")
BLOCK0 = {"id_estudio", "clave_bib", "informes", "titulo", "autores", "anio", "venue", "foro_tipo", "foro_nivel",
          "tipo_pub", "origen", "nivel", "notas_revisora", "extraccion_independiente", "verificado_por"}


def num(v):
    m = re.search(r"-?\d+(?:[.,]\d+)?", str(v))
    return round(float(m.group(0).replace(",", ".")), 1) if m else str(v).strip()


def row_key(r):
    return (norm(r.get("benchmark")), norm(r.get("particion")), norm(r.get("metrica")), norm(r.get("turno")),
            num(r.get("valor")))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("runs")
    ap.add_argument("--sheet", required=True)
    a = ap.parse_args()
    runs = os.path.join(E, a.runs)
    ids = sorted({os.path.basename(f)[2:-5] for f in glob.glob(os.path.join(runs, "[AB]_*.json"))
                  if not f.endswith(".error.json")})
    comp, out, tot = {}, [], Counter()
    out += ["# Revisión de la extracción — piloto (doble extracción por IA)", "",
            "Cada estudio fue extraído por **dos extractores IA independientes (A y B)**. Abajo, primero las "
            "**discrepancias** (con ambos valores y su ubicación) y después los valores **coincidentes**.", "",
            "**Cómo responder:** en cada discrepancia escriba `A`, `B` o el valor correcto en `Decisión:`. "
            "En los coincidentes, solo marque los que estén mal (escriba el valor correcto al lado). "
            "Al final de cada estudio, anote cualquier comentario sobre el formulario (campos confusos, vocabularios que falten).", ""]
    for sid in ids:
        A, B = (load(os.path.join(runs, f"{r}_{sid}.json")) for r in "AB")
        if not A or not B:
            out += [f"## {sid}: falta una extracción", ""]
            continue
        ea, eb = A.get("extraccion", {}), B.get("extraccion", {})
        allf = [k for k in dict.fromkeys(list(ea) + list(eb)) if not k.endswith("_ubic") and k not in BLOCK0]
        free = [k for k in allf if FREE.search(k)]
        fields = [k for k in allf if k not in free]
        dis, agr = [], []
        for k in fields:
            same = norm(ea.get(k)) == norm(eb.get(k))
            (agr if same else dis).append(k)
        qa = {k: v for k, v in (A.get("calidad") or {}).items() if re.fullmatch(r"CQ\d+", k)}
        qb = {k: v for k, v in (B.get("calidad") or {}).items() if re.fullmatch(r"CQ\d+", k)}
        qdis = [q for q in sorted(set(qa) | set(qb), key=lambda x: int(x[2:])) if num((qa.get(q) or {}).get("p")) != num((qb.get(q) or {}).get("p"))]
        ra, rb = {row_key(r) for r in A.get("resultados", [])}, {row_key(r) for r in B.get("resultados", [])}
        comp[sid] = {"campos": len(fields), "discrepancias": dis, "calidad_discrepancias": qdis,
                     "resultados": {"A": len(ra), "B": len(rb), "comunes": len(ra & rb)},
                     "contrastes": {"A": len(A.get("contrastes", [])), "B": len(B.get("contrastes", []))}}
        tot.update(campos=len(fields), coinciden=len(agr), cq=len(set(qa) | set(qb)), cq_coinciden=len(set(qa) | set(qb)) - len(qdis))
        out += ["---", "", f"## {sid}", "",
                f"Campos: {len(agr)}/{len(fields)} coinciden · calidad: {len(set(qa)|set(qb)) - len(qdis)}/10 ítems coinciden · "
                f"resultados: A {len(ra)} filas, B {len(rb)}, comunes {len(ra & rb)} · contrastes: A {len(A.get('contrastes', []))}, B {len(B.get('contrastes', []))}", "",
                "### Discrepancias", ""]
        for k in dis:
            out += [f"- **{k}**", f"  - A: `{ea.get(k)}` *(p. {ea.get(k + '_ubic', 'NR')})*",
                    f"  - B: `{eb.get(k)}` *(p. {eb.get(k + '_ubic', 'NR')})*", "  - **Decisión:** "]
        for q in qdis:
            x, y = qa.get(q) or {}, qb.get(q) or {}
            out += [f"- **{q}** (calidad)", f"  - A: {x.get('p')} — {x.get('justif')} *(p. {x.get('ubic')})*",
                    f"  - B: {y.get('p')} — {y.get('justif')} *(p. {y.get('ubic')})*", "  - **Decisión:** "]
        out += ["", "### Coincidentes (marque solo si algo está mal)", ""]
        out += [f"- {k}: `{ea.get(k)}` *(p. {ea.get(k + '_ubic', 'NR')})*" for k in agr]
        out += ["", "### Texto libre (versión A; corrija solo si algo es falso)", ""]
        out += [f"- {k}: {ea.get(k)} *(p. {ea.get(k + '_ubic', 'NR')})*" for k in free]
        out += ["", "**Comentarios sobre el formulario:** ", ""]
    json.dump(comp, open(os.path.join(runs, "_comparacion.json"), "w"), indent=1, ensure_ascii=False, default=list)
    open(os.path.join(E, a.sheet), "w", encoding="utf-8").write("\n".join(out))
    print(f"fields agree {tot['coinciden']}/{tot['campos']} ({100 * tot['coinciden'] / max(1, tot['campos']):.0f}%), "
          f"quality items agree {tot['cq_coinciden']}/{tot['cq']}")
    for sid, c in comp.items():
        print(sid, f"disagree {len(c['discrepancias'])}/{c['campos']}", "CQ", c["calidad_discrepancias"], "res", c["resultados"])


if __name__ == "__main__":
    main()
