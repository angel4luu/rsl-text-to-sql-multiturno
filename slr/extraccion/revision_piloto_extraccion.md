# Revisión de la extracción — piloto (doble extracción por IA)

Cada estudio fue extraído por **dos extractores IA independientes (A y B)**. Abajo, primero las **discrepancias** (con ambos valores y su ubicación) y después los valores **coincidentes**.

**Cómo responder:** en cada discrepancia escriba `A`, `B` o el valor correcto en `Decisión:`. En los coincidentes, solo marque los que estén mal (escriba el valor correcto al lado). Al final de cada estudio, anote cualquier comentario sobre el formulario (campos confusos, vocabularios que falten).

---

## R00078

Campos: 27/33 coinciden · calidad: 10/10 ítems coinciden · resultados: A 14 filas, B 18, comunes 5 · contrastes: A 11, B 12

### Discrepancias

- **paradigma_principal**
  - A: `LLM_FINETUNING` *(p. p.7 Sec.7.1 (LLaMA2-7B instruction-tuned on 662 groups, 8006 pairs); the proposed prompt framework is otherwise prompting-only)*
  - B: `LLM_PROMPTING` *(p. p.5-6 §5, p.7 §7.1 (prompt framework + in-context learning; instruction tuning only for a LLaMA2-7B comparison setting))*
  - **Decisión:** B
- **paradigmas_secundarios**
  - A: `LLM_PROMPTING` *(p. p.7 Sec.7.1 (prompt framework + in-context learning))*
  - B: `LLM_FINETUNING` *(p. p.7 §7.1 (LLaMA2-7B tuned, 8006 instruction pairs))*
  - **Decisión:** B
- **pilares_contenidos**
  - A: `NA` *(p. NA)*
  - B: `PI2` *(p. p.5 §5 (dialogue history appended to the prompt))*
  - **Decisión:** B
- **codigo_disponible**
  - A: `SI` *(p. p.1 Abstract (GitHub link for the dataset))*
  - B: `PARCIAL` *(p. p.1 Abstract (GitHub link stated for the dataset; code not mentioned))*
  - **Decisión:** B
- **pi3_escala_esquema**
  - A: `166 databases, average 5.23 tables per DB` *(p. p.5 Table 2)*
  - B: `Average 5.23 tables per DB; 166 databases (max not reported)` *(p. p.5 Table 2)*
  - **Decisión:** B
- **pi3_metricas_linking**
  - A: `NR (Table Name Accuracy and Field Match Ratio reported for Create/Insert, not linking recall)` *(p. p.9 Table 6)*
  - B: `No linking recall; Table Name Accuracy and Field Match Ratio for Create/Insert (e.g., GPT-4 Self Refine 0.984/0.988 and 0.769/0.963)` *(p. p.9 Table 6, §7.3)*
  - **Decisión:** B

### Coincidentes (marque solo si algo está mal)

- escenario: `MULTITURNO` *(p. p.1 Abstract; p.2 Introduction)*
- etiquetas: `USA_HISTORIAL;RONDAS_INTERNAS` *(p. p.5 Sec.5 (history integration, self-refinement with SQL executor); p.6 Fig.4)*
- tipo_contribucion: `BENCHMARK;TECNICA` *(p. p.2 Contributions; p.5 Sec.5)*
- modelos_base: `GPT-3.5; GPT-4; LLaMA2-7B; TableLlama-7B; CodeLlama-7B; DeepSeek-Coder-7B` *(p. p.7 Sec.7.1)*
- fecha_modelo: `NR` *(p. p.7 Sec.7.1 (no versions given in main text; appendix not available))*
- pilares_centrales: `PI1;PI4` *(p. p.2 Contributions; p.5 Sec.5 (prompt framework integrating historical data and self-refinement))*
- idioma_dataset: `EN` *(p. p.1 Fig.1; p.6 Fig.5 (examples in English))*
- requiere_entrenamiento: `PARCIAL` *(p. p.7 Sec.7.1 (prompting for most models; LLaMA2-7B also instruction-tuned))*
- pi1_tecnica: `CONCATENACION` *(p. p.5 Sec.5 ('Adds previous dialogue excerpts to the current query'))*
- pi1_insumos_historial: `PREGUNTAS_PREVIAS;SQL_PREVIOS` *(p. p.6 Fig.4; p.7 Sec.7.1 (history of dialogue data; exact content not detailed))*
- pi2_representacion: `HISTORIAL_PLANO` *(p. p.5 Sec.5; p.6 Fig.4)*
- pi2_grafo_nodos: `NA` *(p. NA)*
- pi2_grafo_dinamico: `NA` *(p. NA)*
- pi2_actualizacion: `NR` *(p. NR)*
- pi2_coste_contexto: `NR` *(p. NR)*
- pi3_tecnica_linking: `NINGUNA_EXPLICITA` *(p. p.3 Fig.2; p.5 Sec.5 (full schema and top-3 rows in the prompt))*
- pi3_inferencia_joins: `IMPLICITA_MODELO` *(p. p.3 Fig.2; p.5 Sec.5)*
- pi3_algoritmo: `NA` *(p. NA)*
- pi4_mecanismo: `EJECUCION_FEEDBACK_ERRORES` *(p. p.5 Sec.5 (Self-Refinement Mechanism))*
- pi4_senal: `ERROR_DBMS;RESULTADO_EJECUCION` *(p. p.5 Sec.5; p.9 Sec.7.4 (feedback from the database/SQL executor; signal type not specified precisely))*
- pi4_rondas_max: `NR` *(p. NR in main text)*
- pi4_aplicado_multiturno: `SI` *(p. p.6 Fig.4; p.7 Sec.7.1)*
- historial_eval: `NR` *(p. p.7 Sec.7.1 (whether previous turns use gold or predicted SQL is not stated))*
- degradacion_reportada: `NO` *(p. p.2 (error accumulation mentioned as motivation; no per-turn analysis))*
- errores_join_reportados: `NO` *(p. p.8-9 Sec.7.2-7.4)*
- coste_reportado: `NINGUNO` *(p. p.7-9 Sec.7)*
- contaminacion_discutida: `NO` *(p. p.4-10)*

### Texto libre (versión A; corrija solo si algo es falso)

- pi1_resumen: Previous dialogue interactions are appended to the current query in the prompt (History setting). Not further specified in the main text (p.5 Sec.5; p.7 Sec.7.1). *(p. p.5 Sec.5; p.7 Sec.7.1)*
- pi2_resumen: Dialogue state is the raw dialogue history placed in the prompt; schema changes are expected to be captured via that history. No explicit state structure. *(p. p.5 Sec.5)*
- pi3_resumen: No explicit schema linking; the full schema and sample rows are given in the prompt. Schema changes (Create/Alter) are tracked in the metric (Context-aware Match), not in the method. *(p. p.5 Sec.5; p.6-7 Sec.6.1)*
- pi4_resumen: An SQL executor runs the generated SQL and its feedback is used to produce a refined answer (Self Refine). Number of rounds not reported. *(p. p.5 Sec.5; p.6 Fig.4)*
- limitaciones_autores: Only 166 databases, so limited diversity and generalizability; metrics miss runtime efficiency and SQL best practices. *(p. p.9-10 Limitations)*

**Comentarios sobre el formulario:** 

---

## R00101

Campos: 30/33 coinciden · calidad: 10/10 ítems coinciden · resultados: A 38 filas, B 37, comunes 29 · contrastes: A 17, B 13

### Discrepancias

- **pi1_tecnica**
  - A: `CONCATENACION; RESOLUCION_EXPLICITA` *(p. p.3 §4.1 Eq.3 (concatenation); p.5 §4.2 and Fig.2 (coreference links from coreferee))*
  - B: `CONCATENACION;OTRA:relaciones de correferencia entre preguntas (coreferee) como aristas del grafo de interacción` *(p. p.3 Eq.3; p.5 §4.2; p.6-7 §5.1)*
  - **Decisión:** A
- **pi2_grafo_nodos**
  - A: `TOKENS_PREGUNTA; ELEMENTOS_ESQUEMA` *(p. p.4 Fig.1, Table 1 (question, table, column and value tokens as vertices))*
  - B: `TOKENS_PREGUNTA;ELEMENTOS_ESQUEMA;OTROS:tokens de valores de la base de datos` *(p. p.4 Fig.1 y Table 1)*
  - **Decisión:** B
- **pi2_actualizacion**
  - A: `REGLAS_DETERMINISTAS` *(p. p.6 §5.1 (edges produced by n-gram matching, coreferee and stanza; no learned state tracker))*
  - B: `IMPLICITA_NEURONAL` *(p. p.3 §4.1 (no hay estado explícito; el modelo relee las preguntas previas))*
  - **Decisión:** A

### Coincidentes (marque solo si algo está mal)

- escenario: `MULTITURNO` *(p. p.1 Abstract; p.3 §3.1, §4.1 (SParC and CoSQL multi-turn plus Spider single-turn))*
- etiquetas: `USA_HISTORIAL` *(p. p.3 §4.1 Eq.3 (previous questions prepended to the input))*
- tipo_contribucion: `TECNICA` *(p. p.1 Abstract; p.2 §1)*
- paradigma_principal: `PLM_FINETUNING` *(p. p.3 §4.1 (T5 fine-tuned with relation-aware self-attention); p.2 §1)*
- paradigmas_secundarios: `NA` *(p. NA)*
- modelos_base: `T5-small; T5-base; T5-large; T5-3B` *(p. p.8 Table 8; p.7 Tables 4-5 (RASAT-3B as main model))*
- fecha_modelo: `NR` *(p. NR)*
- pilares_centrales: `PI3` *(p. p.1 Abstract; p.4-5 §4.2 (schema encoding/linking relations in the interaction graph are the central contribution))*
- pilares_contenidos: `PI1; PI2` *(p. p.5 §4.2 Coreference between questions; p.3 §4.1 Eq.3 (history concatenation))*
- idioma_dataset: `EN` *(p. p.9 Limitation (English only))*
- codigo_disponible: `SI` *(p. p.1 footnote 1 (github.com/LUMIA-group/rasat))*
- requiere_entrenamiento: `SI` *(p. p.3 §4.1; p.9 Limitation (trained 2 days on 8 A100))*
- pi1_insumos_historial: `PREGUNTAS_PREVIAS` *(p. p.3 §3.1, §4.1)*
- pi2_representacion: `HISTORIAL_PLANO; GRAFO` *(p. p.3 §4.1; p.4 §4.2 'Interaction Graph')*
- pi2_grafo_dinamico: `SI` *(p. p.3-4 §4.1-4.2 (the graph is built over the serialized input, which includes all previous questions, so it grows with each turn; the paper does not say 'dynamic' explicitly))*
- pi2_coste_contexto: `ACOTADO` *(p. p.3 §4.1; p.9 Limitation (truncation at 512 tokens; about 3% of CoSQL training data affected))*
- pi3_tecnica_linking: `COINCIDENCIA_CADENAS; GRAFO_ESQUEMA` *(p. p.5 §4.2 (n-gram exact/partial match following RAT-SQL; BRIDGE value match; schema encoding relations))*
- pi3_inferencia_joins: `IMPLICITA_MODELO` *(p. p.5 §4.2 (FOREIGN-KEY relation given as a model input; the T5 decoder generates the SQL, with no join algorithm))*
- pi3_algoritmo: `NA` *(p. NA)*
- pi3_escala_esquema: `NR` *(p. NR)*
- pi3_metricas_linking: `NR` *(p. NR)*
- pi4_mecanismo: `NA` *(p. p.6-7 §5.1 (PICARD is only an optional constrained-decoding grammar filter; no execution feedback or self-correction))*
- pi4_senal: `NA` *(p. NA)*
- pi4_rondas_max: `NA` *(p. NA)*
- pi4_aplicado_multiturno: `NO` *(p. NA)*
- historial_eval: `SOLO_PREGUNTAS` *(p. p.3 §3.1 ('only the questions in the interaction history are available'); §4.1)*
- degradacion_reportada: `NO` *(p. NA (no per-turn analysis; only question vs interaction level metrics))*
- errores_join_reportados: `NO` *(p. NA (two case studies are in Appendix C, which is not in the supplied text))*
- coste_reportado: `NINGUNO` *(p. p.9 Limitation (only a statement of 8 A100 GPUs for about 2 days; no tokens, latency or cost metric))*
- contaminacion_discutida: `NO` *(p. NA)*

### Texto libre (versión A; corrija solo si algo es falso)

- pi1_resumen: Previous questions are concatenated at the start of the input, and the input is truncated at 512 tokens. Coreference links between question tokens across turns (coreferee) are added as explicit relation edges. p.3 §4.1; p.5 §4.2; p.6 §5.1 *(p. p.3, p.5, p.6)*
- pi2_resumen: No separate dialog state is kept. The state is the flat history of questions plus a relation graph over the input tokens that includes coreference edges, truncated at 512 tokens. p.3 §4.1; p.5 §4.2 *(p. p.3-5)*
- pi3_resumen: Schema encoding and linking relations (PK, FK, belongs-to, exact/partial match, value match) are given to the encoder as edges in relation-aware self-attention, propagated to subword level. Only end-task accuracy is reported, with ablations in Tables 9-10. p.4-5 §4.2; p.9 *(p. p.4-5; p.8-9 Tables 9-10)*
- pi4_resumen: No execution feedback or self-correction loop. PICARD (Scholak et al.) prunes invalid beam hypotheses during decoding, with beam size 8. p.7 §5.1 *(p. p.7 §5.1)*
- limitaciones_autores: High compute cost with T5-3B (8 A100 for about 2 days). The 512-token truncation loses information (about 3% of CoSQL training data). English only. *(p. p.9 Limitation)*

**Comentarios sobre el formulario:** 

---

## R01031

Campos: 31/33 coinciden · calidad: 10/10 ítems coinciden · resultados: A 38 filas, B 39, comunes 36 · contrastes: A 7, B 6

### Discrepancias

- **paradigmas_secundarios**
  - A: `NA` *(p. NA)*
  - B: `` *(p. NA)*
  - **Decisión:** A
- **modelos_base**
  - A: `RoBERTa-large; BERT-base; RAT-SQL; TripPy; SOM-DST; Wang et al. 2019 (SQA parser)` *(p. p.4 §3 Metrics & Base Models; p.8 App. D.1-D.2)*
  - B: `RoBERTa-large; BERT-base; RAT-SQL; TripPy; SOM-DST; Wang et al. 2019 parser` *(p. p.4 §3 Metrics & Base Models; p.7 App. A Table 9; p.8 App. D.1)*
  - **Decisión:** A

### Coincidentes (marque solo si algo está mal)

- escenario: `MULTITURNO` *(p. p.1-2 §1, §2.1 (CSP: SParC, CoSQL, MWOZ, SQA))*
- etiquetas: `USA_HISTORIAL` *(p. p.2 §2.1 (query q_t from utterance u_t, history h_t=[u_1..u_{t-1}] and schema c); p.4 §3 (history concatenated))*
- tipo_contribucion: `TECNICA` *(p. p.1 Abstract, §1; p.3 §2.2 (new pre-training objectives CCS/TCS, synthetic data))*
- paradigma_principal: `PLM_FINETUNING` *(p. p.1 §1; p.2 §2.1 (second pre-training phase of RoBERTa, used as drop-in encoder for downstream base parsers); p.8 App. D)*
- fecha_modelo: `NR` *(p. NA)*
- pilares_centrales: `PI2` *(p. p.1 Abstract, §1 (conversational flow/TCS context representation); p.3 §2.2)*
- pilares_contenidos: `PI1; PI3` *(p. p.4 §3 (history concatenation, PI1); p.3 §2.2 (CCS column-operation objective aligns utterance and schema, PI3))*
- idioma_dataset: `EN` *(p. p.4 Tables 1-3 (SParC, CoSQL, MultiWOZ, SQA); language not stated explicitly)*
- codigo_disponible: `NO` *(p. Not mentioned in the text provided)*
- requiere_entrenamiento: `SI` *(p. p.3 §2.2, p.8 App. D.1)*
- pi1_tecnica: `CONCATENACION` *(p. p.4 §3 ('extend it to a multi-turn setting by concatenating current utterances and dialog history'))*
- pi1_insumos_historial: `PREGUNTAS_PREVIAS; RESPUESTAS_SISTEMA` *(p. p.2 §2.1 (u = user query + system response for CoSQL and MWOZ; only the user question for SParC and SQA))*
- pi2_representacion: `HISTORIAL_PLANO` *(p. p.2 §2.1; p.4 §3)*
- pi2_grafo_nodos: `NA` *(p. NA)*
- pi2_grafo_dinamico: `NA` *(p. NA)*
- pi2_actualizacion: `IMPLICITA_NEURONAL` *(p. p.2 §2.1 (contextualized representations per token))*
- pi2_coste_contexto: `NR` *(p. NA (max input length 248/512 in pre-training only, p.8 App. D.1))*
- pi3_tecnica_linking: `CLASIFICADOR_ENTRENADO` *(p. p.3 §2.2 (CCS: per-column operation classifier as an auxiliary pre-training loss))*
- pi3_inferencia_joins: `NR` *(p. NA)*
- pi3_algoritmo: `NA` *(p. NA)*
- pi3_escala_esquema: `NR` *(p. NA (about 400k tables used for synthetic data, p.3 §2.2))*
- pi3_metricas_linking: `NR` *(p. NA)*
- pi4_mecanismo: `NA` *(p. NA (no execution feedback or self-correction))*
- pi4_senal: `NA` *(p. NA)*
- pi4_rondas_max: `NA` *(p. NA)*
- pi4_aplicado_multiturno: `NO` *(p. NA)*
- historial_eval: `SOLO_PREGUNTAS` *(p. p.2 §2.1, p.4 §3 (inputs are previous utterances, plus system responses in CoSQL and MWOZ; no previous SQL is given as input; gold/predicted is not stated explicitly))*
- degradacion_reportada: `SI` *(p. p.7 App. A, Tables 6-8 (per-turn accuracy falls from Q1 to later turns))*
- errores_join_reportados: `NO` *(p. NA)*
- coste_reportado: `NINGUNO` *(p. p.8 App. C-D.1 (pre-training cost only: under half a day on 8 V100 GPUs; no inference cost))*
- contaminacion_discutida: `NO` *(p. NA)*

### Texto libre (versión A; corrija solo si algo es falso)

- pi1_resumen: Current utterance and dialog history are concatenated and encoded by the pre-trained encoder. The TCS objective teaches the encoder to predict the query difference between turns. p.2 §2.1, p.3 §2.2, p.4 §3 *(p. NR)*
- pi2_resumen: No explicit dialogue state. The encoder is pre-trained with TCS (26 context-switch labels) to capture flow between turns, over the flat history. p.3 §2.2 *(p. NR)*
- pi3_resumen: CCS pre-training predicts the operations (e.g. GROUPBY, HAVING, WHERE) applied to each schema column per turn, to align utterance and schema. Join inference is left to the base parser and is not discussed. p.3 §2.2 *(p. NR)*
- pi4_resumen: NA *(p. NA)*
- limitaciones_autores: No limitations section. They note that the synthetic grammar was induced from SParC and may overfit to SParC, and that longer pre-training overfits to unnatural synthetic utterances. p.4 §3 ablation, p.8 App. C *(p. p.4 §3; p.8 App. C)*

**Comentarios sobre el formulario:** 
