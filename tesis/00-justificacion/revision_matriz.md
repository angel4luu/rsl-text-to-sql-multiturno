# Revisión — matriz de decisión (Fase 14, paso 3a)

**Cómo responder:** debajo de cada decisión escriba `A` (base propuesta), `B` (alternativa) o texto libre.
Reglas: `reglas_matriz.md`. Puntuaciones: `datos/matriz_decision.csv`; efecto de cada alternativa:
`datos/matriz_alternativas.csv` (generados por `analysis/src/tesis/matriz_decision.py`). Solo se listan las
entradas de juicio; el resto de puntuaciones sale de reglas fijas sobre los datos de los pasos 1 y 2.

| Código | Significado |
|---|---|
| C1–C5 | problema, beneficio, novedad, factibilidad, riesgo nulo (0–3; 3 = favorable) |
| E0–E3 | pesos iguales; prioridad factibilidad; prioridad evidencia; iguales con C2 no aplicable a evaluación |
| rangos | posición en E0, E1, E2, E3 (1 = mejor; 15 candidatos) |

## Matriz base

| Candidato | Tipo | C1 | C2 | C3 | C4 | C5 | E0 | E1 | E2 | E3 | rangos | dominado por |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OE2 | tecnica | 3 | 2 | 2 | 2 | 2 | 73.3 | 71.4 | 76.2 | 73.3 | 1–8 | — |
| DC | evaluacion | 3 | 0 | 1 | 3 | 3 | 66.7 | 76.2 | 61.9 | 83.3 | 1–2 | — |
| DB+DD | combinacion | 1.5 | 0 | 3 | 2 | 3 | 63.3 | 69.0 | 52.4 | 79.2 | 2–9 | — |
| DE+DF+DG | combinacion | 1.33 | 1 | 3 | 1 | 3 | 62.2 | 63.5 | 55.5 | 75.5 | 3–10 | — |
| OE1 | tecnica | 1 | 2 | 1 | 3 | 2 | 60.0 | 66.7 | 57.1 | 60.0 | 3–10 | — |
| OE4 | tecnica | 1 | 2 | 2 | 2 | 2 | 60.0 | 61.9 | 57.1 | 60.0 | 3–11 | OE2 |
| OE5 | evaluacion | 3 | 0 | 1 | 2 | 3 | 60.0 | 66.7 | 57.1 | 75.0 | 3–6 | DC |
| DB | evaluacion | 1 | 0 | 3 | 2 | 3 | 60.0 | 66.7 | 47.6 | 75.0 | 4–13 | DB+DD |
| DD | evaluacion | 2 | 0 | 2 | 2 | 3 | 60.0 | 66.7 | 52.4 | 75.0 | 4–9 | — |
| DE | evaluacion | 0 | 3 | 0 | 3 | 3 | 60.0 | 71.4 | 57.1 | 60.0 | 2–10 | — |
| DF | evaluacion | 3 | 0 | 0 | 3 | 3 | 60.0 | 71.4 | 57.1 | 75.0 | 2–5 | DC |
| OE3 | tecnica | 2 | 0 | 3 | 3 | 0 | 53.3 | 52.4 | 47.6 | 53.3 | 12–15 | — |
| DA | tecnica | 1 | 2 | 1 | 2 | 2 | 53.3 | 57.1 | 52.4 | 53.3 | 9–14 | OE1, OE2, OE4 |
| DG | evaluacion | 1 | 0 | 3 | 1 | 3 | 53.3 | 57.1 | 42.9 | 66.7 | 9–15 | DB, DB+DD, DE+DF+DG |
| DA+DC | combinacion | 2 | 1 | 1 | 2 | 2 | 53.3 | 57.1 | 52.4 | 60.0 | 9–12 | OE2 |

---

**D13. Base de C2 para candidatos de evaluación sin contrastes.** A: 0 en E0–E2 y no aplicable en E3 (propuesto) · B: E3 como escenario base (C2 no aplicable).
Efecto de B: ver la columna E3 de la matriz base.
**Decisión:** A — aprobado por la autora (2026-10-14)

**D14. Indicador de novedad de OE1.** A: reescritura de la pregunta (salida principal del OE) · B: OE1: novedad por clasificación de actos de discurso.
Efecto de B: OE1 60.0→73.3 (rangos 5/6/3/10→1/1/2/8).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D15. Indicador de novedad de OE4.** A: retroalimentación de errores de ejecución · B: OE4: novedad por reparación simbólica.
Efecto de B: OE4 60.0→66.7 (rangos 5/11/3/10→2/6/2/9).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D16. C1 de DE (líneas base simples).** A: 0: no hay indicador de que falten líneas base (paso 2) · B: DE: problema cualitativo (1).
Efecto de B: DE 60.0→66.7 (rangos 5/2/3/10→2/1/2/9); DE+DF+DG 62.2→64.5 (rangos 4/10/8/3→4/10/4/3).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D17. Indicador de problema de DG.** A: brecha de cobertura de datos industriales (los errores de join no son específicos de la escala) · B: DG: problema por errores de join (déficit).
Efecto de B: DG 53.3→60.0 (rangos 12/12/15/9→5/11/9/4); DE+DF+DG 62.2→64.5 (rangos 4/10/8/3→3/10/3/3).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D18a. Requisitos de OE5.** A: SUSTITUTO: la propuesta incluye esquemas empresariales · B: OE5 sin SUSTITUTO (solo SParC/CoSQL).
Efecto de B: OE5 60.0→66.7 (rangos 5/6/3/4→2/1/2/1).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D18b. Requisitos de OE3.** A: ninguno: un solo componente sobre esquemas públicos con FK · B: OE3 con MULTICOMPONENTE.
Efecto de B: OE3 53.3→46.7 (rangos 12/15/13/14→15/15/14/15).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D19. Evidencia (C1, C2) de las combinaciones.** A: media de los componentes · B: Combinaciones: evidencia = máximo de componentes.
Efecto de B: DA+DC 53.3→66.7 (rangos 12/12/9/10→3/7/3/9); DB+DD 63.3→66.7 (rangos 3/5/9/2→3/3/5/2); DE+DF+DG 62.2→86.7 (rangos 4/10/8/3→1/1/1/1).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D20. C5 de los candidatos de evaluación.** A: 3: el resultado es informativo en cualquier dirección · B: Riesgo nulo de candidatos de evaluación = 2.
Efecto de B: OE5 60.0→53.3 (rangos 5/6/3/4→7/8/5/5); DB 60.0→53.3 (rangos 5/6/13/4→7/8/14/5); DC 66.7→60.0 (rangos 2/1/2/1→2/2/2/1); DD 60.0→53.3 (rangos 5/6/9/4→7/8/11/5); DE 60.0→53.3 (rangos 5/2/3/10→7/4/5/13); DF 60.0→53.3 (rangos 5/2/3/4→7/4/5/5); DG 53.3→46.7 (rangos 12/12/15/9→15/15/15/12); DB+DD 63.3→56.7 (rangos 3/5/9/2→5/7/11/3); DE+DF+DG 62.2→55.5 (rangos 4/10/8/3→6/13/10/4).
**Decisión:** A — aprobado por la autora (2026-10-14)
