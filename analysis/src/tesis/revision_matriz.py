"""Phase 14, step 3a — author's review sheet for the decision matrix (only the judgment inputs).

Reads datos/matriz_decision.csv and matriz_alternativas.csv (from matriz_decision.py) and writes
tesis/00-justificacion/revision_matriz.md. Does not overwrite a sheet that already has answers.
"""
import csv

from mapa_oe import SALIDA
from matriz_decision import ALTERNATIVAS, ESCENARIOS

HOJA = SALIDA.parent / "revision_matriz.md"
PREGUNTAS = {  # code: (question, base option A)
    "D13": ("Base de C2 para candidatos de evaluación sin contrastes", "0 en E0–E2 y no aplicable en E3 (propuesto)"),
    "D14": ("Indicador de novedad de OE1", "reescritura de la pregunta (salida principal del OE)"),
    "D15": ("Indicador de novedad de OE4", "retroalimentación de errores de ejecución"),
    "D16": ("C1 de DE (líneas base simples)", "0: no hay indicador de que falten líneas base (paso 2)"),
    "D17": ("Indicador de problema de DG", "brecha de cobertura de datos industriales (los errores de join no son específicos de la escala)"),
    "D18a": ("Requisitos de OE5", "SUSTITUTO: la propuesta incluye esquemas empresariales"),
    "D18b": ("Requisitos de OE3", "ninguno: un solo componente sobre esquemas públicos con FK"),
    "D19": ("Evidencia (C1, C2) de las combinaciones", "media de los componentes"),
    "D20": ("C5 de los candidatos de evaluación", "3: el resultado es informativo en cualquier dirección"),
}


def main():
    if HOJA.exists() and "**Decisión:** " in HOJA.read_text(encoding="utf-8").replace("**Decisión:** \n", ""):
        raise SystemExit(f"{HOJA} already has answers; not overwritten")
    M = {r["candidato"]: r for r in csv.DictReader(open(SALIDA / "matriz_decision.csv", encoding="utf-8"))}
    A = list(csv.DictReader(open(SALIDA / "matriz_alternativas.csv", encoding="utf-8")))
    esc = list(ESCENARIOS)
    L = ["# Revisión — matriz de decisión (Fase 14, paso 3a)", "",
         "**Cómo responder:** debajo de cada decisión escriba `A` (base propuesta), `B` (alternativa) o texto libre.",
         "Reglas: `reglas_matriz.md`. Puntuaciones: `datos/matriz_decision.csv`; efecto de cada alternativa:",
         "`datos/matriz_alternativas.csv` (generados por `analysis/src/tesis/matriz_decision.py`). Solo se listan las",
         "entradas de juicio; el resto de puntuaciones sale de reglas fijas sobre los datos de los pasos 1 y 2.", "",
         "| Código | Significado |", "|---|---|",
         "| C1–C5 | problema, beneficio, novedad, factibilidad, riesgo nulo (0–3; 3 = favorable) |",
         "| E0–E3 | pesos iguales; prioridad factibilidad; prioridad evidencia; iguales con C2 no aplicable a evaluación |",
         "| rangos | posición en E0, E1, E2, E3 (1 = mejor; 15 candidatos) |", "",
         "## Matriz base", "",
         "| Candidato | Tipo | C1 | C2 | C3 | C4 | C5 | " + " | ".join(e.split("_")[0] for e in esc) + " | rangos | dominado por |",
         "|---|---|" + "---|" * (5 + len(esc)) + "---|---|"]
    for k, r in sorted(M.items(), key=lambda x: -float(x[1]["E0_iguales"])):
        L.append(f"| {k} | {r['tipo']} | " + " | ".join(r[c] for c in ("C1_problema", "C2_beneficio", "C3_novedad", "C4_factibilidad", "C5_riesgo_nulo"))
                 + " | " + " | ".join(r[e] for e in esc) + f" | {r['rango_min']}–{r['rango_max']} | {r['dominado_por'].replace(';', ', ') or '—'} |")
    L += ["", "---", ""]
    desc = {c: d for c, d, _ in ALTERNATIVAS}
    for cod, (preg, base) in PREGUNTAS.items():
        L.append(f"**{cod}. {preg}.** A: {base} · B: {desc.get(cod, 'E3 como escenario base (C2 no aplicable)')}.")
        efectos = [a for a in A if a["decision"] == cod]
        if efectos:
            L.append("Efecto de B: " + "; ".join(
                f"{a['candidato']} {a['base_E0_iguales']}→{a['alt_E0_iguales']} (rangos "
                f"{'/'.join(a['base_rango_' + e] for e in esc)}→{'/'.join(a['alt_rango_' + e] for e in esc)})" for a in efectos) + ".")
        elif cod == "D13":
            L.append("Efecto de B: ver la columna E3 de la matriz base.")
        L += ["**Decisión:** ", ""]
    HOJA.write_text("\n".join(L), encoding="utf-8")
    print(f"{HOJA}: {len(PREGUNTAS)} decisiones, {len(L)} líneas")


if __name__ == "__main__":
    main()
