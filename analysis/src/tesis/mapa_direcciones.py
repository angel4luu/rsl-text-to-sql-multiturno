"""Phase 14, step 2 — indicators for alternative thesis directions not derived from the proposal.

Candidates come from the article's coverage gaps (05-discusion.tex, «Criterio de reformulación y brechas de
cobertura»), the PI1-PI5 «Para la discusión» notes and the step-1 map (mapa_oe.json). For each direction: counts over
all studies / Level 2 / Level 2 above the quality threshold, plus the within-study contrasts already computed in step 1
when a direction coincides with one of its classes. Same populations and rules as mapa_oe.py.
Output: tesis/00-justificacion/datos/mapa_direcciones.json, mapa_direcciones_indicadores.csv.
"""
import csv
import json

from mapa_oe import SALIDA, SLR, EXT, estudios, leer_csv, lista

# indicator kinds: ("campo", field, codes) | ("familia", benchmark family) | ("por_turno",) | ("cq", item, value)
# | ("reportado", field) = field filled with something other than NR/NA
DIRECCIONES = {
    "DA": {"nombre": "Aclaración con el usuario e interacción (incl. abstención)",
           "indicadores": [("Mecanismo: aclaración con el usuario", ("campo", "pi4_mecanismo", {"ACLARACION_USUARIO"})),
                           ("Mecanismo: abstención", ("campo", "pi4_mecanismo", {"ABSTENCION"})),
                           ("Señal de corrección: usuario", ("campo", "pi4_senal", {"USUARIO"})),
                           ("Etiqueta: interactivo", ("campo", "etiquetas", {"INTERACTIVO"})),
                           ("Resultados en benchmarks interactivos / de aclaración", ("familia", "Interactivo / aclaración"))],
           "contrastes_paso1": [("OE4", "Aclaración / interacción con el usuario (alternativa)")]},
    "DB": {"nombre": "Datos en español y multilingües",
           "indicadores": [("Datos en español", ("campo", "idioma_dataset", {"ES"})),
                           ("Datos en chino", ("campo", "idioma_dataset", {"ZH"})),
                           ("Datos en otros idiomas", ("campo", "idioma_dataset", {"OTRO"})),
                           ("Datos en inglés", ("campo", "idioma_dataset", {"EN"})),
                           ("Resultados en variantes de un turno (robustez, dominio, idioma)", ("familia", "Variantes de un turno (robustez, dominio, idioma)"))],
           "contrastes_paso1": []},
    "DC": {"nombre": "Metodología de evaluación multiturno (historial predicho, reporte por turno, reproducibilidad)",
           "indicadores": [("Historial de evaluación: predicho", ("campo", "historial_eval", {"PREDICHO"})),
                           ("Historial de evaluación: solo preguntas", ("campo", "historial_eval", {"SOLO_PREGUNTAS"})),
                           ("Historial de evaluación: gold", ("campo", "historial_eval", {"GOLD"})),
                           ("Historial de evaluación: no reportado", ("campo_nr", "historial_eval")),
                           ("Resultados desagregados por turno", ("por_turno",)),
                           ("Degradación por turno reportada", ("campo", "degradacion_reportada", {"SI"})),
                           ("Técnica reproducible (CQ2 = sí)", ("cq", "CQ2", "1.0")),
                           ("Código disponible", ("campo", "codigo_disponible", {"SI"}))],
           "contrastes_paso1": []},
    "DD": {"nombre": "Contaminación de benchmarks y fecha de los modelos",
           "indicadores": [("Contaminación discutida", ("campo", "contaminacion_discutida", {"SI"})),
                           ("Fecha / versión del modelo reportada", ("reportado", "fecha_modelo"))],
           "contrastes_paso1": []},
    "DE": {"nombre": "Líneas base simples fuertes (historial plano, concatenación, edición del SQL previo)",
           "indicadores": [("Representación: historial plano", ("campo", "pi2_representacion", {"HISTORIAL_PLANO"})),
                           ("Representación: edición del SQL previo", ("campo", "pi2_representacion", {"SQL_PREVIO_EDICION"})),
                           ("Técnica: concatenación", ("campo", "pi1_tecnica", {"CONCATENACION"}))],
           "contrastes_paso1": [("OE2", "SQL previo / edición / ventana (alternativa)"), ("OE1", "Concatenación / historial (alternativa)")]},
    "DF": {"nombre": "Coste y eficiencia (latencia, tokens, coste monetario, crecimiento del contexto)",
           "indicadores": [("Coste reportado: latencia", ("campo", "coste_reportado", {"LATENCIA"})),
                           ("Coste reportado: tokens", ("campo", "coste_reportado", {"TOKENS"})),
                           ("Coste reportado: monetario", ("campo", "coste_reportado", {"MONETARIO"})),
                           ("Coste reportado: ninguno", ("campo", "coste_reportado", {"NINGUNO"})),
                           ("Coste de contexto que crece con los turnos", ("campo", "pi2_coste_contexto", {"CRECE_CON_TURNOS"}))],
           "contrastes_paso1": []},
    "DG": {"nombre": "Esquemas grandes / empresariales",
           "indicadores": [("Resultados en datos propios / industriales", ("familia", "Datos propios / industriales")),
                           ("Escala del esquema reportada", ("reportado", "pi3_escala_esquema")),
                           ("Errores de join reportados", ("campo", "errores_join_reportados", {"SI"}))],
           "contrastes_paso1": []},
}


def main():
    E = {r["id_estudio"]: r for r in estudios()}
    cal = {r["id_estudio"]: r for r in leer_csv(SLR / "calidad" / "calidad.csv")}
    L2 = {s for s, r in E.items() if str(r["nivel"]) == "2"}
    ok = {s for s in L2 if cal.get(s, {}).get("supera_umbral") == "SI"}
    pobl = {"todos": set(E), "nivel2": L2, "nivel2_umbral": ok}
    R = leer_csv(EXT / "resultados_taxonomia.csv")
    paso1 = json.load(open(SALIDA / "mapa_oe.json", encoding="utf-8"))
    fam = {}
    for r in R:
        fam.setdefault(r["benchmark_familia"], set()).add(r["id_estudio"])
    por_turno = {r["id_estudio"] for r in R if r["turno"].upper() not in ("TODOS", "NA", "")}
    res, filas = {"poblaciones": {k: len(v) for k, v in pobl.items()}, "direcciones": {}}, []
    for d, m in DIRECCIONES.items():
        ind = []
        for etiqueta, spec in m["indicadores"]:
            tipo, solo_l2 = spec[0], False
            if tipo == "campo":
                sel = {s for s in E if set(lista(E[s][spec[1]])) & spec[2]}
            elif tipo == "campo_nr":
                sel = {s for s in L2 if E[s][spec[1]].strip().upper() in ("NR", "")}
            elif tipo == "reportado":
                sel = {s for s in E if E[s][spec[1]].strip() and E[s][spec[1]].strip().upper() not in ("NR", "NA")
                       and not E[s][spec[1]].strip().upper().startswith(("OTROS: NR", "COLUMNAS NR", "MÁXIMO DE COLUMNAS NR"))}
            elif tipo == "familia":
                sel = fam.get(spec[1], set())
            elif tipo == "por_turno":
                sel = por_turno
            else:  # cq
                sel = {s for s in L2 if cal.get(s, {}).get(spec[1]) == spec[2]}
            if tipo in ("campo", "campo_nr", "reportado"):
                solo_l2 = all(not E[s][spec[1]].strip() for s in set(E) - L2)
            solo_l2 = solo_l2 or tipo in ("cq", "campo_nr", "familia", "por_turno")  # results were extracted for Level 2 only
            fila = {"direccion": d, "indicador": etiqueta, "definicion": ":".join(str(sorted(x)) if isinstance(x, set) else x for x in spec),
                    "solo_nivel2": solo_l2}
            for p, ids in pobl.items():
                if p == "todos" and solo_l2:
                    fila[f"n_{p}"], fila[f"pct_{p}"] = "", ""
                    continue
                k = len(sel & ids)
                fila[f"n_{p}"], fila[f"pct_{p}"] = k, round(100 * k / len(ids), 1)
            fila["estudios_nivel2"] = ";".join(sorted(sel & L2))
            ind.append(fila)
        filas += ind
        con = []
        for oe, clase in m["contrastes_paso1"]:
            c = next(x for x in paso1["oe"][oe]["contrastes"]["principal_nivel2_umbral"] if x["clase"] == clase)
            con.append({"origen": f"mapa_oe.json: {oe}/principal_nivel2_umbral/{clase}", **{k: v for k, v in c.items() if k != "deltas_por_estudio"}})
        res["direcciones"][d] = {"nombre": m["nombre"], "indicadores": ind, "contrastes_paso1": con}
    json.dump(res, open(SALIDA / "mapa_direcciones.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    cols = list(dict.fromkeys(k for f in filas for k in f))
    with open(SALIDA / "mapa_direcciones_indicadores.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(filas)
    print(json.dumps(res["poblaciones"]))
    for f in filas:
        print(f"{f['direccion']} {f['indicador'][:55]:<55} todos={f['n_todos']!s:>4} L2={f['n_nivel2']:>3} L2u={f['n_nivel2_umbral']:>3}")
    for d, v in res["direcciones"].items():
        for c in v["contrastes_paso1"]:
            print(d, c["clase"][:45], c["n_estudios"], c.get("mediana_pp"), c.get("confianza"))


if __name__ == "__main__":
    main()
