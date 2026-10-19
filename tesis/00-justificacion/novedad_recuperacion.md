# Paso 5a — Verificación de novedad de la recuperación guiada por ejecución (2026-10-14)

Pregunta: ¿existen ya mecanismos de puntos de control y recuperación (*rollback*) del estado en *Text-to-SQL*
conversacional?

## Búsquedas

| Fuente | Consulta | Fecha |
|---|---|---|
| Corpus RSL (`slr/extraccion/extraccion.csv`, 389 estudios, todos los campos) | `rollback\|roll back\|checkpoint\|backtrack\|revert\|undo\|recover\|error propagation\|state repair\|reset` | 2026-10-14 |
| arXiv | `(text-to-SQL OR text2sql OR NL2SQL) AND (rollback OR checkpoint OR backtrack OR "error recovery" OR "error propagation") AND (conversational OR multi-turn OR context-dependent)` (resumen) | 2026-10-14 |
| arXiv | `SQL AND (conversational OR multi-turn) AND ("dialogue state" OR "state tracking") AND (correction OR repair OR revert OR recover)` | 2026-10-14 |
| arXiv | `(rollback OR checkpoint) AND "LLM agent" AND (failure OR recovery)`, desde 2024 | 2026-10-14 |
| DBLP (volcado 2026-09-01) | `SQL rollback or checkpoint or backtrack* or recovery conversational or multi-turn or context-dependent` | 2026-10-14 |
| OpenAlex | `multi-turn text-to-SQL error propagation recovery dialogue state rollback`, desde 2019 | 2026-10-14 |

## Resultados

- **Corpus:** 7 estudios multiturno con coincidencias. El único con puntos de control y retroceso es **R00499
  (Yang2026GitHarness, 2026)**: guarda una versión por turno exitoso en un grafo ramificable y permite continuar,
  retroceder o ramificar. El retroceso se decide por **cambios de requisito del usuario**, no por fallos, y no hay
  retroalimentación de ejecución en SQL (`extraccion.csv`, `pi2_resumen`, `pi4_resumen`; texto completo, §2 y §4).
  Su trabajo relacionado cita métodos de agentes generales que restauran puntos de control tras fallos de ejecución.
  R00088 reinicia ranuras por reglas (no retrocede a estados previos); R00019 evalúa la recuperación interactiva, pero
  no propone un mecanismo; R00131 atribuye la robustez a la edición, no a un ciclo de corrección.
- **arXiv (Text-to-SQL):** 4 resultados: MIGA, STAR y EditSQL, ya en el corpus, sin mecanismo de retroceso, y
  ReToolSQL (arXiv 2608.27796, 2026), que repara SQL con retroalimentación de ejecución dentro de una sola pregunta
  mediante entrenamiento por refuerzo, sin diálogo multiturno. La búsqueda con «dialogue state» no devolvió resultados.
- **arXiv (agentes generales):** 26 resultados desde 2024. El retroceso a puntos de control es un patrón activo en
  agentes LLM de horizonte largo (p. ej., arXiv 2609.18304, «Rollback the World, Keep the Reflection», 2026).
- **DBLP y OpenAlex:** sin resultados pertinentes para *Text-to-SQL*.

## Conclusión

No se encontró un mecanismo que, en *Text-to-SQL* conversacional, use señales de ejecución para detectar un turno
fallido y retroceder a un estado estructurado válido del diálogo. Sin embargo, (a) el retroceso a puntos de control es
un patrón establecido en agentes LLM generales y (b) GitHarness ya aplica puntos de control y retroceso en un grafo de
versiones en tareas multiturno, incluido SQL, con disparador distinto.

Por tanto, la novedad debe formularse como **adaptación** de un patrón conocido de agentes a un escenario y disparador
específicos (estado del diálogo en *Text-to-SQL* conversacional, señales de ejecución, historial predicho), no como
invención del retroceso. GitHarness y un trabajo de retroceso en agentes generales deberán citarse como antecedentes,
tras verificarlos en `bib/referencias.bib` (DOI / DBLP / OpenAlex). La búsqueda es exploratoria y no exhaustiva; DBLP
no incluye trabajos añadidos después del 2026-09-01.
