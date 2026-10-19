"""Phase 10, steps 5-7 — in-depth synthesis (PI1-PI5, Level 2), confidence in findings and sensitivity analyses.
Rules as registered in plan_sintesis.md and 01_preguntas_picoc.md (M8 gap criterion); no meta-analysis (SWiM).

Population for PI1-PI5: Level 2 studies with validity >= 50 % (calidad.csv). Within-study contrasts are the main
evidence: per contrast Δ = valor_con - valor_sin (pp) on accuracy-type metric families; per study the median Δ of each
component class; across studies median, range and direction. Δ over the study's own reference baseline (same
configuration and base model, M7e) is secondary. Degradation per turn is stratified by evaluation history.
Outputs: slr/sintesis/tablas/pi*.csv, confianza_hallazgos.csv, sensibilidad.json, pi15_resultados.json, and figures.
"""
import collections
import csv
import json
import re
import statistics as st

import matplotlib.pyplot as plt
import numpy as np

from comun import EXT, SLR, escribir_tabla, estudios, leer_csv, lista, wilson
from estilo import ANCHO_COLUMNA, ANCHO_PAGINA, PALETA, aplicar_estilo, guardar

ACC = {"Ejecución por pregunta", "Ejecución por interacción (multiturno)", "Coincidencia exacta / lógica",
       "Coincidencia por pregunta (multiturno)", "Coincidencia por interacción (multiturno)", "Éxito de tarea / agente",
       "Estado del diálogo / aclaración"}
CLASES = {  # pillar -> [(class, regex on component name)] — first match wins; else "Otros componentes del pilar"
    "PI1": [("Reescritura de la pregunta", r"reescrit|rewrit|cqr|reformul"), ("Concatenación / historial", r"concat|historial|history|context")],
    "PI2": [("Grafo / estado estructurado", r"grafo|graph|estado|state|tracker|memoria|memory"),
            ("SQL / resultados previos", r"prev|sql previo|previous|edici|edit|result")],
    "PI3": [("Vinculación de esquemas", r"schema|esquema|linking|vincul|column|tabla|table"), ("Inferencia de joins", r"join|fk|clave")],
    "PI4": [("Autocorrección / retroalimentación de ejecución", r"autocorr|correc|refine|feedback|ejecuci|execut|depura|debug|repair|repar|verif|critic"),
            ("Autoconsistencia / selección de candidatos", r"consisten|vot|candidat|selec|rerank|re-rank"),
            ("Aclaración / interacción con el usuario", r"aclar|clarif|usuario|user|interact")],
}


def num(v):
    m = re.search(r"-?\d+(?:[.,]\d+)?", str(v))
    return float(m.group(0).replace(",", ".")) if m else None


OTROS = "Otros componentes del pilar"


def clase_regex(pilar, comp):
    for c, rx in CLASES.get(pilar, []):
        if re.search(rx, comp, re.I):
            return c
    return OTROS


def _otros():
    """Author-accepted decisions on «Otros» (slr/sintesis/otros_subclases.csv, revision_otros.md, 2026-10-19):
    reassignments of regex misses to a named class, and sub-classes of what stays in «Otros»."""
    f = SLR / "sintesis" / "otros_subclases.csv"
    filas = [r for r in leer_csv(f) if r["decision"].startswith("aceptad")] if f.exists() else []
    return ({(r["pilar"], r["componente"]): r["reasignar_a"] for r in filas if r["reasignar_a"]},
            {(r["pilar"], r["componente"]): r["subclase"] for r in filas if r["subclase"]})


REASIG, SUBCLASE = _otros()


def clase(pilar, comp):
    return REASIG.get((pilar, comp)) or clase_regex(pilar, comp)


def subclase_otros(pilar, comp):
    return SUBCLASE.get((pilar, comp)) if clase(pilar, comp) == OTROS else None


def efectos(contrastes, ids, clasif=None):
    """per finding (pillar, class): per-study median Δ, then median/range/direction across studies.
    clasif(pillar, component) -> class name or None (skip); default: clase()."""
    clasif = clasif or clase
    porest = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in contrastes:
        if r["id_estudio"] not in ids or r["metrica_familia"] not in ACC:
            continue
        a, b = num(r["valor_con"]), num(r["valor_sin"])
        if a is None or b is None:
            continue
        for p in [x for x in lista(r["pilar"]) if x in CLASES]:
            c = clasif(p, r["componente"])
            if c:
                porest[(p, c)][r["id_estudio"]].append(a - b)
    out = []
    for (p, c), d in sorted(porest.items()):
        meds = {s: st.median(v) for s, v in d.items()}
        vals = list(meds.values())
        n_con = sum(len(v) for v in d.values())
        conc = sum(1 for v in d.values() for x in v if x > 0)
        out.append({"pilar": p, "clase": c, "n_estudios": len(vals), "n_contrastes": n_con,
                    "mediana_pp": round(st.median(vals), 2), "min_pp": round(min(vals), 2), "max_pp": round(max(vals), 2),
                    "estudios_positivos": sum(1 for x in vals if x > 0), "estudios_negativos": sum(1 for x in vals if x < 0),
                    "estudios_nulos": sum(1 for x in vals if x == 0), "pct_contrastes_positivos": round(100 * conc / n_con, 1),
                    "_estudios": sorted(meds), "_deltas": meds})
    return out


def main():
    E = {r["id_estudio"]: r for r in estudios()}
    cal = {r["id_estudio"]: r for r in leer_csv(SLR / "calidad" / "calidad.csv")}
    L2 = [s for s, r in E.items() if str(r["nivel"]) == "2"]
    ok = {s for s in L2 if cal.get(s, {}).get("supera_umbral") == "SI"}
    res = {"nivel2": len(L2), "nivel2_umbral": len(ok)}
    R = leer_csv(EXT / "resultados_taxonomia.csv")
    C = leer_csv(EXT / "contrastes_taxonomia.csv")
    aplicar_estilo()

    # --- taxonomy tables per PI (Level 2 above threshold) ---
    for nombre, campos in (("pi1_tecnicas", ["pi1_tecnica", "pi1_insumos_historial"]),
                           ("pi2_representacion", ["pi2_representacion", "pi2_grafo_nodos", "pi2_grafo_dinamico", "pi2_actualizacion", "pi2_coste_contexto"]),
                           ("pi3_joins", ["pi3_tecnica_linking", "pi3_inferencia_joins"]),
                           ("pi4_mecanismos", ["pi4_mecanismo", "pi4_senal", "pi4_aplicado_multiturno"]),
                           ("pi5_historial", ["historial_eval", "degradacion_reportada", "errores_join_reportados", "contaminacion_discutida"])):
        filas = []
        for f in campos:
            c = collections.Counter(v for s in ok for v in (lista(E[s][f]) or ["NR"]))
            filas += [{"campo": f, "codigo": k, "estudios": v, "pct": round(100 * v / len(ok), 1)} for k, v in c.most_common()]
        escribir_tabla(nombre, filas, ["campo", "codigo", "estudios", "pct"])

    # --- comparative table + Δ over own reference baseline ---
    deltas = []
    grupos = collections.defaultdict(dict)
    for r in R:
        if r["id_estudio"] not in ok or r["metrica_familia"] not in ACC:
            continue
        key = (r["id_estudio"], r["benchmark_canonico"], r["version"], r["particion"], r["metrica_canonica"], r["turno"],
               r["historial_eval"], r["conocimiento_externo"])
        v = num(r["valor"])
        if v is None:
            continue
        if r["sistema"].upper() == "PROPUESTO":
            grupos[key]["p"] = max(v, grupos[key].get("p", -1e9))
        elif r["es_linea_base_referencia"].upper() == "SI":
            grupos[key]["b"] = v
    for k, g in grupos.items():
        if "p" in g and "b" in g:
            deltas.append({"id_estudio": k[0], "benchmark": k[1], "metrica": k[4], "turno": k[5], "historial_eval": k[6],
                           "propuesto": g["p"], "linea_base": g["b"], "delta_pp": round(g["p"] - g["b"], 2)})
    escribir_tabla("pi_deltas_linea_base", deltas, ["id_estudio", "benchmark", "metrica", "turno", "historial_eval", "propuesto", "linea_base", "delta_pp"])
    comp = []
    for s in sorted(ok):
        r = E[s]
        main_ = [d for d in deltas if d["id_estudio"] == s and d["turno"].upper() == "TODOS"]
        best = max(main_, key=lambda d: d["delta_pp"]) if main_ else None
        comp.append({"id_estudio": s, "anio": r["anio"], "pilares": r["pilares_centrales"], "paradigma": r["paradigma_principal"],
                     "sin_entrenamiento": "SI" if r["requiere_entrenamiento"].upper() == "NO" else "NO",
                     "pi1": r["pi1_tecnica"], "pi2": r["pi2_representacion"], "pi3_joins": r["pi3_inferencia_joins"], "pi4": r["pi4_mecanismo"],
                     "historial_eval": r["historial_eval"], "benchmark": best["benchmark"] if best else "", "metrica": best["metrica"] if best else "",
                     "resultado": best["propuesto"] if best else "", "delta_pp": best["delta_pp"] if best else "", "validez": cal[s]["validez_pct"]})
    escribir_tabla("pi_tabla_comparativa", comp, list(comp[0].keys()))
    res["deltas_linea_base"] = {"configuraciones": len(deltas), "estudios": len({d["id_estudio"] for d in deltas}),
                                "mediana_pp": round(st.median([d["delta_pp"] for d in deltas]), 2) if deltas else None}

    # --- within-study component effects (main evidence) ---
    ef = efectos(C, ok)
    escribir_tabla("pi_efectos_componentes", ef, [k for k in ef[0] if not k.startswith("_")])
    fig, ax = plt.subplots(figsize=(ANCHO_PAGINA * 0.75, 0.32 * len(ef) + 0.9))
    for i, e in enumerate(ef):
        xs = list(e["_deltas"].values())
        ax.scatter(xs, [i] * len(xs), s=10, color=PALETA[0], alpha=0.6, linewidths=0, zorder=2)
        ax.plot([e["mediana_pp"]] * 2, [i - 0.3, i + 0.3], color=PALETA[1], lw=2, zorder=3)
    ax.axvline(0, color="grey", lw=0.6, ls="--")
    ax.set_yticks(range(len(ef)), [f"{e['pilar']} · {e['clase']} (n = {e['n_estudios']})" for e in ef], fontsize=6.5)
    ax.invert_yaxis()
    ax.set_xlabel("Efecto del componente (pp; con − sin, mediana por estudio)")
    ax.grid(axis="y", visible=False)
    ax.scatter([], [], s=10, color=PALETA[0], label="Estudio (mediana de sus contrastes)")
    ax.plot([], [], color=PALETA[1], lw=2, label="Mediana entre estudios")
    ax.legend(loc="lower right", fontsize=6)
    guardar(fig, "pi_efectos_componentes", leyenda="Efecto de cada clase de componente según los contrastes dentro del estudio "
            "(activado frente a desactivado, mismo modelo base y configuración), en puntos porcentuales sobre métricas de exactitud. "
            "Cada punto es la mediana de los contrastes de un estudio; la barra, la mediana entre estudios. Síntesis sin metaanálisis "
            "(SWiM); estudios del Nivel 2 con validez ≥ 50 %.")
    res["efectos"] = [{k: v for k, v in e.items() if not k.startswith("_")} for e in ef]
    # sub-classes of «Otros» (post-close-out revision 2026-10-19; exploratory, appendix)
    efo = efectos(C, ok, subclase_otros)
    escribir_tabla("pi_efectos_otros_subclases", efo, [k for k in efo[0] if not k.startswith("_")])
    res["efectos_otros_subclases"] = [{k: v for k, v in e.items() if not k.startswith("_")} for e in efo]

    # --- PI5: benchmarks, metrics, history, degradation per turn ---
    bf = collections.Counter((r["benchmark_familia"], r["id_estudio"]) for r in R if r["id_estudio"] in ok)
    escribir_tabla("pi5_benchmarks", [{"familia": f, "estudios": n} for f, n in collections.Counter(f for f, _ in bf).most_common()], ["familia", "estudios"])
    mf = collections.Counter((r["metrica_familia"], r["id_estudio"]) for r in R if r["id_estudio"] in ok)
    escribir_tabla("pi5_metricas", [{"familia": f, "estudios": n} for f, n in collections.Counter(f for f, _ in mf).most_common()], ["familia", "estudios"])
    # per-turn values: verified rows of the targeted extraction (resultados_turnos.csv); turns >= 4 merged into "4+"
    curvas = collections.defaultdict(lambda: collections.defaultdict(list))
    MET_ACC = {"QM", "EX", "EM", "ESM", "TS", "IM", "OTRA:ACCURACY"}
    for r in leer_csv(EXT / "resultados_turnos.csv"):
        if r["id_estudio"] not in ok or r["verificacion"] == "no_verificado" or r["sistema"].upper() != "PROPUESTO":
            continue
        if r["metrica"].upper() not in MET_ACC:
            continue
        t = re.sub(r"[^0-9]", "", r["turno"])
        if not t:
            continue
        tn = min(int(t), 4)
        v = num(r["valor"])
        if v is None:
            continue
        key = (r["id_estudio"], r["benchmark"].upper(), r["metrica"].upper(), (r["historial_eval"] or "NR").upper())
        curvas[key][tn].append((v, num(r["n_turno"]) or 1))
    curvas = {k: {t: (sum(v * w for v, w in xs) / sum(w for _, w in xs), sum(w for _, w in xs)) for t, xs in d.items()}
              for k, d in curvas.items()}
    pend = []
    for (s, b, m, h), pts in curvas.items():
        if len(pts) < 3 or 1 not in pts:
            continue
        xs = np.array(sorted(pts))
        ys = np.array([pts[x][0] for x in xs])
        w = np.array([pts[x][1] for x in xs])
        slope = float(np.polyfit(xs, ys, 1, w=np.sqrt(w))[0])
        pend.append({"id_estudio": s, "benchmark": b, "metrica": m, "historial_eval": h, "turnos": len(xs),
                     "pendiente_pp_por_turno": round(slope, 2), "valor_turno1": pts[1][0], "_xs": xs, "_ys": ys})
    escribir_tabla("pi5_pendientes", pend, ["id_estudio", "benchmark", "metrica", "historial_eval", "turnos", "pendiente_pp_por_turno", "valor_turno1"])
    NOMBRE_H = {"PREDICHO": "Historial predicho", "SOLO_PREGUNTAS": "Solo preguntas previas", "GOLD": "Historial gold", "NR": "No reportado"}
    estratos = [h for h in ["PREDICHO", "SOLO_PREGUNTAS", "GOLD", "NR"] if any(p["historial_eval"] == h for p in pend)]
    sin_datos = [NOMBRE_H[h] for h in ["PREDICHO", "SOLO_PREGUNTAS", "GOLD", "NR"] if h not in estratos]
    res["degradacion"] = {}
    fig, axs = plt.subplots(1, len(estratos), figsize=(ANCHO_PAGINA * 0.25 * max(2, len(estratos)) + 0.6, 2.4), sharey=True, squeeze=False)
    axs = axs[0]
    for ax, h, let in zip(axs, estratos, "abcd"):
        grp = [p for p in pend if p["historial_eval"] == h]
        for p in grp:
            ax.plot(p["_xs"], 100 * p["_ys"] / p["valor_turno1"], color=PALETA[0], lw=0.6, alpha=0.5, marker="o", ms=1.5)
        if grp:
            med = st.median([p["pendiente_pp_por_turno"] for p in grp])
            res["degradacion"][h] = {"curvas": len(grp), "estudios": len({p["id_estudio"] for p in grp}), "pendiente_mediana_pp": round(med, 2)}
            ax.text(0.97, 0.95, f"{len({p['id_estudio'] for p in grp})} estudios\nmediana {med:+.1f} pp/turno", transform=ax.transAxes,
                    ha="right", va="top", fontsize=6)
        ax.axhline(100, color="grey", lw=0.5, ls="--")
        ax.set_title(f"({let}) {NOMBRE_H[h]}")
        ax.set_xticks([1, 2, 3, 4], ["1", "2", "3", "4+"])
        ax.set_xlabel("Turno")
    axs[0].set_ylabel("Exactitud relativa al turno 1 (%)")
    guardar(fig, "pi5_degradacion", leyenda="Degradación de la exactitud a lo largo de los turnos (sistema propuesto, normalizada al "
            "turno 1; turnos ≥ 4 agrupados en «4+»), separada por el tipo de historial usado en la evaluación: "
            + "; ".join(f"({l}) {NOMBRE_H[h].lower()}" for l, h in zip("abcd", estratos))
            + ". Valores por turno extraídos de las tablas de cada estudio y verificados en la página citada. "
            + (f"Sin curvas con al menos tres turnos para: {', '.join(x.lower() for x in sin_datos)}. " if sin_datos else "")
            + "Los grupos de turno contienen preguntas distintas, por lo que la pendiente mezcla profundidad y dificultad; "
            "las pendientes no se agrupan entre estratos.")

    # --- M8 gap criterion ---
    def a_(r, laxo=False):
        rep = lista(r["pi2_representacion"])
        upd = r["pi2_actualizacion"].upper()
        return "ESTRUCTURA_EXPLICITA" in rep or ("GRAFO" in rep and (upd in ("REGLAS_DETERMINISTAS", "LLM_GENERATIVA") or laxo))
    b_ = lambda r: r["pi3_inferencia_joins"].upper() in ("ALGORITMICA_CAMINOS", "GRAFO_FK_RESTRICCIONES") or \
        any(x in lista(r["pi4_mecanismo"]) for x in ("EJECUCION_FEEDBACK_ERRORES", "REPARACION_SIMBOLICA"))
    c_ = lambda r: r["historial_eval"].upper() in ("PREDICHO", "SOLO_PREGUNTAS")
    estricto = [s for s in L2 if a_(E[s]) and b_(E[s]) and c_(E[s])]
    laxo = [s for s in L2 if a_(E[s], True) and b_(E[s]) and c_(E[s])]
    res["brecha_M8"] = {"estudios_que_combinan_a_b_c": estricto, "n": len(estricto),
                        "reformular_tesis": len(estricto) >= 2, "sensibilidad_grafos_neuronales": {"estudios": laxo, "n": len(laxo)},
                        "sin_entrenamiento_entre_ellos": [s for s in estricto if E[s]["requiere_entrenamiento"].upper() == "NO"]}
    # marginal and pairwise counts (added 2026-10-14): shows whether the null triple comes from rare components or
    # only from their conjunction (anti-bias refactor of the Discussion)
    res["brecha_M8"]["componentes"] = {
        "a": sum(a_(E[s]) for s in L2), "b": sum(b_(E[s]) for s in L2), "c": sum(c_(E[s]) for s in L2),
        "ab": sum(a_(E[s]) and b_(E[s]) for s in L2), "ac": sum(a_(E[s]) and c_(E[s]) for s in L2),
        "bc": sum(b_(E[s]) and c_(E[s]) for s in L2), "base": len(L2)}

    # --- Step 6: confidence in findings (GRADE-CERQual-like, registered rules) ---
    conf = []
    for e in ef:
        vs = [float(cal[s]["validez_pct"]) for s in e["_estudios"] if cal.get(s, {}).get("validez_pct")]
        mv = st.mean(vs) if vs else 0
        lim_m = "sin" if mv >= 75 else ("leves" if mv >= 50 else "importantes")
        pct = e["pct_contrastes_positivos"]
        coh = "sin" if pct >= 80 else ("leves" if pct >= 60 else "importantes")
        if e["n_contrastes"] < 3 and coh == "sin":
            coh = "leves"
        suf = "sin" if e["n_estudios"] >= 5 else ("leves" if e["n_estudios"] >= 3 else "importantes")
        rel = [r for r in C if r["id_estudio"] in e["_estudios"] and lista(r["pilar"]) and e["pilar"] in lista(r["pilar"])
               and clase(e["pilar"], r["componente"]) == e["clase"]]
        share = sum(1 for r in rel if r["benchmark_familia"] in ("Multiturno conversacional", "Un turno estándar")) / max(1, len(rel))
        per = "sin" if share == 1 else ("leves" if share >= 0.5 else "importantes")
        comps = [lim_m, coh, suf, per]
        nivel = "alta" if comps.count("importantes") == 0 and comps.count("leves") <= 1 else ("moderada" if comps.count("importantes") <= 1 else "baja")
        if e["clase"] == OTROS:  # heterogeneous bucket: no confidence rating (revision 2026-10-19)
            nivel = "no evaluada"
        conf.append({"hallazgo": f"{e['pilar']} · {e['clase']}: mediana {e['mediana_pp']:+.1f} pp ({e['estudios_positivos']}/{e['n_estudios']} estudios positivos)",
                     "limitaciones_metodologicas": lim_m, "validez_media": round(mv, 1), "coherencia": coh, "suficiencia": suf,
                     "pertinencia": per, "confianza": nivel})
    escribir_tabla("confianza_hallazgos", conf, list(conf[0].keys()))
    res["confianza"] = conf

    # --- Step 7: sensitivity analyses ---
    sens = {}
    allL2 = set(L2)
    ef_all = efectos(C, allL2)
    sens["1_reincorporar_bajo_umbral"] = [{"hallazgo": f"{e['pilar']} · {e['clase']}", "mediana_pp": e["mediana_pp"], "n_estudios": e["n_estudios"]} for e in ef_all]
    nopre = {s for s in ok if E[s]["foro_tipo"] != "PREPRINT"}
    sens["2_sin_preprints_efectos"] = [{"hallazgo": f"{e['pilar']} · {e['clase']}", "mediana_pp": e["mediana_pp"], "n_estudios": e["n_estudios"]} for e in efectos(C, nopre)]
    central = lambda r: any(p in lista(r["pilares_centrales"]) for p in ("PI3", "PI4"))
    contiene = lambda r: any(p in lista(r["pilares_contenidos"]) for p in ("PI3", "PI4"))
    mt = lambda r: str(r["nivel"]) == "2"

    def d4(pob):
        k = sum(1 for r in pob if mt(r))
        lo, hi = wilson(k, len(pob))
        return {"k": k, "n": len(pob), "p": round(k / len(pob), 4) if pob else None, "ic95": [round(lo, 4), round(hi, 4)],
                "conclusion": "minoritario" if hi < 0.50 else ("no concluyente" if lo <= 0.50 else "mayoritario")}
    todos = list(E.values())
    sens["2_sin_preprints_D4"] = d4([r for r in todos if central(r) and r["foro_tipo"] != "PREPRINT"])
    sens["3_D4_laxo"] = d4([r for r in todos if central(r) or (mt(r) and contiene(r))])
    sens["4_D4_solo_busqueda_en_bases"] = d4([r for r in todos if central(r) and r["origen"] == "BUSQUEDA"])
    sens["5_contingencia_nivel1"] = "No aplica: la regla de contingencia por volumen no se activó (texto completo de un turno < 400)."
    top = {"A*", "A", "Q1", "Q2"}
    sens["A5_D4_foros_de_primer_nivel"] = d4([r for r in todos if central(r) and r["foro_nivel"] in top])
    nrs = json.load(open(SLR / "sintesis" / "pi0_resultados.json"))["no_recuperados_por_senal"]
    base = [r for r in todos if central(r)]
    k0 = sum(1 for r in base if mt(r))
    kk, nn = k0 + nrs.get("multiturno", 0), len(base) + nrs.get("multiturno", 0) + nrs.get("un_turno", 0)
    lo, hi = wilson(kk, nn)
    sens["A4_D4_con_no_recuperados_segun_senal"] = {"k": kk, "n": nn, "p": round(kk / nn, 4), "ic95": [round(lo, 4), round(hi, 4)],
                                                    "supuesto": "todos los no recuperados cuentan en el denominador; los de señal multiturno, también en el numerador (cota conservadora)"}
    json.dump(sens, open(SLR / "sintesis" / "sensibilidad.json", "w"), indent=1, ensure_ascii=False)
    res["sensibilidad"] = sens
    json.dump(res, open(SLR / "sintesis" / "pi15_resultados.json", "w"), indent=1, ensure_ascii=False, default=str)
    print(json.dumps({k: v for k, v in res.items() if k not in ("confianza",)}, indent=1, ensure_ascii=False, default=str)[:6000])
    print("CONFIANZA", json.dumps(conf, indent=1, ensure_ascii=False)[:3000])


if __name__ == "__main__":
    main()
