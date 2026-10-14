
##### Revisión final de la extracción (casos no obvios y muestras)
###### Qué escribir en Decisión: (por sección)
| Sección | Tipo de ítem | Opciones válidas | Ejemplo |
| ------ | ------ | ------ | ------ |
| **A** | campo | A · B (acepta ese valor) · el valor correcto con los códigos de la tabla de abajo · NR (no reportado) | B · REESCRITURA; CONCATENACION |
| **A** | calidad CQn | A · B · 1 · 0.5 · 0 | 0.5 |
| **A** | contraste | OK (la fila es correcta) · NO (descartar la fila) · valores corregidos con X / sin Y | con 52.1 / sin 48.3 |
| **B** | cada ítem de validez CQ2, CQ4–CQ7 | OK (acepta la puntuación mostrada) · 1 · 0.5 · 0 | OK |
| **C** | valor concordante | OK · el valor correcto (códigos de la tabla de abajo) | OK |
| **D** | estudio del Nivel 1 | OK (todo correcto) · solo los campos a corregir como campo=valor, separados por ; | paradigma_principal=LLM_PROMPTING; pi4_mecanismo=NR |

Listas de varios códigos: sepárelos con ;. Páginas = páginas del PDF. Calidad: 1 = sí/completo · 0,5 = parcial · 0 = no (descriptores completos en ../calidad/checklist_calidad.md).
###### Códigos de los campos que aparecen en esta hoja (del formulario)
| Campo | Vocabulario |
| ------ | ------ |
| codigo_disponible | SI · NO · PARCIAL |
| contaminacion_discutida | SI · NO |
| coste_reportado | TOKENS · LATENCIA · MONETARIO · NINGUNO (;) |
| degradacion_reportada | SI · NO |
| errores_join_reportados | SI · NO |
| escenario | MULTITURNO · UN_TURNO (definición revisada; caso B6) |
| etiquetas | INTERACTIVO (B1) · USA_HISTORIAL (B2) · COMPONENTE (B3) · RONDAS_INTERNAS (B6) · ninguna |
| fecha_modelo | Versión/fecha del modelo si se reporta (p. ej., gpt-4o-2024-05-13), si no NR |
| historial_eval | GOLD · PREDICHO · SOLO_PREGUNTAS · NR (definición en el bloque 5b) |
| idioma_dataset | EN · ZH · ES · OTRO (;) |
| modelos_base | Normalizado (p. ej., GPT-4o; T5-3B) |
| paradigma_principal | **Un solo código**, con precedencia: AGENTES > HIBRIDO_NEUROSIMBOLICO > LLM_FINETUNING > LLM_PROMPTING > PLM_FINETUNING > NEURONAL_PRE_PLM > REGLAS_SIMBOLICO (se asigna el primero que aplique) |
| paradigmas_secundarios | Los demás que apliquen (;) |
| pi1_insumos_historial | PREGUNTAS_PREVIAS · SQL_PREVIOS · RESPUESTAS_SISTEMA · RESULTADOS_EJECUCION (;) |
| pi1_tecnica | CONCATENACION · REESCRITURA · RESOLUCION_EXPLICITA · CLASIFICACION_DISCURSO · OTRA:<descripción> (;) |
| pi2_actualizacion | IMPLICITA_NEURONAL · REGLAS_DETERMINISTAS · LLM_GENERATIVA · NR |
| pi2_coste_contexto | CRECE_CON_TURNOS · ACOTADO · NR |
| pi2_grafo_dinamico | SI (cambia por turno) · NO · NA |
| pi2_grafo_nodos | Si GRAFO: qué representan los nodos (ELEMENTOS_ESQUEMA · TOKENS_PREGUNTA · TURNOS · OTROS:<descripción>; ;); si no NA |
| pi2_representacion | HISTORIAL_PLANO · VENTANA_DESLIZANTE · RESUMEN · SQL_PREVIO_EDICION · ARBOL_AST · GRAFO · MEMORIA_EXTERNA · ESTRUCTURA_EXPLICITA · OTRA:<descripción> (;) |
| pi3_algoritmo | Si algorítmica (p. ej., STEINER; DIJKSTRA), si no NA *(Nivel 2)* |
| pi3_escala_esquema | Máximo de tablas/columnas evaluado *(Nivel 2)* |
| pi3_inferencia_joins | IMPLICITA_MODELO · ALGORITMICA_CAMINOS · GRAFO_FK_RESTRICCIONES · NR |
| pi3_metricas_linking | Recall/precisión de *linking* *(Nivel 2)* |
| pi3_tecnica_linking | COINCIDENCIA_CADENAS · EMBEDDINGS_RECUPERACION · CLASIFICADOR_ENTRENADO · LLM_PROMPTING · GRAFO_ESQUEMA · PODA_ESQUEMA · NINGUNA_EXPLICITA (;) |
| pi4_aplicado_multiturno | SI · NO |
| pi4_mecanismo | EJECUCION_FEEDBACK_ERRORES · AUTODEPURACION_LLM · AUTOCONSISTENCIA_VOTACION · VERIFICADOR_CRITICO · REPARACION_SIMBOLICA · ACLARACION_USUARIO · ABSTENCION (;) |
| pi4_rondas_max | Número o NR *(Nivel 2)* |
| pi4_senal | ERROR_DBMS · RESULTADO_VACIO · RESULTADO_EJECUCION · JUICIO_LLM · USUARIO (;) |
| pilares_centrales | PI declarados como contribución central (PI1…PI4; ;) |
| pilares_contenidos | PI presentes solo como componente (;) — para el indicador D4 laxo |
| requiere_entrenamiento | SI · NO (*training-free*) · PARCIAL |
| tipo_contribucion | TECNICA · BENCHMARK · ESTUDIO_EMPIRICO (;) |

---

###### A. No decididos por el desempate (29)
*   **R00029**   — campo calidad_nota: A: Fig. 2 y Tabla 3 (apéndice E) no ofrecen valores numéricos en el texto extraído; los apéndices fueron omitidos. (None) · B: None (None)
    *   **Decisión:**  A
*   **R00035**   — campo codigo_disponible: A: NO (pp.1-7: no hay enlace ni declaración de liberación. Las páginas 20-31 (prompts y apéndice D) no se leyeron completas) · B: NR (pp. 1–33, sin declaración de disponibilidad de código)
    *   **Decisión:**  B
*   **R00042**   — campo pi4_aplicado_multiturno: A: NO (p.7 §3.2 ("without employing any SQL post-processing")) · B: SI (p. 8, Effect of Schema-aware Context Extractor)
    *   **Decisión:**  A
*   **R00074**   — campo codigo_disponible: A: NO (No code or repository link anywhere in the text) · B: NR (pp. 1–12; no se declara disponibilidad del código de TP-Link)
    *   **Decisión:**  B
*   **R00079**   — campo codigo_disponible: A: PARCIAL (p.2 §1 (the dataset is made public; code release is not stated in the main text)) · B: NR (p. 2, se anuncia publicación del dataset, sin indicar disponibilidad del código)
    *   **Decisión:**  A
*   **R00097**   — campo codigo_disponible: A: NO (No code link in the main text; appendix not available) · B: NR (pp. 1–9, no se declara disponibilidad en el texto suministrado)
    *   **Decisión:**  B
*   **R00099**   — campo pi3_escala_esquema: A: 8 domains in MultiWOZ; all domains' SQL tables concatenated in the prompt (5 domains in zero-shot evaluation) (p.5 §3.1; p.4 §2.2) · B: NR (pp. 4–5, §§2.2 y 3.1: no se informa el máximo de tablas y columnas evaluado)
    *   **Decisión:**  B
*   **R00107**   — calidad CQ8: A: 0 — No code or data availability statement in the text; rewrite annotations not stated as released. · B: 0.5 — Utiliza datasets públicos; no declara disponibilidad del código ni de las nuevas anotaciones de reescritura.
    *   **Decisión:**  B
*   **R00117**   — campo pi2_coste_contexto: A: NR (NA) · B: CRECE_CON_TURNOS (pp. 3 y 5, secciones 3 y 4.3; historial de preguntas y atención entre turnos)
    *   **Decisión:**  B
*   **R00238**   — campo requiere_entrenamiento: A: PARCIAL (p.2 §3.1 (ML scoring model for logical forms; training not described)) · B: NR (p. 2, §3.1, se menciona un modelo de aprendizaje automático sin describir su entrenamiento)
    *   **Decisión:**  A
*   **R00238**   — campo pi3_escala_esquema: A: NR (Spider databases, no sizes) (p.3 §4) · B: NR (p. 3, §4, diez bases de Spider sin máximos de tablas o columnas)
    *   **Decisión:**  OK
*   **R00288**   — campo paradigma_principal: A: NR (p.7 §5.1; los detalles de implementación están en el Apéndice A, que no está en el texto; no se indica si los modelos de referencia usan PLM) · B: NEURONAL_PRE_PLM (pp. 2–3, §2; p. 8, §5.2; no se identifican modelos preentrenados en el texto disponible)
    *   **Decisión:**  B
*   **R00288**   — campo pi3_escala_esquema: A: 201 BD; 813 tablas (p.3 §3.2; Table 2) · B: NR (p. 3, §3.2; p. 6, tabla 2: 201 bases y 813 tablas en total, sin máximo por esquema ni número de columnas)
    *   **Decisión:**  B
*   **R00309**   — calidad CQ9: A: 0.5 — The discussion covers small dataset size and the lack of golden SQL, but no broader threats to validity. · B: 1 — Discute explícitamente tamaño reducido, ausencia de SQL de referencia y dificultades de evaluación y ampliación.
    *   **Decisión:**  B
*   **R00370**   — campo pi3_escala_esquema: A: NR (p.6 §4.2.1 (schema size not stated in main text; demo MIMIC-IV and eICU with renamed schemas)) · B: MIMIC-IV⋆: 17 tablas; eICU⋆: 11 tablas; máximo de columnas NR (pp. 30–31, tablas 12–13; p. 34, listado de tablas)
    *   **Decisión:**  B
*   **R00373**   — campo fecha_modelo: A: claude-3-7-sonnet-20250219; claude-sonnet-4-20250514; o3-mini-2025-01-31; deepseek-chat-v3.1; Qwen3-Coder-480B-A35B; gemini-2-5-pro; gpt-5 (sin fecha) (p.30 App. I.2) · B: gpt-5;claude-3-7-sonnet-20250219;deepseek-chat-v3.1;Qwen3-Coder-480B-A35B;claude-sonnet-4-20250514;o3-mini-2025-01-31;gemini-2-5-pro;deepseek-chat;deepseek-r1;gemini-2-0-flash-001;gpt-4o-2024-11-20;Qwen3-235B-A22B-Instruct-2507 (p. 30, apéndice I.2; p. 38, apéndice O.2)
    *   **Decisión:**  B
*   **R00373**   — campo pi4_rondas_max: A: 1 depuración por subtarea (c-Interact); aclaraciones = m_amb + paciencia (0,3,5,7) (p.5-6 §4.1; p.30 App. I.3) · B: NR (pp. 5–6, §4: c-Interact permite una revisión por subtarea; a-Interact usa presupuesto adaptativo B=6+2mamb+2λpat)
    *   **Decisión:**  A
*   **R00373**   — contraste fila 27: AUTOCORRECCION · OTRO:BIRD-INTERACT OTRA:SR: con 32.00 / sin 29.00 (p. 35, tabla 10, Overall; sin calculado restando ganancia impresa de 3.00) — ¿correcto?
    *   **Decisión:**  OK
*   **R00373**   — contraste fila 28: AUTOCORRECCION · OTRO:BIRD-INTERACT OTRA:SR: con 15.67 / sin 11.67 (p. 35, tabla 10, Overall; sin calculado restando ganancia impresa de 4.00) — ¿correcto?
    *   **Decisión:**  OK
*   **R00373**   — contraste fila 29: AUTOCORRECCION · OTRO:BIRD-INTERACT OTRA:SR: con 32.33 / sin 27.33 (p. 35, tabla 10, Overall; sin calculado restando ganancia impresa de 5.00) — ¿correcto?
    *   **Decisión:**  OK
*   **R00373**   — contraste fila 30: AUTOCORRECCION · OTRO:BIRD-INTERACT OTRA:SR: con 20.67 / sin 18.67 (p. 35, tabla 10, Overall; sin calculado restando ganancia impresa de 2.00) — ¿correcto?
    *   **Decisión:**  OK
*   **R00373**   — contraste fila 31: AUTOCORRECCION · OTRO:BIRD-INTERACT OTRA:SR: con 36.00 / sin 29.00 (p. 35, tabla 10, Overall; sin calculado restando ganancia impresa de 7.00) — ¿correcto?
    *   **Decisión:**  OK
*   **R00373**   — contraste fila 32: AUTOCORRECCION · OTRO:BIRD-INTERACT OTRA:SR: con 20.00 / sin 18.67 (p. 35, tabla 10, Overall; sin calculado restando ganancia impresa de 1.33) — ¿correcto?
    *   **Decisión:**  OK
*   **R00373**   — contraste fila 33: AUTOCORRECCION · OTRO:BIRD-INTERACT OTRA:SR: con 37.33 / sin 35.00 (p. 35, tabla 10, Overall; sin calculado restando ganancia impresa de 2.33) — ¿correcto?
    *   **Decisión:**  OK
*   **R00453**   — campo pi3_escala_esquema: A: Up to 2281 tables / 65000 columns (MS-Commercial, Table 1); the evaluated SRD production set has 148 tables / 25258 columns; views average up to 219 columns (p.2 Table 1; p.9 Sec. 8.1.1) · B: Evaluación E2E de producción: 148 tablas y 25258 columnas; evaluación específica de linking: hasta 52 vistas y 11388 columnas, con media de 219 columnas por vista. No se informa el máximo de columnas de una vista individual. (p. 2, tabla 1; p. 9, §8.1.1; p. 12, §8.3.3)
    *   **Decisión:**  B
*   **R00453**   — campo historial_eval: A: NR (p.9-14 (the study does not say whether previous-turn IRs are gold or predicted; Table 12 uses oracle schema linking and routing labels)) · B: GOLD (p. 7, §6; p. 14, §8.4.3: edición de la IR golden anterior)
    *   **Decisión:**  B
*   **R00499**   — campo pi3_inferencia_joins: A: NR (NR) · B: IMPLICITA_MODELO (p. 19, tabla 8; p. 23, tabla 12)
    *   **Decisión:**  B
*   **R00499**   — campo contaminacion_discutida: A: NO (p.9 RQ4 (solo se afirma que la memoria de guía no tiene fuga de test; no se discute contaminación de BIRD en los LLM)) · B: SI (p. 9, RQ4; pp. 17–19, apéndices C y F)
    *   **Decisión:**  B
*   **R00950**   — calidad CQ10: A: 1 — Published in a peer-reviewed LNCS volume (Scopus-indexed), also on arXiv. · B: 0.5 — El texto suministrado se identifica como arXiv; no contiene evidencia del foro revisado por pares indicado externamente.
    *   **Decisión:**  A

---

###### B. Estudios cerca del umbral de validez, 40–60 % (19)
Umbral: ≥ 50 % entra a la síntesis en profundidad. Revise los 5 ítems de validez.
###### R00029 — SPENCE: A Syntactic Probe for Detecting Contamination in NL2SQL Benchmarks — validez 60 %
*  CQ2:   **0.5**   — Pipeline y modelos descritos, pero sin prompts, umbral de coseno ni versiones de modelo en el texto principal.   *(p. pp.4-5 §2.2, §2.4)*    ·   **Decisión:**  OK
*  CQ4:   **0.0**   — Los seis LLM son los modelos evaluados, no líneas base; no se compara con otros métodos de detección de contaminación.   *(p. pp.4-5 §2.4)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — Se usa exactitud de ejecución, pero no se define el historial gold/predicho en los multiturno ni QM/IM.   *(p. p.4 §2.1; p.10 §7)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Controles sistemáticos: longitud, solapamiento léxico, schema linking, generador de paráfrasis, temperatura, validación humana.   *(p. pp.7-9 §5; p.5 §2.5)*    ·   **Decisión:**  OK
*  CQ7:   **1.0**   — Seis LLM, cuatro benchmarks, bootstrap con IC, otro generador y T=0.   *(p. p.6 §4; p.9 §5)*    ·   **Decisión:**  OK

###### R00068 — ABACUS-SQL: A Text-to-SQL System Empowering Cross-Domain and Open-Domain Database Retrieva — validez 60 %
*  CQ2:   **0.5**   — Components described; prompts and details in appendices (not available); no hyperparameters beyond 3-shot, temp 0   *(p. p.3-6 §3, §5.1)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Only the unaugmented Qwen2.5-Coder baseline; no competing multi-turn methods compared   *(p. p.5 Table 2)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — QEX/IEX defined; type of history (gold vs predicted) not stated   *(p. p.6 §5.1)*    ·   **Decisión:**  OK
*  CQ6:   **0.5**   — Ablation of Pre-SQL and self-debug only mentioned briefly; numbers in Appendix D   *(p. p.6 §5.2)*    ·   **Decisión:**  OK
*  CQ7:   **1.0**   — Three datasets and two model sizes; single run, no variance   *(p. p.5 Table 2)*    ·   **Decisión:**  OK

###### R00114 — AirConcierge: Generating task-oriented dialogue via efficient large-scale knowledge retrie — validez 50 %
*  CQ2:   **0.5**   — Equations and hyperparameters given, but no code and few details on SQL labels and value handling.   *(p. p.3-6 §3-4.2)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Only the 2018 AirDialogue supervised and RL baselines; different model architectures.   *(p. p.7 Table 1)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — Acc_lf, Acc_ex and BLEU defined; self-play used but gold vs predicted history not explicitly discussed.   *(p. p.6-7 §4.3)*    ·   **Decisión:**  OK
*  CQ6:   **0.5**   — Sin ablación de componentes; solo desglose de exactitud por slot (Tabla 3) y breve explicación.   *(p. p.7-8 §4.4, Tabla 3)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Dev y conjunto sintetizado, variaciones de KB; sin semillas, varianza ni significancia.   *(p. p.7 Tabla 1; p.8 §4.5)*    ·   **Decisión:**  OK

###### R00123 — Speak to your parser: Interactive text-to-SQL with natural language feedback — validez 60 %
*  CQ2:   **0.5**   — Dataset construction is detailed. Model hyperparameters are left to defaults and prompts or appendix are not in the text.   *(p. p.3-4 Sec.3; p.8 fn.8)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Baselines are the authors' own adaptations of Seq2Struct and EditSQL. There is no same-base-model no-feedback comparison.   *(p. p.8-9 Sec.6.1; Table 4)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — Exact set match defined and mispredicted-parse history stated, but no EX/TS/QM/IM metrics and no gold-vs-predicted comparison.   *(p. p.2 Sec.2; p.8 Sec.6)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Quantified edit-distance and feedback-type error analyses, shuffled-feedback test, and baselines compared with and without feedback.   *(p. p.5 Sec.4; p.9 Sec.6.3)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Several models and a second error source (EditSQL errors) are evaluated, but single runs with no variance or significance reported.   *(p. p.9 Sec.6.3)*    ·   **Decisión:**  OK

###### R00148 — Utilizing Past User Feedback for More Accurate Text-to-SQL — validez 60 %
*  CQ2:   **0.5**   — Pipeline descrito, pero sin prompts completos, hiperparámetros, número de ejemplos ni versiones de modelo; código no disponible.   *(p. p.2-6 §2-3)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Líneas base con el mismo modelo, pero débiles: sin feedback, few-shot fijo, historial ingenuo. No hay comparación con otros sistemas.   *(p. Tabla 1, p.4)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — EX definida; el historial son SQL generados y aceptados, pero no se nombra gold/predicho ni hay métricas multiturno.   *(p. p.5)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Comparación sistemática de métodos de extracción, sus combinaciones y la robustez ante errores del usuario.   *(p. Tablas 1-2, p.4-6; §3.3-3.5)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Tres datasets y dos modelos, pero una sola ejecución, sin varianza ni significancia.   *(p. p.4-6)*    ·   **Decisión:**  OK

###### R00170 — ASTormer++: A Study on a Chinese Medical Text-to-SQL Model Integrating Conceptual Understa — validez 60 %
*  CQ2:   **0.5**   — Hay tabla de hiperparámetros, pero faltan detalles de Prefix Tuning y RGAT, y no hay código.   *(p. p.4-7 §2.3, §3.2, Tabla 2)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Solo se compara con líneas base de 2021-2022 con valores publicados; solo ASTormer-Chinese comparte modelo base.   *(p. p.7 Tabla 3; p.8 Tabla 4)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — Se reportan EM y EXEC, pero no se declara el tipo de historial (gold o predicho) en CHASE.   *(p. p.6 §3.2.3; p.8 Tabla 4-5)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Ablación por módulo (Tabla 6) y análisis de errores por cláusula y de ejecución.   *(p. p.9 Tabla 6; p.11-12 §3.7)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Dos datasets y varias longitudes, pero una sola ejecución de exactitud; sin semillas ni significancia.   *(p. p. 6 §3.1; p. 8 Tabla 4; pp. 10-11)*    ·   **Decisión:**  OK

###### R00222 — SiriusBI: A Comprehensive LLM-Powered Solution for Data Analytics in Business Intelligence — validez 60 %
*  CQ2:   **0.5**   — Fine-tuning hyperparameters and base models given; prompts, thresholds, model versions and some module details missing from paper.   *(p. p.8-10 Sec.3.4, 4.1.3)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — MRD-SQL shares the base model, but DIN-SQL and MAC-SQL use GPT-4o and are older.   *(p. p.10)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — EX, VES, UEX defined; gold vs predicted history is not specified.   *(p. p.9-10 Sec.4.1.2)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Ablations of MRD-Q, intention querying, knowledge management and table selection.   *(p. p.11 Tables 3-5)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Several datasets and variants, but single runs with no variance or significance; only Data Insight repeated three times.   *(p. p.11)*    ·   **Decisión:**  OK

###### R00232 — A natural language and interactive end-to-end querying and reporting system — validez 40 %
*  CQ2:   **0.5**   — Architecture described, but classifier hyperparameters, data-generation details and baseline setup missing.   *(p. p.3-4 §3)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Compared to older seq2seq, SQLNet and SyntaxSQLNet on own data, with details missing.   *(p. p.5 §4)*    ·   **Decisión:**  OK
*  CQ5:   **0.0**   — Accuracy is undefined and the history type is not reported.   *(p. p.5-6 §4, §5.1)*    ·   **Decisión:**  OK
*  CQ6:   **0.5**   — Brief qualitative error analysis of baselines; no ablation of components.   *(p. p.5 §4)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Two company datasets and baselines compared, but single run with no variance or significance reported.   *(p. p.5)*    ·   **Decisión:**  OK

###### R00292 — A comprehensive evaluation of ChatGPT's zero-shot Text-to-SQL capability — validez 60 %
*  CQ2:   **0.5**   — Se muestra el prompt, pero no la versión de ChatGPT ni los hiperparámetros o la fecha de consulta.   *(p. p.2 Method, Fig.1)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Compara con PICARD, RASAT y RESDSQL, que usan otro modelo base (T5-3B). No hay línea base con el mismo modelo.   *(p. p.3 Baselines, Tables 1-4)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — Define VA, EX y TS, pero no QM/IM ni declara explícitamente si el historial es gold o predicho; solo se infiere de la figura.   *(p. p.2 Fig.1; p.3 Evaluation Metrics)*    ·   **Decisión:**  OK
*  CQ6:   **0.5**   — No hay ablación. Solo un case study cualitativo breve con cuatro errores de Spider.   *(p. p.5 §3.3, Table 6)*    ·   **Decisión:**  OK
*  CQ7:   **1.0**   — Evalúa 12 datasets, incluyendo variantes de robustez y perturbaciones adversariales; el criterio admite varios datasets, aunque hay un solo modelo y una sola ejecución.   *(p. pp.3-5 Tablas 1-5)*    ·   **Decisión:**  OK

###### R00309 — ChatBI: Towards Natural Language to Complex Business Intelligence SQL — validez 50 %
*  CQ2:   **0.5**   — Pipeline described, but the JSON prompts, ERNIE hyperparameters, training details and the Erniebot version are missing.   *(p. p.4-8)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — DIN-SQL and MAC-SQL are competitive, but they run on GPT-4 while ChatBI runs on Erniebot-4.0, so the base models differ.   *(p. p. 9, §6.2)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — UEX is defined and the previous-question prompts are described, but there is no EX/EM/TS and gold vs predicted history is not named.   *(p. p.8 s6.1; p.10 s6.3)*    ·   **Decisión:**  OK
*  CQ6:   **0.5**   — Ablates the phased process flow and zero-shot vs few-shot; MRD matching is not ablated. View selection is compared across models only.   *(p. pp. 9-10, Tables 4-6; p. 7, Table 2)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Two proprietary datasets (SRD and MRD) of 153 queries each, a single run, no variance or significance.   *(p. p.8-10)*    ·   **Decisión:**  OK

###### R00450 — StocksTalk: A Voice-Enabled Conversational Agent for Structured Query Generation over Web — validez 40 %
*  CQ2:   **0.5**   — Architecture and metrics described; prompts, retrieval/KB details, constrained decoding, model version and hyperparameters missing.   *(p. p.3-4 §3; p.4 §4.1-4.3)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Baselines are only GPT-4o ablations of own pipeline; no external text-to-SQL systems compared.   *(p. p.4 §4.2; p.5 Table 1)*    ·   **Decisión:**  OK
*  CQ5:   **0.0**   — EX mide ejecutabilidad, no equivalencia de resultados; no hay EM/TS/QM/IM estándar ni se especifica historial gold o predicho.   *(p. p.4 §4.3; p.5 Tablas 1-2)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Component ablation (Table 3), HITL breakdown by category (Table 4), and a clean-vs-noisy comparison (Table 2).   *(p. p.5 Tables 2-4)*    ·   **Decisión:**  OK
*  CQ7:   **0.0**   — Un dataset propio, un modelo base (GPT-4o), sin repeticiones, semillas ni significancia; solo desviación del latencia y condiciones limpia/ruidosa.   *(p. p.4 §4.1; p.5 Tabla 2)*    ·   **Decisión:**  OK

###### R00524 — Evaluating and Enhancing LLMs for Multi-turn Text-to-SQL with Multiple Question Types — validez 60 %
*  CQ2:   **0.5**   — Agents and benchmark construction described; prompts, model versions and Selector threshold missing.   *(p. p.3-4 III.B; p.15-16 IV; p.18 App. A)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Baselines are the same LLMs without the framework; no competing methods such as MAC-SQL are compared.   *(p. p.16 Table VI, V-A)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — EX, EM, TDEX, IEX and RQS defined; gold or predicted history not stated.   *(p. p.12 III.C)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Component ablation on Gemini-1.5 Flash (Table VII) plus per-question-type analysis.   *(p. p.17 Table VII; p.13-14 Table V)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Eight LLMs evaluated and three base models tested, but greedy single run with no variance or significance.   *(p. p.16 Table VI; p.18 App. A)*    ·   **Decisión:**  OK

###### R00904 — ARE SQL for improving semantic alignment in Chinese multi round text to SQL parsing — validez 50 %
*  CQ2:   **0.5**   — Optimizer, learning rates and dimensions given; Ernie version, Algorithm 1 details and code missing   *(p. p.11-15 §3.4, §4.2)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Compared with RATSQL, EditSQL and IGSQL: older baselines, base model equivalence not stated   *(p. p.15 §5 Table 1; Abstract)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — QM and IM defined; gold vs predicted history type not reported   *(p. p.15 §4.3)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Section 5 uses Table 1 to compare each module added separately and both together, which is a module-wise ablation.   *(p. p.15 §5)*    ·   **Decisión:**  OK
*  CQ7:   **0.0**   — Single dataset, no multiple runs, variance or significance reported   *(p. p.17 §6)*    ·   **Decisión:**  OK

###### R00908 — FISQL: Enhancing Text-to-SQL Systems with Rich Interactive Feedback — validez 60 %
*  CQ2:   **0.5**   — Describe el pipeline y esbozos de prompts, pero faltan las demostraciones, el número de ejemplos y los hiperparámetros.   *(p. p.3-5 §3.3, Fig.5-6)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Solo se compara con Query Rewrite (línea base propia y simple), sin sistemas interactivos competitivos.   *(p. p.5 §4.1; p.6 Tabla 2)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — Define una métrica propia (% corregidas), no EX/EM/TS. Solo implícito que el historial es el SQL predicho.   *(p. p.5 §4.1 Baselines and Metrics)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Ablación del enrutamiento y del resaltado, más análisis de errores restantes en tres categorías.   *(p. p.6 §4.2, Tablas 2-3)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Dos datasets pequeños, un solo modelo, una ejecución; sin varianza ni significancia.   *(p. p.5-6)*    ·   **Decisión:**  OK

###### R00924 — DIR: A Large-Scale Dialogue Rewrite Dataset for Cross-Domain Conversational Text-to-SQL — validez 60 %
*  CQ2:   **0.5**   — Annotation process and checks described; annotator numbers, agreement and RAT-SQL/RUN hyperparameters missing.   *(p. p.4-6 §4; p.8-9 §5-6)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Same-model Concat/Seq2Seq/RUN baselines, but STAR (67.4), cited on p.3, is absent from the comparison tables.   *(p. p.10)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — QEM and QEX defined; the history type used in evaluation (gold vs predicted) is not stated explicitly.   *(p. p.9)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Error-type analysis, accumulation-rate analysis and comparison of rewrite models/components.   *(p. p.8 Fig.4; p.10 Fig.5, Tab.5)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Two datasets and several rewriters, but single runs with no variance or significance testing.   *(p. p.10)*    ·   **Decisión:**  OK

###### R00927 — Advancing Conversational Text-to-SQL: Context Strategies and Model Integration with Large — validez 60 %
*  CQ2:   **0.5**   — Hiperparámetros, semilla, prompts GQR y alpha dados; faltan versiones de GPT-4 Turbo y Claude 3 Opus.   *(p. p.5-7)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Baselines GPT-4 Turbo, Claude 3, RASAT+PICARD and STAR use different base models and are partly old; none matches CodeS-7b.   *(p. p.8 Table 2)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — EXE, ESM and ETM at question and interaction level are reported, but whether gold or predicted history is used is not stated.   *(p. p.2 §1; p.4 §2.3; p.8 Table 2)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Compares full history, GQR and merged models and Spider/BIRD pre-tuning, plus a manual analysis of 50 GQR errors.   *(p. p.7-9 §4, §5.1)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Dos datasets y varios modelos, pero una sola semilla (42), sin varianza ni pruebas de significancia.   *(p. p.5; p.8)*    ·   **Decisión:**  OK

###### R00950 — QURG: Question Rewriting Guided Context-Dependent Text-to-SQL Semantic Parsing — validez 60 %
*  CQ2:   **0.5**   — Architecture, layers, hyperparameters and ELECTRA/T5-base given. No ELECTRA version, QR details are in appendix, no code.   *(p. p.4-6 §4-5.1)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Compares with SCoRE, RAT-SQL-TC, HIE-SQL, DELTA and PICARD, but not with the same base model. Authors call results only 'comparable'.   *(p. p.6 §5.2)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — QM and IM are defined, but gold versus predicted history is not stated.   *(p. p. 6)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Ablations on rewriting matrix and encoder, Only/Concat comparison, turn-level and difficulty analysis, case study.   *(p. p.6-7 §5.3-5.4; Fig 5)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Two datasets, one PLM backbone, no seeds, variance or significance tests reported.   *(p. p. 6)*    ·   **Decisión:**  OK

###### R00954 — An Intelligent Natural Language Interface for Querying Databases based on Deep Learning — validez 60 %
*  CQ2:   **0.5**   — Modules, slots and an example LLM input are described, but the LLM, versions, hyperparameters and training details are missing.   *(p. p.12-14)*    ·   **Decisión:**  OK
*  CQ4:   **0.5**   — Baselines are old (SQLNet) or zero-shot GPT-4; RAT-SQL/Seq2SQL not in the main table; base model of Chat-SQL unknown.   *(p. p.17 Table 6)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — EM, EX and turn accuracy defined; gold vs predicted history not stated.   *(p. p.16 Table 5)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — Ablation of sketch planner, dialogue memory and LLM slot filler.   *(p. p.18 Table 8)*    ·   **Decisión:**  OK
*  CQ7:   **0.5**   — Evaluated on three datasets (Spider, SParC, WikiSQL), but no seeds, variance or significance are reported.   *(p. p.15, p.17)*    ·   **Decisión:**  OK

###### R00994 — Pay More Attention to History: A Context Modelling Strategy for Conversational Text-to-SQL — validez 60 %
*  CQ2:   **0.5**   — Losses, alpha/beta and task types are given, but hyperparameters are deferred to and the 17/11 operation types are not listed.   *(p. p.2-4 Sec.4, 5.2)*    ·   **Decisión:**  OK
*  CQ4:   **1.0**   — Compares with recent SOTA (RAT-SQL+Score, R2SQL, IGSQL) and a same-base RAT-SQL (GAP) baseline.   *(p. p.4 Table 1)*    ·   **Decisión:**  OK
*  CQ5:   **0.5**   — QM and IM are named, but the paper never says whether gold or predicted history is used in evaluation.   *(p. p.4 §5.2)*    ·   **Decisión:**  OK
*  CQ6:   **1.0**   — TSP and CSP ablations plus per-turn analysis.   *(p. p.4 Tables 2-3)*    ·   **Decisión:**  OK
*  CQ7:   **0.0**   — Single run, a single dataset (SParC), no variance or significance reported.   *(p. p.4 Sec.5)*    ·   **Decisión:**  OK

---

###### C. Muestra aleatoria del 10 % de valores concordantes del Nivel 2 (182 de 1824)
*   **R00019**   degradacion_reportada = SI   *(p. p.7 Sec.5.3 (Pass^k degrades as k increases); p.8 Sec.5.4 (hallucination); p.12 App.C (OmniSQL-32B multi-turn capability degrades))*   ·   **Decisión:** OK
*   **R00019**   pi2_representacion = HISTORIAL_PLANO   *(p. p.5 Sec.4 (dialogue accumulates in the LLM context; the paper mentions 'long context windows' on p.3))*   ·   **Decisión:** OK
*   **R00029**   etiquetas = USA_HISTORIAL   *(p. p.4 §2.1 (los turnos previos se mantienen sin cambios como contexto))*   ·   **Decisión:**  OK
*   **R00030**   coste_reportado = TOKENS;LATENCIA   *(p. p.8 Fig. 4; p.18 Table 13)*   ·   **Decisión:** OK
*   **R00030**   errores_join_reportados = SI   *(p. p.9 §4.4 Fig. 6 (Join Path error category))*   ·   **Decisión:** OK
*   **R00030**   paradigma_principal = AGENTES   *(p. p.1 Abstract; p.3 §3.1 (MDP agent with exec_sql and memory_retrieve tools))*   ·   **Decisión:** OK
*   **R00030**   tipo_contribucion = TECNICA   *(p. p.2 contributions)*   ·   **Decisión:** OK
*   **R00035**   modelos_base = GPT-5; GPT-4o; GPT-4.1; Grok-3 Mini Fast; LLaMA-3.3   *(p. p.6 §5 (modelos evaluados); p.4 §3 (GPT-5 como generador, GPT-4o, LLaMA-3.3 y Grok-3 Mini Fast como evaluadores))*   ·   **Decisión:**  OK
*   **R00041**   pi2_actualizacion = NR   *(p. NR)*   ·   **Decisión:** OK
*   **R00042**   pi3_inferencia_joins = IMPLICITA_MODELO   *(p. p.4 §2.2 (solo se serializa información de claves foráneas para el generador))*   ·   **Decisión:**  OK
*   **R00068**   errores_join_reportados = NO   *(p. NA)*   ·   **Decisión:**  OK
*   **R00068**   historial_eval = NR   *(p. p.6 §5.1 (not stated))*   ·   **Decisión:**  OK
*   **R00068**   paradigma_principal = LLM_PROMPTING   *(p. p.4 §3.2, p.6 §4.2 (no fine-tuning; few-shot prompting))*   ·   **Decisión:**  OK
*   **R00072**   historial_eval = PREDICHO   *(p. p.3 Sec.3 (R<n son las respuestas del LLM a preguntas previas); p.1 Intro (error propagation))*   ·   **Decisión:** OK
*   **R00072**   pi2_actualizacion = LLM_GENERATIVA   *(p. p.4 Sec.3.5; p.5 Sec.3.4 (el LLM predice la cadena de ediciones y el SQL; las cadenas de los exemplars se extraen por AST de forma determinista))*   ·   **Decisión:** OK
*   **R00072**   pi2_coste_contexto = CRECE_CON_TURNOS   *(p. p.3 Sec.3 (Q≤n y R<n en la entrada); no se discute explícitamente: inferido)*   ·   **Decisión:** OK
*   **R00074**   errores_join_reportados = NO   *(p. NA)*   ·   **Decisión:**  OK
*   **R00074**   pi2_actualizacion = IMPLICITA_NEURONAL   *(p. p.3-4 §2.2 (state learned implicitly in the encoder through pre-training))*   ·   **Decisión:**  OK
*   **R00079**   contaminacion_discutida = NO   *(p. NA)*   ·   **Decisión:**  OK
*   **R00079**   paradigmas_secundarios = PLM_FINETUNING   *(p. p.5 §4.2.1 (T5-Base and T5-3B fine-tuned))*   ·   **Decisión:**  OK
*   **R00079**   pi2_grafo_dinamico = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00084**   errores_join_reportados = NO   *(p. p.8 §6.6, Table 5 (errors classified as context/modification, not joins))*   ·   **Decisión:** OK
*   **R00086**   escenario = MULTITURNO   *(p. p.1 abstract; p.5 §3.4; p.8 §4.4. Mainly single-turn Spider, extended to SParC and CoSQL.)*   ·   **Decisión:** OK
*   **R00086**   pi3_algoritmo = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00096**   idioma_dataset = EN   *(p. p.6 Sec.5.1 (SParC, CoSQL))*   ·   **Decisión:** OK
*   **R00097**   pi3_escala_esquema = NR   *(p. NR)*   ·   **Decisión:**  OK
*   **R00097**   pi4_aplicado_multiturno = NO   *(p. NA)*   ·   **Decisión:**  OK
*   **R00099**   pi3_inferencia_joins = NR   *(p. NA (single-table-per-domain WHERE-only SQL, no joins))*   ·   **Decisión:**  OK
*   **R00100**   pi3_escala_esquema = NR   *(p. p.5 Table 1 reports 200 databases, 1,020 tables in total, not per-database maximum)*   ·   **Decisión:** OK
*   **R00100**   pi4_mecanismo = NA   *(p. p.3 §3.2 (filtering of synthetic data at training time only; no inference-time execution feedback))*   ·   **Decisión:** OK
*   **R00105**   contaminacion_discutida = NO   *(p. p.5 nota 1 solo asegura que no hay solapamiento entre semillas sintéticas y dev)*   ·   **Decisión:** OK
*   **R00105**   tipo_contribucion = TECNICA;ESTUDIO_EMPIRICO   *(p. p.2 Sec.1 (contribuciones 1-4: esquema de ediciones, modelo NL-EDIT, datos sintéticos, análisis))*   ·   **Decisión:** OK
*   **R00107**   historial_eval = SOLO_PREGUNTAS   *(p. p.3 §3.1 (rewriter input is previous user utterances; no previous SQL used))*   ·   **Decisión:**  OK
*   **R00107**   pi4_aplicado_multiturno = NO   *(p. p.5 §3.2.2; p.8 §4.3 (user feedback on rewrite only mentioned as possible, not used))*   ·   **Decisión:**  OK
*   **R00109**   pi1_tecnica = CONCATENACION   *(p. p.4 §3)*   ·   **Decisión:** OK
*   **R00109**   pi2_representacion = HISTORIAL_PLANO   *(p. p.4 §3)*   ·   **Decisión:** OK
*   **R00109**   requiere_entrenamiento = PARCIAL   *(p. p.2 §1 (PICARD is inference-time only, but T5 is fine-tuned); p.3-4 §3)*   ·   **Decisión:** OK
*   **R00110**   paradigma_principal = PLM_FINETUNING   *(p. p.3 Sec.2.2 (all three baselines use BERT encodings))*   ·   **Decisión:** OK
*   **R00114**   errores_join_reportados = NO   *(p. Whole text)*   ·   **Decisión:**  OK
*   **R00114**   pi4_mecanismo = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00114**   pi4_senal = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00116**   codigo_disponible = NO   *(p. p.2 footnote 1 ('We will open-source our code'))*   ·   **Decisión:** OK
*   **R00116**   etiquetas = USA_HISTORIAL   *(p. p.6 §3 Sparc/CoSQL (previous system-produced query concatenated to the utterance))*   ·   **Decisión:** OK
*   **R00117**   pi2_actualizacion = IMPLICITA_NEURONAL   *(p. p.4-5 Sec.4.2.2-4.2.3 (attention layers))*   ·   **Decisión:**  OK
*   **R00117**   pi3_inferencia_joins = IMPLICITA_MODELO   *(p. p.5 Sec.4.4 (decoder generates SQL tokens; no explicit join inference))*   ·   **Decisión:**  OK
*   **R00120**   codigo_disponible = SI   *(p. p1 footnote 1 (GitHub URL))*   ·   **Decisión:** OK
*   **R00120**   escenario = MULTITURNO   *(p. p1 Abstract; p1 Intro)*   ·   **Decisión:** OK
*   **R00120**   pi2_coste_contexto = ACOTADO   *(p. p5 §3.3; p7 §4.1 (attention window h=5, plus one previous SQL))*   ·   **Decisión:** OK
*   **R00123**   contaminacion_discutida = NO   *(p. NA)*   ·   **Decisión:**  OK
*   **R00126**   pi3_metricas_linking = NR   *(p. NA)*   ·   **Decisión:** OK
*   **R00129**   pi2_representacion = HISTORIAL_PLANO; SQL_PREVIO_EDICION   *(p. p.7 §5.1)*   ·   **Decisión:** OK
*   **R00129**   pi4_rondas_max = NR   *(p. NA)*   ·   **Decisión:** OK
*   **R00131**   etiquetas = USA_HISTORIAL   *(p. p.1 Abstract; p.5-6 §3.4 (edits the previous predicted query))*   ·   **Decisión:** OK
*   **R00131**   pi2_actualizacion = IMPLICITA_NEURONAL   *(p. p.4 §3.2 interaction-level LSTM)*   ·   **Decisión:** OK
*   **R00148**   fecha_modelo = NR   *(p. p.5: sin versiones con fecha)*   ·   **Decisión:**  OK
*   **R00170**   codigo_disponible = NO   *(p. No se menciona ningún enlace al código en el texto)*   ·   **Decisión:**  OK
*   **R00170**   fecha_modelo = NR   *(p. NR)*   ·   **Decisión:**  OK
*   **R00170**   pi2_coste_contexto = NR   *(p. NR)*   ·   **Decisión:**  OK
*   **R00170**   requiere_entrenamiento = SI   *(p. p.6 §3.2.3)*   ·   **Decisión:**  OK
*   **R00232**   errores_join_reportados = NO   *(p. p.5-6 §4)*   ·   **Decisión:**  OK
*   **R00232**   fecha_modelo = NR   *(p. NA)*   ·   **Decisión:**  OK
*   **R00232**   paradigma_principal = REGLAS_SIMBOLICO   *(p. p.3-4 §3.1-3.2 (templates, Solr index, bag-of-words clause classifiers, rule-based SQL generator))*   ·   **Decisión:**  OK
*   **R00232**   pi3_algoritmo = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00232**   requiere_entrenamiento = SI   *(p. p.3 §3.1.2 (classifiers trained on synthetic data))*   ·   **Decisión:**  OK
*   **R00238**   fecha_modelo = NR   *(p. NA)*   ·   **Decisión:**  OK
*   **R00238**   historial_eval = NR   *(p. p.3 §4)*   ·   **Decisión:**  OK
*   **R00238**   idioma_dataset = EN   *(p. p.3 §4 (Spider dev set))*   ·   **Decisión:**  OK
*   **R00238**   pi3_algoritmo = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00286**   pi3_escala_esquema = NR   *(p. NR (Table 8 in the appendix is not in the text provided))*   ·   **Decisión:** OK
*   **R00288**   escenario = MULTITURNO   *(p. p.1 Intro, Fig.1; p.2 contributions)*   ·   **Decisión:**  OK
*   **R00288**   pi1_insumos_historial = PREGUNTAS_PREVIAS; SQL_PREVIOS   *(p. p.2 §2; p.8 §5.2)*   ·   **Decisión:**  OK
*   **R00288**   pi2_grafo_dinamico = NA   *(p. NA; el texto no lo especifica)*   ·   **Decisión:**  OK
*   **R00288**   pi2_grafo_nodos = ELEMENTOS_ESQUEMA   *(p. p.2 §2 (IGSQL: el codificador de grafo modela elementos de la BD junto con los mencionados en las preguntas))*   ·   **Decisión:**  OK
*   **R00288**   pi2_representacion = HISTORIAL_PLANO; SQL_PREVIO_EDICION; GRAFO   *(p. p.2-3 §2; p.8 §5.2)*   ·   **Decisión:**  OK
*   **R00288**   pi4_senal = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00292**   paradigmas_secundarios = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00292**   pi1_tecnica = CONCATENACION   *(p. p.2 Fig.1)*   ·   **Decisión:**  OK
*   **R00292**   requiere_entrenamiento = NO   *(p. p.1 Abstract (zero-shot))*   ·   **Decisión:**  OK
*   **R00298**   degradacion_reportada = NO   *(p. p.8 §5.2: no per-turn analysis)*   ·   **Decisión:** OK
*   **R00298**   errores_join_reportados = NO   *(p. p.7 Table 2: breakdown by difficulty only)*   ·   **Decisión:** OK
*   **R00298**   escenario = MULTITURNO   *(p. p.6 §5.1 (evaluated on SParC and CoSQL, plus Spider); the method itself is described as single-question (p.2-3 §3.1))*   ·   **Decisión:** OK
*   **R00298**   idioma_dataset = EN   *(p. p.8 Limitations)*   ·   **Decisión:** OK
*   **R00298**   pi2_coste_contexto = NR   *(p. NR)*   ·   **Decisión:** OK
*   **R00298**   pi4_aplicado_multiturno = NO   *(p. NA)*   ·   **Decisión:** OK
*   **R00298**   tipo_contribucion = TECNICA   *(p. p.1 Abstract; p.2 §1)*   ·   **Decisión:** OK
*   **R00309**   degradacion_reportada = SI   *(p. p.10 s6.3: UEX falls from SRD to MRD (ChatBI -9.55%, MAC-SQL -32.51%))*   ·   **Decisión:**  OK
*   **R00309**   pi4_mecanismo = NA   *(p. p.3 s3: users judge results afterwards and failures go to the DBA via View Advisor; there is no in-loop correction)*   ·   **Decisión:**  OK
*   **R00311**   idioma_dataset = EN   *(p. p.7-8 §4.1 (PACIFIC, Abg-CoQA, Spider-derived AmbigSQL))*   ·   **Decisión:** OK
*   **R00311**   paradigmas_secundarios = LLM_PROMPTING   *(p. p.4 §3.1 (few-shot ICL action classifier and prompted user simulator); p.9-10 §4.3 (prompting baselines))*   ·   **Decisión:** OK
*   **R00311**   pi3_algoritmo = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00312**   contaminacion_discutida = NO   *(p. NR)*   ·   **Decisión:** OK
*   **R00312**   fecha_modelo = NR   *(p. NR)*   ·   **Decisión:** OK
*   **R00312**   paradigma_principal = LLM_FINETUNING   *(p. p.8 Sec. VI-A (QLoRA fine-tuning of 7B LLMs on QDA-SQL data))*   ·   **Decisión:** OK
*   **R00312**   pi1_insumos_historial = PREGUNTAS_PREVIAS;SQL_PREVIOS;RESPUESTAS_SISTEMA   *(p. p.5 Fig. 3; p.4 Table II (Q&A history with system replies))*   ·   **Decisión:** OK
*   **R00312**   pi2_coste_contexto = NR   *(p. NR)*   ·   **Decisión:** OK
*   **R00312**   pilares_centrales = PI4   *(p. p.1 abstract; p.2 contributions (clarification/abstention for ambiguous and unanswerable questions; Verify state))*   ·   **Decisión:** OK
*   **R00312**   tipo_contribucion = TECNICA;BENCHMARK   *(p. p.2 contributions; p.8 Sec. VI-A (MMSQL test set curated from CoSQL))*   ·   **Decisión:** OK
*   **R00370**   escenario = MULTITURNO   *(p. p.1 Abstract; p.5 §4.1 (simulated user conversations, IncreQA/AdaptQA))*   ·   **Decisión:**  OK
*   **R00370**   paradigmas_secundarios = LLM_PROMPTING   *(p. p.7 fn.5 (shared system prompt, off-the-shelf LLMs, no training))*   ·   **Decisión:**  OK
*   **R00373**   requiere_entrenamiento = NO   *(p. p.7 §5 (LLM por API, temperature=0); p.30 App. I.3)*   ·   **Decisión:**  OK
*   **R00374**   codigo_disponible = SI   *(p. p.13 Appendix A Limitations ('we release our code, datasets, and hyperparameters'))*   ·   **Decisión:** OK
*   **R00374**   degradacion_reportada = SI   *(p. p.6 §5.1 (BaselineSharded 0.333 vs OracleFull 0.743))*   ·   **Decisión:** OK
*   **R00374**   escenario = MULTITURNO   *(p. p.5 §4.1 (Text-to-SQL: sharded multi-turn instructions from Lost_in_conversation/Spider, simulated users))*   ·   **Decisión:** OK
*   **R00374**   idioma_dataset = EN;ZH   *(p. p.5 §4.1 (Spider text-to-SQL in English; the Chinese medical QA is a separate task))*   ·   **Decisión:** OK
*   **R00435**   escenario = MULTITURNO   *(p. p.1 Abstract; p.4-5 §3.1)*   ·   **Decisión:** OK
*   **R00435**   modelos_base = GPT-5 mini; GPT-5.2; Claude Sonnet 4.5; Claude Sonnet 4.6; Claude Opus 4.6   *(p. p.8 §5.3)*   ·   **Decisión:** OK
*   **R00435**   pi3_metricas_linking = NR   *(p. NA)*   ·   **Decisión:** OK
*   **R00435**   requiere_entrenamiento = NO   *(p. p.8 §5.3-5.5 (LLM por API, sin entrenamiento))*   ·   **Decisión:** OK
*   **R00435**   tipo_contribucion = BENCHMARK;ESTUDIO_EMPIRICO   *(p. p.2 §1 contribuciones; p.1 Abstract)*   ·   **Decisión:** OK
*   **R00438**   degradacion_reportada = NO   *(p. NR (solo se reporta éxito por Fase 1/Fase 2 de BIRD-Interact, no degradación por turno))*   ·   **Decisión:** OK
*   **R00438**   pi2_grafo_nodos = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00438**   pi3_metricas_linking = NR   *(p. NR)*   ·   **Decisión:** OK
*   **R00450**   degradacion_reportada = SI   *(p. p.5 §4.6 (constraint drift: turn-1 error persists into turn 3 in 34% of cases without HITL); p.5 Table 2 (clean vs noisy))*   ·   **Decisión:**  OK
*   **R00450**   pi4_aplicado_multiturno = SI   *(p. p.5 §4.6 (misidentified constraint persists into turn 3 in 34% of cases without HITL, 9% with))*   ·   **Decisión:**  OK
*   **R00453**   pi4_senal = ERROR_DBMS;USUARIO   *(p. p.7 Sec. 6 (compile/execution failure); p.3 Sec. 3 (expert-authored queries); p.9 Sec. 6.3 (user retry))*   ·   **Decisión:**  OK
*   **R00480**   escenario = MULTITURNO   *(p. p.3 §4.2 (split multi-turn, 200 of 1,200 cases); p.4 A4. Most cases are single-turn)*   ·   **Decisión:** OK
*   **R00480**   etiquetas = USA_HISTORIAL   *(p. p.4 A4 (prior structured state, PATCH/REPLACE))*   ·   **Decisión:** OK
*   **R00482**   degradacion_reportada = SI   *(p. p.6 §4.3 ('errors compound across successive modifications'); Table 10)*   ·   **Decisión:** OK
*   **R00482**   paradigmas_secundarios = LLM_PROMPTING   *(p. p.23 Fig.8 (zero-shot generation prompt); p.5 Table 2)*   ·   **Decisión:** OK
*   **R00482**   pi4_aplicado_multiturno = SI   *(p. p.6 §4.3, Table 3, Table 10)*   ·   **Decisión:** OK
*   **R00491**   contaminacion_discutida = NO   *(p. NR (las referencias citan un survey de contaminación, pero el texto no la discute))*   ·   **Decisión:** OK
*   **R00491**   modelos_base = Claude-Sonnet-4.6; GPT-4o; GPT-5.4; o3-mini; o4-mini; Gemini-2.5-Flash; Grok-4-Fast; Grok-4.1-Fast; Qwen2.5-72B; Qwen-Max; Llama-3.3-70B; DeepSeek-V4-Flash   *(p. p.24 App. D, Tabla 10)*   ·   **Decisión:** OK
*   **R00499**   degradacion_reportada = SI   *(p. p.9 Tabla 4 y RQ5 (el rendimiento baja al crecer el horizonte H=10→30; solo Math e Research, no SQL))*   ·   **Decisión:**  OK
*   **R00499**   pi3_algoritmo = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00499**   pi4_rondas_max = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00499**   pi4_senal = NA   *(p. p.19 Tabla 8)*   ·   **Decisión:**  OK
*   **R00508**   pi3_inferencia_joins = IMPLICITA_MODELO   *(p. p.4 §3.1 (se extraen rutas de join válidas solo para sintetizar tareas); la inferencia en evaluación depende del modelo)*   ·   **Decisión:** OK
*   **R00511**   codigo_disponible = NO   *(p. NR in text (no link or statement))*   ·   **Decisión:** OK
*   **R00511**   degradacion_reportada = SI   *(p. p.3 Table 7, Fig 2, Table 8 (context-dependent turns and later turns are harder: EM 39.1 vs 63.6))*   ·   **Decisión:** OK
*   **R00511**   pi4_aplicado_multiturno = SI   *(p. p.2 §2.2C (CoSQL, multi-turn))*   ·   **Decisión:** OK
*   **R00524**   paradigmas_secundarios = LLM_PROMPTING   *(p. p.15 IV.C (chain-of-thought); zero-shot LLMs p.13)*   ·   **Decisión:**  OK
*   **R00524**   pi3_inferencia_joins = IMPLICITA_MODELO   *(p. p.15 IV.C)*   ·   **Decisión:**  OK
*   **R00525**   modelos_base = RASAT; RAT-SQL; LGE-SQL; T5-3B+PICARD   *(p. p.5 Sec. IV.C; p.9 Tablas 6-7)*   ·   **Decisión:** OK
*   **R00525**   pi3_inferencia_joins = IMPLICITA_MODELO   *(p. p.5 Sec. IV.C: el seq2seq genera el SQL; no hay algoritmo de joins)*   ·   **Decisión:** OK
*   **R00525**   pi4_aplicado_multiturno = NO   *(p. NA)*   ·   **Decisión:** OK
*   **R00526**   idioma_dataset = OTRO   *(p. p.1 Abstract (Arabic))*   ·   **Decisión:** OK
*   **R00526**   pi2_grafo_dinamico = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00526**   pi4_mecanismo = AUTODEPURACION_LLM   *(p. p.4-5 Sec. IV.C, Fig. 2 (a fine-tuned LLM detects and corrects the predicted SQL in one step))*   ·   **Decisión:** OK
*   **R00526**   pi4_rondas_max = 1   *(p. p.5 Sec. IV.C (single step, no regeneration))*   ·   **Decisión:** OK
*   **R00828**   degradacion_reportada = NO   *(p. p.7-8 (sin análisis por turno))*   ·   **Decisión:** OK
*   **R00828**   fecha_modelo = gemini-1.5-flash-latest   *(p. p.5 sec. 2.3; p.6 sec. 3.5)*   ·   **Decisión:** OK
*   **R00828**   pi3_tecnica_linking = LLM_PROMPTING   *(p. p.5-6 secs. 2.2, 3.5 (el LLM usa list_tables y describe_table para inspeccionar el esquema))*   ·   **Decisión:** OK
*   **R00828**   pi4_rondas_max = NR   *(p. NR)*   ·   **Decisión:** OK
*   **R00868**   pi3_inferencia_joins = IMPLICITA_MODELO   *(p. p.7 Case study: the JOIN structure is predicted by the seq2seq model)*   ·   **Decisión:** OK
*   **R00868**   pi4_rondas_max = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00868**   pilares_contenidos = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00904**   coste_reportado = NINGUNO   *(p. p.12-13 gives only theoretical time/space complexity, no measured cost)*   ·   **Decisión:**  OK
*   **R00908**   idioma_dataset = EN   *(p. p.5 §4.1 (SPIDER y datos AEP; idioma de AEP no declarado, se asume EN))*   ·   **Decisión:**  OK
*   **R00908**   requiere_entrenamiento = NO   *(p. p.3 §3.3 (solo prompting con demostraciones))*   ·   **Decisión:**  OK
*   **R00920**   pi2_grafo_dinamico = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00920**   pi3_algoritmo = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00920**   pi4_aplicado_multiturno = NO   *(p. p.6 §6.1 (the retry is described only for the HybridQA pipeline; the conversational agent in p.4 §4 only reports the searched query to the user))*   ·   **Decisión:** OK
*   **R00924**   pi2_actualizacion = IMPLICITA_NEURONAL   *(p. p.8 §5.1 (RUN edit matrix predicted by a U-shaped CNN))*   ·   **Decisión:**  OK
*   **R00924**   pilares_centrales = PI1   *(p. p.1 Abstract; p.2 contributions)*   ·   **Decisión:**  OK
*   **R00927**   etiquetas = USA_HISTORIAL   *(p. p.6 §3.3 (historial completo concatenado y reescritura con GPT))*   ·   **Decisión:**  OK
*   **R00927**   paradigmas_secundarios = LLM_PROMPTING   *(p. p.4 §3.1 (baselines GPT-4 Turbo and Claude 3 Opus with schema prompt); p.6 §3.3 (GQR rewriting with GPT-4 Turbo))*   ·   **Decisión:**  OK
*   **R00936**   coste_reportado = LATENCIA   *(p. p.7 §5.4.2 y Fig. 8-9 (tiempo por paso 0.5-1 min; también RAM gráfica y flash, categorías fuera del vocabulario))*   ·   **Decisión:** OK
*   **R00936**   pi1_insumos_historial = PREGUNTAS_PREVIAS;SQL_PREVIOS   *(p. p.4 §4.1; p.5 §4.2.2)*   ·   **Decisión:** OK
*   **R00936**   pi3_escala_esquema = NR   *(p. p.6 §5.1 (SParC: 200 bases de datos, 138 dominios; sin máximo de tablas/columnas))*   ·   **Decisión:** OK
*   **R00936**   pi3_inferencia_joins = IMPLICITA_MODELO   *(p. p.3 §3.3 (FK como aristas del grafo, sin algoritmo de joins); p.5 decodificador genera palabras SQL o columnas)*   ·   **Decisión:** OK
*   **R00936**   pi4_senal = NA   *(p. NA)*   ·   **Decisión:** OK
*   **R00950**   codigo_disponible = NO   *(p. No code link in the extracted text (appendices omitted))*   ·   **Decisión:**  OK
*   **R00950**   degradacion_reportada = SI   *(p. p.7 Figure 5 and §5.3; p.6 §5.2 Table 4 (results by turn, the gain grows with turn number))*   ·   **Decisión:**  OK
*   **R00950**   pi3_escala_esquema = NR   *(p. NA)*   ·   **Decisión:**  OK
*   **R00950**   pi4_rondas_max = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00954**   contaminacion_discutida = NO   *(p. Not discussed)*   ·   **Decisión:**  OK
*   **R00954**   coste_reportado = NINGUNO   *(p. p.16 Table 5 lists Latency as a metric, but no latency or cost values are reported)*   ·   **Decisión:**  OK
*   **R00954**   pi3_algoritmo = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00981**   coste_reportado = NINGUNO   *(p. p.6 §4.3 (only training time is given, no inference cost))*   ·   **Decisión:** OK
*   **R00994**   pi2_grafo_nodos = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00994**   pi3_algoritmo = NA   *(p. NA)*   ·   **Decisión:**  OK
*   **R00994**   tipo_contribucion = TECNICA   *(p. p.1 Abstract; p.2 Sec.4)*   ·   **Decisión:**  OK
*   **R01029**   degradacion_reportada = SI   *(p. p.7 Table 6 (QM por indice de turno; baja de 56.2 en turno 1 a 26.8 en turno >4))*   ·   **Decisión:** OK
*   **R01029**   errores_join_reportados = NO   *(p. p.7 Table 3 (solo F1 por clausula))*   ·   **Decisión:** OK
*   **R01029**   requiere_entrenamiento = SI   *(p. p.6 Implementation Details)*   ·   **Decisión:** OK
*   **R01034**   pi3_metricas_linking = NR   *(p. NA)*   ·   **Decisión:** OK
*   **R01034**   pi3_tecnica_linking = COINCIDENCIA_CADENAS   *(p. p.6 Sec.5 (Col and Val recognized by a simple matching algorithm without synonyms))*   ·   **Decisión:** OK
*   **R01037**   idioma_dataset = EN   *(p. p.5 Dataset (SParC, CoSQL); language not stated explicitly)*   ·   **Decisión:** OK
*   **R01037**   pi2_grafo_dinamico = SI   *(p. p.3 ('change as the conversation proceeds'); p.1 Introduction)*   ·   **Decisión:** OK
*   **R01037**   pi3_inferencia_joins = IMPLICITA_MODELO   *(p. p.4-5 (foreign-key relations as graph edges, SQL generated by the decoder))*   ·   **Decisión:** OK
*   **R01037**   requiere_entrenamiento = SI   *(p. p.5-6 Implementation Details; reranker trained separately)*   ·   **Decisión:** OK
*   **R01037**   tipo_contribucion = TECNICA   *(p. p.1 Abstract; p.2)*   ·   **Decisión:** OK

---

###### D. Muestra aleatoria del 10 % del Nivel 1 (32 de 315 estudios)
Lea solo título y resumen; corrija lo que no cuadre.
*   **B00012**   — LGESQL: Line Graph Enhanced Text-to-SQL Model with Mixed Local and Non-Local Rel
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=TECNICA; paradigma_principal=PLM_FINETUNING; paradigmas_secundarios=NEURONAL_PRE_PLM; modelos_base=ELECTRA; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=SI; pi3_tecnica_linking=GRAFO_ESQUEMA;CLASIFICADOR_ENTRENADO; pi3_inferencia_joins=IMPLICITA_MODELO; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **B00027**   — PaVeRL-SQL: Text–to–SQL via Partial–Match Rewards and Verbal Reinforcement Learn
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=TECNICA; paradigma_principal=LLM_FINETUNING; paradigmas_secundarios=LLM_PROMPTING; modelos_base=OmniSQL-7B; pilares_centrales=PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=PARCIAL; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES;VERIFICADOR_CRITICO; pi4_senal=RESULTADO_EJECUCION;JUICIO_LLM
    *   **Decisión:** OK
*   **B00072**   — SQLPrompt: In-Context Text-to-SQL with Minimal Labeled Data
    *  escenario=UN_TURNO; etiquetas=NR; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=NINGUNA_EXPLICITA; pi3_inferencia_joins=IMPLICITA_MODELO; pi4_mecanismo=AUTOCONSISTENCIA_VOTACION; pi4_senal=RESULTADO_EJECUCION;ERROR_DBMS
    *   **Decisión:** OK
*   **B00229**   — Metasql: A Generate-Then-Rank Framework for Natural Language to SQL Translation
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=LGESQL; BRIDGE; GAP; RESDSQL; GPT-3.5-Turbo; GPT-4; pilares_centrales=NR; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=SI; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00003**   — SchemaScope: How Join-Hop Depth Breaks Text-to-SQL in Large Language Models, and
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=BENCHMARK;TECNICA;ESTUDIO_EMPIRICO; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=GPT-4o; GPT-4-Turbo; Llama-3-70B; Gemini Pro; Claude-3.5-Sonnet; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=PODA_ESQUEMA; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00008**   — Rethinking Schema Linking: A Context-Aware Bidirectional Retrieval Approach for
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=LLM_PROMPTING;PODA_ESQUEMA; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00011**   — Bidirectional Semantic Enhancement for Schema Routing Across Large-Scale Databas
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=SI; pi3_tecnica_linking=EMBEDDINGS_RECUPERACION;LLM_PROMPTING; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00031**   — SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-
    *  escenario=UN_TURNO; etiquetas=RONDAS_INTERNAS; tipo_contribucion=TECNICA;ESTUDIO_EMPIRICO; paradigma_principal=AGENTES; paradigmas_secundarios=LLM_FINETUNING; modelos_base=NR; pilares_centrales=PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=SI; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES; pi4_senal=ERROR_DBMS;RESULTADO_EJECUCION
    *   **Decisión:** OK
*   **R00048**   — TS-SQL: Test-driven Self-refinement for Text-to-SQL
    *  escenario=UN_TURNO; etiquetas=NR; tipo_contribucion=TECNICA; BENCHMARK; paradigma_principal=AGENTES; paradigmas_secundarios=LLM_PROMPTING; modelos_base=NR; pilares_centrales=PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=NO; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES; AUTODEPURACION_LLM; pi4_senal=RESULTADO_EJECUCION
    *   **Decisión:** OK
*   **R00054**   — LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Tex
    *  escenario=UN_TURNO; etiquetas=COMPONENTE;RONDAS_INTERNAS; tipo_contribucion=TECNICA;BENCHMARK; paradigma_principal=AGENTES; paradigmas_secundarios=LLM_PROMPTING; modelos_base=DeepSeek-R1; DeepSeek-V3; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=NO; pi3_tecnica_linking=EMBEDDINGS_RECUPERACION;LLM_PROMPTING; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00061**   — Boosting Text-to-SQL through Multi-grained Error Identification
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=PLM_FINETUNING; modelos_base=NR; pilares_centrales=PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=PARCIAL; pi3_tecnica_linking=NINGUNA_EXPLICITA; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES;VERIFICADOR_CRITICO; pi4_senal=ERROR_DBMS;RESULTADO_EJECUCION
    *   **Decisión:** OK
*   **R00111**   — Towards robustness of text-to-SQL models against synonym substitution
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=BENCHMARK;ESTUDIO_EMPIRICO;TECNICA; paradigma_principal=PLM_FINETUNING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=PARCIAL; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00115**   — A pilot study of Text-to-SQL semantic parsing for Vietnamese
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=BENCHMARK;ESTUDIO_EMPIRICO; paradigma_principal=PLM_FINETUNING; paradigmas_secundarios=NEURONAL_PRE_PLM; modelos_base=EditSQL; IRNet; PhoBERT; XLM-R; pilares_centrales=NR; pilares_contenidos=PI3; idioma_dataset=OTRO; codigo_disponible=SI; requiere_entrenamiento=SI; pi3_tecnica_linking=COINCIDENCIA_CADENAS; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00140**   — DeepEye-SQL: A Software-Engineering-Inspired Text-to-SQL Framework
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3;PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=NO; pi3_tecnica_linking=LLM_PROMPTING; pi3_inferencia_joins=GRAFO_FK_RESTRICCIONES; pi4_mecanismo=VERIFICADOR_CRITICO;AUTOCONSISTENCIA_VOTACION; pi4_senal=RESULTADO_EJECUCION;JUICIO_LLM
    *   **Decisión:** OK
*   **R00184**   — Phebe: A Multi-Agent Natural Language Interface for Interactive Data Visualizati
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=TECNICA; paradigma_principal=AGENTES; paradigmas_secundarios=LLM_PROMPTING; modelos_base=NR; pilares_centrales=NR; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES; pi4_senal=ERROR_DBMS
    *   **Decisión:** OK
*   **R00278**   — DBTagger: Multi-task learning for keyword mapping in NLIDBs using bi-directional
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=TECNICA; paradigma_principal=NEURONAL_PRE_PLM; paradigmas_secundarios=NR; modelos_base=Bi-directional RNN sequence tagger; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=SI; pi3_tecnica_linking=CLASIFICADOR_ENTRENADO; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00279**   — An Investigation Between Schema Linking and Text-to-SQL Performance
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=BENCHMARK;ESTUDIO_EMPIRICO; paradigma_principal=NR; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=NR; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00324**   — RSL-SQL: Robust Schema Linking in Text-to-SQL Generation
    *  escenario=UN_TURNO; etiquetas=RONDAS_INTERNAS; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=GPT-4o; DeepSeek; pilares_centrales=PI3; pilares_contenidos=PI4; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=NO; pi3_tecnica_linking=PODA_ESQUEMA; LLM_PROMPTING; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES; AUTOCONSISTENCIA_VOTACION; pi4_senal=RESULTADO_EJECUCION
    *   **Decisión:** OK
*   **R00365**   — SQL-of-Thought: Multi-agentic Text-to-SQL with Guided Error Correction
    *  escenario=UN_TURNO; etiquetas=RONDAS_INTERNAS; tipo_contribucion=TECNICA; paradigma_principal=AGENTES; paradigmas_secundarios=LLM_PROMPTING; modelos_base=NR; pilares_centrales=PI4; pilares_contenidos=PI3; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=LLM_PROMPTING; pi3_inferencia_joins=IMPLICITA_MODELO; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES;AUTODEPURACION_LLM; pi4_senal=ERROR_DBMS
    *   **Decisión:** OK
*   **R00382**   — MTIR-SQL: Multi-turn Tool-Integrated Reasoning Reinforcement Learning for Text-t
    *  escenario=UN_TURNO; etiquetas=RONDAS_INTERNAS; tipo_contribucion=TECNICA; paradigma_principal=AGENTES; paradigmas_secundarios=NR; modelos_base=Qwen3-4B; pilares_centrales=PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=SI; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES; pi4_senal=ERROR_DBMS;RESULTADO_EJECUCION
    *   **Decisión:** OK
*   **R00428**   — EGREFINE: An Execution-Grounded Optimization Framework for Text-to-SQL Schema Re
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3;PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=NO; pi3_tecnica_linking=NINGUNA_EXPLICITA; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES; pi4_senal=RESULTADO_EJECUCION
    *   **Decisión:** OK
*   **R00461**   — How Far Do On-Prem Open LLMs Get on Text-to-SQL? A Cross-Family Size x Technique
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=ESTUDIO_EMPIRICO; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=Qwen2.5-Coder-7B; Qwen2.5-Coder-14B; Qwen2.5-Coder-32B; CodeLlama-7B; CodeLlama-13B; CodeLlama-34B; Llama-3.1-8B; Llama-3.3-70B; pilares_centrales=PI3;PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=NO; pi3_tecnica_linking=COINCIDENCIA_CADENAS;EMBEDDINGS_RECUPERACION; pi3_inferencia_joins=NR; pi4_mecanismo=AUTODEPURACION_LLM;AUTOCONSISTENCIA_VOTACION; pi4_senal=NR
    *   **Decisión:** OK
*   **R00463**   — Test-Time Verification for Text-to-SQL via Outcome Reward Models
    *  escenario=UN_TURNO; etiquetas=NR; tipo_contribucion=TECNICA; paradigma_principal=LLM_FINETUNING; paradigmas_secundarios=LLM_PROMPTING; modelos_base=NR; pilares_centrales=PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=SI; requiere_entrenamiento=SI; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=VERIFICADOR_CRITICO; pi4_senal=JUICIO_LLM
    *   **Decisión:** OK
*   **R00485**   — TraceSQL: Traceable Answerability Estimation for Reference-Free Text-to-SQL Veri
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=TECNICA; paradigma_principal=HIBRIDO_NEUROSIMBOLICO; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=SI; pi3_tecnica_linking=NR; pi3_inferencia_joins=NR; pi4_mecanismo=VERIFICADOR_CRITICO; pi4_senal=JUICIO_LLM
    *   **Decisión:** OK
*   **R00502**   — From Benchmarks to Production: A Text-to-SQL System for Complex Financial Data
    *  escenario=UN_TURNO; etiquetas=NR; tipo_contribucion=TECNICA; paradigma_principal=AGENTES; paradigmas_secundarios=LLM_PROMPTING; modelos_base=NR; pilares_centrales=PI3; pilares_contenidos=PI4; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=PODA_ESQUEMA;GRAFO_ESQUEMA;LLM_PROMPTING; pi3_inferencia_joins=GRAFO_FK_RESTRICCIONES; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES; pi4_senal=NR
    *   **Decisión:** OK
*   **R00636**   — Auto Prompt SQL: A Resource-Efficient Architecture for Text-To-SQL Translation i
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=TECNICA; paradigma_principal=LLM_FINETUNING; paradigmas_secundarios=LLM_PROMPTING; modelos_base=Qwen-3B; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=PARCIAL; pi3_tecnica_linking=PODA_ESQUEMA;CLASIFICADOR_ENTRENADO;LLM_PROMPTING; pi3_inferencia_joins=IMPLICITA_MODELO; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00867**   — Schema Retrieval with Embeddings and Vector Stores Using Retrieval-Augmented Gen
    *  escenario=UN_TURNO; etiquetas=NR; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=GPT-4o; pilares_centrales=PI3; pilares_contenidos=PI4; idioma_dataset=OTRO;EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=EMBEDDINGS_RECUPERACION;PODA_ESQUEMA; pi3_inferencia_joins=NR; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES; pi4_senal=ERROR_DBMS
    *   **Decisión:** OK
*   **R00947**   — Contextual information-enhanced large language model for traffic data query
    *  escenario=UN_TURNO; etiquetas=RONDAS_INTERNAS; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3;PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=LLM_PROMPTING;PODA_ESQUEMA; pi3_inferencia_joins=NR; pi4_mecanismo=AUTODEPURACION_LLM;EJECUCION_FEEDBACK_ERRORES; pi4_senal=ERROR_DBMS
    *   **Decisión:** OK
*   **R00956**   — Experimental study of bidirectional and decoder-only embeddings in Text-to-SQL p
    *  escenario=UN_TURNO; etiquetas=COMPONENTE; tipo_contribucion=ESTUDIO_EMPIRICO; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=NR; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=EMBEDDINGS_RECUPERACION; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R00958**   — Dynamic-SQL: an adaptive NL2SQL framework with multi-path fusion reasoning and e
    *  escenario=UN_TURNO; etiquetas=RONDAS_INTERNAS; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=Qwen2.5-Coder-32B-Instruct; pilares_centrales=PI3;PI4; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=EMBEDDINGS_RECUPERACION;LLM_PROMPTING; pi3_inferencia_joins=IMPLICITA_MODELO; pi4_mecanismo=EJECUCION_FEEDBACK_ERRORES;AUTOCONSISTENCIA_VOTACION; pi4_senal=ERROR_DBMS;RESULTADO_EJECUCION
    *   **Decisión:** OK
*   **R00972**   — SRSPSQL: A dual-stage Text-to-SQL framework with semantic rewriting and schema p
    *  escenario=UN_TURNO; etiquetas=ninguna; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=PODA_ESQUEMA;LLM_PROMPTING; pi3_inferencia_joins=IMPLICITA_MODELO; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK
*   **R01011**   — In-Context Reinforcement Learning based Retrieval-Augmented Generation for Text-
    *  escenario=UN_TURNO; etiquetas=NR; tipo_contribucion=TECNICA; paradigma_principal=LLM_PROMPTING; paradigmas_secundarios=NR; modelos_base=NR; pilares_centrales=PI3; pilares_contenidos=NR; idioma_dataset=EN; codigo_disponible=NR; requiere_entrenamiento=NO; pi3_tecnica_linking=EMBEDDINGS_RECUPERACION;GRAFO_ESQUEMA; pi3_inferencia_joins=NR; pi4_mecanismo=NR; pi4_senal=NR
    *   **Decisión:** OK


