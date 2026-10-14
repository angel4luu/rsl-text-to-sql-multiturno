# Fase 0 — Análisis de brecha: revisiones existentes

Fecha de búsqueda exploratoria: 2026-10-11
Herramientas: Scopus (API), OpenAlex, DBLP (volcado 2026-09-01), arXiv, Consensus.
**Carácter:** exploratorio. Estas búsquedas NO forman parte del conteo PRISMA; solo justifican la necesidad de la RSL.

## Consultas usadas
| Fuente | Consulta | Resultados revisados |
|---|---|---|
| Scopus | `TITLE-ABS-KEY(("text-to-SQL" OR "text to SQL" OR NL2SQL OR "natural language interface* to database*" OR NLIDB) AND (survey OR review OR "systematic literature review" OR "systematic review")) AND PUBYEAR > 2018` | 25 primeros por relevancia |
| OpenAlex | revisiones de "text-to-SQL survey" (≥2019) y `(conversational OR multi-turn OR "context-dependent") AND ("text-to-SQL" OR "semantic parsing") AND (survey OR review)` | 30 + 25 |
| DBLP | títulos con survey/review + text-to-SQL/NL2SQL; survey + conversational/multi-turn/context-dependent | 21 + 20 |
| arXiv | survey/review en título + multi-turn/conversational + text-to-SQL en resumen (cs.CL, cs.DB, cs.AI) | 2 |
| Consensus | "survey of multi-turn conversational text-to-SQL context modeling" | 3 |

## Revisiones relevantes encontradas (verificadas por DOI/DBLP)

### A. Solapamiento directo con el alcance (Text-to-SQL conversacional)
| Revisión | Tipo | Observación |
|---|---|---|
| Yang et al. (2025). *Conversational Text-to-SQL: A Comprehensive Survey of Paradigms, Challenges, and Future Directions*. AREA@ECAI, CCIS. DOI 10.1007/978-3-032-08049-3_1 | Survey narrativo (taller) | **Mayor solapamiento.** Según su resumen (leído vía Mendeley, carpeta 9; sin PDF): cubre manejo de contexto (correferencia, elipsis), modelado del flujo semántico, generalización entre dominios, evolución de arquitecturas (encoder-decoder → *relation-aware transformers* → LLM/agentes) y una comparación cuantitativa en SParC y CoSQL. **No menciona** protocolo de búsqueda ni criterios de selección (no PRISMA/Kitchenham), ni vinculación de esquemas/rutas de *join*, ni retroalimentación de ejecución como ejes. **Pendiente:** PDF para confirmar método antes de redactar trabajos relacionados. |
| Li, Qu y Haffari (2020). *Context Dependent Semantic Parsing: A Survey*. COLING. DOI 10.18653/v1/2020.coling-main.226 | Survey narrativo | Pre-LLM; cubre análisis semántico dependiente del contexto en general (no solo SQL). |

### B. Revisiones amplias de Text-to-SQL / NLIDB (tratan lo multiturno como subtema)
| Revisión | Tipo |
|---|---|
| Liu et al. (2026). *A systematic review of natural language interfaces for databases*. Frontiers of Computer Science. DOI 10.1007/s11704-025-50592-w | Revisión sistemática, NLIDB en general |
| Bui et al. (2026). *A systematic survey of LLM-based text-to-SQL: methodologies, security vulnerabilities, and future challenges*. PeerJ Comput. Sci. DOI 10.7717/peerj-cs.3773 | Survey sistemático, enfoque en seguridad |
| Shi et al. (2025/2026). *A Survey on Employing Large Language Models for Text-to-SQL Tasks*. ACM Comput. Surv. DOI 10.1145/3737873 | Survey narrativo |
| Hong et al. (2025). *Next-Generation Database Interfaces: A Survey of LLM-based Text-to-SQL*. IEEE TKDE | Survey narrativo |
| Liu et al. (2025). *A Survey of Text-to-SQL in the Era of LLMs*. IEEE TKDE. DOI 10.1109/TKDE.2025.3592032 | Survey narrativo |
| Katsogiannis-Meimarakis y Koutrika (2023). *A survey on deep learning approaches for text-to-SQL*. VLDB J. | Survey narrativo |
| Deng, Chen y Zhang (2022). *Recent Advances in Text-to-SQL*. COLING | Survey narrativo |
| Abbas et al. (2022). *A Review of NLIDB with Deep Learning*. IEEE Access. DOI 10.1109/ACCESS.2022.3147586 | Revisión |
| Ortiz-Delgado et al. (2026). *Retrieval-Augmented Strategies for LLM-Based Text-to-SQL Systems: A Systematic Literature Review*. OSF. DOI 10.17605/osf.io/qgr2x | RSL (protocolo/materiales en OSF), centrada en RAG; no aborda el escenario multiturno. Hallada en la Fase 1.3 (pruebas de cadenas) |

## Conclusión preliminar (a confirmar tras leer Yang et al. 2025)
- Existen numerosos *surveys* generales de Text-to-SQL, pero **solo uno** se centra en el escenario conversacional (Yang et al., 2025), publicado en un taller y de acceso cerrado.
- **No se encontró ninguna revisión sistemática (PRISMA/Kitchenham)** dedicada a Text-to-SQL conversacional/multiturno, ni que analice conjuntamente: restauración de contexto, representación del estado (incl. grafos), vinculación de esquemas/rutas de *join* y retroalimentación de ejecución, junto con la degradación por turno.
- Brecha candidata: RSL reproducible sobre **anclaje de esquemas con estado en Text-to-SQL multiturno**, en la era LLM y pre-LLM (2019–2026).

## Verificación de las revisiones sistemáticas de 2026 (ronda 1 del Checkpoint 1, N1)
| Revisión | Fuente leída | Hallazgo |
|---|---|---|
| Liu et al. (2026), *A systematic review of natural language interfaces for databases* (Front. Comput. Sci.) | Versión arXiv v2 (2503.02435, «NLI4DB»), texto completo, búsqueda por términos | **Sin protocolo de búsqueda documentado ni diagrama PRISMA** pese al título. **No menciona SParC ni CoSQL**; «multi-turn» aparece solo en el título de una referencia; no trata autocorrección; *schema linking* solo como preprocesamiento (IRNet). Taxonomía: preprocesamiento → comprensión (reglas / aprendizaje automático / híbrido) → traducción. *Limitación: la versión publicada en la revista podría diferir de la v2 de arXiv.* |
| Bui et al. (2026), *A systematic survey of LLM-based text-to-SQL…* (PeerJ CS) | Texto completo (PDF adjuntado por la autora en Mendeley; es la versión de manuscrito en revisión, «Manuscript to be reviewed») | **Sí es sistemática:** búsqueda automatizada en ACM DL, arXiv, IEEE Xplore, ACL Anthology, ScienceDirect y Springer + búsqueda manual en Google Scholar; criterios de inclusión/exclusión; umbral de calidad 6,5; **187 estudios** (arXiv 105, ACL 61). Preguntas: RQ1 estado de Text-to-SQL con LLM y evaluación; RQ2 riesgos de seguridad y mitigaciones. Taxonomía de técnicas que incluye *Schema Linking & Pruning* y *Query Repair and Refinement* (un turno). **Lo multiturno aparece solo como categoría de *datasets*** (descripción de SParC y CoSQL); cita CoE-SQL en su tabla de métodos, pero **no analiza** restauración del contexto, estado del diálogo ni degradación por turno. No se encontró período de búsqueda explícito en el texto extraído. |
| Yang et al. (2025) | Solo resumen | Pendiente de texto completo |

**Repetición de la búsqueda exploratoria de revisiones con términos v4** (*multi-round*, *dialogue state tracking*): pendiente junto con los conteos por base.

## Volumen estimado de literatura (OpenAlex, campo resumen, 2019–2026)
Cotas inferiores orientativas (OpenAlex no indexa todos los resúmenes); las búsquedas oficiales en 5 bases + arXiv darán más registros (con duplicados).

| Conjunto | Consulta (resumen) | Registros |
|---|---|---|
| Todo Text-to-SQL / NLIDB | `"text-to-SQL" OR "text to SQL" OR "NL2SQL" OR "natural language interface to database"` | ≈ 2015 |
| Multiturno / conversacional | anterior AND (`"multi-turn" OR "conversational" OR "context-dependent" OR "SParC" OR "CoSQL"`) | ≈ 176 (≈ 9 %) |
| Pilares 3–4 (uno o varios turnos) | anterior AND (`"schema linking" OR "self-correction" OR "execution feedback" OR "join path" OR "self-refinement" OR "error correction"`) | ≈ 301 |

## Fase 0b — Carpetas antiguas de Mendeley (solo lectura)
- `ts` (26 docs), `ts slr/{scopus, acm dl, sd, others}` (≈30 docs), `slr to justify ts` (vacía).
- Enfoque predominante: **BI + IA generativa + Text-to-SQL de un solo turno / agentes**, más amplio que el alcance actual. Útiles como antecedentes de tesis, no como estudios semilla multiturno.
- Posibles semillas o candidatos relevantes: Urban et al. (2025) *Utilizing Past User Feedback for More Accurate Text-to-SQL* (usa historial de traducciones); Li y Jobson (2024) *LLMs as an Interactive Database Interface*; SQLFixAgent (Cen et al., 2025), MAGIC (Askari et al., 2024), MAG-SQL (Xie et al., 2024) para el pilar de autocorrección / *schema linking* (de un solo turno: decidir en criterios de elegibilidad).
- Revisiones para carpeta 9: Shi et al. (ACM CSUR), además de las listadas arriba.
- Los estudios semilla del *blueprint* (Chen 2021, Jain y Lapata 2023, Liao 2021, Tummalapenta y Addanki 2026, etc.) **no están en Mendeley**: se localizarán y verificarán en la Fase 1.
