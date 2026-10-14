# Fase 1.2 — Criterios de elegibilidad

Fecha: 2026-10-11 · Estado: **v1.1 — revisada tras el Checkpoint 1 (M1, M2, menores); aprobada por la autora (2026-10-11)**
Base: PICOC y decisiones D1–D9 (`01_preguntas_picoc.md`).

## Definiciones operativas
- **Text-to-SQL / NLIDB:** traducción de lenguaje natural a consultas SQL ejecutables sobre bases de datos **relacionales**.
- **Escenario multiturno (revisado, M2):** el **usuario** formula **preguntas sucesivas en lenguaje natural** y la interpretación de la pregunta *t* depende de preguntas o respuestas de turnos **anteriores del usuario** (diálogo o sesión). Las rondas internas de un sistema sobre **una sola pregunta** (agente ↔ SGBD, autorrefinamiento, exploración tipo ReAct) **no** son multiturno (caso B6).
- **Contribución central (revisado, M1/M2; aplica a ambos escenarios):** la técnica de PI3 (vinculación de esquemas / rutas de *join*) o PI4 (retroalimentación de ejecución / autocorrección) se declara como **contribución o novedad del estudio en el título o el resumen**. Un sistema que solo *contiene* un módulo de este tipo no cumple. *(Se elimina la vía «se evalúa por separado / ablación», no verificable en título-resumen.)*
- **Estudio vs. informe (PRISMA 2020):** un estudio puede tener varios informes; la unidad de análisis es el **estudio**.
- **Nivel (D7):** Nivel 1 = todos los incluidos; Nivel 2 = incluidos **multiturno**.

## Regla de incertidumbre (M2c)
En título-resumen, **si hay duda** sobre cualquier criterio, el registro **pasa a texto completo**. Solo se excluye en título-resumen cuando el criterio se cumple con claridad.

## Criterios de inclusión (deben cumplirse todos)
| Código | Criterio |
|---|---|
| IC1 | Estudio **primario** que propone, adapta o evalúa una técnica o un *benchmark* de Text-to-SQL sobre bases de datos relacionales |
| IC2 | **Multiturno:** aborda al menos una de PI1–PI5. **Un turno:** aborda PI3 o PI4 como **contribución central** (D1). Los *benchmarks* de un turno entran por PI3/PI4 (caso B4) |
| IC3 | Reporta una **evaluación empírica cuantitativa** |
| IC4 | **Un turno:** evalúa en al menos un *benchmark* público (p. ej., Spider, BIRD, WikiSQL). **Multiturno:** cualquier evaluación, incluidos datos propietarios |
| IC5 | Publicado entre **2019-01-01** y la fecha de búsqueda |
| IC6 | Escrito en **inglés o español**. Los estudios en español se admiten **si aparecen en la búsqueda** (no hay cadena específica en español; ver limitaciones) |
| IC7 | Artículo completo revisado por pares (revista, conferencia, taller, incluidas las *demo tracks*; ≥ 4 páginas de contenido) **o** preprint de arXiv sin versión revisada a la fecha de búsqueda |

## Criterios de exclusión — ORDENADOS
Se registra el **primer** código aplicable (requisito de sr-screener).

| Código | Excluir si… | Etapa habitual |
|---|---|---|
| EX1 | Publicado antes de 2019 | Metadatos |
| EX2 | Escrito en un idioma distinto de inglés o español | Metadatos |
| EX3 | Tipo no elegible: tesis, póster, solo resumen o resumen extendido, **artículo de < 4 páginas de contenido**, editorial, prefacio/índice de actas, libro completo. *(Los artículos de demo revisados por pares con evaluación cuantitativa no se excluyen aquí)* | Metadatos / texto completo |
| EX4 | No es estudio primario: *survey*, revisión, tutorial, posición (→ carpeta 9 si es pertinente) | Título-resumen |
| EX5 | No trata Text-to-SQL sobre BD relacionales: KGQA/SPARQL, Cypher, NoSQL, QA sobre tablas sin SQL, generación de código general. *Excepción: se incluye si también evalúa en SQL relacional* | Título-resumen |
| EX6 | Un solo turno y no declara PI3/PI4 como contribución central | Título-resumen (con regla de incertidumbre) |
| EX7 | Sin evaluación empírica cuantitativa | Texto completo |
| EX8 | Un solo turno sin evaluación en *benchmark* público | Texto completo |
| EX9 | Informe secundario de un estudio ya incluido (se vincula, no se cuenta aparte) | Deduplicación / texto completo |

**No es exclusión:** el texto completo no recuperable se reporta como «informe no recuperado», por escenario (D6).
**No se excluye por revista:** las posibles revistas depredadoras se tratan en la evaluación de calidad.

## Reglas de versiones
1. Informe principal = versión revisada por pares más completa (revista > conferencia > preprint).
2. Si la versión de revista añade resultados, se vinculan ambos informes y se extrae de la más completa.
3. Un preprint cuenta como estudio solo si no existe versión revisada a la fecha de búsqueda; se registra la versión (v1, v2…).

## Casos límite — DECIDIDOS
| # | Caso | Decisión |
|---|---|---|
| B1 | Aclaración interactiva dentro de **una sola pregunta** independiente (el sistema pide confirmación o pistas, p. ej., Chen et al. 2025) | **Un turno.** Elegible solo vía PI3/PI4; etiqueta `INTERACTIVO`. **Excepción (ronda 1):** las aclaraciones que ocurren **dentro de un diálogo multiturno** (p. ej., *benchmarks* tipo CoSQL, donde el usuario responde a preguntas del sistema en una conversación) son **multiturno** |
| B2 | **Historial de consultas previas independientes** (no un diálogo; p. ej., Urban et al. 2025) | **Un turno.** Elegible solo vía PI3/PI4; etiqueta `USA_HISTORIAL` |
| B3 | Text-to-SQL como **componente** de un sistema mayor (agentes de análisis, Text-to-Vis, BI conversacional) | Incluir **solo si** el componente Text-to-SQL se evalúa por separado con métricas SQL cuantitativas y cumple los demás criterios |
| B4 | **Benchmarks** de un solo turno centrados en PI3/PI4 sin técnica nueva | **Incluir vía PI3/PI4** (Nivel 1) si reportan resultados de modelos de referencia |
| B5 | Text-to-SQL multiturno sobre **NoSQL** o lenguajes híbridos | EX5 salvo que también evalúe en SQL relacional |
| B6 *(nuevo, M2)* | **Rondas internas** de agente ↔ SGBD, autocorrección o exploración sobre **una sola pregunta del usuario**, aunque el estudio las llame «multi-turn» o «multi-round» | **Un turno.** Elegible solo vía PI3/PI4 |

## Limitaciones de idioma (declaradas)
- Se excluye la literatura en chino (EX2) pese a la relevancia de grupos chinos y del *benchmark* CHASE: sesgo de idioma reconocido.
- No se busca en bases hispanohablantes (SciELO, Redalyc): los estudios en español solo entran si los recuperan las fuentes elegidas.
