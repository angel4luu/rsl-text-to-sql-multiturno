"""Phase 9 — final merge: applies the author's decisions and writes the registered tables.

Inputs: l2_resuelto.json (75 studies + pilot, after l2_resolver.py and l2_desempate.py apply), l1_resuelto.json,
revision_piloto_extraccion.md and revision_extraccion.md (author's decisions), confirmacion_nivel2.json,
base_estudios.csv, muestra_independiente.json.
Outputs: extraccion.csv (all included studies), resultados.csv, contrastes.csv (Level 2),
../calidad/calidad.csv (Level 2) and decisiones_autora_extraccion.json (what was applied).
Studies moved to Level 1 by the author (N1) take their Level 1 fields from their two Level 2 extractions with
the same rule (agreement / intersection); a single-code disagreement keeps extractor A's value, flagged.
Usage (from slr/extraccion): python scripts/escribir_final.py
"""
import csv
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
E = os.path.abspath(os.path.join(HERE, ".."))
SLR = os.path.dirname(E)
sys.path.insert(0, HERE)
from l2_resolver import LIST, as_set, load, norm, num  # noqa: E402

L1F = ["escenario", "etiquetas", "tipo_contribucion", "paradigma_principal", "paradigmas_secundarios", "modelos_base",
       "pilares_centrales", "pilares_contenidos", "idioma_dataset", "codigo_disponible", "requiere_entrenamiento",
       "pi3_tecnica_linking", "pi3_inferencia_joins", "pi4_mecanismo", "pi4_senal"]
VALID = ["CQ2", "CQ4", "CQ5", "CQ6", "CQ7"]


def sheet_decisions(path):
    """[(study, kind, key, decision)] from a review sheet, robust to the editor's re-formatting."""
    out, sid, item, sec = [], None, None, None
    for line in open(path, encoding="utf-8"):
        h = re.match(r"#+\s*([ABCD])\.\s", line)
        if h:
            sec = h.group(1)
        hs = re.match(r"#+\s*(?:R|B)\d{5}", line) or re.match(r"##\s*([RB]\d{5})", line)
        if hs:
            sid = re.search(r"[RB]\d{5}", line).group(0)
        m = re.search(r"\*\*([RB]\d{5})\*\*", line)
        if m:
            sid = m.group(1)
        k = re.search(r"campo `?([a-z0-9_]+)`?:?|calidad (CQ\d+)|contraste fila (\d+)|\*\*\s+`?([a-z0-9_]+)`? = |\*\*([a-z0-9_]+)\*\*\s*$|^\s*[-*]\s*(CQ\d+):", line)
        if k:
            kind = "campo" if k.group(1) or k.group(4) or k.group(5) else "calidad" if k.group(2) or k.group(6) else "contraste"
            item = (kind, k.group(1) or k.group(2) or k.group(3) or k.group(4) or k.group(5) or k.group(6))
        d = re.search(r"Decisión:\*\*\s*([^·\n]*)", line)
        if d and d.group(1).strip() and item:
            out.append((sec, sid, item[0], item[1], d.group(1).strip()))
    return out


def main():
    res = json.load(open(os.path.join(E, "l2_resuelto.json")))
    l1 = json.load(open(os.path.join(E, "l1_resuelto.json")))
    base = {r["id_estudio"]: r for r in csv.DictReader(open(os.path.join(E, "base_estudios.csv"), encoding="utf-8"))}
    conf = json.load(open(os.path.join(E, "confirmacion_nivel2.json")))
    n1 = {i for i, _ in conf["N1"]}
    L2 = set(json.load(open(os.path.join(E, "nivel2_final.json"))))
    sample = set(json.load(open(os.path.join(E, "muestra_independiente.json")))["muestra"])
    applied = []
    # pilot decisions (A/B per field) — pilot studies are in res with regla 'pendiente' for those fields
    for sec, sid, kind, key, dec in sheet_decisions(os.path.join(E, "revision_piloto_extraccion.md")):
        f = res.get(sid, {}).get("extraccion", {}).get(key)
        if f and dec.upper() in ("A", "B") and f["regla"] in ("pendiente", "interseccion", "desempate_sonnet"):
            f.update(valor=f[dec.upper()], regla=f"autora_{dec.upper()}")
            applied.append(("piloto", sid, key, dec))
    # final sheet
    for sec, sid, kind, key, dec in sheet_decisions(os.path.join(E, "revision_extraccion.md")):
        D = dec.strip()
        if sid in res and kind == "campo" and key in res[sid]["extraccion"]:
            f = res[sid]["extraccion"][key]
            if D.upper() in ("A", "B") and D.upper() in f:
                f.update(valor=f[D.upper()], regla=f"autora_{D.upper()}")
            elif D.upper() == "OK":
                f["verificado"] = "AJE"
            else:
                f.update(valor=D, regla="autora_valor")
            applied.append((sec, sid, key, D))
        elif sid in res and kind == "calidad" and key in res[sid]["calidad"]:
            c = res[sid]["calidad"][key]
            if D.upper() in ("A", "B") and isinstance(c.get(D.upper()), dict):
                c.update(p=float(num(c[D.upper()].get("p"))), regla=f"autora_{D.upper()}")
            elif num(D) is not None:
                c.update(p=float(num(D)), regla="autora_valor")
            else:
                c["verificado"] = "AJE"
            applied.append((sec, sid, key, D))
        elif sid in res and kind == "contraste":
            r = res[sid]["contrastes"][int(key)]
            r["_regla"] = "descartado_autora" if D.upper() == "NO" else "autora_ok"
            applied.append((sec, sid, f"contraste {key}", D))
        elif sec == "D" and sid in l1 and D.upper() != "OK":
            for part in D.split(";"):
                if "=" in part:
                    k, v = part.split("=", 1)
                    if k.strip() in l1[sid]:
                        l1[sid][k.strip()].update(valor=v.strip(), regla="autora_valor")
            applied.append((sec, sid, "nivel1", D))
    # pending items where both extractors say "not reported" (only the wording differs) -> NR
    for sid, st in res.items():
        for k, f in st["extraccion"].items():
            if f["regla"] == "pendiente" and all(str(f.get(x) or "").upper().startswith("NR") for x in ("A", "B")):
                f.update(valor="NR", regla="acuerdo_NR")
    adj = os.path.join(E, "ajustes_autora.json")
    for sid, fields in (json.load(open(adj)) if os.path.exists(adj) else {}).items():
        for k, v in (fields.items() if isinstance(fields, dict) else []):
            if sid in res and k in res[sid]["extraccion"]:
                res[sid]["extraccion"][k].update(valor=v, regla="autora_valor")
                applied.append(("ajuste", sid, k, v))
    json.dump(res, open(os.path.join(E, "l2_final.json"), "w"), indent=1, ensure_ascii=False)
    # N1 studies: Level 1 fields from their two Level 2 extractions
    for sid in n1:
        A = load(os.path.join(E, "runs_nivel2_claude", f"A_{sid}.json"))
        bpath = os.path.join(E, "runs_nivel2_codex", f"B_{sid}.json")
        B = load(bpath) if os.path.exists(bpath) else A
        ea, eb = A["extraccion"], B["extraccion"]
        l1[sid] = {}
        for k in L1F:
            if norm(ea.get(k)) == norm(eb.get(k)):
                l1[sid][k] = {"valor": ea.get(k), "regla": "acuerdo"}
            elif k in LIST:
                l1[sid][k] = {"valor": "; ".join(sorted(as_set(ea.get(k)) & as_set(eb.get(k)))) or "NR", "regla": "interseccion"}
            else:
                l1[sid][k] = {"valor": ea.get(k), "regla": "A_sin_desempate"}
    # linked reports of the same study (E9 secondary reports) -> listed in `informes` of the primary
    sec = {}
    e9 = os.path.join(SLR, "cribado", "e9_duplicados_post_ft.csv")
    if os.path.exists(e9):
        allb = {}
        for w, p in (("sr_work", "R"), ("sr_work_bola", "B")):
            for r in json.load(open(os.path.join(SLR, "cribado", w, "records.json")))["unique"]:
                allb[p + r["id"][1:]] = (r.get("doi") or "").lower()
        for r in csv.DictReader(open(e9, encoding="utf-8")):
            sec.setdefault(r["primario"], []).append(allb.get(r["secundario"], r["secundario"]))
    # extraccion.csv
    header = open(os.path.join(E, "extraccion.csv"), encoding="utf-8").readline().strip().split(",")
    rows = []
    for sid, b in sorted(base.items()):
        nivel = 2 if sid in L2 else 1
        row = {h: "" for h in header}
        row.update(id_estudio=sid, informes="; ".join(dict.fromkeys(x for x in [b["doi"]] + sec.get(sid, []) if x)), titulo=b["titulo"], autores=b["autores"], anio=b["anio"],
                   venue=b["venue"], foro_tipo=b["foro_tipo"], foro_nivel=b["foro_nivel"], tipo_pub=b["foro_tipo"],
                   origen="BOLA_NIEVE" if b["origen"] == "bola_de_nieve" else "BUSQUEDA", nivel=nivel,
                   extraccion_independiente="SI" if sid in sample else "NO")
        src = res[sid]["extraccion"] if nivel == 2 else l1.get(sid, {})
        reglas = set()
        for k, v in src.items():
            if k in row:
                row[k] = v.get("valor") if v.get("valor") is not None else "PENDIENTE"
                reglas.add(v.get("regla"))
        row["verificado_por"] = "IA doble (" + ", ".join(sorted(x for x in reglas if x)) + ")"
        # scenario follows the author's Level 2 confirmation (confirmacion_nivel2), not the extractor's code
        # (post-close-out fix 2026-10-19: 7 studies had a stale extractor value)
        row["escenario"] = "MULTITURNO" if nivel == 2 else "UN_TURNO"
        rows.append(row)
    with open(os.path.join(E, "extraccion.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    # resultados / contrastes (Level 2 only; duplicates removed; unverified or discarded rows left out)
    keep = {"ambos", "verificado_pagina", "verificado_texto", "desempate_sonnet", "autora_ok"}
    for name, fname, kcols in (("resultados", "resultados.csv", ["benchmark", "version", "particion", "metrica", "turno", "historial_eval", "sistema", "modelo_base", "valor"]),
                               ("contrastes", "contrastes.csv", ["componente", "benchmark", "version", "particion", "metrica", "turno", "valor_con", "valor_sin"])):
        hdr = open(os.path.join(E, fname), encoding="utf-8").readline().strip().split(",")
        seen, out = set(), []
        for sid in sorted(L2):
            for r in res[sid][name]:
                if r.get("_regla") not in keep:
                    continue
                key = (sid,) + tuple(str(norm(r.get(k))) if k not in ("valor", "valor_con", "valor_sin") else str(num(r.get(k))) for k in kcols)
                if key in seen:
                    continue
                seen.add(key)
                out.append(dict(r, id_estudio=sid))
        with open(os.path.join(E, fname), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=hdr, extrasaction="ignore")
            w.writeheader()
            w.writerows(out)
        print(f"{fname}: {len(out)} rows")
    # calidad.csv
    hdr = open(os.path.join(SLR, "calidad", "calidad.csv"), encoding="utf-8").readline().strip().split(",")
    qrows = []
    for sid in sorted(L2):
        c = res[sid]["calidad"]
        row = {q: c.get(q, {}).get("p") for q in [f"CQ{i}" for i in range(1, 11)]}
        vals = [row[q] for q in VALID]
        pct = round(100 * sum(vals) / 5, 1) if None not in vals else None
        row.update(id_estudio=sid, validez_pct=pct, supera_umbral="SI" if pct is not None and pct >= 50 else "NO",
                   muestra_independiente="SI" if sid in sample else "NO",
                   verificado_por="IA doble + desempate; autora (umbral 40–60 % y discrepancias)")
        qrows.append(row)
    with open(os.path.join(SLR, "calidad", "calidad.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=hdr, extrasaction="ignore")
        w.writeheader()
        w.writerows(qrows)
    json.dump(applied, open(os.path.join(E, "decisiones_autora_extraccion.json"), "w"), indent=1, ensure_ascii=False)
    pend = sum(1 for r in rows for v in r.values() if v == "PENDIENTE")
    print(f"extraccion.csv: {len(rows)} rows (L2 {sum(1 for r in rows if r['nivel'] == 2)}), PENDIENTE cells {pend}")
    print(f"calidad.csv: {len(qrows)} rows, above threshold {sum(1 for r in qrows if r['supera_umbral'] == 'SI')}")
    print(f"author decisions applied: {len(applied)}")


if __name__ == "__main__":
    main()
