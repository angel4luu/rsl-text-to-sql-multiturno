"""Phase 14, step 3a — decision matrix for the thesis direction.

Candidates: OE1-OE5 (proposal, step 1), DA-DG (alternatives, step 2) and the three step-2 combinations.
Criteria (0-3, higher = better): C1 problem evidence, C2 benefit evidence, C3 novelty, C4 feasibility,
C5 null-result risk (3 = low risk). Local relevance is dropped (author: not decisive, restricciones_autora.md).
Rules are documented in tesis/00-justificacion/reglas_matriz.md; every evidence score is computed from the step-1/2
outputs. The only judgment inputs are the PROBLEMA kinds, the benefit scope, the novelty indicator, the candidate
type and the feasibility requirements below — each is listed in the author's review sheet (revision_matriz.md).
No winner is declared: ranks under four weightings, rank range and Pareto dominance are reported instead.
Each judgment input has an alternative (ALTERNATIVAS); matriz_alternativas.csv shows the score/rank changes it causes.
Output: tesis/00-justificacion/datos/matriz_decision.csv, matriz_decision.json, matriz_alternativas.csv.
"""
import copy
import csv
import json
import statistics as st

from mapa_oe import SALIDA

CRITERIOS = ["C1_problema", "C2_beneficio", "C3_novedad", "C4_factibilidad", "C5_riesgo_nulo"]
ESCENARIOS = {  # weights per criterion; E3 treats C2 as not applicable for evaluation-type candidates
    "E0_iguales": [1, 1, 1, 1, 1],
    "E1_factibilidad": [1, 1, 1, 2, 2],
    "E2_evidencia": [2, 2, 1, 1, 1],
    "E3_iguales_C2_NA": [1, 1, 1, 1, 1],
}
# feasibility penalties (restricciones_autora.md): each costs 1 point from 3; INVIABLE sets 0
PENALIZACIONES = {
    "SUSTITUTO": "requiere simular usuarios o sustituir datos empresariales por datos públicos",
    "ANOTACION": "requiere construir o anotar un conjunto de datos",
    "MULTICOMPONENTE": "requiere implementar varios componentes nuevos que interactúan",
    "COSTE_API_ALTO": "muchas llamadas por turno o contextos largos (coste de API alto)",
    "INFO_NO_OBSERVABLE": "depende de información no observable (p. ej., datos de entrenamiento de modelos cerrados)",
    "INVIABLE": "requiere GPU, usuarios reales o datos empresariales sin sustituto",
}

# C2 is "not applicable" (E3 only) for evaluation-type candidates with no matching contrast class
# ref = (source, group, indicator label); source "oe" = mapa_oe_indicadores.csv, "dir" = mapa_direcciones_indicadores.csv
# problem kinds: deficit (failure or cost reported), reporte (share of studies NOT reporting something that affects
# validity), cobertura (topic barely covered; not a problem by itself)
CANDIDATOS = {
    "OE1": {"nombre": "Preprocesamiento lingüístico y restauración del contexto", "tipo": "tecnica",
            "problema": [], "problema_cualitativo": True,
            "beneficio": [("OE1", "Reescritura / reformulación / discurso", "amplio")],
            "novedad": ("oe", "OE1", "Reescritura de la pregunta"), "requisitos": []},
    "OE2": {"nombre": "Grafo semántico de estado de dos capas", "tipo": "tecnica",
            "problema": [("deficit", ("oe", "OE2", "Coste de contexto que crece con los turnos"))],
            "beneficio": [("OE2", "Grafo / estado / memoria estructurada", "amplio")],
            "novedad": ("oe", "OE2", "Grafo dinámico entre turnos"), "requisitos": ["MULTICOMPONENTE"]},
    "OE3": {"nombre": "Enrutamiento relacional simbólico", "tipo": "tecnica",
            "problema": [("deficit", ("oe", "OE3", "Errores de join reportados"))],
            "beneficio": [("OE3", "Joins / FK / caminos", "exacto")],
            "novedad": ("oe", "OE3", "Joins por algoritmo de caminos"), "requisitos": []},
    "OE4": {"nombre": "Verificación por ejecución y autocorrección", "tipo": "tecnica",
            "problema": [], "problema_cualitativo": True,
            "beneficio": [("OE4", "Autocorrección / ejecución / verificación", "amplio")],
            "novedad": ("oe", "OE4", "Retroalimentación de errores de ejecución"), "requisitos": ["COSTE_API_ALTO"]},
    "OE5": {"nombre": "Evaluación multiturno y degradación por turno", "tipo": "evaluacion",
            "problema": [("deficit", ("oe", "OE5", "Degradación por turno reportada"))],
            "beneficio": [], "novedad": ("dir", "DC", "Resultados desagregados por turno"),
            "requisitos": ["SUSTITUTO"]},
    "DA": {"nombre": "Aclaración con el usuario e interacción (incl. abstención)", "tipo": "tecnica",
           "problema": [], "problema_cualitativo": True,
           "beneficio": [("OE4", "Aclaración / interacción con el usuario (alternativa)", "exacto")],
           "novedad": ("dir", "DA", "Mecanismo: aclaración con el usuario"), "requisitos": ["SUSTITUTO"]},
    "DB": {"nombre": "Datos en español y multilingües", "tipo": "evaluacion",
           "problema": [("cobertura", ("dir", "DB", "Datos en español"))],
           "beneficio": [], "novedad": ("dir", "DB", "Datos en español"), "requisitos": ["ANOTACION"]},
    "DC": {"nombre": "Metodología de evaluación multiturno", "tipo": "evaluacion",
           "problema": [("deficit", ("dir", "DC", "Degradación por turno reportada")),
                        ("reporte", ("dir", "DC", "Resultados desagregados por turno"))],
           "beneficio": [], "novedad": ("dir", "DC", "Resultados desagregados por turno"), "requisitos": []},
    "DD": {"nombre": "Contaminación de benchmarks y fecha de los modelos", "tipo": "evaluacion",
           "problema": [("reporte", ("dir", "DD", "Contaminación discutida")),
                        ("reporte", ("dir", "DD", "Fecha / versión del modelo reportada"))],
           "beneficio": [], "novedad": ("dir", "DD", "Contaminación discutida"), "requisitos": ["INFO_NO_OBSERVABLE"]},
    "DE": {"nombre": "Líneas base simples fuertes", "tipo": "evaluacion",
           "problema": [], "problema_cualitativo": False,
           "beneficio": [("OE2", "SQL previo / edición / ventana (alternativa)", "exacto"),
                         ("OE1", "Concatenación / historial (alternativa)", "exacto")],
           "novedad": ("dir", "DE", "Representación: historial plano"), "requisitos": []},
    "DF": {"nombre": "Coste y eficiencia", "tipo": "evaluacion",
           "problema": [("deficit", ("dir", "DF", "Coste de contexto que crece con los turnos")),
                        ("reporte_inv", ("dir", "DF", "Coste reportado: ninguno"))],
           "beneficio": [], "novedad": ("complemento", ("dir", "DF", "Coste reportado: ninguno")), "requisitos": []},
    "DG": {"nombre": "Esquemas grandes / empresariales", "tipo": "evaluacion",
           "problema": [("cobertura", ("dir", "DG", "Resultados en datos propios / industriales"))],
           "beneficio": [], "novedad": ("dir", "DG", "Resultados en datos propios / industriales"),
           "requisitos": ["SUSTITUTO", "COSTE_API_ALTO"]},
}
COMBINACIONES = {"DA+DC": ["DA", "DC"], "DB+DD": ["DB", "DD"], "DE+DF+DG": ["DE", "DF", "DG"]}


def indicadores():
    I = {}
    for fuente, archivo, grupo in (("oe", "mapa_oe_indicadores.csv", "oe"), ("dir", "mapa_direcciones_indicadores.csv", "direccion")):
        for r in csv.DictReader(open(SALIDA / archivo, encoding="utf-8")):
            I[(fuente, r[grupo], r["indicador"])] = float(r["pct_nivel2_umbral"])
    return I


def contrastes():
    C = {}
    for r in csv.DictReader(open(SALIDA / "mapa_oe_contrastes.csv", encoding="utf-8")):
        if r["poblacion"] == "principal_nivel2_umbral":
            C[(r["oe"], r["clase"])] = r
    return C


def p_problema(kind, pct):
    if kind == "deficit":
        return 3 if pct >= 100 / 3 else 2 if pct >= 10 else 1
    if kind in ("reporte", "reporte_inv"):  # validity gap without measured consequence: capped at 2
        return 2 if pct >= 50 else 1
    return 1  # cobertura


def p_beneficio(c, alcance):
    n = int(c["n_estudios"] or 0)
    if n == 0:
        return 0
    pos, conf = int(c["estudios_positivos"]) / n, c["confianza"]
    if n >= 5 and pos >= 0.8 and conf == "alta" and alcance == "exacto":
        return 3
    if n >= 3 and pos > 0.5 and conf in ("alta", "moderada"):
        return 2
    return 1


def p_novedad(pct):  # coverage of the candidate's core solution in the main population
    return 3 if pct < 5 else 2 if pct < 15 else 1 if pct < 30 else 0


def puntuar(c, I, C, c5_eval=3):
    ev = {}
    probs = []
    for kind, ref in c["problema"]:
        pct = I[ref]
        if kind == "reporte":
            pct = 100 - pct  # share NOT reporting
        probs.append((kind, ref[2], pct, p_problema(kind, pct)))
    c1 = max((x[3] for x in probs), default=1 if c.get("problema_cualitativo") else 0)
    ev["C1"] = probs or ("cualitativo" if c.get("problema_cualitativo") else "sin indicador")
    bens = [(oe, cl, al, C[(oe, cl)]) for oe, cl, al in c["beneficio"]]
    c2 = max((p_beneficio(x[3], x[2]) for x in bens), default=0)
    ev["C2"] = [{"clase": cl, "alcance": al, "n_estudios": x["n_estudios"], "positivos": x["estudios_positivos"],
                 "confianza": x["confianza"]} for oe, cl, al, x in bens] or "sin contrastes"
    nv = c["novedad"]
    pct = 100 - I[nv[1]] if nv[0] == "complemento" else I[nv]
    c3 = p_novedad(pct)
    ev["C3"] = {"indicador": (nv[1] if nv[0] == "complemento" else nv)[2], "cobertura_pct": round(pct, 1),
                "complemento": nv[0] == "complemento"}
    req = c["requisitos"]
    c4 = 0 if "INVIABLE" in req else max(0, 3 - len(req))
    ev["C4"] = req
    if c["tipo"] == "evaluacion":
        c5 = c5_eval
    else:
        n = max((int(x[3]["n_estudios"] or 0) for x in bens), default=0)
        ok = any(int(x[3]["n_estudios"] or 0) >= 5 and int(x[3]["estudios_positivos"]) / int(x[3]["n_estudios"]) >= 0.8 for x in bens)
        c5 = 2 if ok else 1 if n >= 1 else 0
    return [c1, c2, c3, c4, c5], ev


def total(p, pesos):  # p[i] None = criterion not applicable, weights renormalised
    pares = [(x, w) for x, w in zip(p, pesos) if x is not None]
    return round(100 * sum(x * w for x, w in pares) / (3 * sum(w for _, w in pares)), 1)


def matriz(I, C, cands, ev_comb=st.mean, c5_eval=3):
    filas = {}
    for k, c in cands.items():
        p, ev = puntuar(c, I, C, c5_eval)
        na = c["tipo"] == "evaluacion" and not c["beneficio"]
        filas[k] = {"candidato": k, "nombre": c["nombre"], "tipo": c["tipo"], "p": p, "c2_E3": None if na else p[1], "evidencia": ev}
    for k, partes in COMBINACIONES.items():  # evidence = mean, novelty = max, feasibility and null risk = min
        P = [filas[x]["p"] for x in partes]
        aplic = [filas[x]["c2_E3"] for x in partes if filas[x]["c2_E3"] is not None]
        p = [round(ev_comb([x[0] for x in P]), 2), round(ev_comb([x[1] for x in P]), 2), max(x[2] for x in P),
             min(x[3] for x in P), min(x[4] for x in P)]
        filas[k] = {"candidato": k, "nombre": " + ".join(filas[x]["nombre"] for x in partes), "tipo": "combinacion",
                    "p": p, "c2_E3": round(st.mean(aplic), 2) if aplic else None, "evidencia": {"componentes": partes}}
    for esc, pesos in ESCENARIOS.items():
        for f in filas.values():
            p = [f["p"][0], f["c2_E3"], *f["p"][2:]] if esc.endswith("NA") else f["p"]
            f[esc] = total(p, pesos)
        orden = sorted(filas.values(), key=lambda f: -f[esc])
        for f in orden:  # competition ranking: ties share the best rank
            f["rango_" + esc] = 1 + sum(g[esc] > f[esc] for g in orden)
    for f in filas.values():
        rs = [f["rango_" + e] for e in ESCENARIOS]
        f["rango_min"], f["rango_max"] = min(rs), max(rs)
        f["dominado_por"] = sorted(g["candidato"] for g in filas.values() if g is not f
                                   and all(a >= b for a, b in zip(g["p"], f["p"])) and g["p"] != f["p"])
    return filas


def con(cand, clave, valor):
    d = copy.deepcopy(CANDIDATOS)
    d[cand][clave] = valor
    return d


# alternatives to the judgment inputs, listed in revision_matriz.md: (code, description, kwargs for matriz)
ALTERNATIVAS = [
    ("D14", "OE1: novedad por clasificación de actos de discurso", {"cands": con("OE1", "novedad", ("oe", "OE1", "Clasificación de actos de discurso"))}),
    ("D15", "OE4: novedad por reparación simbólica", {"cands": con("OE4", "novedad", ("oe", "OE4", "Reparación simbólica"))}),
    ("D16", "DE: problema cualitativo (1)", {"cands": con("DE", "problema_cualitativo", True)}),
    ("D17", "DG: problema por errores de join (déficit)", {"cands": con("DG", "problema", [("deficit", ("dir", "DG", "Errores de join reportados"))])}),
    ("D18a", "OE5 sin SUSTITUTO (solo SParC/CoSQL)", {"cands": con("OE5", "requisitos", [])}),
    ("D18b", "OE3 con MULTICOMPONENTE", {"cands": con("OE3", "requisitos", ["MULTICOMPONENTE"])}),
    ("D19", "Combinaciones: evidencia = máximo de componentes", {"ev_comb": max}),
    ("D20", "Riesgo nulo de candidatos de evaluación = 2", {"c5_eval": 2}),
]


def main():
    I, C = indicadores(), contrastes()
    filas = matriz(I, C, CANDIDATOS)
    filas_csv = [{"candidato": f["candidato"], "nombre": f["nombre"], "tipo": f["tipo"],
                  **dict(zip(CRITERIOS, f["p"])), "C2_E3": "NA" if f["c2_E3"] is None else f["c2_E3"], **{e: f[e] for e in ESCENARIOS},
                  **{"rango_" + e: f["rango_" + e] for e in ESCENARIOS},
                  "rango_min": f["rango_min"], "rango_max": f["rango_max"],
                  "dominado_por": ";".join(f["dominado_por"])} for f in filas.values()]
    with open(SALIDA / "matriz_decision.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas_csv[0]))
        w.writeheader()
        w.writerows(filas_csv)
    json.dump({"criterios": CRITERIOS, "escenarios": ESCENARIOS, "penalizaciones": PENALIZACIONES,
               "candidatos": filas}, open(SALIDA / "matriz_decision.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    alt = []
    for cod, desc, kw in ALTERNATIVAS:
        A = matriz(I, C, **{"cands": CANDIDATOS, **kw})
        for k, f in A.items():
            if any(f[e] != filas[k][e] for e in ESCENARIOS):
                alt.append({"decision": cod, "alternativa": desc, "candidato": k,
                            **{f"{v}_{e}": x[k][e] for e in ("E0_iguales",) for v, x in (("base", filas), ("alt", A))},
                            **{f"{v}_rango_{e}": x[k]["rango_" + e] for e in ESCENARIOS for v, x in (("base", filas), ("alt", A))}})
    with open(SALIDA / "matriz_alternativas.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(alt[0]))
        w.writeheader()
        w.writerows(alt)
    print(f"{'cand':<9}{'C1':>5}{'C2':>5}{'C3':>5}{'C4':>5}{'C5':>5}" + "".join(f"{e[:3]:>7}" for e in ESCENARIOS) + "  rango  dominado_por")
    for f in sorted(filas.values(), key=lambda f: -f["E0_iguales"]):
        print(f"{f['candidato']:<9}" + "".join(f"{x:>5}" for x in f["p"]) + "".join(f"{f[e]:>7}" for e in ESCENARIOS)
              + f"  {f['rango_min']}-{f['rango_max']:<4} {','.join(f['dominado_por'])}")
    for a in alt:
        print(a["decision"], a["candidato"], a["base_E0_iguales"], "->", a["alt_E0_iguales"],
              " rangos", [a[f"base_rango_{e}"] for e in ESCENARIOS], "->", [a[f"alt_rango_{e}"] for e in ESCENARIOS])


if __name__ == "__main__":
    main()
