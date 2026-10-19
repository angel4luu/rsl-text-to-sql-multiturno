"""Phase 14, step 1 — evidence map: thesis specific objectives (OE1-OE5) -> SLR extraction codes and contrasts.

The proposal (00-contexto/TS Research Proposal.md) is treated as a hypothesis. For each OE this script counts, from the
closed SLR data (read-only): how often the proposed component appears (all studies / Level 2 / Level 2 above the quality
threshold), how often the competing alternatives appear, problem-evidence indicators, and within-study contrasts
(per-study median Δ in pp on accuracy-type metric families, same rules as figs/pi15_sintesis.py). Confidence follows the
registered GRADE-CERQual-like rules of pi15_sintesis.py step 6. The OE -> code mapping is in MAPEO and is approved by the
author in tesis/00-justificacion/revision_mapeo_oe.md.
clases_componentes.csv: regex class per contrast component (written on first run); a filled clase_final column
(class name, or NINGUNA) overrides the regex. Outputs: tesis/00-justificacion/datos/mapa_oe.json, mapa_oe_indicadores.csv, mapa_oe_contrastes.csv.
"""
import collections
import csv
import json
import re
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figs"))
from comun import EXT, RAIZ, SLR, estudios, leer_csv, lista  # noqa: E402
from pi15_sintesis import ACC, num  # noqa: E402

SALIDA = RAIZ / "tesis" / "00-justificacion" / "datos"
SALIDA.mkdir(parents=True, exist_ok=True)

# Indicator: (label, field, accepted codes, role). Roles: propuesta = what the OE proposes; alternativa = competing
# approach with its own evidence; problema = evidence that the problem the OE targets exists; contexto = scope info.
MAPEO = {
    "OE1": {"nombre": "Preprocesamiento lingüístico (clasificación de actos de discurso, anáfora/elipsis, reescritura)",
            "indicadores": [
                ("Reescritura de la pregunta", "pi1_tecnica", {"REESCRITURA"}, "propuesta"),
                ("Clasificación de actos de discurso", "pi1_tecnica", {"CLASIFICACION_DISCURSO"}, "propuesta"),
                ("Resolución explícita (anáfora/elipsis)", "pi1_tecnica", {"RESOLUCION_EXPLICITA"}, "propuesta"),
                ("Concatenación del historial", "pi1_tecnica", {"CONCATENACION"}, "alternativa")],
            "contrastes": [
                ("Reescritura / reformulación / discurso", {"PI1"}, r"reescrit|rewrit|cqr|reformul|discurso|intenci|intent|corefer|fup|ancla"),
                ("Concatenación / historial (alternativa)", {"PI1"}, r"concat|historial|history")]},
    "OE2": {"nombre": "Grafo semántico de estado de dos capas (seguimiento explícito del estado del diálogo)",
            "indicadores": [
                ("Representación: grafo", "pi2_representacion", {"GRAFO"}, "propuesta"),
                ("Representación: estructura explícita", "pi2_representacion", {"ESTRUCTURA_EXPLICITA"}, "propuesta"),
                ("Grafo dinámico entre turnos", "pi2_grafo_dinamico", {"SI"}, "propuesta"),
                ("Actualización por reglas deterministas", "pi2_actualizacion", {"REGLAS_DETERMINISTAS"}, "propuesta"),
                ("Coste de contexto acotado", "pi2_coste_contexto", {"ACOTADO"}, "propuesta"),
                ("Representación: historial plano", "pi2_representacion", {"HISTORIAL_PLANO"}, "alternativa"),
                ("Representación: edición del SQL previo", "pi2_representacion", {"SQL_PREVIO_EDICION"}, "alternativa"),
                ("Representación: memoria externa / ventana / resumen", "pi2_representacion", {"MEMORIA_EXTERNA", "VENTANA_DESLIZANTE", "RESUMEN"}, "alternativa"),
                ("Coste de contexto que crece con los turnos", "pi2_coste_contexto", {"CRECE_CON_TURNOS"}, "problema")],
            "contrastes": [
                ("Grafo / estado / memoria estructurada", {"PI2"}, r"grafo|graph|estado|state|memoria|memory|sst|tsp|csp|trayector"),
                ("SQL previo / edición / ventana (alternativa)", {"PI2"}, r"prev|previo|edici|edit|ventana|window|historial")]},
    "OE3": {"nombre": "Enrutamiento relacional simbólico (grafo de claves foráneas, árbol de Steiner / caminos mínimos)",
            "indicadores": [
                ("Joins por algoritmo de caminos", "pi3_inferencia_joins", {"ALGORITMICA_CAMINOS"}, "propuesta"),
                ("Joins por grafo de FK / restricciones", "pi3_inferencia_joins", {"GRAFO_FK_RESTRICCIONES"}, "propuesta"),
                ("Vinculación por grafo de esquema", "pi3_tecnica_linking", {"GRAFO_ESQUEMA"}, "contexto"),
                ("Joins implícitos en el modelo", "pi3_inferencia_joins", {"IMPLICITA_MODELO"}, "alternativa"),
                ("Errores de join reportados", "errores_join_reportados", {"SI"}, "problema")],
            "contrastes": [
                ("Joins / FK / caminos", {"PI3"}, r"join|\bfk\b|clave|camino|path|steiner"),
                ("Grafo de esquema (codificación)", {"PI3"}, r"grafo|graph"),
                ("Vinculación de esquemas (otras técnicas)", {"PI3"}, r"schema|esquema|linking|vincul|column|tabla|table")]},
    "OE4": {"nombre": "Verificación por ejecución y autocorrección en bucle cerrado",
            "indicadores": [
                ("Retroalimentación de errores de ejecución", "pi4_mecanismo", {"EJECUCION_FEEDBACK_ERRORES"}, "propuesta"),
                ("Reparación simbólica", "pi4_mecanismo", {"REPARACION_SIMBOLICA"}, "propuesta"),
                ("Autodepuración por LLM", "pi4_mecanismo", {"AUTODEPURACION_LLM"}, "propuesta"),
                ("Corrección aplicada en multiturno", "pi4_aplicado_multiturno", {"SI"}, "propuesta"),
                ("Aclaración con el usuario", "pi4_mecanismo", {"ACLARACION_USUARIO"}, "alternativa"),
                ("Abstención", "pi4_mecanismo", {"ABSTENCION"}, "alternativa"),
                ("Autoconsistencia / votación", "pi4_mecanismo", {"AUTOCONSISTENCIA_VOTACION"}, "alternativa"),
                ("Verificador / crítico", "pi4_mecanismo", {"VERIFICADOR_CRITICO"}, "alternativa")],
            "contrastes": [  # first match wins: clarification before correction, as in pi15_sintesis.CLASES
                ("Aclaración / interacción con el usuario (alternativa)", {"PI4"}, r"aclar|clarif|usuario|user|interact|intention|intenci"),
                ("Autoconsistencia / reranking (alternativa)", {"PI4"}, r"consisten|vot|candidat|rerank|re-rank"),
                ("Autocorrección / ejecución / verificación", {"PI4"}, r"autocorr|correc|refine|feedback|ejecuci|execut|depura|debug|repair|repar|verif|critic")]},
    "OE5": {"nombre": "Evaluación multiturno (SParC/CoSQL/empresarial; EX/EM por turno y curvas de degradación)",
            "indicadores": [
                ("Evaluación con historial predicho", "historial_eval", {"PREDICHO"}, "propuesta"),
                ("Evaluación solo con preguntas previas", "historial_eval", {"SOLO_PREGUNTAS"}, "propuesta"),
                ("Evaluación con historial gold", "historial_eval", {"GOLD"}, "problema"),
                ("Degradación por turno reportada", "degradacion_reportada", {"SI"}, "problema"),
                ("Contaminación de benchmarks discutida", "contaminacion_discutida", {"SI"}, "contexto"),
                ("Coste reportado (latencia/tokens/monetario)", "coste_reportado", {"LATENCIA", "TOKENS", "MONETARIO"}, "contexto"),
                ("Datos en español", "idioma_dataset", {"ES"}, "contexto")],
            "contrastes": []},
    "TRANSVERSAL": {"nombre": "Premisas transversales (sin entrenamiento, multiagente)",
                    "indicadores": [
                        ("Sin entrenamiento", "requiere_entrenamiento", {"NO"}, "propuesta"),
                        ("Paradigma principal: agentes", "paradigma_principal", {"AGENTES"}, "propuesta"),
                        ("Paradigma principal: híbrido neurosimbólico", "paradigma_principal", {"HIBRIDO_NEUROSIMBOLICO"}, "propuesta"),
                        ("Paradigma principal: prompting de LLM", "paradigma_principal", {"LLM_PROMPTING"}, "alternativa"),
                        ("Paradigma principal: ajuste fino de LLM", "paradigma_principal", {"LLM_FINETUNING"}, "alternativa")],
                    "contrastes": []},
}
BENCH_OE5 = ("SPARC", "COSQL")


CLASES_CSV = SALIDA / "clases_componentes.csv"  # (oe, pilar, componente) -> clase_final; overrides the regex when filled
OVR = {}


def clase(reglas, pilares, comp, oe=None, pilar=""):
    k = (oe, pilar, comp)
    if k in OVR:
        return OVR[k] or None
    for nombre, pils, rx in reglas:
        if pils & pilares and re.search(rx, comp, re.I):
            return nombre
    return None


def contrastes_oe(C, reglas, ids, cal, oe=None):
    porest = collections.defaultdict(lambda: collections.defaultdict(list))
    benchfam = collections.defaultdict(list)
    for r in C:
        if r["id_estudio"] not in ids or r["metrica_familia"] not in ACC:
            continue
        a, b = num(r["valor_con"]), num(r["valor_sin"])
        if a is None or b is None:
            continue
        c = clase(reglas, set(lista(r["pilar"])), r["componente"], oe, r["pilar"])
        if c:
            porest[c][r["id_estudio"]].append(a - b)
            benchfam[c].append(r["benchmark_familia"])
    out = []
    for nombre, _, _ in reglas:
        d = porest.get(nombre)
        if not d:
            out.append({"clase": nombre, "n_estudios": 0})
            continue
        meds = {s: round(st.median(v), 2) for s, v in d.items()}
        vals = list(meds.values())
        n_con = sum(len(v) for v in d.values())
        pct = round(100 * sum(1 for v in d.values() for x in v if x > 0) / n_con, 1)
        # confidence: same registered rules as pi15_sintesis.py step 6
        vs = [float(cal[s]["validez_pct"]) for s in meds if cal.get(s, {}).get("validez_pct")]
        mv = st.mean(vs) if vs else 0
        lim = "sin" if mv >= 75 else ("leves" if mv >= 50 else "importantes")
        coh = "sin" if pct >= 80 else ("leves" if pct >= 60 else "importantes")
        if n_con < 3 and coh == "sin":
            coh = "leves"
        suf = "sin" if len(vals) >= 5 else ("leves" if len(vals) >= 3 else "importantes")
        share = sum(1 for f in benchfam[nombre] if f in ("Multiturno conversacional", "Un turno estándar")) / len(benchfam[nombre])
        per = "sin" if share == 1 else ("leves" if share >= 0.5 else "importantes")
        comps = [lim, coh, suf, per]
        conf = "alta" if comps.count("importantes") == 0 and comps.count("leves") <= 1 else ("moderada" if comps.count("importantes") <= 1 else "baja")
        out.append({"clase": nombre, "n_estudios": len(vals), "n_contrastes": n_con, "mediana_pp": round(st.median(vals), 2),
                    "min_pp": min(vals), "max_pp": max(vals), "estudios_positivos": sum(x > 0 for x in vals),
                    "estudios_negativos": sum(x < 0 for x in vals), "estudios_nulos": sum(x == 0 for x in vals),
                    "pct_contrastes_positivos": pct, "validez_media": round(mv, 1), "limitaciones": lim, "coherencia": coh,
                    "suficiencia": suf, "pertinencia": per, "confianza": conf, "deltas_por_estudio": meds})
    return out


def main():
    E = {r["id_estudio"]: r for r in estudios()}
    cal = {r["id_estudio"]: r for r in leer_csv(SLR / "calidad" / "calidad.csv")}
    L2 = {s for s, r in E.items() if str(r["nivel"]) == "2"}
    ok = {s for s in L2 if cal.get(s, {}).get("supera_umbral") == "SI"}
    pobl = {"todos": set(E), "nivel2": L2, "nivel2_umbral": ok}
    C = leer_csv(EXT / "contrastes_taxonomia.csv")
    R = leer_csv(EXT / "resultados_taxonomia.csv")
    if CLASES_CSV.exists():
        for f in leer_csv(CLASES_CSV):
            if f["clase_final"].strip():
                OVR[(f["oe"], f["pilar"], f["componente"])] = "" if f["clase_final"].strip() == "NINGUNA" else f["clase_final"].strip()
    else:  # first run: write the regex assignment of every Level 2 contrast component for review
        filas = []
        for oe, m in MAPEO.items():
            pils = set().union(*[p for _, p, _ in m["contrastes"]]) if m["contrastes"] else set()
            for pil, comp in sorted({(r["pilar"], r["componente"]) for r in C if r["id_estudio"] in L2}):
                if pils & set(lista(pil)):
                    filas.append({"oe": oe, "pilar": pil, "componente": comp,
                                  "clase_regex": clase(m["contrastes"], set(lista(pil)), comp) or "NINGUNA", "clase_final": "", "motivo": ""})
        with open(CLASES_CSV, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(filas[0]))
            w.writeheader()
            w.writerows(filas)
    res = {"poblaciones": {k: len(v) for k, v in pobl.items()}, "oe": {}}
    filas_i, filas_c = [], []
    for oe, m in MAPEO.items():
        ind = []
        for etiqueta, campo, codigos, rol in m["indicadores"]:
            sel = {s for s in E if set(lista(E[s][campo])) & codigos}
            # Level 1 studies have no PI1/PI2/PI5 fields: their denominator is Level 2 only
            solo_l2 = all(not E[s][campo].strip() for s in set(E) - L2)
            fila = {"oe": oe, "indicador": etiqueta, "campo": campo, "codigos": ";".join(sorted(codigos)), "rol": rol,
                    "solo_nivel2": solo_l2}
            for p, ids in pobl.items():
                if p == "todos" and solo_l2:
                    fila[f"n_{p}"], fila[f"pct_{p}"] = "", ""
                    continue
                k = len(sel & ids)
                fila[f"n_{p}"], fila[f"pct_{p}"] = k, round(100 * k / len(ids), 1)
            fila["sin_entrenamiento_nivel2"] = sum(1 for s in sel & L2 if E[s]["requiere_entrenamiento"].upper() == "NO")
            fila["estudios_nivel2"] = ";".join(sorted(sel & L2))
            ind.append(fila)
        filas_i += ind
        con = {"principal_nivel2_umbral": contrastes_oe(C, m["contrastes"], ok, cal, oe),
               "sensibilidad_nivel2": contrastes_oe(C, m["contrastes"], L2, cal, oe)} if m["contrastes"] else {}
        for pob, lst in con.items():
            for c in lst:
                filas_c.append({"oe": oe, "poblacion": pob, **{k: v for k, v in c.items() if k != "deltas_por_estudio"},
                                "estudios": ";".join(f"{s}:{d:+g}" for s, d in sorted(c.get("deltas_por_estudio", {}).items()))})
        res["oe"][oe] = {"nombre": m["nombre"], "indicadores": ind, "contrastes": con}
    # OE5 extra: share of Level 2 studies reporting SParC/CoSQL results, and the M8 conjunction from the synthesis
    usa = {r["id_estudio"] for r in R if r["benchmark_canonico"] in BENCH_OE5}
    res["oe"]["OE5"]["benchmarks_sparc_cosql"] = {"nivel2": len(usa & L2), "nivel2_umbral": len(usa & ok)}
    p15 = json.load(open(SLR / "sintesis" / "pi15_resultados.json", encoding="utf-8"))
    res["brecha_M8_sintesis"] = {k: p15["brecha_M8"][k] for k in ("n", "componentes", "sensibilidad_grafos_neuronales")}
    json.dump(res, open(SALIDA / "mapa_oe.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    for nombre, filas in (("mapa_oe_indicadores", filas_i), ("mapa_oe_contrastes", filas_c)):
        cols = list(dict.fromkeys(k for f in filas for k in f))
        with open(SALIDA / f"{nombre}.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            w.writerows(filas)
    print(json.dumps(res["poblaciones"]))
    for f in filas_i:
        print(f"{f['oe']:<11} {f['rol']:<11} {f['indicador'][:48]:<48} todos={f['n_todos']!s:>4} L2={f['n_nivel2']:>3} L2u={f['n_nivel2_umbral']:>3} sinEnt={f['sin_entrenamiento_nivel2']}")
    for f in filas_c:
        if f["poblacion"].startswith("principal"):
            print(f"{f['oe']} {f['clase'][:45]:<45} est={f['n_estudios']} " + (f"med={f['mediana_pp']:+} [{f['min_pp']},{f['max_pp']}] +{f['estudios_positivos']}/-{f['estudios_negativos']} conf={f['confianza']}" if f["n_estudios"] else ""))
    print("OE5 SParC/CoSQL", res["oe"]["OE5"]["benchmarks_sparc_cosql"], "M8", res["brecha_M8_sintesis"]["n"], res["brecha_M8_sintesis"]["componentes"])


if __name__ == "__main__":
    main()
