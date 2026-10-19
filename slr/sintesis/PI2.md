# PI2 — Representación y actualización del estado del diálogo (Nivel 2)

> **Nota (revisión posterior al cierre, 2026-10-19):** las cifras de efectos por clase de este archivo están superadas. Tras reasignar componentes de «Otros» (`otros_subclases.csv`, `revision_otros.md`), los valores vigentes están en `tablas/pi_efectos_componentes.csv`, `confianza_hallazgos.csv` y `sensibilidad.json`.


Pregunta: ¿cómo se representa y actualiza el estado del diálogo y cómo influye en el rendimiento a lo largo de los turnos?

Base: 72 estudios del Nivel 2 con validez ≥ 50 % [pi15_resultados.json, `nivel2_umbral`; pi2_representacion.csv]. Estudios con PI2 como pilar central: 26 [pi0_pilares_escenario.csv].

## Taxonomía

| Representación (`pi2_representacion`) | Estudios | % |
|---|---|---|
| HISTORIAL_PLANO | 38 | 52,8 |
| SQL_PREVIO_EDICION | 11 | 15,3 |
| NR | 11 | 15,3 |
| ESTRUCTURA_EXPLICITA | 10 | 13,9 |
| GRAFO | 9 | 12,5 |
| MEMORIA_EXTERNA | 7 | 9,7 |
| VENTANA_DESLIZANTE | 5 | 6,9 |
| RESUMEN | 1 | 1,4 |

| Actualización (`pi2_actualizacion`) | Estudios | % |
|---|---|---|
| IMPLICITA_NEURONAL | 34 | 47,2 |
| NR | 16 | 22,2 |
| REGLAS_DETERMINISTAS | 16 | 22,2 |
| LLM_GENERATIVA | 12 | 16,7 |

| Coste del contexto (`pi2_coste_contexto`) | Estudios | % |
|---|---|---|
| CRECE_CON_TURNOS | 36 | 50,0 |
| NR | 22 | 30,6 |
| ACOTADO | 14 | 19,4 |

Fuente: [pi2_representacion.csv]. Para los grafos: nodos de tipo ELEMENTOS_ESQUEMA 8 estudios, TOKENS_PREGUNTA 4, VALORES_BD 2 (NR 64); grafo dinámico SI 7, NO 1 (NR 64) [pi2_representacion.csv]. Ejemplos: ESTRUCTURA_EXPLICITA en R00033 (Rose-SQL), R00099 (*In-Context Learning for Few-Shot Dialogue State Tracking*), R00480 (SemPlan), R01029 (*Tracking Interaction States*); GRAFO en R00117 (IGSQL), R00936 (*interaction-modeling*, grafo heterogéneo), R01037 (*Dynamic Hybrid Relation Network*); SQL_PREVIO_EDICION en R00072 (CoE-SQL), R00131 (EditSQL) [pi_tabla_comparativa.csv].

## Evidencia principal: contrastes dentro del estudio

(Figura `pi_efectos_componentes`) [pi15_resultados.json; pi_efectos_componentes.csv].

| Clase de componente | Estudios | Contrastes | Mediana (pp) | Rango (pp) | Estudios +/−/nulos | % contrastes positivos |
|---|---|---|---|---|---|---|
| Grafo / estado estructurado | 11 | 74 | 2,9 | 0,5 a 32,0 | 11 / 0 / 0 | 95,9 |
| SQL / resultados previos | 7 | 41 | 5,65 | −0,1 a 10,45 | 6 / 1 / 0 | 90,2 |
| Otros componentes del pilar | 22 | 124 | 2,85 | −0,7 a 17,8 | 21 / 1 / 0 | 91,9 |

## Evidencia secundaria: Δ sobre la línea base propia

Conjunto de pilares: 229 configuraciones de 43 estudios, mediana de Δ 2,8 pp [pi15_resultados.json]. Valores descriptivos de estudios de PI2 (cada uno en su *benchmark*, métrica e historial) [pi_tabla_comparativa.csv]: R00072 (CoE-SQL), SPARC, EM(QM), PREDICHO, +6,0 pp; R01029, CoSQL, QM, PREDICHO, +4,5 pp; R00117 (IGSQL), SPARC, IM, PREDICHO, +4,2 pp; R00936, SPARC, QM, +0,8 pp; R01037, SPARC, QM, +7,9 pp; R00131 (EditSQL), SPARC, QM, +27,8 pp (historial registrado como PREDICHO;GOLD).

## Criterio de reformulación de la brecha (M8)

Resultado tal como figura en [pi15_resultados.json, `brecha_M8`]:

- `estudios_que_combinan_a_b_c`: lista vacía; `n`: 0.
- `reformular_tesis`: false.
- `sensibilidad_grafos_neuronales`: estudios, lista vacía; `n`: 0.
- `sin_entrenamiento_entre_ellos`: lista vacía.

Definiciones aplicadas: (a) estado estructurado explícito, (b) inferencia algorítmica de *joins* o autocorrección por ejecución, (c) historial PREDICHO o SOLO_PREGUNTAS [01_preguntas_picoc.md]. El umbral de reformulación es ≥ 2 estudios [01_preguntas_picoc.md].

## Confianza en los hallazgos

| Hallazgo | Limit. metodológicas (validez media) | Coherencia | Suficiencia | Pertinencia | Confianza |
|---|---|---|---|---|---|
| Grafo / estado estructurado: +2,9 pp (11/11) | sin (79,1) | sin | sin | leves | alta |
| SQL / resultados previos: +5,7 pp (6/7) | sin (81,4) | sin | sin | leves | alta |
| Otros componentes: +2,9 pp (21/22) | sin (76,8) | sin | sin | leves | alta |

Fuente: [confianza_hallazgos.csv]. Las medianas figuran redondeadas en el texto del hallazgo del archivo.

## Sensibilidad

[sensibilidad.json]

| Clase | Reincorporar bajo umbral (mediana pp; estudios) | Sin preprints (mediana pp; estudios) |
|---|---|---|
| Grafo / estado estructurado | 2,9; 11 | 2,9; 7 |
| SQL / resultados previos | 5,65; 7 | 3,33; 6 |
| Otros componentes | 2,85; 22 | 2,65; 17 |

Sin preprints, la mediana de «SQL / resultados previos» pasa de 5,65 a 3,33 pp; las demás medianas varían poco o nada.

## Limitaciones

- Acuerdo entre extractores en campos codificados del Nivel 2: 1824/2478 (73,6 %; IC 95 % 71,8–75,3 %) [informe_acuerdo_extraccion.md].
- Los archivos no incluyen el cruce entre tipo de representación y coste del contexto; solo se reportan las frecuencias marginales [pi2_representacion.csv].
- Los campos de grafo (nodos, dinámico) son NR en 64 de 72 estudios [pi15_resultados.json; pi2_representacion.csv].
- Comparaciones entre estudios solo descriptivas [plan_sintesis.md].
- La clase «Otros componentes del pilar» agrupa componentes heterogéneos [pi_efectos_componentes.csv].

## Para la discusión (no forma parte de los hallazgos)

- Ningún estudio del Nivel 2 cumple a la vez (a), (b) y (c) según los criterios registrados.
- La representación más frecuente es el historial plano; las estructuradas explícitas y los grafos son minoritarias.
