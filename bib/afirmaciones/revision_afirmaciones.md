# Hoja de revisión — respaldo de las citas a referencias que no son estudios (fase 13, paso 1b)

Generada por `bib/scripts/hoja_afirmaciones.py`. Codex (`gpt-6.1-sol`, razonamiento medio, solo lectura) juzgó 58 oraciones que citan 31 referencias, con el título y el resumen de OpenAlex: 28 respaldadas, 24 parciales y 6 no evaluables. Aquí solo están los casos no obvios: A = 3, B = 9 revisiones (22 oraciones); C es informativa.

## Cómo responder

| Sección | Qué es | Respuestas válidas en `Decisión:` |
|---|---|---|
| **A** | La oración afirma más que la fuente; hay una redacción propuesta | **OK** = aplicar la propuesta · **M** = mantener el texto actual · o escriba la redacción que prefiera |
| **B** | Descriptores de una revisión previa que usted tomó de su lectura (columna «Fuente leída»); Codex solo vio el resumen | **OK** = lo confirmo contra la fuente · **C** = corregir (añada la nota: `Decisión: C — …`) |
| **C** | Informativa: resuelta con registros del repositorio | (no responder) |

Veredictos de Codex: *supported* (respaldada), *partial* (la fuente respalda solo una parte o la oración es más fuerte), *unsupported* (no coincide), *cannot_judge* (el registro no basta). Las revisiones previas están en Mendeley, carpeta «9 · Revisiones previas (trabajos relacionados)».

---

## A · Redacción (3)

### A1 · Li2020ContextSurvey#2, Li2020ContextSurvey#3
- Archivo: secciones/02-trabajos-relacionados.tex, secciones/05-discusion.tex
- Texto actual: «…una revisión narrativa, anterior a los LLM, …» / «…una visión narrativa anterior a los LLM…»
- Codex (partial), Li2020ContextSurvey#2: The abstract supports the broader semantic-parsing scope, but does not establish a narrative methodology, and general historical knowledge shows that LLMs already existed in 2020.
- Codex (partial), Li2020ContextSurvey#3: The abstract supports its broader semantic-parsing scope, but not the narrative classification, while general historical knowledge makes the unqualified claim that it predates LLMs inaccurate.
- **Propuesta:** «…anterior a la adopción generalizada de los LLM…» en ambas oraciones (en 2020 ya existían modelos como GPT-3).

Decisión: OK (autora, 2026-10-14; aplicado)

### A2 · Quamar2022NLI#1, Shi2026SurveyLLM#1
- Archivo: secciones/01-introduccion.tex
- Texto actual: «…y la tarea de traducir una pregunta a una consulta SQL (Text-to-SQL) es su formulación computacional más estudiada~[Quamar, Shi].»
- Codex (partial), Quamar2022NLI#1: The abstract supports natural-language data access for nontechnical users and translation into SQL, but does not establish Text-to-SQL as the most studied computational formulation.
- Codex (partial), Shi2026SurveyLLM#1: The abstract establishes the relevance of LLM-based Text-to-SQL but does not define NLIDB or establish that Text-to-SQL is its most studied computational formulation.
- **Propuesta:** «…es una de sus formulaciones computacionales principales…» (ninguna de las dos fuentes afirma que sea la más estudiada).

Decisión: OK (autora, 2026-10-14; aplicado)

### A3 · Deng2022Recent#2
- Archivo: tabla «Revisiones previas» (slr/sintesis/tablas/revisiones_previas.csv)
- Texto actual: Tipo = «Narrativa»
- Codex (partial), Deng2022Recent#2: The abstract establishes general Text-to-SQL coverage but does not establish the narrative or multiturn-subtopic classifications, instead describing the survey as systematic.
- **Propuesta:** Tipo = «Narrativa (se declara sistemática)»: su resumen dice «we … provide this systematic survey», sin protocolo. Mantener «Narrativa» también es defendible si el criterio de la tabla es el método y no la autodenominación.

Decisión: OK (autora, 2026-10-14; aplicado)

---

## B · Descriptores de revisiones previas (9)

### B1 · Li2020ContextSurvey — fuente leída: Resumen
- **Li2020ContextSurvey#1** (secciones/01-introduccion.tex): Esto introduce elipsis, correferencia y referencias implícitas a consultas previas, que el sistema debe resolver antes de decidir qué tablas y columnas intervienen~\cite{Li2020ContextSurvey}.
  - Codex (partial): The abstract supports contextual dependence, but does not establish the listed phenomena or require resolving them before selecting SQL tables and columns.
- **Li2020ContextSurvey#4** (tablas/relacionados.tex): \midrule \cite{Li2020ContextSurvey} (2020) & Narrativa & Análisis semántico dependiente del contexto (no solo SQL) & Eje central & No reportado & Resumen
  - Codex (partial): The abstract supports the broad scope and contextual focus and reports no review protocol, but does not establish the narrative classification or equate contextual dependence exclusively with multiturn interaction.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

### B2 · Yang2025Conversational — fuente leída: Resumen
- **Yang2025Conversational#1** (secciones/01-introduccion.tex): Solo una revisión se centra en el Text-to-SQL conversacional~\cite{Yang2025Conversational}, y según su resumen es narrativa y no reporta protocolo de búsqueda.
  - Codex (partial): The title establishes a conversational Text-to-SQL focus, but the unavailable abstract prevents verification of narrative methodology or search-protocol reporting.
- **Yang2025Conversational#2** (secciones/02-trabajos-relacionados.tex): Yang et al.~\cite{Yang2025Conversational} es la revisión más cercana en alcance: según su resumen, cubre el manejo del contexto (correferencia y elipsis), la evolución de las arquitecturas desde codificador-decodificador hasta LLM y agentes, y una comparación cuantitativa en SParC y CoSQL.
  - Codex (partial): The title supports the broad conversational Text-to-SQL scope, but the record cannot verify the specific topics or quantitative comparisons attributed to its abstract.
- **Yang2025Conversational#3** (secciones/05-discusion.tex): Según su resumen, Yang et al.~\cite{Yang2025Conversational} cubren el manejo del contexto, la evolución de las arquitecturas y una comparación cuantitativa en SParC y CoSQL, sin mencionar protocolo de búsqueda ni tratar como ejes la vinculación de esquemas, la inferencia de \en{joins} o la retroalimentación de ejecución.
  - Codex (cannot_judge): No abstract or substantive content is provided to verify either the claimed coverage or the claimed omissions.
- **Yang2025Conversational#4** (tablas/relacionados.tex): \cite{Yang2025Conversational} (2025) & Narrativa & Text-to-SQL conversacional & Eje central & No reportado & Resumen
  - Codex (partial): The title supports conversational scope and multiturn centrality, but the record cannot verify narrative methodology, protocol reporting, or descriptors supposedly checked against an abstract.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

### B3 · Abbas2022NLIDB — fuente leída: Resumen
- **Abbas2022NLIDB#2** (tablas/relacionados.tex): \cite{Abbas2022NLIDB} (2022) & Narrativa & NLIDB con aprendizaje profundo & Subtema & No verificado & Resumen
  - Codex (partial): The abstract supports the stated deep learning NLIDB scope but does not establish either a narrative review methodology or coverage of multiturn interaction as a subtopic.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

### B4 · Katsogiannis2023Survey — fuente leída: Resumen
- **Katsogiannis2023Survey#2** (tablas/relacionados.tex): \cite{Katsogiannis2023Survey} (2023) & Narrativa & Text-to-SQL con aprendizaje profundo & Subtema & No verificado & Resumen
  - Codex (partial): The abstract supports the deep-learning text-to-SQL scope but does not establish a narrative methodology or the treatment of multi-turn interaction as a subtopic.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

### B5 · Liu2025SurveyLLMs — fuente leída: Resumen
- **Liu2025SurveyLLMs#2** (tablas/relacionados.tex): \cite{Liu2025SurveyLLMs} (2025) & Narrativa & Text-to-SQL con LLM & Subtema & No verificado & Resumen
  - Codex (partial): The abstract supports the LLM Text-to-SQL scope but does not establish a narrative methodology or coverage of multi-turn interaction as a subtopic.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

### B6 · Shi2026SurveyLLM — fuente leída: Resumen
- **Shi2026SurveyLLM#3** (tablas/relacionados.tex): \cite{Shi2026SurveyLLM} (2026) & Narrativa & Text-to-SQL con LLM & Subtema & No verificado & Resumen
  - Codex (partial): The abstract confirms the LLM-based Text-to-SQL scope but does not establish a narrative methodology or identify multiturn interaction as a subtopic.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

### B7 · Liu2026NLIDBReview — fuente leída: Texto completo (arXiv v2)
- **Liu2026NLIDBReview#1** (secciones/01-introduccion.tex): Las revisiones de 2026 que se declaran sistemáticas no analizan el escenario multiturno~\cite{Liu2026NLIDBReview,Bui2026Survey}.
  - Codex (cannot_judge): The title identifies a systematic review, but the abstract cannot establish whether the full paper analyzes multi-turn scenarios.
- **Liu2026NLIDBReview#2** (secciones/02-trabajos-relacionados.tex): Liu et al.~\cite{Liu2026NLIDBReview} revisan las NLIDB en general.
  - Codex (partial): The title refers broadly to natural language interfaces for databases, but the abstract describes a review specifically focused on Text-to-SQL.
- **Liu2026NLIDBReview#3** (secciones/05-discusion.tex): Entre las revisiones sistemáticas de 2026, la versión arXiv v2 de Liu et al.~\cite{Liu2026NLIDBReview} no documenta protocolo ni menciona SParC ni CoSQL.
  - Codex (cannot_judge): The supplied record does not include arXiv v2, so omissions of a protocol or dataset mentions cannot be verified.
- **Liu2026NLIDBReview#4** (tablas/relacionados.tex): \cite{Liu2026NLIDBReview} (2026) & Sistemática (declarada) & NLIDB general & No tratado & No documentado & Texto completo (arXiv v2)
  - Codex (partial): The title supports the declared systematic classification, but the abstract focuses on Text-to-SQL and cannot verify the multi-turn, protocol, or consulted-version descriptors.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

### B8 · Bui2026Survey — fuente leída: Texto completo (manuscrito)
- **Bui2026Survey#1** (secciones/01-introduccion.tex): Las revisiones de 2026 que se declaran sistemáticas no analizan el escenario multiturno~\cite{Liu2026NLIDBReview,Bui2026Survey}.
  - Codex (cannot_judge): The abstract identifies a systematic review but does not establish whether multi-turn scenarios are analyzed.
- **Bui2026Survey#2** (secciones/02-trabajos-relacionados.tex): Bui et al.~\cite{Bui2026Survey} sí documentan una búsqueda sistemática, con criterios de inclusión y exclusión, sobre Text-to-SQL con LLM y su seguridad.
  - Codex (partial): The abstract supports the systematic review designation and its focus on LLM-based Text-to-SQL security, but does not describe a search protocol or eligibility criteria.
- **Bui2026Survey#3** (secciones/05-discusion.tex): Bui et al.~\cite{Bui2026Survey} documentan una búsqueda sistemática, pero en el manuscrito leído el escenario multiturno aparece solo como categoría de \en{datasets}.
  - Codex (partial): The abstract supports the systematic review designation, but does not establish a documented search or that multi-turn scenarios appear only as a dataset category.
- **Bui2026Survey#4** (secciones/05-discusion.tex): Bui et al.~\cite{Bui2026Survey} también reportan arXiv como la fuente con más estudios.
  - Codex (cannot_judge): The supplied record provides no study counts or comparisons among literature sources.
- **Bui2026Survey#5** (tablas/relacionados.tex): \cite{Bui2026Survey} (2026) & Sistemática & Text-to-SQL con LLM y seguridad & Solo como categoría de \en{datasets} & Documentado & Texto completo (manuscrito)
  - Codex (partial): The abstract supports the systematic review designation and stated scope, but cannot verify the multi-turn classification, protocol documentation, or which text was read.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

### B9 · OrtizDelgado2026RAG — fuente leída: Resumen y registro OSF
- **OrtizDelgado2026RAG#1** (secciones/02-trabajos-relacionados.tex): Ortiz-Delgado et al.~\cite{OrtizDelgado2026RAG} presentan una revisión sistemática, con protocolo en OSF, sobre estrategias de generación aumentada por recuperación para Text-to-SQL; según su resumen y su registro, no trata el escenario multiturno.
  - Codex (partial): The abstract establishes the systematic review, its RAG Text-to-SQL scope, and its OSF protocol, but silence about multi-turn scenarios does not establish their exclusion.
- **OrtizDelgado2026RAG#2** (secciones/05-discusion.tex): Ortiz-Delgado et al.~\cite{OrtizDelgado2026RAG} no tratan el escenario multiturno, según su resumen y su registro.
  - Codex (cannot_judge): The supplied record does not mention multi-turn scenarios, but this omission is insufficient to determine whether the review addresses them.
- **OrtizDelgado2026RAG#3** (tablas/relacionados.tex): \cite{OrtizDelgado2026RAG} (2026) & Sistemática & Estrategias RAG para Text-to-SQL & No tratado & Documentado (OSF) & Resumen y registro OSF
  - Codex (partial): The record supports the year, systematic-review classification, RAG Text-to-SQL scope, and documented OSF protocol, but does not establish that multi-turn scenarios are untreated.

Decisión: OK (autora, 2026-10-14; confirmado contra la fuente leída)

---

## C · Informativa

- **OSF2026Protocolo** (OSF2026Protocolo#1, OSF2026Protocolo#2, OSF2026Protocolo#3): Registro OSF 2026-10-11 13:09 (commit 52b5042) y búsquedas oficiales confirmadas a las 17:08 (commit 970cde1); los conteos de prueba anteriores figuran como «previo al registro» en slr/busqueda/registro_busquedas.csv. La afirmación se sostiene con los registros del repositorio.
- Respaldadas sin observaciones: 28 oraciones (detalle en `bib/afirmaciones/runs/`).
