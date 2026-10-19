# Decisión de la autora — Fase 14, paso 5

Fecha: 2026-10-14.

## Decisión

Se decide **ajustar** la propuesta. Se mantiene como producto principal un artefacto software funcional para *Text-to-SQL* multiturno, encuadrado como investigación en ciencia del diseño (*design science research*): se construye un artefacto y se evalúa su utilidad. No se conserva la propuesta sin cambios: se reduce el alcance de las afirmaciones, se separa lo sustentado por la RSL de las decisiones de ingeniería, se concentra la innovación en un solo componente y se retiran del alcance los mecanismos sin respaldo directo.

## Razón expresada por la autora

La autora elige ajustar porque desea que su investigación, derivada del tema de la RSL sobre *Text-to-SQL* multiturno, produzca un artefacto software, y no un estudio comparativo. Considera compatible que la propuesta tenga un artefacto como producto y, al mismo tiempo, una evaluación que permita comprobar el aporte de su componente innovador. La cercanía con la propuesta original se conserva por el dominio, el tipo de producto y su mecanismo central, no porque se presuponga que obtendrán un resultado favorable.

Esta razón es de Ingeniería de Software y de preferencia de producto; no se presenta como un hallazgo de eficacia de la RSL. La evidencia se usa para construir la base del artefacto, delimitar el componente innovador y definir cómo se evalúa.

En el paso 4a se declaró el costo hundido como motivo para conservar OE2 (`desafio_socratico.md`, ítem 6). Para que ese riesgo no condicione los resultados, el componente innovador se evalúa frente a una base construida con prácticas que tienen evidencia favorable en la RSL, y el plan de análisis se fija antes de ejecutar los experimentos.

## Alcance decidido

### Estructura del artefacto

| Capa | Contenido | Origen |
|---|---|---|
| **Base** | Canalización sin entrenamiento basada en *prompting* de un LLM: vinculación del esquema por *prompting*, historial con reutilización del SQL previo como contexto y validación por ejecución | Prácticas predominantes de la RSL, seleccionadas por ser frecuentes **y** contar con evidencia favorable |
| **Componente innovador** | Grafo de estado de dos capas con puntos de control y **recuperación guiada por ejecución**: ante una señal de fallo en un turno, el sistema vuelve al último estado válido | Aporte propio; atiende la propagación de errores bajo historial predicho |
| **Subsistema de evaluación** | Repetición de diálogos con historial predicho, métricas por turno, tasa de recuperación tras un turno fallido, *tokens* y coste, trazas de transición del estado | Brecha DC de la RSL; entregable de Ingeniería de Software |

La reutilización del SQL previo forma parte de la base porque la RSL muestra evidencia favorable para esa clase (SQL previo, edición o ventana: 12 estudios, 11 positivos, mediana +5,08 pp). <!-- mapa_evidencia.md: OE2/Contrastes dentro del estudio --> «Frecuente» no se presenta como «eficaz»: cada práctica de la base se identifica en el texto por su frecuencia y, por separado, por su evidencia.

### Arquitectura multiagente y ausencia de entrenamiento

Se conserva una arquitectura multiagente ligera, de tres o cuatro agentes con funciones delimitadas (diálogo y estado, esquema, generación SQL, validación). La RSL documenta una tendencia creciente del paradigma de agentes como enfoque principal (1, 6, 27 y 43 estudios en 2023, 2024, 2025 y 2026, este último parcial), lo que respalda su vigencia, no su eficacia. <!-- slr/sintesis/PI0.md: Paradigma técnico principal por año --> La ausencia de entrenamiento se justifica por factibilidad (sin GPU; `restricciones_autora.md`). No se afirmará que ninguna de las dos premisas mejora la exactitud, pues no existen contrastes comparativos para ellas. <!-- mapa_evidencia.md: Premisas transversales --> La coordinación entre agentes no se plantea como un segundo aporte.

### Evaluación

La evaluación tiene dos partes:

1. **Calidad del software:** corrección de las mutaciones del estado, conformidad de interfaces, cobertura de pruebas, reproducibilidad de las ejecuciones y trazabilidad SQL–estado, con métricas definidas operacionalmente en el paso 6.
2. **Eficacia del componente innovador mediante ablación**, en una sola cadena de tres configuraciones del mismo artefacto: base → base + grafo de estado → base + grafo + recuperación. Se miden la exactitud por turno bajo historial predicho, la tasa de recuperación tras un turno fallido y el coste.

No se compara un conjunto de estrategias como pares; la ablación es el mínimo necesario para sostener que el componente innovador aporta algo.

*Benchmark* principal: SParC. CoSQL se añadirá solo si el presupuesto de API estimado lo permite.

### Fuera del alcance

La restauración lingüística como módulo propio, el enrutamiento mediante caminos o árbol de Steiner y la autorreparación de doble etapa quedan **fuera del alcance** y se registran como trabajo futuro. No se mantienen como extensiones opcionales, para no ampliar el alcance durante la implementación. El enrutamiento simbólico carece de contrastes directos en la RSL, la inferencia de *joins* es implícita en el modelo en 54 de 72 estudios multiturno (75,0 %) y la combinación integral solo demuestra novedad dentro del corpus, no eficacia. <!-- mapa_evidencia.md: OE3/Contrastes dentro del estudio; Conjunción M8; latex/slr/secciones/04b-resultados.tex: PI3 --> Tampoco se incluyen esquemas empresariales, por no disponerse de esos datos.

## Contraste con la propuesta original

| Propuesta original (anterior a la RSL) | Lo que mostró la RSL | Propuesta ajustada |
|---|---|---|
| OE1 preprocesamiento lingüístico (HE1) | La concatenación del historial y la reescritura son las técnicas más frecuentes | Absorbido por la base mediante *prompting*; sin módulo propio |
| OE2 grafo de estado de dos capas (HE2) | El estado estructurado es una clase con contrastes favorables; el diseño exacto no está contrastado | Se conserva como núcleo y se amplía con puntos de control y recuperación |
| OE3 enrutamiento de Steiner (HE3) | *Joins* implícitos en el 75,0 % de los estudios multiturno; sin contrastes | Fuera del alcance (trabajo futuro) |
| OE4 *sandbox* y autorreparación (HE4) | El mecanismo de autocorrección no se reporta en 46 de 72 estudios | Se reduce a validación por ejecución, reutilizada como disparador de la recuperación |
| OE5 evaluación, incluidos esquemas empresariales | La evaluación con historial predicho es la primera brecha por solidez; no hay datos empresariales | Historial predicho, métricas por turno y recuperación; sin esquemas empresariales |
| Cuatro hipótesis de eficacia | Solo un mecanismo tiene evidencia de clase | Una hipótesis sobre el componente innovador, estimada con intervalos |

<!-- fuentes: 00-contexto/TS Blueprints.md (OE1–OE5, HE1–HE4); latex/slr/secciones/07-conclusiones.tex (PI1); 04b-resultados.tex (PI3, PI4, causas de no reporte); desafio.md H1–H2 -->

Se mantienen el problema, el dominio, el título y el mecanismo central. Cambia la afirmación: de «cuatro mecanismos nuevos que mejoran cada uno la exactitud» a «un mecanismo innovador, construido sobre una base sustentada en la RSL y evaluado por ablación».

## Respuestas a las cuestiones del desafío

### Origen de la pregunta

Se conserva el cruce entre estado estructurado y evaluación con historial predicho, pero se declara que la idea de estudiar la degradación por turno ya estaba en HE2 antes de la RSL. La revisión posterior respalda la brecha metodológica y la clase general de estado estructurado; no convierte la hipótesis previa en un hallazgo. <!-- desafio.md: H1–H3 --> La pendiente será un resultado, no el único criterio de éxito; la tasa de recuperación es un segundo resultado, más directo.

### Permanencia de OE2

OE2 se mantiene aun separándolo del coste administrativo del título, porque proporciona el mecanismo central que se desea materializar. El diseño de dos capas con mutaciones explícitas, puntos de control y recuperación constituye el componente novedoso del artefacto; su novedad se evalúa, no se presupone. La novedad es de adaptación: el retroceso a puntos de control es un patrón conocido en agentes LLM y GitHarness (R00499) lo aplica con disparador por cambio de requisito; no se encontró su uso guiado por señales de ejecución sobre el estado del diálogo en *Text-to-SQL* conversacional (`novedad_recuperacion.md`). Se conserva como una implementación concreta de estado estructurado, no como una solución ya demostrada ni como inferencia sobre toda la clase.

### Límite de la detección de fallos

Bajo historial predicho, el sistema solo puede detectar fallos mediante señales observables: errores de ejecución, resultados vacíos o inconsistencias del estado. Los errores semánticos silenciosos (SQL ejecutable pero incorrecto) no activarán la recuperación. La tasa de recuperación se calcula contra la referencia en la evaluación, pero el disparador no puede usarla. Este límite se declarará como cota del mecanismo.

### Resultados contrarios a la hipótesis

Si el componente mejora la exactitud global pero no la degradación por turno ni la recuperación, solo se sostendrá el primer resultado. Si iguala o empeora a la base, se informará como resultado del estudio y no se reinterpretará la construcción del artefacto como evidencia de eficacia. El producto software y su evaluación reproducible siguen siendo resultados aun cuando la ablación no favorezca al grafo.

### Implementación y aporte propio

Se implementará un artefacto propio con interfaces comunes, en lugar de inferir el efecto de la clase mediante la comparación de sistemas ajenos heterogéneos. El aporte de Ingeniería de Software comprenderá la arquitectura, la implementación modular, las pruebas, la trazabilidad SQL–estado, la repetición de diálogos y la observabilidad. La inferencia empírica se limitará a las configuraciones evaluadas.

### Precisión y dificultad

Antes de fijar la diferencia de pendientes como resultado principal, se realizará un análisis de precisión con los tamaños por turno y la variabilidad observada. El análisis deberá respetar la dependencia entre turnos del mismo diálogo y examinar la dificultad SQL sin fragmentar la muestra hasta volver inestables las estimaciones. Si la precisión no resulta suficiente, se reportarán resultados por turno e intervalos sin afirmar una diferencia de pendientes. <!-- desafio.md: H5 -->

### Contaminación

Con SParC no se afirmará ausencia de contaminación para modelos cerrados. Se registrarán modelo, versión, fecha de acceso y corte declarado cuando exista; una sonda temporal podrá añadirse si es factible, pero se tratará como análisis de sensibilidad y no como prueba de independencia. La información no observable permanecerá como limitación. <!-- desafio.md: H10 -->

### Verificaciones pendientes

1. **Novedad de la recuperación (resuelta, 2026-10-14):** no se encontró el mecanismo en el corpus, arXiv, DBLP ni OpenAlex; el antecedente más cercano es GitHarness (R00499, retroceso por cambio de requisito, sin retroalimentación de ejecución). La novedad se formula como adaptación (`novedad_recuperacion.md`).
2. **Ablaciones por turno en texto completo:** sigue pendiente comprobar si los estudios con historial predicho reportan curvas por turno con y sin el componente de estado (`HANDOFF_codex_texto_completo.md`). Condiciona si la pendiente puede ser resultado principal.

### Candidatos alternativos

La sensibilidad de las combinaciones impide descartarlas por rango como si la matriz ofreciera una selección estable. <!-- desafio.md: H6–H8 --> De ellas se incorporan los elementos compatibles con el alcance elegido: la reutilización del SQL previo en la base y el coste como dimensión de evaluación. No se adopta la escala empresarial porque no se dispone de datos empresariales, ni la aclaración con usuarios como núcleo porque no se dispone de participantes reales. <!-- restricciones_autora.md: acceso a usuarios y datos -->

## Título

Se mantiene el título inscrito: «Marco multiagente con grafos para mitigar la degradación por turno en consultas conversacionales a bases de datos relacionales». <!-- latex/comun/metadatos.tex --> «Para mitigar» se interpreta como finalidad del artefacto: la recuperación guiada por ejecución es un mecanismo diseñado con ese fin y la tasa de recuperación lo mide directamente. Si la Escuela no aceptara esa lectura, se preparará la modificación correspondiente (Directiva 007, art. 7).

## Límites para el paso 6

La actualización de la propuesta deberá:

- conservar el artefacto como producto principal y la ablación como mecanismo de evaluación;
- reducir los objetivos a cuatro: arquitectura basada en las prácticas de la RSL, componente innovador, subsistema de evaluación y evaluación (calidad del software y ablación);
- separar requisitos del producto, decisiones de arquitectura e hipótesis empíricas;
- estimar el presupuesto de API para SParC (y CoSQL, si procede) con tres configuraciones y repeticiones;
- definir operacionalmente las métricas de Ingeniería de Software;
- fijar por escrito, antes de ejecutar los experimentos, las configuraciones, las métricas, los *benchmarks* y el análisis por turno, incluida la regla para declarar una diferencia de pendientes;
- evitar promesas de mitigación, coste acotado o eliminación de errores que no se hayan demostrado.

## Estado de la decisión

El paso 5 queda resuelto como **ajustar**: se conserva un marco software cercano a la propuesta original, pero su contribución se redefine como un artefacto con una base sustentada en la RSL y un único componente innovador (grafo de estado con recuperación guiada por ejecución), evaluado por ablación bajo historial predicho. Quedan pendientes las verificaciones de novedad y de ablaciones por turno. El paso 6 deberá convertir esta decisión en propuesta, objetivos, hipótesis y metas actualizados; no se inicia en este documento.
