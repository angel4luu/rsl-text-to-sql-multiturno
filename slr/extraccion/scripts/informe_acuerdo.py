"""Phase 9 — agreement report for the methods section (all numbers computed here, none typed by hand).

A vs B (Level 1, Level 2 fields and quality), resolution rules used, author's verification samples (C, D)
with Wilson 95 % CI, and the author's blind sample (5 studies) vs the final AI-derived values on the fields
that can be compared exactly: escenario, historial_eval, CQ1-CQ10, and headline result values present in
resultados.csv. Writes informe_acuerdo_extraccion.md and informe_acuerdo.json (k/n per measure, for the LaTeX tables).
Usage (from slr/extraccion): python scripts/informe_acuerdo.py
"""
import collections
import csv
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
E = os.path.abspath(os.path.join(HERE, ".."))
SLR = os.path.dirname(E)
sys.path.insert(0, HERE)
from escribir_final import sheet_decisions  # noqa: E402
from l2_resolver import norm, num  # noqa: E402


def wilson(k, n, z=1.96):
    if not n:
        return (0, 0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(100 * (c - h), 1), round(100 * (c + h), 1))


def pct(k, n):
    lo, hi = wilson(k, n)
    return f"{k}/{n} ({100 * k / max(n, 1):.1f} %; IC95 {lo}–{hi} %)"


def main():
    ab = json.load(open(os.path.join(E, "runs_nivel1", "_ab.json")))
    l1 = json.load(open(os.path.join(E, "l1_resuelto.json")))
    res = json.load(open(os.path.join(E, "l2_final.json")))
    comp = json.load(open(os.path.join(E, "runs_nivel2_ab", "_comparacion.json")))
    st = {}  # k/n per measure -> informe_acuerdo.json
    out = ["# Informe de acuerdo — extracción y calidad (fase 9)", "",
           "Generado por `scripts/informe_acuerdo.py`. Diseño: doble extracción por IA (A, B), comparación automática, "
           "reglas preespecificadas (A5 c) y verificación de la autora por muestreo.", ""]
    # Level 1
    k = n = 0
    for sid in ab["A"]:
        for f, v in ab["A"][sid].items():
            n += 1
            k += norm(v) == norm(ab["B"].get(sid, {}).get(f))
    rules = collections.Counter(v["regla"] for s in l1.values() for v in s.values())
    st["n1_estudios"], st["n1_ab"] = len(ab["A"]), [k, n]
    out += [f"## Nivel 1 ({len(ab['A'])} estudios; A y B = Claude Sonnet)", f"- Acuerdo A–B por campo: {pct(k, n)}",
            f"- Resolución: {dict(rules)}", ""]
    # Level 2
    fk = sum(v["campos"] - len(v["discrepancias"]) for v in comp.values())
    fn = sum(v["campos"] for v in comp.values())
    qn = sum(10 for _ in comp.values())
    qk = qn - sum(len(v["calidad_discrepancias"]) for v in comp.values())
    r2 = collections.Counter(v["regla"] for s in res.values() for v in s["extraccion"].values())
    rq = collections.Counter(v["regla"] for s in res.values() for v in s["calidad"].values())
    st["n2_estudios"], st["n2_no_piloto"], st["n2_campos_ab"], st["n2_calidad_ab"] = len(res), len(comp), [fk, fn], [qk, qn]
    out += [f"## Nivel 2 ({len(res)} estudios; A = Claude Sonnet, B = GPT Codex salvo piloto y 2 reasignados)",
            f"- Acuerdo A–B en campos codificados ({len(comp)} estudios no piloto): {pct(fk, fn)}",
            f"- Acuerdo A–B en ítems de calidad: {pct(qk, qn)}",
            f"- Resolución de campos: {dict(r2)}", f"- Resolución de calidad: {dict(rq)}", ""]
    # author's samples
    dec = sheet_decisions(os.path.join(E, "revision_extraccion.md"))
    for sec, name in (("C", "valores concordantes del Nivel 2 (muestra 10 %)"), ("D", "estudios del Nivel 1 (muestra 10 %)"), ("B", "ítems de validez cerca del umbral")):
        items = [d for d in dec if d[0] == sec]
        ok = sum(1 for d in items if d[4].strip().upper() == "OK")
        st["verif_" + sec] = [ok, len(items)]
        out.append(f"- Verificación de la autora, {name}: confirmados sin cambios {pct(ok, len(items))}")
    a_items = [d for d in dec if d[0] == "A"]
    out += [f"- No decididos por el desempate y resueltos por la autora: {len(a_items)} "
            f"({dict(collections.Counter(d[4].strip().upper()[:2] for d in a_items))})", ""]
    # blind sample
    blind = {}
    cur = None
    for line in open(os.path.join(E, "muestra_independiente_autora.md"), encoding="utf-8"):
        h = re.match(r"##\s*([RB]\d{5})", line)
        if h:
            cur = h.group(1)
            blind[cur] = {"res": []}
            continue
        if not cur:
            continue
        m = re.search(r"\*\*(escenario|historial_eval):\*\*\s*([A-Z_]+)", line)
        if m:
            blind[cur][m.group(1)] = m.group(2)
        for q, v in re.findall(r"(CQ\d+):\s*([0-9.]+)", line):
            blind[cur][q] = float(v)
        if re.search(r"·.*·\s*[0-9.]+\s*%?", line):
            blind[cur]["res"].append(num(line.rsplit("·", 1)[1]))
    rows = list(csv.DictReader(open(os.path.join(E, "resultados.csv"), encoding="utf-8")))
    vals = collections.defaultdict(set)
    for r in rows:
        vals[r["id_estudio"]].add(num(r["valor"]))
    # blind comparison uses the AI-derived values BEFORE any author decision (l2_resuelto.json)
    pre = json.load(open(os.path.join(E, "l2_resuelto.json")))
    ext = {sid: {f: (v.get("valor") or "PENDIENTE") for f, v in st["extraccion"].items()} for sid, st in pre.items()}
    cal = {r["id_estudio"]: r for r in csv.DictReader(open(os.path.join(SLR, "calidad", "calidad.csv"), encoding="utf-8"))}
    sc = collections.Counter()
    detail = []
    for sid, b in blind.items():
        for f in ("escenario", "historial_eval"):
            if f in b:
                sc[f + "_n"] += 1
                same = b[f] == ext[sid][f]
                sc[f] += same
                if not same:
                    detail.append(f"{sid} {f}: autora {b[f]} · IA {ext[sid][f]}")
        for q in [f"CQ{i}" for i in range(1, 11)]:
            if q in b and cal.get(sid, {}).get(q) not in (None, ""):
                sc["cq_n"] += 1
                d = abs(b[q] - float(cal[sid][q]))
                sc["cq"] += d == 0
                sc["cq_1paso"] += d <= 0.5
        for v in b["res"]:
            if v:
                sc["res_n"] += 1
                sc["res"] += v in vals.get(sid, set())
    out += ["## Muestra independiente de la autora (5 estudios, a ciegas)",
            f"- escenario: {pct(sc['escenario'], sc['escenario_n'])}",
            f"- historial_eval: {pct(sc['historial_eval'], sc['historial_eval_n'])}",
            f"- calidad, ítem idéntico: {pct(sc['cq'], sc['cq_n'])}; a ≤ 0,5 puntos: {pct(sc['cq_1paso'], sc['cq_n'])}",
            f"- resultados principales de la autora presentes en `resultados.csv`: {pct(sc['res'], sc['res_n'])}",
            "- Los demás campos de la muestra se anotaron en texto libre (no en el vocabulario controlado); se comparan cualitativamente.",
            ""] + [f"  - discrepancia: {x}" for x in detail]
    st["ciega_n"] = len(blind)
    for f in ("escenario", "historial_eval"):
        st["ciega_" + f] = [sc[f], sc[f + "_n"]]
    st["ciega_calidad_identico"], st["ciega_calidad_medio_punto"] = [sc["cq"], sc["cq_n"]], [sc["cq_1paso"], sc["cq_n"]]
    st["ciega_resultados"] = [sc["res"], sc["res_n"]]
    json.dump(st, open(os.path.join(E, "informe_acuerdo.json"), "w"), indent=1)
    adj = json.load(open(os.path.join(E, "ajustes_autora.json")))
    out += ["", "Resolución final de estas discrepancias por la autora: " + adj.get("_nota", "") +
            " Valores aplicados: " + json.dumps({k: v for k, v in adj.items() if not k.startswith("_")}, ensure_ascii=False)]
    open(os.path.join(E, "informe_acuerdo_extraccion.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
