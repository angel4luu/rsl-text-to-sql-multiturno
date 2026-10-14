# PI3 — Vinculación de esquemas e inferencia de *joins* (Nivel 2 + contraste Nivel 1)

Pregunta: ¿qué técnicas de vinculación de esquemas e inferencia de rutas de *join* se emplean en multiturno y cómo se comparan con las de un solo turno?

Base de la taxonomía multiturno: 72 estudios del Nivel 2 con validez ≥ 50 % [pi15_resultados.json, `nivel2_umbral`; pi3_joins.csv]. Estudios con PI3 como pilar central: 13 multiturno y 156 de un turno [pi0_pilares_escenario.csv].

## Taxonomía (multiturno)

| Técnica de vinculación (`pi3_tecnica_linking`) | Estudios | % |
|---|---|---|
| NR | 22 | 30,6 |
| COINCIDENCIA_CADENAS | 15 | 20,8 |
| NINGUNA_EXPLICITA | 12 | 16,7 |
| GRAFO_ESQUEMA | 12 | 16,7 |
| LLM_PROMPTING | 10 | 13,9 |
| CLASIFICADOR_ENTRENADO | 9 | 12,5 |
| PODA_ESQUEMA | 7 | 9,7 |
| EMBEDDINGS_RECUPERACION | 6 | 8,3 |

| Inferencia de *joins* (`pi3_inferencia_joins`) | Estudios | % |
|---|---|---|
| IMPLICITA_MODELO | 54 | 75,0 |
| NR | 16 | 22,2 |
| ALGORITMICA_CAMINOS | 1 | 1,4 |
| GRAFO_FK_RESTRICCIONES | 1 | 1,4 |

Fuente: [pi3_joins.csv]. Las dos inferencias no implícitas corresponden a R00981 (UniSAr, ALGORITMICA_CAMINOS) y R00120 (PG-GSQL, GRAFO_FK_RESTRICCIONES) [pi_tabla_comparativa.csv]. Estudios que reportan errores de *join*: 10 (13,9 %) [pi5_historial.csv].

## Contraste un turno frente a multiturno (Nivel 1)

Número de estudios con cada código y porcentaje dentro de cada escenario (descriptivo) [pi34_tecnicas_escenario.csv].

| Código | Multiturno (n; %) | Un turno (n; %) |
|---|---|---|
| LLM_PROMPTING | 12; 15,6 | 75; 24,0 |
| PODA_ESQUEMA | 7; 9,1 | 53; 16,9 |
| CLASIFICADOR_ENTRENADO | 11; 14,3 | 45; 14,4 |
| EMBEDDINGS_RECUPERACION | 6; 7,8 | 47; 15,0 |
| NINGUNA_EXPLICITA | 12; 15,6 | 38; 12,1 |
| GRAFO_ESQUEMA | 13; 16,9 | 28; 8,9 |
| COINCIDENCIA_CADENAS | 17; 22,1 | 17; 5,4 |
| Joins: IMPLICITA_MODELO | 55; 71,4 | 71; 22,7 |
| Joins: GRAFO_FK_RESTRICCIONES | 1; 1,3 | 14; 4,5 |
| Joins: ALGORITMICA_CAMINOS | 1; 1,3 | 8; 2,6 |

Todos los códigos de PI3 aparecen al menos una vez en multiturno; el archivo no marca ninguno como «no trasladado» [pi34_tecnicas_escenario.csv]. Las bases de los porcentajes son las de cada escenario en ese archivo, por lo que difieren de las del Nivel 2 con validez ≥ 50 % (p. ej., LLM_PROMPTING 12 frente a 10 estudios multiturno).

## Evidencia principal: contrastes dentro del estudio

(Figura `pi_efectos_componentes`) [pi15_resultados.json; pi_efectos_componentes.csv].

| Clase de componente | Estudios | Contrastes | Mediana (pp) | Rango (pp) | Estudios +/−/nulos | % contrastes positivos |
|---|---|---|---|---|---|---|
| Vinculación de esquemas | 19 | 92 | 2,15 | 0,25 a 33,2 | 19 / 0 / 0 | 81,5 |
| Otros componentes del pilar | 15 | 143 | 2,05 | −0,2 a 24,99 | 14 / 1 / 0 | 87,4 |

## Evidencia secundaria: Δ sobre la línea base propia

Conjunto de pilares: 229 configuraciones de 43 estudios, mediana de Δ 2,8 pp [pi15_resultados.json]. Los archivos no desagregan Δ por pilar. Valores descriptivos de estudios con PI3 central [pi_tabla_comparativa.csv]: R00086 (ACT-SQL), CoSQL, QM, SOLO_PREGUNTAS, +18,3 pp; R00298 (SQLformer), SPARC, IM, +4,1 pp; R00120 (PG-GSQL), SPARC, QM, PREDICHO, +5,9 pp.

## Confianza en los hallazgos

| Hallazgo | Limit. metodológicas (validez media) | Coherencia | Suficiencia | Pertinencia | Confianza |
|---|---|---|---|---|---|
| Vinculación de esquemas: +2,1 pp (19/19) | sin (76,3) | sin | sin | leves | alta |
| Otros componentes: +2,0 pp (14/15) | sin (75,3) | sin | sin | leves | alta |

Fuente: [confianza_hallazgos.csv].

## Sensibilidad

[sensibilidad.json]

| Clase | Principal (mediana pp; estudios) | Reincorporar bajo umbral | Sin preprints |
|---|---|---|---|
| Vinculación de esquemas | 2,15; 19 | 2,15; 19 | 1,3; 16 |
| Otros componentes | 2,05; 15 | 2,58; 16 | 2,05; 13 |

Sin preprints, la mediana de «Vinculación de esquemas» pasa de 2,15 a 1,3 pp. Reincorporar estudios bajo el umbral añade un estudio a «Otros componentes» y cambia su mediana de 2,05 a 2,58 pp.

## Limitaciones

- Acuerdo entre extractores en campos codificados del Nivel 2: 1824/2478 (73,6 %; IC 95 % 71,8–75,3 %) [informe_acuerdo_extraccion.md].
- Solo 1 estudio multiturno usa inferencia algorítmica de caminos y 1 grafo FK con restricciones; los datos no permiten contrastar inferencia implícita y algorítmica con contrastes dentro del estudio [pi3_joins.csv; pi_efectos_componentes.csv].
- Los archivos no contienen un análisis de escala (tamaño del esquema); no se reporta.
- El contraste un turno frente a multiturno compara frecuencias de códigos, no resultados; los estudios de un turno solo se caracterizan en el Nivel 1 [plan_sintesis.md].
- Las comparaciones entre estudios son descriptivas [plan_sintesis.md].

## Para la discusión (no forma parte de los hallazgos)

- La inferencia de *joins* es implícita al modelo en la gran mayoría de los estudios multiturno (75,0 %).
- Las técnicas de un turno se encuentran en multiturno con frecuencias relativas distintas.
