"""Phase 9 — final author review sheet for extraction (A5 (c)) and the blind-sample comparison.

Sections: A) items the tie-break could not decide; B) Level 2 studies with validity score 40-60 % (threshold
decisions), with their 5 validity items; C) random 10 % of agreed Level 2 coded values (seed 2026);
D) random 10 % of Level 1 studies (all light fields). Also writes acuerdo_muestra_autora.md comparing the
author's blind extraction (muestra_independiente_autora.md, parsed leniently) is left to the merge step.
Answers: OK, or the corrected value, on each "Decisión:" line. Writes revision_extraccion.md.
Usage (from slr/extraccion): python scripts/hoja_revision_extraccion.py
"""
import csv
import json
import os
import random

E = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
VALID = ["CQ2", "CQ4", "CQ5", "CQ6", "CQ7"]


def main():
    res = json.load(open(os.path.join(E, "l2_resuelto.json")))
    l1 = json.load(open(os.path.join(E, "l1_resuelto.json")))
    base = {r["id_estudio"]: r for r in csv.DictReader(open(os.path.join(E, "base_estudios.csv"), encoding="utf-8"))}
    conf = json.load(open(os.path.join(E, "confirmacion_nivel2.json")))
    n1 = {i for i, _ in conf["N1"]}
    rnd = random.Random(2026)
    out = ["# Revisión final de la extracción (casos no obvios y muestras)", "",
           "## Qué escribir en `Decisión:` (por sección)", "",
           "| Sección | Tipo de ítem | Opciones válidas | Ejemplo |", "|---|---|---|---|",
           "| **A** | campo | `A` · `B` (acepta ese valor) · el valor correcto con los códigos de la tabla de abajo · `NR` (no reportado) | `B` · `REESCRITURA; CONCATENACION` |",
           "| **A** | calidad CQn | `A` · `B` · `1` · `0.5` · `0` | `0.5` |",
           "| **A** | contraste | `OK` (la fila es correcta) · `NO` (descartar la fila) · valores corregidos `con X / sin Y` | `con 52.1 / sin 48.3` |",
           "| **B** | cada ítem de validez CQ2, CQ4–CQ7 | `OK` (acepta la puntuación mostrada) · `1` · `0.5` · `0` | `OK` |",
           "| **C** | valor concordante | `OK` · el valor correcto (códigos de la tabla de abajo) | `OK` |",
           "| **D** | estudio del Nivel 1 | `OK` (todo correcto) · solo los campos a corregir como `campo=valor`, separados por `;` | `paradigma_principal=LLM_PROMPTING; pi4_mecanismo=NR` |",
           "",
           "Listas de varios códigos: sepárelos con `;`. Páginas = páginas del PDF. Calidad: 1 = sí/completo · 0,5 = parcial · 0 = no "
           "(descriptores completos en `../calidad/checklist_calidad.md`).", ""]
    form = open(os.path.join(E, "formulario_extraccion.md"), encoding="utf-8").read()
    rows = {m.group(1): m.group(0) for m in __import__("re").finditer(r"(?m)^\| `([a-z0-9_]+)` \|.*$", form)}
    a = []
    for sid, s in sorted(res.items()):
        for k, v in s["extraccion"].items():
            if v["regla"] == "pendiente":
                a.append((sid, f"campo `{k}`", f"A: `{v['A']}` ({v.get('ubic_A')}) · B: `{v['B']}` ({v.get('ubic_B')})"))
        for k, v in s["calidad"].items():
            if v["regla"] == "pendiente":
                a.append((sid, f"calidad {k}", f"A: {v['A'].get('p')} — {v['A'].get('justif')} · B: {v['B'].get('p')} — {v['B'].get('justif')}"))
        for i, r in enumerate(s["contrastes"]):
            if r["_regla"] == "no_verificado":
                a.append((sid, f"contraste fila {i}", f"{r.get('componente')} · {r.get('benchmark')} {r.get('metrica')}: con {r.get('valor_con')} / sin {r.get('valor_sin')} ({r.get('ubicacion')}) — ¿correcto?"))
    out += [f"## A. No decididos por el desempate ({len(a)})", ""]
    for sid, item, txt in a:
        out += [f"- **{sid}** — {item}: {txt}", "  - **Decisión:** "]
    b = []
    for sid, s in sorted(res.items()):
        ps = [s["calidad"].get(q, {}).get("p") for q in VALID]
        if None not in ps:
            pct = 100 * sum(ps) / 5
            if 40 <= pct <= 60:
                b.append((sid, pct, s))
    out += ["", f"## B. Estudios cerca del umbral de validez, 40–60 % ({len(b)})", "",
            "Umbral: ≥ 50 % entra a la síntesis en profundidad. Revise los 5 ítems de validez.", ""]
    for sid, pct, s in b:
        out += [f"### {sid} — {base[sid]['titulo'][:90]} — validez {pct:.0f} %"]
        for q in VALID:
            c = s["calidad"][q]
            out += [f"- {q}: **{c['p']}** — {c.get('justif')} *(p. {c.get('ubic')})*  · **Decisión:** "]
        out.append("")
    agreed = [(sid, k, v) for sid, s in sorted(res.items()) for k, v in s["extraccion"].items() if v["regla"] == "acuerdo"]
    c = rnd.sample(agreed, max(1, round(0.10 * len(agreed))))
    out += [f"## C. Muestra aleatoria del 10 % de valores concordantes del Nivel 2 ({len(c)} de {len(agreed)})", ""]
    for sid, k, v in sorted(c):
        out += [f"- **{sid}** `{k}` = `{v['valor']}` *(p. {v.get('ubic')})* · **Decisión:** "]
    l1ids = sorted(i for i in l1 if i not in res or i in n1)
    d = sorted(rnd.sample(l1ids, max(1, round(0.10 * len(l1ids)))))
    out += ["", f"## D. Muestra aleatoria del 10 % del Nivel 1 ({len(d)} de {len(l1ids)} estudios)", "",
            "Lea solo título y resumen; corrija lo que no cuadre.", ""]
    for sid in d:
        vals = "; ".join(f"{k}=`{v['valor']}`" for k, v in l1[sid].items())
        out += [f"- **{sid}** — {base.get(sid, {}).get('titulo', '')[:80]}", f"  - {vals}", "  - **Decisión:** "]
    used = sorted({k for _, k, _ in c} | {k for sid in d for k in l1[sid]} |
                  {it.split("`")[1] for _, it, _ in a if it.startswith("campo")})
    codes = ["## Códigos de los campos que aparecen en esta hoja (del formulario)", "", "| Campo | Vocabulario |", "|---|---|"]
    codes += [rows[k] for k in used if k in rows] + [""]
    out[out.index("## Qué escribir en `Decisión:` (por sección)") + 13:out.index("## Qué escribir en `Decisión:` (por sección)") + 13] = codes
    open(os.path.join(E, "revision_extraccion.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"A {len(a)}  B {len(b)}  C {len(c)}  D {len(d)}")


if __name__ == "__main__":
    main()
