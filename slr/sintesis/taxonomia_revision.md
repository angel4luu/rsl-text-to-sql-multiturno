# Taxonomía de los códigos OTRO/OTRA (consolidación inductiva) — para aprobar

Generada por `scripts/taxonomia_otra.py` (`tablas/taxonomia_otra.csv` tiene la correspondencia completa nombre original → canónico → familia, con el número de filas).

**Cómo responder:** bajo cada familia escriba **OK**, o indique cambios como `mover <nombre> → <familia>` o `renombrar familia → <nuevo nombre>`.

Además, `pi2_grafo_nodos` tiene 2 valores `OTROS:` («tokens de valores de la base de datos», «palabras clave y valores SQL»): propuesta → nueva categoría **VALORES_BD** (nodos que representan valores/palabras clave de la base de datos). **Decisión:** OK — aprobado por la autora (2026-10-13)

## Benchmarks

### Multiturno conversacional (17 nombres, 496 filas)
Lost in conversation (76), MultiSQL (70), Ar-SParC (66), MMSQL (44), FollowUp (41), DySQL-Bench (39), PLSQLBench-Spider2-MT (38), EHR-SeqSQL (28), Spider2-MT (24), COSQL-CG (17), SPARC-CG (17), SESQL (16), MRD-BIRD (6), CHASE-C (5), CHASE-T (5), COSQL CQR (2), SPARC CQR (2)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Interactivo / aclaración (20 nombres, 450 filas)
BIRD-INTERACT (55), CLARITY-Spider (48), EnterpriseMem-Bench (44), AmbigSQL (38), BIRD-Interact (34), BIRD-Interact-Full (34), EHR-ChatQA (34), TIDE-Bench (33), SPLASH (18), PRACTIQ (17), EHR-ChatQA-IncreQA (14), EHR-ChatQA-AdaptQA (12), TIDE-Bench Chain-only (12), TIDE-Bench Drift-only (11), CLARITY-Spider-ColAmb-MultiFacet (10), CLARITY-Spider-ColAmb-UniFacet (10), TIDE-Bench Joint (10), BIRD-Interact Mini (9), PRACTIQ excluyendo Answerable (6), TIDE-Bench candidatos de construcción (1)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Variantes de un turno (robustez, dominio, idioma) (18 nombres, 182 filas)
FinScreenBench (42), FIBEN (27), DUSQL (14), Spider2-ST (14), MBPP+-PLSQL (12), EHRSQL (10), PLSQLBench-Spider2-ST (10), LiveSQLBench (8), LiveSQLBench Base-Lite SQLite (8), Spider2-Snow (8), ADVETA(ADD) (4), ADVETA(RPL) (4), Spider-CG(APP) (4), Spider-CG(SUB) (4), Spider-DK (4), Spider-Realistic (4), Spider-SYN (4), CSpider (1)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Diálogo orientado a tareas / estado del diálogo (6 nombres, 156 filas)
AirDialogue (58), MultiWOZ (46), MULTIWOZ (44), Restaurant CONVERSATIONAL (3), Restaurant SINGLE TURN (3), SemPlan (2)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### QA conversacional / tabular híbrida (4 nombres, 88 filas)
HybridQA (45), PACIFIC (29), Abg-CoQA (8), SQA (6)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Datos propios / industriales (16 nombres, 58 filas)
BAIDU MRD PRODUCTION (8), Fleet-Sweep (6), MRD-Industry (6), SRD-Industry (6), Yelp Restaurants (6), MRD BI Baidu (5), SRD BI Baidu (5), BAIDU SRD PRODUCTION (4), SRD production dataset (3), AEP (2), MRD production dataset (2), BD-Business Line A (1), DATAQUE PRODUCCION PROPIO (1), Experience Platform (1), MRD (1), SRD (1)

**Decisión:** OK — aprobado por la autora (2026-10-13)

## Métricas

### Éxito de tarea / agente (18 nombres, 397 filas)
Mean Test Pass@1 (84), SR (55), functional accuracy (41), PASS^1 (38), SR-5 (28), SR priority overall (21), SuccessRate (16), SR followup overall (13), SUCCESS RATE PHASE 2 (13), SuccessRate Phase2 Overall (13), PASS∧5 (12), SUCCESS RATE PHASE 1 (12), SuccessRate Phase1 Overall (12), PASS@5 (11), EpisodePass@1 (10), PASS^5 (10), Progress (4), TurnSuitePass@1 (4)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Ejecución por pregunta (17 nombres, 231 filas)
QM-EX (61), UEX (35), Database State Match (Insert) (20), QEX (16), Post-clarification EX (12), EX(QM) (10), ContextAwareMatch Update (9), TDEX (9), CEA (8), SQL Executability (8), Context-aware Match (Select) (7), DatabaseStateMatch Create (6), DatabaseStateMatch Update (6), FX (6), QM-TS (6), TS(QM) (6), VA (6)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Estado del diálogo / aclaración (13 nombres, 165 filas)
JGA (89), turn accuracy (18), Flight Acc (14), State Acc (14), LCR (11), CRS@0.5 (4), TRS@0.5 (4), USER DIALOG ACT ACCURACY (4), ACCURACY CLASIFICACION 9 CATEGORIAS (2), clarification correct (2), CLASSIFICATION ACCURACY (1), F1 de pares slot-valor del estado completo (1), Post-Clarification DROP F1 (1)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Ejecución por interacción (multiturno) (9 nombres, 159 filas)
IM-EX (53), IEX (51), IM-TS (15), EX(IM) (13), TS(IM) (11), sequence state correct (6), MTS (5), EM(IM) (3), IACCS (2)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Coincidencia exacta / lógica (17 nombres, 126 filas)
Symbol Accuracy (33), Name Acc (11), ETM (10), LEM (10), SEM (10), LEM MULTIFACET COLUMN AMBIGUITY (7), LEM UNIFACET COLUMN AMBIGUITY (7), SEM MULTIFACET COLUMN AMBIGUITY (7), SEM UNIFACET COLUMN AMBIGUITY (7), LX (QM as in Table 3; Table 5 caption says Logical Form Accuracy) (6), QM-EM (4), EM(QM) (3), LX (Table 5 caption; EM in Table 2) (3), ACCCOL (2), ACCOP (2), ACCS (2), ACCVAL (2)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Generación de texto / respuesta (8 nombres, 109 filas)
BLEU (52), Trajectory-level DROP F1 (19), F1 (14), F1 Score (10), answer correct (5), Grammar (3), Post-Clarify F1 (3), Trajectory DROP F1 (3)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Específicas del benchmark (8 nombres, 90 filas)
DEA (33), DEA chain-only strict (12), DEA drift-only all (11), DEA joint all (10), RQS (10), Trajectory-level Similarity (8), QED (4), ERROR (2)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Mejora / efecto de un componente (7 nombres, 57 filas)
MEJORA EX SOBRE NO FEEDBACK PP (23), delta EX vs NoFeedback (12), % de instancias corregidas con feedback (7), PORCENTAJE INSTANCIAS CORREGIDAS (6), Edit decreased % (4), Edit increased % (4), Persistencia de restricción errónea (1)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Recuperación / ordenamiento (9 nombres, 25 filas)
KENDALL TAU RANGOS GE3 (4), KENDALL TAU TODOS LOS RANGOS (4), Kendall tau medio rangos >=3 (4), Kendall tau medio todos los rangos (4), Macro F1 (action level) (3), Recall@5 (3), Avg. F1 (1), Avg. Pre (1), Avg. Rec (1)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Calidad de la explicación (evaluación humana) (4 nombres, 20 filas)
EA CONCISE (5), EA NOT HELPFUL (5), EA PARTIAL (5), EA VERBOSE (5)

**Decisión:** OK — aprobado por la autora (2026-10-13)

### Exactitud no especificada (3 nombres, 10 filas)
accuracy (6), WikiSQL Acc. (3), ACC. (1)

**Decisión:** OK — aprobado por la autora (2026-10-13)

