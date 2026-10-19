# Revisión: subclases de «Otros componentes del pilar» (refactor posterior al cierre, 2026-10-19)

Datos: `slr/sintesis/otros_subclases.csv`. Textos completos: `slr/texto_completo/texto/<ID>.txt` (o `texto_bola/`). Escriba su respuesta después de «Respuesta:» en cada punto.

## Opciones

| Sección | Respuestas válidas |
|---|---|
| A (subclases) | **OK** (aceptar) · **CAMBIAR:** texto libre |
| B (reasignaciones a una clase existente) | **SI** (reasignar) · **NO** (dejar en «Otros») |
| C (casos dudosos) | código de la subclase de la tabla de códigos, o **SIN** (sin agrupar) |

## Códigos de subclase

| Código | Pilar | Subclase |
|---|---|---|
| PI1-1 | PI1 | Análisis del discurso, la intención y la correferencia |
| PI1-2 | PI1 | Selección, alineación y codificación del historial |
| PI1-3 | PI1 | Entrenamiento, objetivos auxiliares y datos |
| PI2-1 | PI2 | Gestión del historial y la memoria |
| PI2-2 | PI2 | Entrenamiento, objetivos auxiliares y datos |
| PI3-1 | PI3 | Enriquecimiento del esquema y del contenido |
| PI3-2 | PI3 | Vistas generadas |
| PI3-3 | PI3 | Decodificación y razonamiento guiados |
| PI3-4 | PI3 | Entrenamiento, objetivos auxiliares y datos |
| PI4-1 | PI4 | Agentes con herramientas |
| PI4-2 | PI4 | Detección de ambigüedad y consulta de la intención |
| PI4-3 | PI4 | Decodificación restringida |
| PI4-4 | PI4 | Entrenamiento, objetivos auxiliares y datos |

## A. Subclases propuestas

La clase transversal «Entrenamiento, objetivos auxiliares y datos» reúne estrategias de entrenamiento (preentrenamiento, objetivos auxiliares, RL/SFT, aumento de datos) que no son técnicas propias del pilar.

| Pilar | Subclase | Componentes | Estudios | Ejemplos |
|---|---|---|---|---|
| PI1 | Análisis del discurso, la intención y la correferencia | 8 | 4 | ANALISIS_DIFERENCIAS_ENTRE_PREGUNTA; ANALISIS_DIFERENCIA_PREGUNTAS; CLASIFICACION_DISCURSO: intención A |
| PI1 | Entrenamiento, objetivos auxiliares y datos | 14 | 7 | ANONIMIZACION; APRENDIZAJE_MULTITAREA_CON_PROMPTS; CONSISTENCIAS_SGKL_Y_SPKL_CON_BOW_F |
| PI1 | Otros (sin agrupar) | 2 | 1 | EXPLICACION; PREGUNTA |
| PI1 | Selección, alineación y codificación del historial | 12 | 8 | AJUSTE_DEL_RECUPERADOR_SBERT para s; Enhance dialogue turn; MODELO_RANKING (FAnDa – Ranking, ra |
| PI2 | Entrenamiento, objetivos auxiliares y datos | 18 | 8 | AUMENTO_DATOS_SELF_PLAY (w/o PICARD; AUMENTO_DATOS_SELF_PLAY (with PICAR; AUMENTO_TURNOS_DIALOGO |
| PI2 | Gestión del historial y la memoria | 18 | 12 | AGREGACION_A_NIVEL_DE_TURNO; CONTEXTO_32K vs 8K; EQQ (pares pregunta-SQL extraídos d |
| PI2 | Otros (sin agrupar) | 2 | 2 | NL2IR2SQL (IR + compilador determin; P_ALIGN |
| PI3 | Decodificación y razonamiento guiados | 5 | 4 | AUTO_COT; CONSTRAINED_DECODING; ROLE_STATE (razonamiento guiado por |
| PI3 | Enriquecimiento del esquema y del contenido | 25 | 11 | ACID; DCRE añadido a DCRI, sin decaimient; DCRI añadido a DCRE, sin decaimient |
| PI3 | Entrenamiento, objetivos auxiliares y datos | 3 | 1 | SLP (sin ULP); SQL-similarity filtering of SLP lab; ULP+SLP (both objectives) |
| PI3 | Vistas generadas | 5 | 1 | VISTAS_AUTOGENERADAS en DIN-SQL; VISTAS_AUTOGENERADAS_EN_DIN_SQL; VISTAS_GENERADAS_POR_DeepSeek-v4-pr |
| PI4 | Agentes con herramientas | 3 | 2 | AGENTE_CON_HERRAMIENTAS_BD_Y_SKILLS; AGENTE_HERRAMIENTA_BD_CODEX; RAZONAMIENTO_LONG_HORIZON (vs direc |
| PI4 | Decodificación restringida | 2 | 1 | PICARD: parsing incremental con gua; PICARD_PARSING_GUARDS |
| PI4 | Detección de ambigüedad y consulta de la intención | 4 | 3 | DECOMPOSER; DETECTOR; Intention querying (Q) |
| PI4 | Entrenamiento, objetivos auxiliares y datos | 14 | 6 | ALGORITMO_RL: DAPO vs GRPO; ENTRENAMIENTO_HARNESS_NATIVE_VS_NON; ENTRENAMIENTO_HARNESS_NATIVO vs NO_ |

Respuesta A:OK

## B. Reasignaciones propuestas a una clase existente (la expresión regular no las detectó)

Si se aceptan, cambian los recuentos de esas clases en la Tabla VI y la Figura 6.

**B1.** PI2 → «Grafo / estado estructurado»: SST, SST+UDT, SST_CON_DATOS_PROPIOS, SST_CON_DATOS_SCORE (R00096). Motivo: R00096: «schema state tracking (SST) objective … schema slot».

Respuesta B1: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**B2.** PI2 → «SQL / resultados previos»: REUSE_AND_PATCH, SELECCION_VERSION_HISTORICA (R00499). Motivo: R00499: reutiliza o selecciona versiones previas.

Respuesta B2: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**B3.** PI3 → «Vinculación de esquemas»: ALL2C, C2C, MODO_ALL2C, MODO_C2C, MODO_V2C, V2C (R00453). Motivo: R00453 p. 1: «three linking modes» (C2C, V2C, ALL2C).

Respuesta B3: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**B4.** PI3 → «Vinculación de esquemas»: DB_CONTENT, DB_CONTENT (RASAT-small), DB_CONTENT (T5-small), VALORES_CELDA_ORACULO, VALORES_ORACULO_EN_RECUPERACION (R00041/R00101). Motivo: vinculación de valores (contenido de la BD), incluida en la definición de vinculación del protocolo.

Respuesta B4: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**B5.** PI4 → «Autocorrección / retroalimentación de ejecución»: GUIA_GENERAL_GG (R00160). Motivo: R00160: el maestro corrige errores del alumno («general guidance»).

Respuesta B5: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
## C. Casos dudosos (asignación propuesta entre paréntesis)

**C1.** PI1 · `EXPLICACION` (R00105) — R00105 (NL-EDIT): explicación del SQL y corrección por retroalimentación del usuario; codificado en PI1. Propuesta: SIN (Otros (sin agrupar)).

Respuesta C1: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**C2.** PI1 · `PREGUNTA` (R00105) — R00105 (NL-EDIT): explicación del SQL y corrección por retroalimentación del usuario; codificado en PI1. Propuesta: SIN (Otros (sin agrupar)).

Respuesta C2: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**C3.** PI1 · `UDT` (R00096) — R00096: objetivos auxiliares de seguimiento (estado del esquema / dependencia entre enunciados). Propuesta: PI1-3 (Entrenamiento, objetivos auxiliares y datos).

Respuesta C3: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**C4.** PI2 · `NL2IR2SQL (IR + compilador determinista; sin él se usa XiYan` (R00453) — R00453: representación intermedia + compilador determinista. Propuesta: SIN (Otros (sin agrupar)).

Respuesta C4: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**C5.** PI2 · `OPTIMIZACION_RL_RECUPERACION` (R00438) — R00438/R00099: recuperación aprendida de memoria o de ejemplos (método de recuperación vs. entrenamiento). Propuesta: PI2-1 (Gestión del historial y la memoria).

Respuesta C5: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**C6.** PI2 · `OPTIMIZACION_RL_SELECTOR` (R00438) — R00438/R00099: recuperación aprendida de memoria o de ejemplos (método de recuperación vs. entrenamiento). Propuesta: PI2-1 (Gestión del historial y la memoria).

Respuesta C6: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**C7.** PI2 · `P_ALIGN` (R00084) — R00084: alineación texto–SQL para la generalización composicional. Propuesta: SIN (Otros (sin agrupar)).

Respuesta C7: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**C8.** PI2 · `RETRIEVER_AJUSTADO_VS_SBERT_NO_SUPERVISADO` (R00099) — R00438/R00099: recuperación aprendida de memoria o de ejemplos (método de recuperación vs. entrenamiento). Propuesta: PI2-1 (Gestión del historial y la memoria).

Respuesta C8: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)
**C9.** PI4 · `SIMULACION_MULTITURNO;50 conversaciones` (R00311) — R00311: autoentrenamiento contrastivo con conversaciones simuladas. Propuesta: PI4-4 (Entrenamiento, objetivos auxiliares y datos).

Respuesta C9: aceptado (la autora aceptó todas las propuestas en la sesión del 2026-10-19)