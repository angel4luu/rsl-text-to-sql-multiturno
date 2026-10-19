# PI1 — Restauración del contexto conversacional (Nivel 2)

> **Nota (revisión posterior al cierre, 2026-10-19):** las cifras de efectos por clase de este archivo están superadas. Tras reasignar componentes de «Otros» (`otros_subclases.csv`, `revision_otros.md`), los valores vigentes están en `tablas/pi_efectos_componentes.csv`, `confianza_hallazgos.csv` y `sensibilidad.json`.


Pregunta: ¿qué técnicas se usan para restaurar el contexto (elipsis, correferencia, reescritura con historial) y qué resultados reportan?

Base: 72 estudios multiturno del Nivel 2 con validez ≥ 50 % (denominador de los porcentajes de la taxonomía) [pi15_resultados.json, `nivel2_umbral`; pi1_tecnicas.csv]. Los estudios con PI1 como pilar central son 13 [pi0_pilares_escenario.csv].

## Taxonomía de técnicas

| Técnica (`pi1_tecnica`) | Estudios | % |
|---|---|---|
| CONCATENACION | 35 | 48,6 |
| NR (no reportado) | 25 | 34,7 |
| REESCRITURA | 12 | 16,7 |
| CLASIFICACION_DISCURSO | 2 | 2,8 |
| RESOLUCION_EXPLICITA | 2 | 2,8 |

Fuente: [pi1_tecnicas.csv]. Un estudio puede tener más de un código.

| Insumo del historial (`pi1_insumos_historial`) | Estudios | % |
|---|---|---|
| PREGUNTAS_PREVIAS | 59 | 81,9 |
| SQL_PREVIOS | 32 | 44,4 |
| RESPUESTAS_SISTEMA | 13 | 18,1 |
| NR | 11 | 15,3 |
| RESULTADOS_EJECUCION | 3 | 4,2 |

Fuente: [pi1_tecnicas.csv]. Ejemplos de estudios con reescritura: R00033 (Rose-SQL), R00086 (ACT-SQL), R00097 (CQR-SQL), R00924 (DIR), R00950 (QURG), R01034 (FANDA); con concatenación y sin reescritura: R00072 (CoE-SQL), R00100 (*Self-Play*) [pi_tabla_comparativa.csv].

## Evidencia principal: contrastes dentro del estudio

Contrastes con el componente activado frente a desactivado, mismo modelo base y configuración, en puntos porcentuales (pp) (Figura `pi_efectos_componentes`) [pi15_resultados.json; pi_efectos_componentes.csv].

| Clase de componente | Estudios | Contrastes | Mediana (pp) | Rango (pp) | Estudios +/−/nulos | % contrastes positivos |
|---|---|---|---|---|---|---|
| Reescritura de la pregunta | 5 | 46 | 1,95 | −4,75 a 19,15 | 4 / 1 / 0 | 73,9 |
| Concatenación / historial | 3 | 16 | 0,6 | 0,15 a 1,99 | 3 / 0 / 0 | 87,5 |
| Otros componentes del pilar | 17 | 119 | 2,35 | −0,2 a 25,0 | 16 / 1 / 0 | 92,4 |

Pregunta específica (reescritura frente a concatenación): ambas clases tienen efecto de dirección positiva en la mayoría de los estudios; las medianas son 1,95 pp (reescritura, 5 estudios) y 0,6 pp (concatenación, 3 estudios) [pi_efectos_componentes.csv]. Son clases de contrastes distintos, no una comparación directa dentro de un mismo estudio; la comparación es descriptiva.

## Evidencia secundaria: Δ sobre la línea base propia

Para el conjunto de pilares (no desagregado por pilar en los archivos): 229 configuraciones de 43 estudios, mediana de Δ 2,8 pp [pi15_resultados.json]. Valores de estudios con reescritura, cada uno en su propio *benchmark*, métrica e historial (descriptivo, sin comparación entre ellos) [pi_tabla_comparativa.csv]: R00033 (Rose-SQL), SPARC, IM-EX, +14,77 pp; R00086 (ACT-SQL), CoSQL, QM, SOLO_PREGUNTAS, +18,3 pp; R00924 (DIR), CoSQL, QM, SOLO_PREGUNTAS, +27,17 pp; R01034 (FANDA), FollowUp, *Symbol Accuracy*, SOLO_PREGUNTAS, +23,5 pp; R00222 (SiriusBI), MRD-BIRD, EX, SOLO_PREGUNTAS, +0,53 pp.

## Confianza en los hallazgos

| Hallazgo | Limit. metodológicas (validez media) | Coherencia | Suficiencia | Pertinencia | Confianza |
|---|---|---|---|---|---|
| Concatenación / historial: +0,6 pp (3/3 positivos) | leves (66,7) | sin | leves | sin | moderada |
| Reescritura de la pregunta: +1,9 pp (4/5 positivos) | sin (76,0) | leves | sin | sin | alta |
| Otros componentes: +2,4 pp (16/17 positivos) | sin (77,1) | sin | sin | leves | alta |

Fuente: [confianza_hallazgos.csv; pi15_resultados.json]. Las medianas se reproducen tal como figuran en el texto del hallazgo del archivo.

## Sensibilidad

- Reincorporar estudios bajo el umbral de validez: Concatenación 0,6 pp (3 estudios); Reescritura 1,95 pp (5); Otros componentes 2,35 pp (17); sin cambio respecto del análisis principal [sensibilidad.json].
- Excluir preprints: Concatenación 0,6 pp (3); Reescritura 1,95 pp (5); Otros componentes 2,35 pp (17); sin cambio [sensibilidad.json].

## Limitaciones

- Acuerdo entre extractores en campos codificados del Nivel 2: 1824/2478 (73,6 %; IC 95 % 71,8–75,3 %) [informe_acuerdo_extraccion.md].
- Muestra independiente de la autora (5 estudios): resultados principales presentes en `resultados.csv` 10/15 (66,7 %; IC 95 % 41,7–84,8 %) [informe_acuerdo_extraccion.md].
- La clase «Concatenación / historial» tiene 3 estudios; con menos de 3 contrastes la coherencia se califica como máximo «leves» según el plan [plan_sintesis.md].
- Las comparaciones entre estudios son descriptivas (distintos *benchmarks*, métricas e historiales) [plan_sintesis.md].
- La clase «Otros componentes del pilar» agrupa componentes heterogéneos [pi_efectos_componentes.csv].

## Para la discusión (no forma parte de los hallazgos)

- Las medianas de los contrastes de PI1 son del orden de unos pocos pp, con un rango amplio en reescritura.
- Un 34,7 % de los estudios no reporta la técnica de restauración de contexto (NR).
