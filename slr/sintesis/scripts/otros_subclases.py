"""Post-close-out revision (2026-10-19): split the «Otros componentes del pilar» class of the effects synthesis.

Lists every component that pi15_sintesis.clase() puts in «Otros» (same filters as the effects analysis: Level 2
studies above the validity threshold, accuracy metric families, numeric with/without values) and proposes
(a) a reassignment to an existing named class when the regex missed it (checked against the full text), or
(b) a sub-class. The author decides on the review sheet; pi15_sintesis.py then reads the confirmed CSV.
Outputs: slr/sintesis/otros_subclases.csv, slr/sintesis/revision_otros.md
Usage (repo root): uv run --project analysis python slr/sintesis/scripts/otros_subclases.py
"""
import collections
import csv
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "analysis" / "src" / "figs"))
import pi15_sintesis as P  # noqa: E402

SIN = RAIZ / "slr" / "sintesis"
ENT = "Entrenamiento, objetivos auxiliares y datos"
SUB = {  # pillar -> [(sub-class, regex on component name)], first match wins; then ENT; else «sin agrupar»
    "PI1": [("Análisis del discurso, la intención y la correferencia", r"DIFERENCIA|DISCURSO|INTENCION|COREFER|MRD-Q|DEPENDENCIA_SINT"),
            ("Selección, alineación y codificación del historial", r"RECUPERADOR|RANKING|SIMILITUD|p-align|TOKENS_PREV|STRUCTURE_MARK|SACE|SESE|Enhance dialogue")],
    "PI2": [("Gestión del historial y la memoria", r"VENTANA|CONTEXTO_32K|HISTORIAL|EQQ|FS \(|AGREGACION|Gate|NO_CHANGE|TRAYECTORIA|FRESH|INSPECT|RETRIEVER|RECUPERACION|SELECTOR|STRUCTURE_MARK")],
    "PI3": [("Enriquecimiento del esquema y del contenido", r"RELACIONES|METADATOS|DESCRIPCIONES|SELECTOR|STRUCTURE_MARK|PISTAS|Knowledge|ROLE_KNOWLEDGE|com-enh|col-enh|SACE|SESE|DCR|ACID"),
            ("Vistas generadas", r"VISTAS"),
            ("Decodificación y razonamiento guiados", r"CONSTRAINED|SQL_COMPLETION|GRUESO|AUTO_COT|ROLE_STATE")],
    "PI4": [("Agentes con herramientas", r"AGENTE|LONG_HORIZON"),
            ("Detección de ambigüedad y consulta de la intención", r"DETECTOR|DECOMPOSER|INTENCION|Intention"),
            ("Decodificación restringida", r"PICARD")],
}
ENT_RX = (r"PREENTREN|MULTITAREA|DUAL_LEARN|FUSION_PESOS|MERGING|DATOS_|AUMENTO|SELF_PLAY|synthetic|MLM|TCS_|SQLBERT|SST|UDT|"
          r"\bRL\b|_RL|RL_|SFT|RECOMPENSA|REPLAY|JUEZ|PUNTUADOR|MUESTRAS_ENTREN|CONSISTENCIA|ANONIMIZ|ULP|SLP|TSP|CSP|TWP|"
          r"TRAZAS|MT_PROMPTS|FORMATO_TEXT|HARNESS|SQL-similarity|QUERY_PLAN|SIMULACION")
# Reassignment to an existing named class (regex miss), proposed from the full text: (pillar, regex) -> (class, reason)
REASIGNAR = [
    ("PI3", r"^(C2C|V2C|ALL2C|MODO_)", "Vinculación de esquemas", "R00453 p. 1: «three linking modes» (C2C, V2C, ALL2C)"),
    ("PI3", r"DB_CONTENT|VALORES_", "Vinculación de esquemas", "vinculación de valores (contenido de la BD), incluida en la definición de vinculación del protocolo"),
    ("PI2", r"^SST", "Grafo / estado estructurado", "R00096: «schema state tracking (SST) objective … schema slot»"),
    ("PI2", r"REUSE_AND_PATCH|SELECCION_VERSION_HISTORICA", "SQL / resultados previos", "R00499: reutiliza o selecciona versiones previas"),
    ("PI4", r"GUIA_GENERAL", "Autocorrección / retroalimentación de ejecución", "R00160: el maestro corrige errores del alumno («general guidance»)"),
]
DUDA = {  # component regex -> note shown on the sheet (non-obvious cases only)
    r"^EXPLICACION$|^PREGUNTA$": "R00105 (NL-EDIT): explicación del SQL y corrección por retroalimentación del usuario; codificado en PI1",
    r"NL2IR2SQL": "R00453: representación intermedia + compilador determinista",
    r"^P_ALIGN$": "R00084: alineación texto–SQL para la generalización composicional",
    r"^SST|UDT": "R00096: objetivos auxiliares de seguimiento (estado del esquema / dependencia entre enunciados)",
    r"RECUPERACION|RL_SELECTOR|RETRIEVER": "R00438/R00099: recuperación aprendida de memoria o de ejemplos (método de recuperación vs. entrenamiento)",
    r"SIMULACION": "R00311: autoentrenamiento contrastivo con conversaciones simuladas",
}


def main():
    cal = {r["id_estudio"]: r for r in csv.DictReader(open(RAIZ / "slr" / "calidad" / "calidad.csv", encoding="utf-8"))}
    ok = {s for s, r in cal.items() if r.get("supera_umbral") == "SI"}
    comp = collections.defaultdict(set)
    for r in csv.DictReader(open(RAIZ / "slr" / "extraccion" / "contrastes_taxonomia.csv", encoding="utf-8")):
        if r["id_estudio"] not in ok or r["metrica_familia"] not in P.ACC:
            continue
        if P.num(r["valor_con"]) is None or P.num(r["valor_sin"]) is None:
            continue
        for p in [x for x in P.lista(r["pilar"]) if x in P.CLASES]:
            if P.clase_regex(p, r["componente"]) == P.OTROS:
                comp[(p, r["componente"])].add(r["id_estudio"])
    previas = {}  # keep the author's decisions when the sheet is regenerated
    if (SIN / "otros_subclases.csv").exists():
        previas = {(r["pilar"], r["componente"]): r["decision"] for r in csv.DictReader(open(SIN / "otros_subclases.csv", encoding="utf-8"))}
    filas = []
    for (p, c), ids in sorted(comp.items()):
        clase, motivo = "", ""
        for pp, rx, cl, mo in REASIGNAR:
            if pp == p and re.search(rx, c):
                clase, motivo = cl, mo
                break
        sub = next((n for n, rx in SUB[p] if re.search(rx, c)), None)
        if sub is None:
            sub = ENT if re.search(ENT_RX, c, re.I) else "Otros (sin agrupar)"
        duda = next((v for k, v in DUDA.items() if re.search(k, c)), "")
        filas.append({"pilar": p, "componente": c, "estudios": "/".join(sorted(ids)), "reasignar_a": clase,
                      "motivo_reasignacion": motivo, "subclase": "" if clase else sub, "duda": duda, "decision": previas.get((p, c), "")})
    with open(SIN / "otros_subclases.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    hoja(filas)
    print(f"{len(filas)} componentes; reasignados {sum(bool(f['reasignar_a']) for f in filas)}; dudas {sum(bool(f['duda']) for f in filas)}")


def hoja(filas):
    L = ["# Revisión: subclases de «Otros componentes del pilar» (refactor posterior al cierre, 2026-10-19)", "",
         "Datos: `slr/sintesis/otros_subclases.csv`. Textos completos: `slr/texto_completo/texto/<ID>.txt` "
         "(o `texto_bola/`). Escriba su respuesta después de «Respuesta:» en cada punto.", "",
         "## Opciones", "", "| Sección | Respuestas válidas |", "|---|---|",
         "| A (subclases) | **OK** (aceptar) · **CAMBIAR:** texto libre |",
         "| B (reasignaciones a una clase existente) | **SI** (reasignar) · **NO** (dejar en «Otros») |",
         "| C (casos dudosos) | código de la subclase de la tabla de códigos, o **SIN** (sin agrupar) |", "",
         "## Códigos de subclase", "", "| Código | Pilar | Subclase |", "|---|---|---|"]
    codigos = {}
    for p in sorted(SUB):
        for i, (n, _) in enumerate(SUB[p] + [(ENT, "")], 1):
            codigos[(p, n)] = f"{p}-{i}"
            L.append(f"| {p}-{i} | {p} | {n} |")
    L += ["", "## A. Subclases propuestas", "",
          "La clase transversal «" + ENT + "» reúne estrategias de entrenamiento (preentrenamiento, objetivos auxiliares, "
          "RL/SFT, aumento de datos) que no son técnicas propias del pilar.", "",
          "| Pilar | Subclase | Componentes | Estudios | Ejemplos |", "|---|---|---|---|---|"]
    g = collections.defaultdict(list)
    for f in filas:
        if not f["reasignar_a"]:
            g[(f["pilar"], f["subclase"])].append(f)
    for (p, s), fs in sorted(g.items()):
        est = sorted(set("/".join(f["estudios"] for f in fs).split("/")))
        L.append(f"| {p} | {s} | {len(fs)} | {len(est)} | {'; '.join(f['componente'][:35] for f in fs[:3])} |")
    L += ["", "Respuesta A:", "", "## B. Reasignaciones propuestas a una clase existente (la expresión regular no las detectó)", "", "Si se aceptan, cambian los recuentos de esas clases en la Tabla VI y la Figura 6.", ""]
    rb = collections.defaultdict(list)
    for f in filas:
        if f["reasignar_a"]:
            rb[(f["pilar"], f["reasignar_a"], f["motivo_reasignacion"])].append(f)
    for i, ((p, cl, mo), fs) in enumerate(sorted(rb.items()), 1):
        L += [f"**B{i}.** {p} → «{cl}»: {', '.join(f['componente'][:40] for f in fs)} ({'/'.join(sorted({f['estudios'] for f in fs}))}). "
              f"Motivo: {mo}.", "", f"Respuesta B{i}:", ""]
    L += ["## C. Casos dudosos (asignación propuesta entre paréntesis)", ""]
    for i, f in enumerate([f for f in filas if f["duda"] and not f["reasignar_a"]], 1):
        L += [f"**C{i}.** {f['pilar']} · `{f['componente'][:60]}` ({f['estudios']}) — {f['duda']}. "
              f"Propuesta: {codigos.get((f['pilar'], f['subclase']), 'SIN')} ({f['subclase']}).", "", f"Respuesta C{i}:", ""]
    (SIN / "revision_otros.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
