"""Phase 9 step 4 (A5) — Level 2 confirmation sheet: one line per study (author confirms the level).
Rows: studies with nivel_previsto MULTITURNO + Level 1 studies an extractor coded as MULTITURNO.
Reason shown: full-text reviewer A's reason (main or snowball workspace). Writes confirmacion_nivel2.md.
Usage (from slr/extraccion): python scripts/hoja_nivel2.py
"""
import csv
import json
import os

E = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
C = os.path.join(os.path.dirname(E), "cribado")
ft = {}
for w, p in (("sr_work", "R"), ("sr_work_bola", "B")):
    for rid, x in json.load(open(os.path.join(C, w, "ft_decisions.json"))).items():
        ft[p + rid[1:]] = (x.get("A") or {}).get("why", "")
base = list(csv.DictReader(open(os.path.join(E, "base_estudios.csv"), encoding="utf-8")))
ab = json.load(open(os.path.join(E, "runs_nivel1", "_ab.json")))
flag = {i for i in ab["A"] if "MULTITURNO" in (ab["A"][i].get("escenario"), ab["B"].get(i, {}).get("escenario"))}
out = ["# Confirmación del Nivel 2 (multiturno)", "",
       "Marque en la última columna **OK** si el estudio es **multiturno** (preguntas sucesivas del usuario dependientes "
       "del contexto) y va al Nivel 2, o **N1** si es de un turno. La sección B son estudios previstos como de un turno que "
       "algún extractor codificó como multiturno: escriba **N2** si deben pasar al Nivel 2, si no **OK**.", "",
       "## A. Previstos multiturno", "", "| ID | Año | Título | Motivo (revisor de texto completo) | Decisión |", "|---|---|---|---|---|"]
rows_b = []
for b in base:
    line = f"| {b['id_estudio']} | {b['anio']} | {b['titulo'][:90].replace('|', '/')} | {ft.get(b['id_estudio'], '')[:140].replace('|', '/')} | |"
    if b["nivel_previsto"] == "MULTITURNO":
        out.append(line)
    elif b["id_estudio"] in flag:
        rows_b.append(line)
out += ["", "## B. Previstos de un turno, marcados multiturno por un extractor", "",
        "| ID | Año | Título | Motivo (revisor de texto completo) | Decisión |", "|---|---|---|---|---|"] + rows_b
open(os.path.join(E, "confirmacion_nivel2.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"A: {sum(1 for b in base if b['nivel_previsto'] == 'MULTITURNO')}  B: {len(rows_b)}")
