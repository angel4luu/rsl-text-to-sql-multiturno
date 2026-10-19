"""Phase 11, step 3: LaTeX tables of the SLR article (main text, decision D1 a).

Every number is read from the synthesis outputs (CSV/JSON); percentages are recomputed from counts and bases
and checked against the CSVs (assert), rounding is half-up from the raw values (outline alert 7), and each
caption states the base of its percentages (alert 4). Also writes the quality aggregation (alert 6):
slr/calidad/calidad_resultados.json and slr/sintesis/CALIDAD.md (findings for the author's approval).

Outputs: latex/slr/tablas/<label>.tex and latex/slr/tablas/leyendas.json (captions, generated, never typed).
Usage (from repo root): uv run --project analysis python analysis/src/tablas/tablas.py   (or: make tablas)
"""
import csv
import json
import re
import statistics
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SLR = RAIZ / "slr"
SIN = SLR / "sintesis"
TAB = SIN / "tablas"
OUT = RAIZ / "latex" / "slr" / "tablas"

# Code labels (vocabulary of slr/extraccion/formulario_extraccion.md)
ETIQUETA = {
    "NR": "No reportado",
    "CONCATENACION": "Concatenación del historial", "REESCRITURA": "Reescritura de la pregunta",
    "CLASIFICACION_DISCURSO": "Clasificación del discurso", "RESOLUCION_EXPLICITA": "Resolución explícita de referencias",
    "HISTORIAL_PLANO": "Historial plano", "SQL_PREVIO_EDICION": "SQL previo (edición)",
    "ESTRUCTURA_EXPLICITA": "Estructura explícita", "GRAFO": "Grafo", "MEMORIA_EXTERNA": "Memoria externa",
    "VENTANA_DESLIZANTE": "Ventana deslizante", "RESUMEN": "Resumen",
    "IMPLICITA_NEURONAL": "Implícita (neuronal)", "REGLAS_DETERMINISTAS": "Reglas deterministas",
    "LLM_GENERATIVA": "Generativa (LLM)", "CRECE_CON_TURNOS": "Crece con los turnos", "ACOTADO": "Acotado",
    "LLM_PROMPTING": r"LLM con \en{prompting}", "PODA_ESQUEMA": "Poda del esquema",
    "CLASIFICADOR_ENTRENADO": "Clasificador entrenado", "EMBEDDINGS_RECUPERACION": r"Recuperación por \en{embeddings}",
    "NINGUNA_EXPLICITA": "Ninguna explícita", "GRAFO_ESQUEMA": "Grafo del esquema",
    "COINCIDENCIA_CADENAS": "Coincidencia de cadenas", "IMPLICITA_MODELO": "Implícita en el modelo",
    "GRAFO_FK_RESTRICCIONES": "Grafo de claves foráneas", "ALGORITMICA_CAMINOS": "Algorítmica (caminos)",
    "EJECUCION_FEEDBACK_ERRORES": "Retroalimentación de ejecución", "VERIFICADOR_CRITICO": "Verificador o crítico",
    "AUTODEPURACION_LLM": "Autodepuración con LLM", "AUTOCONSISTENCIA_VOTACION": "Autoconsistencia (votación)",
    "ACLARACION_USUARIO": "Aclaración con el usuario", "ABSTENCION": "Abstención",
    "REPARACION_SIMBOLICA": "Reparación simbólica", "RESULTADO_EJECUCION": "Resultado de la ejecución",
    "ERROR_DBMS": "Error del SGBD", "JUICIO_LLM": "Juicio de un LLM", "USUARIO": "Usuario",
    "RESULTADO_VACIO": "Resultado vacío", "PREDICHO": "Predicho", "SOLO_PREGUNTAS": "Solo preguntas",
    "GOLD": r"De referencia (\en{gold})",
}
CAMPO = {
    "pi1_tecnica": "PI1 · Técnica de restauración del contexto", "pi2_representacion": "PI2 · Representación del estado",
    "pi2_actualizacion": "PI2 · Actualización del estado", "pi2_coste_contexto": "PI2 · Coste del contexto",
    "pi3_tecnica_linking": "PI3 · Vinculación de esquemas", "pi3_inferencia_joins": r"PI3 · Inferencia de \en{joins}",
    "pi4_mecanismo": "PI4 · Mecanismo", "pi4_senal": "PI4 · Señal",
}
# Reviewer models per phase: screening from Screening_*/*_methods_selection.md (sr-screener), extraction and
# quality from slr/extraccion/informe_acuerdo_extraccion.md (resolution rules) and enmiendas.md A5.
MODELOS = {
    "TA": ("Sonnet / Sonnet", "Opus"), "FT": ("Sonnet / Sonnet\\textsuperscript{a}", "Opus"),
    "TA_bola": ("Sonnet / Sonnet", "Opus"), "FT_bola": ("Sonnet / Sonnet", "Opus"),
    "N1": ("Sonnet / Sonnet", "Codex"), "N2": ("Sonnet / Codex", "Sonnet"), "CAL": ("Sonnet / Codex", "Sonnet"),
}

leyendas = {}


def leer(p):
    return list(csv.DictReader(open(p, encoding="utf-8")))


def jl(p):
    return json.load(open(p, encoding="utf-8"))


def red(x, d=1):
    return Decimal(str(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)


def num(x, d=1):
    return r"\num{%s}" % red(x, d)


def pct(k, n, d=1):
    return num(100 * k / n, d)


def kn(k, n):
    """'k (p %)' with p recomputed."""
    return f"{k} ({pct(k, n)})"


def chk(k, n, p_csv):
    assert red(100 * int(k) / n) == red(float(p_csv)), (k, n, p_csv)


def esc(s):
    return re.sub(r"([&%#_$])", r"\\\1", s)


def tabla(nombre, leyenda, cuerpo, ancho=False, pos="!tbp"):
    env = "table*" if ancho else "table"
    leyendas[nombre] = leyenda
    tex = (f"% Generado por analysis/src/tablas/tablas.py — no editar a mano.\n\\begin{{{env}}}[{pos}]\n\\centering\n"
           f"\\caption{{{leyenda}}}\n\\label{{tab:{nombre}}}\n\\footnotesize\n{cuerpo}\n\\end{{{env}}}\n")
    (OUT / f"{nombre}.tex").write_text(tex, encoding="utf-8")


def anio_bib(clave):
    for f in ("referencias.bib", "referencias_metodo.bib"):
        t = (RAIZ / "bib" / f).read_text(encoding="utf-8")
        i = t.find("{" + clave + ",")
        if i >= 0:
            return re.search(r"year\s*=\s*\{?(\d{4})", t[i:]).group(1)
    raise KeyError(clave)


# ----------------------------------------------------------------------------------------------------------
def t_relacionados():
    filas = [rf"\cite{{{r['clave_bib']}}} ({anio_bib(r['clave_bib'])}) & {esc(r['tipo'])} & {esc(r['alcance'])} & "
             f"{esc(r['multiturno']).replace('datasets', chr(92) + 'en{datasets}')} & {esc(r['protocolo'])} & {esc(r['fuente_leida'])} \\\\"
             for r in leer(TAB / "revisiones_previas.csv")]
    cuerpo = ("\\begin{tabularx}{\\textwidth}{@{}l l X l l l@{}}\n\\toprule\n"
              "Revisión & Tipo & Alcance & Multiturno & Protocolo & Fuente leída \\\\\n\\midrule\n"
              + "\n".join(filas) + "\n\\bottomrule\n\\end{tabularx}")
    tabla("relacionados", "Revisiones previas sobre Text-to-SQL y NLIDB frente al alcance de esta revisión. "
          "«Fuente leída» indica sobre qué texto se verificó cada descriptor.", cuerpo, ancho=True)


def t_criterios():
    """Eligibility criteria exactly as registered (03_criterios_elegibilidad.md); only markup is converted and the
    internal Mendeley-folder note is dropped."""
    def tex(c):
        c = re.sub(r"\s*\(→ carpeta[^)]*\)", "", c)
        c = esc(c.replace("**", ""))
        c = re.sub(r"\*([^*]+)\*", r"\\textit{\1}", c)
        return c.replace("≥", r"$\geq$").replace("<", r"$<$").replace("–", "--")
    # Phase in which each criterion was actually applied (post-close-out revision 2026-10-19). Source: exclusion
    # counts per stage in the PRISMA flow (prisma_flujo.py): T/R E1–E6; texto completo E1–E3, E5–E9; dedup EX9.
    # Each IC is checked through its matching EX code(s).
    tr, tc = "Título-resumen", "texto completo"
    fases = {
        "IC1": f"{tr} y {tc} (EX4, EX5)", "IC2": f"{tr} y {tc} (EX6)", "IC3": "Texto completo (EX7)",
        "IC4": "Texto completo (EX8)", "IC5": f"{tr} y {tc} (EX1)", "IC6": f"{tr} y {tc} (EX2)",
        "IC7": f"{tr} y {tc} (EX3, EX9)",
        "EX1": f"{tr} y {tc}", "EX2": f"{tr} y {tc}", "EX3": f"{tr} y {tc}", "EX4": tr,
        "EX5": f"{tr} y {tc}", "EX6": f"{tr} (regla de incertidumbre) y {tc}", "EX7": "Texto completo",
        "EX8": "Texto completo", "EX9": f"Deduplicación y {tc}",
    }
    filas = {"IC": [], "EX": []}
    for l in open(SLR / "protocolo" / "03_criterios_elegibilidad.md", encoding="utf-8"):
        m = re.match(r"\|\s*((IC|EX)\d+)\s*\|(.*)\|\s*$", l.strip())
        if m:
            celdas = [x.strip() for x in m.group(3).split("|")]
            filas[m.group(2)].append(f"{m.group(1)} & {tex(celdas[0])} & {fases[m.group(1)]} \\\\")
    cuerpo = ("\\begin{tabularx}{\\textwidth}{@{}l X >{\\raggedright\\arraybackslash}p{3.4cm}@{}}\n\\toprule\n"
              "Código & Criterio & Fase en que se aplica \\\\\n\\midrule\n"
              "\\multicolumn{3}{@{}l}{\\textit{Inclusión (se deben cumplir todos)}} \\\\\n" + "\n".join(filas["IC"])
              + "\n\\addlinespace\n\\multicolumn{3}{@{}l}{\\textit{Exclusión (basta uno)}} \\\\\n" + "\n".join(filas["EX"])
              + "\n\\bottomrule\n\\end{tabularx}")
    tabla("criterios", f"Criterios de elegibilidad ({len(filas['IC'])} de inclusión y "
          f"{len(filas['EX'])} de exclusión) y fase en que se aplicó cada uno. Cada código EX$n$ corresponde al motivo de exclusión E$n$ del diagrama "
          "PRISMA.", cuerpo, ancho=True)




def t_d4():
    p0, s = jl(SIN / "pi0_resultados.json"), jl(SIN / "sensibilidad.json")
    filas_def = [("Principal (estricto)", p0["D4"]["estricto"]), ("Laxo", p0["D4"]["laxo"]),
                 ("Sin \\en{preprints}", s["2_sin_preprints_D4"]), ("Solo búsqueda en bases", s["4_D4_solo_busqueda_en_bases"]),
                 ("Foros de primer nivel", s["A5_D4_foros_de_primer_nivel"]),
                 ("Con no recuperados, cota", s["A4_D4_con_no_recuperados_segun_senal"])]
    filas = []
    for nombre, d in filas_def:
        assert red(d["k"] / d["n"], 4) == red(d["p"], 4), nombre
        filas.append(f"{nombre} & {d['k']} & {d['n']} & {pct(d['k'], d['n'])} & "
                     f"{num(100 * d['ic95'][0])}--{num(100 * d['ic95'][1])} \\\\")
    assert all(d["ic95"][1] < 0.5 for _, d in filas_def)  # caption claim: minority in every variant
    t = p0["D4"]["tendencia_2019_2025"]
    a26 = p0["D4"]["anio_2026_parcial"]
    cuerpo = ("\\begin{tabular}{@{}l r r r c@{}}\n\\toprule\n"
              "Análisis & $k$ & $n$ & D4 (\\%) & IC 95 \\% \\\\\n\\midrule\n" + "\n".join(filas)
              + "\n\\bottomrule\n\\end{tabular}")
    tabla("d4", "Indicador D4 (proporción multiturno) y análisis de sensibilidad, con IC de Wilson al 95 \\%. "
          "La proporción multiturno es minoritaria (límite superior del IC $<$ 50 \\%) en todas las variantes. Tendencia 2019--2025 "
          f"(Cochran--Armitage, {num(t['replicas'], 0)} réplicas): $p$ = {num(t['p_exacta_bilateral'], 2)}; "
          f"{a26['anio']} (año parcial) se informa aparte: {a26['k']}/{a26['n']}.", cuerpo)


def calidad():
    filas = leer(SLR / "calidad" / "calidad.csv")
    n = len(filas)
    validez, reporte = ["CQ2", "CQ4", "CQ5", "CQ6", "CQ7"], ["CQ1", "CQ3", "CQ8", "CQ9", "CQ10"]
    por_item = {}
    for q in validez + reporte:
        vals = [r[q] for r in filas]
        por_item[q] = {"tipo": "validez" if q in validez else "reporte", "1": vals.count("1.0"),
                       "0.5": vals.count("0.5"), "0": vals.count("0.0"), "sin_dato": sum(v == "" for v in vals)}
        assert sum(v for k, v in por_item[q].items() if k != "tipo") == n, q
    v = [float(r["validez_pct"]) for r in filas]
    q1, med, q3 = statistics.quantiles(v, n=4, method="inclusive")
    res = {"n": n, "por_item": por_item, "validez_mediana": med, "validez_q1": q1, "validez_q3": q3,
           "validez_min": min(v), "validez_max": max(v), "supera_umbral": sum(r["supera_umbral"] == "SI" for r in filas),
           "bajo_umbral": [r["id_estudio"] for r in filas if r["supera_umbral"] != "SI"]}
    assert res["supera_umbral"] == jl(SIN / "pi15_resultados.json")["nivel2_umbral"]
    json.dump(res, open(SLR / "calidad" / "calidad_resultados.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return res


def t_calidad(res):
    n = res["n"]
    nombres = {"CQ1": "Objetivo y escenario definidos", "CQ2": "Reproducibilidad de la técnica",
               "CQ3": "Benchmarks públicos", "CQ4": "Líneas base competitivas", "CQ5": "Métricas e historial reportados",
               "CQ6": "Ablación o análisis de errores", "CQ7": "Robustez", "CQ8": "Código o datos disponibles",
               "CQ9": "Limitaciones discutidas", "CQ10": "Foro revisado por pares"}
    filas = []
    for tipo, titulo in (("validez", "Validez (umbral)"), ("reporte", "Reporte y apertura")):
        filas.append(f"\\multicolumn{{5}}{{@{{}}l}}{{\\textit{{{titulo}}}}} \\\\")
        for q, d in res["por_item"].items():
            if d["tipo"] == tipo:
                filas.append(f"{q} & {nombres[q].replace('Benchmarks', chr(92) + 'en{Benchmarks}')} & "
                             f"{kn(d['1'], n)} & {kn(d['0.5'], n)} & {kn(d['0'], n)} \\\\")
    cuerpo = ("\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}l l r r r@{}}\n\\toprule\n"
              "Ítem & Pregunta (resumida) & Sí & Parcial & No \\\\\n\\midrule\n" + "\n".join(filas)
              + "\n\\bottomrule\n\\end{tabular}")
    tabla("calidad", f"Perfil de calidad de los estudios del Nivel 2: estudios (y porcentaje sobre $n = {n}$) con "
          "puntuación 1 (sí), 0,5 (parcial) y 0 (no). "
          f"Puntuación de validez: mediana {num(res['validez_mediana'])} \\% (RIC {num(res['validez_q1'])}--"
          f"{num(res['validez_q3'])} \\%); {res['supera_umbral']} estudios alcanzan el umbral del 50 \\%.", cuerpo)


def t_efectos():
    conf = {r["hallazgo"].split(":")[0]: r for r in leer(TAB / "confianza_hallazgos.csv")}
    rv = jl(SIN / "revision_4f.json")  # step 4f, decision A4
    pen = rv["A4_confianza_penalizada"]
    nul = {f"{x['pilar']} · {x['clase']}": x["nulos_umbral"] for x in rv["A4_nulos"]["por_clase"]}
    filas, prev = [], None
    for r in leer(TAB / "pi_efectos_componentes.csv"):
        clave = f"{r['pilar']} · {r['clase']}"
        c = conf[clave]
        assert int(r["estudios_positivos"]) + int(r["estudios_negativos"]) + int(r["estudios_nulos"]) == int(r["n_estudios"])
        if prev and prev != r["pilar"]:
            filas.append("\\addlinespace")
        prev = r["pilar"]
        filas.append(f"{r['pilar']} & {esc(r['clase']).replace('Autoconsistencia', 'Auto\\-consistencia')} & {r['n_estudios']} & {r['n_contrastes']} & "
                     f"{num(float(r['mediana_pp']))} & {num(float(r['min_pp']))} a {num(float(r['max_pp']))} & "
                     f"{r['estudios_positivos']}/{r['estudios_negativos']}/{r['estudios_nulos']} & "
                     f"{num(float(r['pct_contrastes_positivos']))} & {nul[clave]} & {num(float(c['validez_media']))} & {c['confianza'].replace('no evaluada', '---')} & {pen[clave].replace('no evaluada', '---')} \\\\")
    base = jl(SIN / "pi15_resultados.json")["nivel2_umbral"]
    cuerpo = ("\\begin{tabularx}{\\textwidth}{@{}l >{\\raggedright\\arraybackslash}X r r r r c r r r l l@{}}\n\\toprule\n"
              "Pilar & Clase de componente & Est. & Contr. & Med. (pp) & Rango (pp) & Est. $+/-/0$ & "
              "Contr. $+$ (\\%) & Nulos\\textsuperscript{c} & Val. (\\%) & Conf. & Conf. pen.\\textsuperscript{d} \\\\\n\\midrule\n" + "\n".join(filas)
              + "\n\\bottomrule\n\\end{tabularx}")
    tabla("efectos", "Efecto de los componentes en contrastes dentro del estudio (diferencia en puntos porcentuales "
          f"frente a la variante sin el componente), estudios del Nivel 2 que alcanzan el umbral de validez ($n = {base}$). "
          "Est.: estudios; Contr.: contrastes; Med.: mediana; Val.: validez media de los estudios de la clase; "
          "\\textsuperscript{c}Estudios con $|\\Delta| < 0{,}5$~pp. \\textsuperscript{d}Confianza asignada rebajada un nivel por sesgo de notificación. Conf.: confianza inspirada en GRADE-CERQual; no se valora para «otros componentes», clase heterogénea (subclases en la \\cref{tab:otros})."
          , cuerpo, ancho=True)


def bloque(filas_csv, campos, base, chk_pct=True):
    out = []
    for campo in campos:
        rs = [r for r in filas_csv if r["campo"] == campo]
        out.append(f"\\multicolumn{{3}}{{@{{}}l}}{{\\textit{{{CAMPO[campo]}}}}} \\\\")
        for r in sorted(rs, key=lambda r: (r["codigo"] == "NR", -int(r["estudios"]))):
            if chk_pct:
                chk(r["estudios"], base, r["pct"])
            out.append(f"\\quad {ETIQUETA[r['codigo']]} & {r['estudios']} & {pct(int(r['estudios']), base)} \\\\")
    return out


def t_otros():
    """Sub-classes of «Otros componentes del pilar» (post-close-out revision 2026-10-19; author-accepted proposal in
    slr/sintesis/revision_otros.md). Same within-study effect rules as tab:efectos; exploratory."""
    filas, prev = [], None
    for r in leer(TAB / "pi_efectos_otros_subclases.csv"):
        if prev and prev != r["pilar"]:
            filas.append("\\addlinespace")
        prev = r["pilar"]
        filas.append(f"{r['pilar']} & {esc(r['clase'])} & {r['n_estudios']} & {r['n_contrastes']} & "
                     f"{num(float(r['mediana_pp']))} & {num(float(r['min_pp']))} a {num(float(r['max_pp']))} & "
                     f"{r['estudios_positivos']}/{r['estudios_negativos']}/{r['estudios_nulos']} \\\\")
    cuerpo = ("\\begin{tabularx}{\\linewidth}{@{}l X r r r r c@{}}\n\\toprule\n"
              "Pilar & Subclase & Est. & Contr. & Med. (pp) & Rango (pp) & Est. $+/-/0$ \\\\\n\\midrule\n"
              + "\n".join(filas) + "\n\\bottomrule\n\\end{tabularx}")
    tabla("otros", "Subclases de la clase «otros componentes del pilar» de la \\cref{tab:efectos}, con las mismas reglas "
          "(contrastes dentro del estudio, estudios del Nivel 2 que alcanzan el umbral de validez). Análisis exploratorio "
          "\\en{post hoc}, sin valoración de la confianza. Un estudio puede figurar en varias subclases.", cuerpo, pos="!htbp")


def t_taxo_pi12():
    base = jl(SIN / "pi15_resultados.json")["nivel2_umbral"]
    filas = (bloque(leer(TAB / "pi1_tecnicas.csv"), ["pi1_tecnica"], base)
             + bloque(leer(TAB / "pi2_representacion.csv"), ["pi2_representacion", "pi2_actualizacion", "pi2_coste_contexto"], base))
    cuerpo = ("\\begin{tabular}{@{}l r r@{}}\n\\toprule\nCódigo & Estudios & \\% \\\\\n\\midrule\n"
              + "\n".join(filas) + "\n\\bottomrule\n\\end{tabular}")
    tabla("taxo-pi12", f"Taxonomía de PI1 y PI2: estudios del Nivel 2 que alcanzan el umbral de validez ($n = {base}$). "
          "Un estudio puede tener varios códigos, por lo que los porcentajes de un campo pueden sumar más de 100.", cuerpo)


def t_contraste_pi34():
    """Decision A1 (step 4f): both arms restricted to studies with PI3/PI4 as central contribution (same entry rule),
    with «no reportado» rows; source revision_4f.py -> pi34_tecnicas_central.csv."""
    rv = jl(SIN / "revision_4f.json")["A1_contraste_central"]
    nm, nu = rv["n_multiturno"], rv["n_un_turno"]
    filas, prev = [], None
    for r in leer(TAB / "pi34_tecnicas_central.csv"):
        chk(r["multiturno"], nm, r["pct_multiturno"])
        chk(r["un_turno"], nu, r["pct_un_turno"])
        if r["campo"] != prev:
            filas.append(f"\\multicolumn{{3}}{{@{{}}l}}{{\\textit{{{CAMPO[r['campo']]}}}}} \\\\")
            prev = r["campo"]
        marca = "\\textsuperscript{b}" if r["no_trasladado"] == "SI" else ""
        filas.append(f"\\quad {ETIQUETA[r['codigo']]}{marca} & {kn(int(r['multiturno']), nm)} & {kn(int(r['un_turno']), nu)} \\\\")
    cuerpo = ("\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}l r r@{}}\n\\toprule\n"
              "Código & Multiturno & Un turno \\\\\n\\midrule\n" + "\n".join(filas)
              + "\n\\bottomrule\n\\end{tabular}")
    tabla("contraste-pi34", "Técnicas de PI3 y PI4 por escenario, con ambos brazos restringidos a los estudios cuya contribución "
          f"central es PI3 o PI4 (misma regla de entrada): multiturno ($n = {nm}$) y un turno ($n = {nu}$). Un estudio puede "
          "tener varios códigos. Los estudios de un turno se extrajeron de las páginas iniciales (Nivel 1), por lo que la fila "
          "«no reportado» no es comparable entre escenarios. \\textsuperscript{b}Técnica de un turno no trasladada al multiturno.", cuerpo)


def t_pi5():
    base = jl(SIN / "pi15_resultados.json")["nivel2_umbral"]
    deg = jl(SIN / "pi15_resultados.json")["degradacion"]
    rs = leer(TAB / "pi5_historial.csv")
    filas = ["\\multicolumn{5}{@{}l}{\\textit{Historial usado en la evaluación}} \\\\"]
    for r in sorted([r for r in rs if r["campo"] == "historial_eval"], key=lambda r: (r["codigo"] == "NR", -int(r["estudios"]))):
        chk(r["estudios"], base, r["pct"])
        d = deg.get(r["codigo"])
        extra = f"{d['estudios']} & {d['curvas']} & {num(d['pendiente_mediana_pp'])}" if d else "--- & --- & ---"
        filas.append(f"\\quad {ETIQUETA[r['codigo']]} & {kn(int(r['estudios']), base)} & {extra} \\\\")
    filas.append("\\multicolumn{5}{@{}l}{\\textit{Prácticas de reporte (estudios que sí las reportan)}} \\\\")
    for campo, nombre in (("degradacion_reportada", "Degradación por turno"), ("errores_join_reportados", r"Errores de \en{join}"),
                          ("contaminacion_discutida", "Contaminación del \\en{benchmark}")):
        r = next(r for r in rs if r["campo"] == campo and r["codigo"] == "SI")
        chk(r["estudios"], base, r["pct"])
        filas.append(f"\\quad {nombre} & {kn(int(r['estudios']), base)} & & & \\\\")
    cuerpo = ("\\begin{tabular}{@{}l r r r r@{}}\n\\toprule\n"
              "Estrato o práctica & Estudios (\\%) & Est. con curva & Curvas & Pendiente (pp/turno) \\\\\n\\midrule\n"
              + "\n".join(filas) + "\n\\bottomrule\n\\end{tabular}")
    tabla("pi5", f"PI5: historial usado en la evaluación y degradación por turno, estudios del Nivel 2 que alcanzan el "
          f"umbral de validez ($n = {base}$). La pendiente es la mediana por estrato; los estratos no se combinan.", cuerpo,
          ancho=True)


def informe_calidad(res):
    n = res["n"]
    lineas = ["# Calidad de los estudios del Nivel 2 — hallazgos (para aprobación de la autora)", "",
              "Generado por `analysis/src/tablas/tablas.py` desde `slr/calidad/calidad.csv`; no editar a mano.", "",
              f"- Estudios evaluados: {n}. Alcanzan el umbral de validez (≥ 50 %): {res['supera_umbral']}; "
              f"bajo el umbral: {len(res['bajo_umbral'])} ({', '.join(res['bajo_umbral'])}).",
              f"- Puntuación de validez: mediana {red(res['validez_mediana'])} % (RIC {red(res['validez_q1'])}–"
              f"{red(res['validez_q3'])} %; rango {red(res['validez_min'])}–{red(res['validez_max'])} %).", ""]
    orden = sorted(res["por_item"].items(), key=lambda kv: -kv[1]["1"])
    lineas.append("Ítems ordenados por proporción de «sí» (1):")
    for q, d in orden:
        lineas.append(f"- {q} ({d['tipo']}): sí {d['1']} ({red(100 * d['1'] / n)} %), parcial {d['0.5']} "
                      f"({red(100 * d['0.5'] / n)} %), no {d['0']} ({red(100 * d['0'] / n)} %)")
    (SIN / "CALIDAD.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    res = calidad()
    t_relacionados()
    t_criterios()
    t_d4()
    t_calidad(res)
    t_efectos()
    t_otros()
    t_taxo_pi12()
    t_contraste_pi34()
    t_pi5()
    informe_calidad(res)
    json.dump(leyendas, open(OUT / "leyendas.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{len(leyendas)} tablas → {OUT.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
