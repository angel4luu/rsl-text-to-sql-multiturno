# PI4 — Retroalimentación de ejecución y autocorrección (Nivel 2 + contraste Nivel 1)

Pregunta: ¿qué mecanismos de retroalimentación de ejecución y autocorrección se han aplicado al escenario multiturno y cómo se comparan con los de un solo turno?

Base de la taxonomía multiturno: 72 estudios del Nivel 2 con validez ≥ 50 % [pi15_resultados.json, `nivel2_umbral`; pi4_mecanismos.csv]. Estudios con PI4 como pilar central: 22 multiturno y 140 de un turno [pi0_pilares_escenario.csv].

## Taxonomía (multiturno)

| Mecanismo (`pi4_mecanismo`) | Estudios | % |
|---|---|---|
| NR | 46 | 63,9 |
| ACLARACION_USUARIO | 18 | 25,0 |
| EJECUCION_FEEDBACK_ERRORES | 10 | 13,9 |
| ABSTENCION | 4 | 5,6 |
| AUTODEPURACION_LLM | 4 | 5,6 |
| VERIFICADOR_CRITICO | 2 | 2,8 |
| REPARACION_SIMBOLICA | 1 | 1,4 |

| Señal (`pi4_senal`) | Estudios | % |
|---|---|---|
| NR | 47 | 65,3 |
| USUARIO | 16 | 22,2 |
| RESULTADO_EJECUCION | 9 | 12,5 |
| ERROR_DBMS | 9 | 12,5 |
| JUICIO_LLM | 3 | 4,2 |
| RESULTADO_VACIO | 2 | 2,8 |

Mecanismo aplicado al escenario multiturno (`pi4_aplicado_multiturno`): SI 30 estudios (41,7 %), NO 42 (58,3 %). Fuente: [pi4_mecanismos.csv]. Ejemplos: R00123 (*Speak to your parser*, ACLARACION_USUARIO), R00160 (*Learn From Mistakes*, EJECUCION_FEEDBACK_ERRORES), R00508 (HarnessSQL, EJECUCION_FEEDBACK_ERRORES; AUTODEPURACION_LLM; ACLARACION_USUARIO), R00109 (PICARD, REPARACION_SIMBOLICA), R00511 (VERIFICADOR_CRITICO) [pi_tabla_comparativa.csv].

## Contraste un turno frente a multiturno (Nivel 1)

Número de estudios y porcentaje dentro de cada escenario (descriptivo) [pi34_tecnicas_escenario.csv].

| Código | Multiturno (n; %) | Un turno (n; %) |
|---|---|---|
| EJECUCION_FEEDBACK_ERRORES | 10; 13,0 | 99; 31,6 |
| VERIFICADOR_CRITICO | 2; 2,6 | 64; 20,4 |
| AUTODEPURACION_LLM | 4; 5,2 | 46; 14,7 |
| AUTOCONSISTENCIA_VOTACION | 0; 0,0 | 42; 13,4 |
| ACLARACION_USUARIO | 22; 28,6 | 7; 2,2 |
| ABSTENCION | 5; 6,5 | 8; 2,6 |
| REPARACION_SIMBOLICA | 1; 1,3 | 6; 1,9 |
| Señal: RESULTADO_EJECUCION | 9; 11,7 | 100; 31,9 |
| Señal: ERROR_DBMS | 9; 11,7 | 63; 20,1 |
| Señal: JUICIO_LLM | 3; 3,9 | 55; 17,6 |
| Señal: USUARIO | 20; 26,0 | 9; 2,9 |

El único código marcado como no trasladado al multiturno es AUTOCONSISTENCIA_VOTACION (0 multiturno; 42 de un turno) [pi34_tecnicas_escenario.csv; pi0_resultados.json]. Las bases de porcentaje de este archivo difieren de las del Nivel 2 con validez ≥ 50 % (p. ej., ACLARACION_USUARIO 22 frente a 18 estudios).

## Evidencia principal: contrastes dentro del estudio

(Figura `pi_efectos_componentes`) [pi15_resultados.json; pi_efectos_componentes.csv].

| Clase de componente | Estudios | Contrastes | Mediana (pp) | Rango (pp) | Estudios +/−/nulos | % contrastes positivos |
|---|---|---|---|---|---|---|
| Autocorrección / retroalimentación de ejecución | 11 | 141 | 1,5 | 0,01 a 13,76 | 11 / 0 / 0 | 93,6 |
| Aclaración / interacción con el usuario | 3 | 7 | 8,9 | −19,05 a 43,0 | 2 / 1 / 0 | 71,4 |
| Autoconsistencia / selección de candidatos | 2 | 9 | 1,1 | 0,2 a 2,0 | 2 / 0 / 0 | 88,9 |
| Otros componentes del pilar | 11 | 90 | 4,1 | −2,3 a 13,75 | 10 / 1 / 0 | 86,7 |

## Evidencia secundaria: Δ sobre la línea base propia

Conjunto de pilares: 229 configuraciones de 43 estudios, mediana de Δ 2,8 pp [pi15_resultados.json]; sin desagregar por pilar. Valores descriptivos de estudios con PI4 central [pi_tabla_comparativa.csv]: R00160 (*Learn From Mistakes*), CoSQL, IEX, +14,4 pp; R00311 (*Learning to Clarify*), AmbigSQL, *Post-clarification EX*, PREDICHO, +2,3 pp; R00312 (QDA-SQL), SPARC, IM, +29,8 pp; R00526 (*Prompt Engineering… Arabic*), SPARC, EX, +1,0 pp; R00508 (HarnessSQL), Spider, EX, PREDICHO, +32,6 pp.

## Criterio de reformulación de la brecha (M8)

Sin cambios respecto de PI2: `estudios_que_combinan_a_b_c` vacío, `n` 0, `reformular_tesis` false; sensibilidad con grafos neuronales, `n` 0; `sin_entrenamiento_entre_ellos` vacío [pi15_resultados.json, `brecha_M8`].

## Confianza en los hallazgos

| Hallazgo | Limit. metodológicas (validez media) | Coherencia | Suficiencia | Pertinencia | Confianza |
|---|---|---|---|---|---|
| Autocorrección / ejecución: +1,5 pp (11/11) | leves (72,7) | sin | sin | leves | moderada |
| Aclaración / usuario: +8,9 pp (2/3) | sin (80,0) | leves | leves | importantes | moderada |
| Autoconsistencia: +1,1 pp (2/2) | leves (70,0) | sin | importantes | sin | moderada |
| Otros componentes: +4,1 pp (10/11) | sin (77,3) | sin | sin | leves | alta |

Fuente: [confianza_hallazgos.csv].

## Sensibilidad

[sensibilidad.json]

| Clase | Principal (mediana pp; estudios) | Reincorporar bajo umbral | Sin preprints |
|---|---|---|---|
| Autocorrección / ejecución | 1,5; 11 | 1,5; 12 | 1,5; 7 |
| Aclaración / usuario | 8,9; 3 | 8,9; 3 | no reportada |
| Autoconsistencia | 1,1; 2 | 1,1; 2 | 1,1; 2 |
| Otros componentes | 4,1; 11 | 3,1; 12 | 2,98; 6 |

La mediana de «Otros componentes» pasa de 4,1 a 3,1 pp al reincorporar y a 2,98 pp sin preprints. La clase «Aclaración» no figura en el análisis sin preprints.

## Limitaciones

- Acuerdo entre extractores en campos codificados del Nivel 2: 1824/2478 (73,6 %; IC 95 % 71,8–75,3 %) [informe_acuerdo_extraccion.md].
- El mecanismo es NR en 46 de 72 estudios [pi15_resultados.json; pi4_mecanismos.csv].
- Las clases «Aclaración» (3 estudios, 7 contrastes) y «Autoconsistencia» (2 estudios, 9 contrastes) tienen pocos estudios; su suficiencia es «leves» e «importantes» [confianza_hallazgos.csv].
- La clase «Aclaración» tiene pertinencia/comparabilidad «importantes» [confianza_hallazgos.csv].
- Comparaciones entre estudios solo descriptivas; los estudios de un turno se caracterizan solo en el Nivel 1 [plan_sintesis.md].

## Para la discusión (no forma parte de los hallazgos)

- La aclaración con el usuario es proporcionalmente más frecuente en multiturno que en un turno, y el recurso a ejecución y verificación es proporcionalmente menos frecuente.
- Los contrastes de autocorrección por ejecución son positivos en todos los estudios, con medianas de magnitud moderada.
