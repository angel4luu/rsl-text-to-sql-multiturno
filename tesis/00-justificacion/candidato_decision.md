# Candidate decision for step 5 (draft, not yet the author's decision) — 2026-10-14

Source: proposal discussed by the author with Codex (pasted into the Claude session), then reviewed by Claude.
Codex's own classification: **ajustar** (not reorientar). Author agreed to carry it into step 5 and close the gaps below.

## Codex proposal (summary, as pasted)
- **Keep:** training-free framework; modular/multiagent architecture; explicit conversational state as a graph; schema
  grounding and execution; predicted-history evaluation on SParC and CoSQL; a working, documented software product.
- **Change:** do not claim the exact dual-layer graph is supported by the SLR; do not require every original module to
  show an independent accuracy gain; Steiner routing, linguistic restoration and iterative repair become replaceable
  plug-ins; engineering contribution = architecture, extensibility, traceability, replayability, controlled evaluation;
  compare graph state with simpler context strategies inside the same artifact.
- **Research question:** ¿Cómo diseñar, implementar y evaluar un marco software modular sin entrenamiento que gestione
  explícitamente el estado conversacional y permita comparar estrategias de contexto bajo historial predicho en
  consultas a bases de datos relacionales?
- **General objective:** Diseñar, implementar y evaluar un marco software modular sin entrenamiento para consultas
  conversacionales a bases de datos relacionales, que incorpore gestión explícita del estado, componentes
  intercambiables de procesamiento y un entorno reproducible de evaluación con historial predicho.
- **Specific objectives:** (1) requisitos, atributos de calidad y arquitectura modular con interfaces entre diálogo,
  estado, vinculación del esquema, generación SQL y validación por ejecución; (2) núcleo de orquestación con estado
  explícito y trazable (adición, modificación, eliminación, reinicio de restricciones); (3) estrategias de contexto
  intercambiables: historial plano, reutilización del SQL previo, estado estructurado basado en grafos; (4) módulos
  configurables de vinculación del esquema y validación por ejecución, sin presuponer que un algoritmo sea mejor;
  (5) observabilidad y evaluación: repetición de diálogos, realimentación de salidas predichas, transiciones de estado,
  errores, latencia, tokens, resultados por turno; (6) evaluación en SParC y CoSQL: pruebas funcionales y de
  integración, comparaciones controladas de exactitud, degradación por turno, recuperación tras errores y coste.
- **Evaluation:** software-engineering (state-mutation correctness, interface conformance, test coverage,
  reproducibility, SQL→state traceability, failure handling, effort to add a strategy) + empirical (EX and
  conversational metrics, per-turn under predicted history, recovery after error, latency/tokens/API cost, flat vs
  previous-SQL vs structured state). The slope is one outcome, not the sole criterion.
- **Title options (Codex):** keep the registered title, or «Marco software modular sin entrenamiento con estado
  explícito para consultas conversacionales a bases de datos relacionales».

## Claude review
- **Title correction:** Codex quoted a wrong registered title. The registered one (`latex/comun/metadatos.tex:17`) is
  «Marco multiagente con grafos para mitigar la degradación por turno en consultas conversacionales a bases de datos
  relacionales». «Para mitigar» can be read as an aim (keeps it, no Directiva 007 modification) — author's call.
- **Basis of each component** (for `decision.md`):

| Component | Basis |
|---|---|
| Predicted-history evaluation, per-turn results | SLR gap (first-ranked by evidence solidity) |
| Graph-based structured state | SLR class: graphs 9/72 (12,5 %); structured-state contrasts 11 studies, 10 positive, high confidence |
| Two-layer design, deterministic mutations | Innovation (C3), tested, not assumed |
| Multiagent, training-free | SLR growth trend (AGENTES 0/1/6/27/43 in 2022–2026*, `slr/sintesis/PI0.md`) + feasibility (no GPU); no efficacy contrasts (`mapa_evidencia.md` §Premisas transversales) |
| Flat history / previous-SQL comparators | SLR evidence (SQL previo/edición/ventana: 12 studies, 11 positive, median +5,08 pp) |
| Title «…para mitigar…» | Registration (Directiva 007), read as aim |

  Note: a multi-turn-only agent count by year (ad hoc in chat: 4/12 in 2025, 8/18 in 2026) is **not** in any script
  output — if used in text, add it to `analysis/src/tesis/` first.
- **Gaps to close in step 5/6:**
  1. Scope vs calendar (Nov 2026 – Jul 2027): 6 objectives, 3 strategies × 2 benchmarks × repetitions → API cost estimate.
  2. Contamination (desafío H10): SParC/CoSQL are 2019; state as limitation or add a SPENCE-style probe (R00029).
  3. SQL-hardness strata + precision analysis for per-turn differences (H5; dialogue-level dependence).
  4. Measurement protocol for SE metrics such as «effort to add a strategy».
- Classification: **ajustar**. Still the proposal's components; legitimate if `decision.md` separates what comes from
  the SLR from what comes from engineering, feasibility, innovation or registration.
