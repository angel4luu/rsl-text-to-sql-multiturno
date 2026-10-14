# PI5 — *Benchmarks*, métricas y degradación por turno (Nivel 2)

Pregunta: ¿qué *benchmarks* y métricas se emplean en multiturno y qué degradación por turno se reporta?

Base: 72 estudios del Nivel 2 con validez ≥ 50 % [pi15_resultados.json, `nivel2_umbral`; pi5_historial.csv].

## Taxonomía de *benchmarks* y métricas

| Familia de *benchmark* | Estudios |
|---|---|
| Multiturno conversacional | 50 |
| Un turno estándar | 18 |
| Interactivo / aclaración | 11 |
| Variantes de un turno (robustez, dominio, idioma) | 7 |
| Diálogo orientado a tareas / estado del diálogo | 5 |
| Datos propios / industriales | 3 |
| QA conversacional / tabular híbrida | 3 |

Fuente: [pi5_benchmarks.csv].

| Familia de métrica | Estudios |
|---|---|
| Ejecución por pregunta | 34 |
| Coincidencia por interacción (multiturno) | 31 |
| Coincidencia por pregunta (multiturno) | 30 |
| Coincidencia exacta / lógica | 21 |
| Ejecución por interacción (multiturno) | 9 |
| Éxito de tarea / agente | 7 |
| Generación de texto / respuesta | 7 |
| Estado del diálogo / aclaración | 6 |
| Mejora / efecto de un componente | 3 |
| Específicas del *benchmark* | 3 |
| OTRAS | 2 |
| Recuperación / ordenamiento | 1 |
| Calidad de la explicación (evaluación humana) | 1 |
| Exactitud no especificada | 1 |

Fuente: [pi5_metricas.csv]. Un estudio puede aparecer en varias familias.

**Categorías `OTRA` consolidadas** [taxonomia_otra.csv]: los *benchmarks* se agruparon en las familias Datos propios / industriales (p. ej., BAIDU MRD PRODUCTION, Fleet-Sweep), Diálogo orientado a tareas (AirDialogue, MultiWOZ, SemPlan), Interactivo / aclaración (BIRD-Interact, AmbigSQL, CLARITY-Spider, EHR-ChatQA, PRACTIQ, SPLASH, TIDE-Bench), Multiturno conversacional (Ar-SParC, CHASE, DySQL-Bench, EHR-SeqSQL, FollowUp, MMSQL, MultiSQL, Spider2-MT, entre otros), QA conversacional / tabular híbrida (HybridQA, PACIFIC, SQA, Abg-CoQA) y Variantes de un turno (p. ej., Spider-DK, Spider-SYN, EHRSQL, DuSQL, LiveSQLBench). Las métricas se agruparon en 14 familias, entre ellas Ejecución por interacción (IEX, IM-EX, IM-TS), Ejecución por pregunta (QM-EX, UEX, QEX), Estado del diálogo / aclaración (JGA, *turn accuracy*) y Éxito de tarea / agente (SR, *Pass^1*, *Mean Test Pass@1*).

## Tipo de historial en la evaluación

| `historial_eval` | Estudios | % |
|---|---|---|
| PREDICHO | 31 | 43,1 |
| NR | 20 | 27,8 |
| SOLO_PREGUNTAS | 19 | 26,4 |
| GOLD | 5 | 6,9 |

Fuente: [pi5_historial.csv]. Otros campos: degradación reportada SI 38 (52,8 %) y NO 34 (47,2 %); errores de *join* reportados SI 10 (13,9 %); contaminación discutida SI 7 (9,7 %) [pi5_historial.csv].

## Degradación por turno, estratificada por historial

Figura `pi5_degradacion`. Los estratos nunca se agrupan [plan_sintesis.md]. Solo el estrato PREDICHO se interpreta como propagación de errores; SOLO_PREGUNTAS es degradación sin *teacher forcing* y sin propagación de salidas previas; GOLD es referencia con *teacher forcing* [plan_sintesis.md].

| Estrato | Curvas | Estudios | Pendiente mediana (pp por turno) |
|---|---|---|---|
| PREDICHO | 6 | 5 | −7,0 |
| SOLO_PREGUNTAS | 8 | 6 | −10,96 |
| GOLD | sin curvas con al menos tres turnos | — | — |

Fuente: [pi15_resultados.json; leyendas.json]. Pendientes individuales [pi5_pendientes.csv]:

| Estrato | Estudio | *Benchmark* | Métrica | Turnos | Pendiente (pp/turno) | Valor turno 1 |
|---|---|---|---|---|---|---|
| PREDICHO | R00117 (IGSQL) | SPARC | EM | 4 | −16,95 | 63,2 |
| PREDICHO | R00117 (IGSQL) | COSQL | EM | 4 | −4,85 | 53,1 |
| PREDICHO | R00120 (PG-GSQL) | SPARC | QM | 4 | −11,38 | 66,5 |
| PREDICHO | R00435 (*Memory Architectures*) | ENTERPRISEMEM-BENCH | EX | 4 | −5,53 | 69,54 |
| PREDICHO | R00868 (MIGA) | SPARC | QM | 4 | −7,59 | 74,9 |
| PREDICHO | R01029 (*Tracking Interaction States*) | COSQL | QM | 4 | −6,41 | 56,2 |
| SOLO_PREGUNTAS | R00097 (CQR-SQL) | SPARC | QM | 4 | −7,81 | 75,6 |
| SOLO_PREGUNTAS | R00100 (*Self-Play*) | SPARC | QM | 4 | −12,66 | 77,0 |
| SOLO_PREGUNTAS | R00126 (SPARC) | SPARC | QM | 4 | −14,87 | 38,6 |
| SOLO_PREGUNTAS | R00950 (QURG) | SPARC | QM | 4 | −10,62 | 75,4 |
| SOLO_PREGUNTAS | R00994 (*Pay More Attention to History*) | SPARC | QM | 4 | −11,31 | 75,4 |
| SOLO_PREGUNTAS | R01031 (SCORE) | SPARC | QM | 4 | −8,62 | 70,6 |
| SOLO_PREGUNTAS | R01031 (SCORE) | COSQL | QM | 4 | −6,55 | 60,8 |
| SOLO_PREGUNTAS | R01031 (SCORE) | SQA | QM | 3 | −14,32 | 76,44999999999999 |

Todas las pendientes individuales son negativas en ambos estratos. Las comparaciones entre filas son descriptivas (distintos *benchmarks* y métricas).

## Sensibilidad

Los archivos de sensibilidad no contienen análisis específicos de PI5 (sin efectos ni curvas recalculados) [sensibilidad.json]. Sí registran el D4 sin preprints (23/176; 13,07 %) y la contingencia del Nivel 1 («No aplica») [sensibilidad.json].

## Limitaciones

- Los grupos de turno contienen preguntas distintas (composición y dificultad), por lo que la pendiente mezcla profundidad del turno y dificultad de las preguntas [plan_sintesis.md; leyendas.json].
- Las pendientes no se agrupan entre estratos [leyendas.json].
- Solo hay 6 curvas (5 estudios) en PREDICHO y 8 (6 estudios) en SOLO_PREGUNTAS, y ninguna en GOLD ni en NR [pi15_resultados.json; leyendas.json].
- El historial es NR en 20 de 72 estudios [pi15_resultados.json; pi5_historial.csv].
- Muestra independiente de la autora: `historial_eval` coincide en 3/5 (60,0 %; IC 95 % 23,1–88,2 %); discrepancias en R00920 (SUQL) y R00924 (DIR); R00920 se corrigió a SOLO_PREGUNTAS [informe_acuerdo_extraccion.md].
- Acuerdo entre extractores en campos codificados del Nivel 2: 1824/2478 (73,6 %; IC 95 % 71,8–75,3 %) [informe_acuerdo_extraccion.md].

## Para la discusión (no forma parte de los hallazgos)

- Los estudios con historial PREDICHO son los que permiten observar propagación de errores; son 31 de 72.
- Las medidas de degradación no son comparables entre *benchmarks*, métricas ni estratos de historial.
