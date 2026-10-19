# Mapa de evidencia de los objetivos específicos

Este mapa confronta los objetivos de la propuesta con la evidencia de la RSL. La población principal comprende 72 estudios multiturno que superan el umbral de validez y la población de sensibilidad comprende los 77 estudios multiturno del Nivel 2. <!-- mapa_oe.json: poblaciones/nivel2_umbral; poblaciones/nivel2 --> Los efectos son contrastes dentro de cada estudio, expresados en puntos porcentuales (pp); debido a la heterogeneidad de *benchmarks*, métricas, modelos base e historiales, no se interpretan como un efecto combinado ni como evidencia de significación estadística.

## OE1 — Preprocesamiento lingüístico y restauración del contexto

### Qué propone el OE

Se propone distinguir continuaciones y cambios de tema, resolver anáforas y elipsis y producir una pregunta semánticamente completa para los módulos posteriores.

### Frecuencia en la RSL: propuesta frente a alternativas

En la población principal, la reescritura aparece en 12 de 72 estudios (16,7 %), la clasificación del discurso en 2 de 72 (2,8 %) y la resolución explícita de anáforas o elipsis en 2 de 72 (2,8 %). <!-- mapa_oe_indicadores.csv: OE1/Reescritura de la pregunta; OE1/Clasificación de actos de discurso; OE1/Resolución explícita (anáfora/elipsis), n_nivel2_umbral/pct_nivel2_umbral --> La alternativa dominante es la concatenación del historial, presente en 35 de 72 estudios (48,6 %). <!-- mapa_oe_indicadores.csv: OE1/Concatenación del historial, n_nivel2_umbral/pct_nivel2_umbral --> En sensibilidad, las frecuencias son 12 de 77 (15,6 %), 3 de 77 (3,9 %), 2 de 77 (2,6 %) y 35 de 77 (45,5 %), respectivamente. <!-- mapa_oe_indicadores.csv: OE1, n_nivel2/pct_nivel2 -->

### Contrastes dentro del estudio

- Reescritura, reformulación o discurso: mediana de Δ = +1,99 pp, rango de −4,75 a +25,0 pp, con 10 estudios positivos, 1 negativo y ninguno nulo; confianza alta. <!-- mapa_oe_contrastes.csv: OE1/principal_nivel2_umbral/Reescritura / reformulación / discurso --> La sustentan R00033 (Zhou2026RoseSQL), R00072 (Zhang2024CoESQL), R00074 (Liu2024TPLink), R00097 (Xiao2022CQRSQL), R00101 (Qi2022RASAT), R00107 (Chen2021Decoupled), R00222 (Jiang2025SiriusBI), R00868 (Fu2023MIGA), R00924 (Li2023DIR), R00927 (Ascoli2025Advancing) y R01034 (Liu2019FANDA). <!-- mapa_oe_contrastes.csv: OE1/principal_nivel2_umbral/Reescritura / reformulación / discurso, estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->
- Concatenación o historial: mediana de Δ = +0,60 pp, rango de +0,15 a +7,70 pp, con 3 estudios positivos, ninguno negativo y ninguno nulo; confianza moderada. <!-- mapa_oe_contrastes.csv: OE1/principal_nivel2_umbral/Concatenación / historial (alternativa) --> La sustentan R00078 (Li2024MultiSQL), R00079 (Ryu2024EHRSeqSQL) y R00927 (Ascoli2025Advancing). <!-- mapa_oe_contrastes.csv: OE1/principal_nivel2_umbral/Concatenación / historial (alternativa), estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->

La población de sensibilidad produce los mismos efectos y estudios en ambas clases. <!-- mapa_oe_contrastes.csv: OE1/sensibilidad_nivel2 -->

### Contraevidencia y limitaciones

R00927 (Ascoli2025Advancing) aporta el contraste negativo de la reescritura y señala pérdida de información, simplificación de ambigüedades, uso del conjunto de desarrollo como sustituto y posible memorización del LLM. R00107 (Chen2021Decoupled) identifica al reescritor como cuello de botella en turnos posteriores; R00924 (Li2023DIR) informa que los reescritores quedan lejos de la cota oráculo y no se transfieren entre formatos sin anotaciones; R01034 (Liu2019FANDA) se limita a seguimiento inmediato y deja el multiturno y las múltiples tablas como trabajo futuro. <!-- extraccion.csv: R00927/R00107/R00924/R01034, limitaciones_autores; pi1_resumen --> La pertinencia de la clase principal presenta limitaciones leves, pues no todos los contrastes miden el mismo escenario multiturno final. <!-- mapa_oe_contrastes.csv: OE1/principal_nivel2_umbral/Reescritura / reformulación / discurso, pertinencia -->

### ¿Escaso = necesario?

(a) La clasificación del discurso y la resolución explícita están poco estudiadas; (b) el mapa no dispone de un indicador directo de errores de restauración del contexto: el predominio del historial refleja una práctica habitual, no evidencia del problema; (c) existe evidencia favorable para la familia amplia de reescritura o análisis del discurso, pero no aísla la combinación exacta de clasificación, anáfora y elipsis propuesta. Por tanto, los datos apoyan la escasez y una utilidad parcial de la familia; no evidencian el problema de forma directa ni la necesidad del mecanismo completo.

### Alternativas con evidencia comparable o mayor

La concatenación del historial posee mayor cobertura y contrastes positivos propios, aunque con efecto mediano menor y confianza moderada. <!-- mapa_oe_indicadores.csv: OE1/Concatenación del historial; mapa_oe_contrastes.csv: OE1/principal_nivel2_umbral/Concatenación / historial (alternativa) --> También aparecen el análisis de diferencias entre preguntas y la vinculación entre enunciados, incluidos en la clase amplia, sin que la evidencia permita afirmar que una de estas rutas sea superior.

### Balance provisional

**Respaldo parcial.** La familia de restauración lingüística presenta dirección mayormente favorable y confianza alta, pero el efecto es heterogéneo y la evidencia no aísla todos los subcomponentes del OE. <!-- mapa_oe_contrastes.csv: OE1/principal_nivel2_umbral/Reescritura / reformulación / discurso -->

## OE2 — Grafo semántico de estado de dos capas

### Qué propone el OE

Se propone un grafo de estado dinámico que registre medidas, dimensiones y filtros, aplique mutaciones explícitas y mantenga acotado el coste del contexto.

### Frecuencia en la RSL: propuesta frente a alternativas

En la población principal, los grafos aparecen en 9 de 72 estudios (12,5 %), las estructuras explícitas en 10 de 72 (13,9 %), los grafos dinámicos entre turnos en 7 de 72 (9,7 %), las reglas deterministas en 16 de 72 (22,2 %) y el contexto acotado en 14 de 72 (19,4 %). <!-- mapa_oe_indicadores.csv: OE2 indicadores de propuesta, n_nivel2_umbral/pct_nivel2_umbral --> Frente a ello, el historial plano aparece en 38 de 72 (52,8 %), la edición del SQL previo en 11 de 72 (15,3 %) y la memoria externa, ventana o resumen en 11 de 72 (15,3 %); el coste crece con los turnos en 36 de 72 (50,0 %). <!-- mapa_oe_indicadores.csv: OE2 indicadores de alternativa y problema, n_nivel2_umbral/pct_nivel2_umbral --> En sensibilidad, los grafos son 9 de 77 (11,7 %), las estructuras explícitas 13 de 77 (16,9 %) y el historial plano 38 de 77 (49,4 %). <!-- mapa_oe_indicadores.csv: OE2, n_nivel2/pct_nivel2 -->

### Contrastes dentro del estudio

- Grafo, estado o memoria estructurada: mediana de Δ = +3,50 pp, rango de −1,30 a +20,70 pp, con 10 estudios positivos, 1 negativo y ninguno nulo; confianza alta. <!-- mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/Grafo / estado / memoria estructurada --> Contribuyen R00033 (Zhou2026RoseSQL), R00096 (Cai2022STAR), R00099 (Hu2022InContext), R00117 (Cai2020IGSQL), R00435 (Tummalapenta2026Memory), R00438 (Wang2026Learning), R00480 (Teixeira2026SemPlan), R00499 (Yang2026GitHarness), R00936 (Yu2021Interactionmodeling), R00954 (Khadija2026Intelligent) y R01029 (Wang2021Tracking). <!-- mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/Grafo / estado / memoria estructurada, estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->
- SQL previo, edición o ventana: mediana de Δ = +5,08 pp, rango de −0,10 a +29,95 pp, con 11 estudios positivos, 1 negativo y ninguno nulo; confianza alta. <!-- mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/SQL previo / edición / ventana (alternativa) --> Contribuyen R00072 (Zhang2024CoESQL), R00079 (Ryu2024EHRSeqSQL), R00093 (Zheng2022HIESQL), R00120 (Wang2020PGGSQL), R00126 (Yu2019SParC), R00131 (Zhang2019EditSQL), R00148 (Urban2025Utilizing), R00435 (Tummalapenta2026Memory), R00453 (Lian2026CoeusBI), R00499 (Yang2026GitHarness), R00508 (Yang2026HarnessSQL) y R00868 (Fu2023MIGA). <!-- mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/SQL previo / edición / ventana (alternativa), estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->

La sensibilidad no cambia los resultados de las clases. <!-- mapa_oe_contrastes.csv: OE2/sensibilidad_nivel2 -->

### Contraevidencia y limitaciones

R00435 (Tummalapenta2026Memory) produce el contraste negativo para la clase estructurada y advierte ejecución única sin varianza, preguntas de plantilla, alcance restringido de datos y motor, y no determinismo. R00093 (Zheng2022HIESQL) produce el contraste negativo de la alternativa y reconoce sensibilidad al SQL predicho anterior. <!-- extraccion.csv: R00435/R00093, limitaciones_autores --> Parte de la evidencia de la alternativa usa *benchmarks* de un turno y algunos contrastes incorporan historial *gold* o mezclado, por lo que no prueban por sí solos robustez conversacional con errores acumulados. <!-- mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/SQL previo / edición / ventana (alternativa), pertinencia; extraccion.csv: R00131, historial_eval --> Tampoco se contrasta de forma aislada la arquitectura exacta de dos capas ni la complejidad acotada prometida.

### ¿Escaso = necesario?

(a) El grafo dinámico y el estado explícito son minoritarios; (b) el problema de crecimiento del contexto sí está documentado; (c) los componentes estructurados muestran efectos mayormente favorables, pero una alternativa más simple presenta evidencia al menos comparable. La evidencia apoya los tres planos solo de forma parcial: confirma escasez y problema, y respalda la familia estructurada, no la necesidad del diseño exacto.

### Alternativas con evidencia comparable o mayor

La edición del SQL previo, las ventanas y la reutilización de artefactos alcanzan una mediana descriptiva mayor con confianza alta. <!-- mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/SQL previo / edición / ventana (alternativa) --> El historial plano es además la representación más frecuente. <!-- mapa_oe_indicadores.csv: OE2/Representación: historial plano --> Estas comparaciones no establecen superioridad causal entre clases.

### Balance provisional

**Respaldo parcial.** Se respalda el valor de representar estado y memoria de forma estructurada, pero no la arquitectura exacta de dos capas ni su necesidad frente a edición, ventana o reutilización del SQL.

## OE3 — Enrutamiento relacional simbólico

### Qué propone el OE

Se propone modelar el esquema como grafo ponderado y derivar *joins* válidos mediante caminos mínimos y árbol de Steiner.

### Frecuencia en la RSL: propuesta frente a alternativas

En la población principal, la inferencia por caminos aparece en 1 de 72 estudios (1,4 %), el grafo de claves foráneas con restricciones en 1 de 72 (1,4 %) y la vinculación mediante grafo de esquema en 12 de 72 (16,7 %); los *joins* implícitos aparecen en 54 de 72 (75,0 %). <!-- mapa_oe_indicadores.csv: OE3, n_nivel2_umbral/pct_nivel2_umbral --> Se reportan errores de *join* en 10 de 72 estudios (13,9 %). <!-- mapa_oe_indicadores.csv: OE3/Errores de join reportados, n_nivel2_umbral/pct_nivel2_umbral --> En sensibilidad, las inferencias no implícitas siguen en 1 de 77 estudios cada una (1,3 %), mientras los *joins* implícitos aparecen en 55 de 77 (71,4 %). <!-- mapa_oe_indicadores.csv: OE3, n_nivel2/pct_nivel2 -->

### Contrastes dentro del estudio

- *Joins*, claves foráneas o caminos: no hay estudios ni contrastes válidos en la población principal ni en sensibilidad; por ello no existe mediana, rango o confianza para el componente central del OE. <!-- mapa_oe_contrastes.csv: OE3/principal_nivel2_umbral y sensibilidad_nivel2/Joins / FK / caminos -->
- Grafo de esquema como codificación: mediana de Δ = +4,20 pp, rango de +1,30 a +7,10 pp, con 2 estudios positivos, ninguno negativo y ninguno nulo; confianza moderada. <!-- mapa_oe_contrastes.csv: OE3/principal_nivel2_umbral/Grafo de esquema (codificación) --> Los estudios son R00117 (Cai2020IGSQL) y R00936 (Yu2021Interactionmodeling). <!-- mapa_oe_contrastes.csv: OE3/principal_nivel2_umbral/Grafo de esquema (codificación), estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->
- Otras técnicas de vinculación: mediana de Δ = +1,50 pp, rango de +0,25 a +33,20 pp, con 15 estudios positivos, ninguno negativo y ninguno nulo; confianza alta. <!-- mapa_oe_contrastes.csv: OE3/principal_nivel2_umbral/Vinculación de esquemas (otras técnicas) --> La sustentan R00074 (Liu2024TPLink), R00086 (Zhang2023ACTSQL), R00093 (Zheng2022HIESQL), R00097 (Xiao2022CQRSQL), R00101 (Qi2022RASAT), R00120 (Wang2020PGGSQL), R00160 (Zhai2024Learn), R00170 (Bian2026ASTormer), R00298 (Bazaga2023SQLformer), R00309 (Lian2024ChatBI), R00453 (Lian2026CoeusBI), R00511 (HariKrishnanParthasarathi2023Conversational), R00525 (Zhang2024SEHCL), R00868 (Fu2023MIGA) y R00981 (Dou2023UniSAr). <!-- mapa_oe_contrastes.csv: OE3/principal_nivel2_umbral/Vinculación de esquemas (otras técnicas), estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->

La sensibilidad no altera estas clases. <!-- mapa_oe_contrastes.csv: OE3/sensibilidad_nivel2 -->

### Contraevidencia y limitaciones

La principal contraevidencia es la ausencia de un contraste directo que active o desactive la inferencia algorítmica de rutas: la evidencia positiva de grafo de esquema se refiere a codificación, no a síntesis determinista de *joins*. <!-- mapa_oe_contrastes.csv: OE3/principal_nivel2_umbral/Joins / FK / caminos; Grafo de esquema (codificación) --> R00120 (Wang2020PGGSQL) solo evalúa en desarrollo y no presenta una discusión de limitaciones; R00981 (Dou2023UniSAr) reconoce que errores de vinculación producen marcas estructurales y tablas incorrectas. <!-- extraccion.csv: R00120/R00981, limitaciones_autores --> Parte de los contrastes de vinculación usa *benchmarks* de un turno, lo que origina limitaciones leves de pertinencia para esa clase. <!-- mapa_oe_contrastes.csv: OE3/principal_nivel2_umbral/Vinculación de esquemas (otras técnicas), pertinencia -->

### ¿Escaso = necesario?

(a) La inferencia algorítmica de *joins* es muy poco estudiada; (b) existen reportes de errores de *join*, aunque no son mayoritarios; (c) no existe evidencia de contraste para el algoritmo de caminos propuesto. Los datos sostienen la escasez y que el problema existe en parte del corpus, pero no sostienen que Steiner o los caminos mínimos sean necesarios ni eficaces.

### Alternativas con evidencia comparable o mayor

La inferencia implícita domina la literatura, y la vinculación mediante grafos de esquema u otras técnicas sí tiene contrastes favorables. <!-- mapa_oe_indicadores.csv: OE3/Joins implícitos en el modelo; mapa_oe_contrastes.csv: OE3/principal_nivel2_umbral --> No se dispone de una comparación directa entre inferencia implícita y rutas algorítmicas.

### Balance provisional

**Sin evidencia suficiente.** La novedad y escasez del enrutamiento algorítmico están claras, pero el componente central carece de contrastes de eficacia dentro del estudio.

## OE4 — Verificación por ejecución y autocorrección

### Qué propone el OE

Se propone un ciclo aislado que combine corrección simbólica de identificadores y reflexión del LLM guiada por errores del SGBD hasta obtener consultas compilables.

### Frecuencia en la RSL: propuesta frente a alternativas

En la población principal, la retroalimentación de errores de ejecución aparece en 10 de 72 estudios (13,9 %), la reparación simbólica en 1 de 72 (1,4 %), la autodepuración por LLM en 4 de 72 (5,6 %) y la corrección aplicada en multiturno en 30 de 72 (41,7 %). <!-- mapa_oe_indicadores.csv: OE4 indicadores de propuesta, n_nivel2_umbral/pct_nivel2_umbral --> Como alternativas, la aclaración con el usuario aparece en 18 de 72 (25,0 %), la abstención en 4 de 72 (5,6 %), la autoconsistencia en ninguno de 72 (0,0 %) y el verificador o crítico en 2 de 72 (2,8 %). <!-- mapa_oe_indicadores.csv: OE4 indicadores de alternativa, n_nivel2_umbral/pct_nivel2_umbral --> En sensibilidad, la aclaración aumenta a 22 de 77 (28,6 %) y la corrección multiturno a 34 de 77 (44,2 %). <!-- mapa_oe_indicadores.csv: OE4, n_nivel2/pct_nivel2 -->

### Contrastes dentro del estudio

- Autocorrección, ejecución o verificación: mediana de Δ = +2,08 pp, rango de +0,01 a +13,76 pp, con 10 estudios positivos, ninguno negativo y ninguno nulo; confianza moderada. <!-- mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Autocorrección / ejecución / verificación --> Contribuyen R00030 (Guo2026MTSQLR1), R00078 (Li2024MultiSQL), R00105 (Elgohary2021NLEDIT), R00123 (Elgohary2020Speak), R00312 (Sun2024QDASQL), R00373 (Huo2025BIRDINTERACT), R00374 (Lin2025Prompt), R00508 (Yang2026HarnessSQL), R00524 (Guo2025Evaluating) y R00526 (Almohaimeed2025Prompt). <!-- mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Autocorrección / ejecución / verificación, estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->
- Aclaración o interacción con el usuario: mediana de Δ = +16,20 pp, rango de −19,05 a +43,00 pp, con 4 estudios positivos, 1 negativo y ninguno nulo; confianza moderada. <!-- mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Aclaración / interacción con el usuario (alternativa) --> Contribuyen R00123 (Elgohary2020Speak), R00222 (Jiang2025SiriusBI), R00311 (Chen2024Learning), R00312 (Sun2024QDASQL) y R00480 (Teixeira2026SemPlan). <!-- mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Aclaración / interacción con el usuario (alternativa), estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->
- Autoconsistencia o reordenamiento: mediana de Δ = +1,10 pp, rango de +0,20 a +2,00 pp, con 2 estudios positivos, ninguno negativo y ninguno nulo; confianza moderada. <!-- mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Autoconsistencia / reranking (alternativa) --> Los estudios son R00511 (HariKrishnanParthasarathi2023Conversational) y R01037 (Hui2021Dynamic). <!-- mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Autoconsistencia / reranking (alternativa), estudios; latex/slr/apendices/d_calidad.tex: clave_bib -->

En sensibilidad, la aclaración pasa a una mediana de +14,97 pp en 6 estudios y la autocorrección a +1,65 pp en 11 estudios; ambas conservan confianza moderada. <!-- mapa_oe_contrastes.csv: OE4/sensibilidad_nivel2 --> El cambio se debe a R00450 (Parmar2026StocksTalk), estudio bajo el umbral de validez. <!-- mapa_oe_contrastes.csv: OE4/sensibilidad_nivel2, estudios; CALIDAD.md: estudios bajo el umbral -->

### Contraevidencia y limitaciones

R00480 (Teixeira2026SemPlan) produce el contraste negativo de aclaración y limita su evidencia a un dominio sintético, un modelo y un proveedor, con baja corrección absoluta. R00123 (Elgohary2020Speak) cubre una sola ronda de corrección y deja la interacción prolongada como trabajo futuro. R00508 (Yang2026HarnessSQL) se concentra en SQLite; R00030 (Guo2026MTSQLR1) informa errores residuales y mayor latencia y consumo de tokens. <!-- extraccion.csv: R00480/R00123/R00508/R00030, limitaciones_autores --> Algunos Δ proceden de Spider u otras variantes de un turno y R00030 mezcla historial *gold* y predicho; por ello no todos prueban el bucle en el escenario conversacional de interés. <!-- contrastes_taxonomia.csv: R00508, benchmark_familia; extraccion.csv: R00030, historial_eval --> La aclaración tiene limitaciones importantes de pertinencia, y la autoconsistencia tiene suficiencia importante. <!-- mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral, pertinencia/suficiencia -->

### ¿Escaso = necesario?

(a) La combinación exacta de reparación simbólica y reflexión guiada por el SGBD está poco estudiada; (b) el mapa no dispone de un indicador directo de errores de ejecución (la corrección aplicada en multiturno mide adopción, no el problema); (c) la clase amplia de autocorrección presenta efectos positivos, pero no aísla esa combinación. La evidencia apoya la familia de solución, no la garantía de consultas compilables ni la necesidad de ambas etapas.

### Alternativas con evidencia comparable o mayor

La aclaración con el usuario presenta un efecto mediano descriptivo mayor, aunque más heterogéneo y menos pertinente; el reordenamiento de candidatos también tiene evidencia positiva pero escasa. <!-- mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral --> La abstención y los verificadores o críticos aparecen como alternativas de diseño, sin una clase de contraste suficiente para compararlos directamente con el bucle propuesto. <!-- mapa_oe_indicadores.csv: OE4/Abstención; OE4/Verificador / crítico -->

### Balance provisional

**Respaldo parcial.** Se respalda un ciclo amplio de ejecución, verificación y corrección, pero no la combinación exacta ni la promesa de garantía; la aclaración con el usuario constituye una alternativa fuerte.

## OE5 — Evaluación multiturno y degradación por turno

### Qué propone el OE

Se propone evaluar el marco integrado en SParC, CoSQL y esquemas empresariales mediante EX, EM y curvas de degradación por turno.

### Frecuencia en la RSL: propuesta frente a alternativas

En la población principal, 31 de 72 estudios (43,1 %) evalúan con historial predicho y 19 de 72 (26,4 %) solo con preguntas previas; 5 de 72 (6,9 %) emplean historial *gold*. <!-- mapa_oe_indicadores.csv: OE5/Evaluación con historial predicho; solo preguntas; historial gold, n_nivel2_umbral/pct_nivel2_umbral --> La degradación se reporta en 38 de 72 estudios (52,8 %), la contaminación se discute en 7 de 72 (9,7 %) y algún coste se reporta en 20 de 72 (27,8 %). <!-- mapa_oe_indicadores.csv: OE5/Degradación; Contaminación; Coste, n_nivel2_umbral/pct_nivel2_umbral --> SParC o CoSQL aparecen en 40 de 72 estudios de la población principal. <!-- mapa_oe.json: oe/OE5/benchmarks_sparc_cosql/nivel2_umbral; poblaciones/nivel2_umbral --> En sensibilidad, el historial predicho aparece en 31 de 77 (40,3 %) y la degradación en 39 de 77 (50,6 %). <!-- mapa_oe_indicadores.csv: OE5, n_nivel2/pct_nivel2 -->

### Contrastes dentro del estudio

No se definieron clases de componentes para OE5, por lo que no hay mediana Δ, rango, dirección por estudio ni nivel de confianza en `mapa_oe_contrastes.csv`. <!-- mapa_oe.json: oe/OE5/contrastes --> La síntesis de degradación mantiene separados los historiales: el estrato predicho contiene 6 curvas de 5 estudios con pendiente mediana de −7,0 pp por turno, y el de solo preguntas 8 curvas de 6 estudios con −10,96 pp por turno; no hay curvas *gold* con longitud suficiente. <!-- slr/sintesis/PI5.md: Degradación por turno, estratificada por historial --> Impulsan el estrato predicho R00117 (Cai2020IGSQL), R00120 (Wang2020PGGSQL), R00435 (Tummalapenta2026Memory), R00868 (Fu2023MIGA) y R01029 (Wang2021Tracking); el estrato de solo preguntas incluye R00097 (Xiao2022CQRSQL), R00100 (Liu2022Augmenting), R00126 (Yu2019SParC), R00950 (Chai2023QURG), R00994 (Li2022Pay) y R01031 (Yu2021SCoRe). <!-- slr/sintesis/PI5.md: Pendientes individuales; latex/slr/apendices/d_calidad.tex: clave_bib -->

### Contraevidencia y limitaciones

El historial *gold* impide observar la propagación de errores y puede sobrestimar la robustez; el historial no se reporta en 20 de 72 estudios. <!-- slr/sintesis/PI5.md: Tipo de historial; Limitaciones --> Las curvas son pocas, no existen para el estrato *gold* y agrupan preguntas de distinta composición y dificultad, por lo que la pendiente mezcla profundidad del turno y dificultad. <!-- slr/sintesis/PI5.md: Limitaciones --> Las métricas, *benchmarks* y estratos no son comparables entre sí, y la discusión de contaminación y costes es minoritaria. <!-- slr/sintesis/PI5.md: Para la discusión; mapa_oe_indicadores.csv: OE5/Contaminación; Coste -->

### ¿Escaso = necesario?

(a) Las curvas con historial predicho son escasas; (b) la degradación existe en todas las curvas sintetizadas de los estratos analizados; (c) OE5 es un protocolo de evaluación, no un componente cuya mejora se estime mediante Δ. Los datos sostienen la existencia del problema y la necesidad metodológica de medirlo con historial predicho, pero no validan de antemano el marco propuesto.

### Alternativas con evidencia comparable o mayor

El historial de solo preguntas evita *teacher forcing* sin propagar salidas previas y sirve como estrato complementario, no sustituto. <!-- slr/sintesis/PI5.md: Degradación por turno, estratificada por historial --> Las métricas por pregunta y por interacción, la ejecución y el éxito de tarea capturan aspectos distintos; ninguna medida aislada reemplaza el reporte estratificado.

### Balance provisional

**Respaldado.** La RSL sustenta evaluar con historial predicho y reportar degradación por turno; permanece abierta la selección final de métricas y conjuntos empresariales.

## Premisas transversales — sin entrenamiento y multiagente

### Qué propone el OE

La propuesta presupone un marco multiagente sin entrenamiento que coordine módulos lingüísticos, de estado, enrutamiento y autocorrección.

### Frecuencia en la RSL: propuesta frente a alternativas

En la población principal, 21 de 72 estudios (29,2 %) no requieren entrenamiento, 11 de 72 (15,3 %) usan agentes como paradigma principal y 7 de 72 (9,7 %) son híbridos neurosimbólicos; como alternativas, 17 de 72 (23,6 %) se basan principalmente en *prompting* de LLM y 5 de 72 (6,9 %) en ajuste fino. <!-- mapa_oe_indicadores.csv: TRANSVERSAL, n_nivel2_umbral/pct_nivel2_umbral --> En todo el corpus, las cifras son 139 de 389 (35,7 %) sin entrenamiento, 78 de 389 (20,1 %) con agentes, 27 de 389 (6,9 %) híbridos, 116 de 389 (29,8 %) con *prompting* y 64 de 389 (16,5 %) con ajuste fino. <!-- mapa_oe_indicadores.csv: TRANSVERSAL, n_todos/pct_todos; mapa_oe.json: poblaciones/todos -->

### Contrastes dentro del estudio

No se definieron clases de contraste para estas premisas; por tanto, no hay mediana Δ, rango, estudios positivos o negativos ni confianza que compare un diseño multiagente sin entrenamiento con sus alternativas. <!-- mapa_oe.json: oe/TRANSVERSAL/contrastes -->

### Contraevidencia y limitaciones

La frecuencia no demuestra que prescindir del entrenamiento o repartir funciones entre agentes mejore la exactitud, el coste o la degradación. Además, «agentes» solo registra el paradigma principal y puede omitir arquitecturas donde la agencia sea secundaria. <!-- revision_mapeo_oe.md: D5; mapa_oe_indicadores.csv: TRANSVERSAL/Paradigma principal: agentes --> La evidencia disponible tampoco separa el efecto de la orquestación del modelo base, las herramientas y el *prompting*.

### ¿Escaso = necesario?

(a) Los paradigmas multiagente e híbrido son minoritarios; (b) la RSL no define un indicador de problema que requiera múltiples agentes; (c) no existen contrastes de eficacia para estas premisas. Solo se sostiene su cobertura limitada, no su necesidad ni superioridad.

### Alternativas con evidencia comparable o mayor

El *prompting* de un único LLM, el ajuste fino y los sistemas híbridos no necesariamente multiagente son alternativas observadas. <!-- mapa_oe_indicadores.csv: TRANSVERSAL --> Sin contrastes directos, la elección debe justificarse por requisitos de modularidad, inspeccionabilidad o coste que se medirán en la tesis, no por una ventaja ya establecida.

### Balance provisional

**Sin evidencia suficiente.** La presencia de ambas premisas en el corpus está documentada, pero no existe evidencia comparativa de que su combinación mejore los resultados.

## Conjunción M8

La conjunción preespecificada M8 reúne estado estructurado explícito, inferencia algorítmica de *joins* o autocorrección por ejecución, y evaluación con historial predicho o solo preguntas. No se identificó ningún estudio que combine los tres elementos, ni en la sensibilidad con grafos neuronales. <!-- mapa_oe.json: brecha_M8_sintesis/n; sensibilidad_grafos_neuronales/n --> Sus componentes aparecen por separado en 14, 13 y 46 estudios, y las intersecciones por pares en 1, 8 y 7 estudios. <!-- mapa_oe.json: brecha_M8_sintesis/componentes --> Este resultado nulo demuestra novedad de la conjunción dentro del corpus; no demuestra necesidad ni eficacia.

## Resumen

| OE | componente | frecuencia | efecto (mediana, n) | confianza | problema evidenciado | alternativa más fuerte | balance |
|---|---|---|---|---|---|---|---|
| OE1 | Restauración lingüística | Reescritura: 12/72 (16,7 %) <!-- mapa_oe_indicadores.csv: OE1/Reescritura, principal --> | +1,99 pp, n = 11 <!-- mapa_oe_contrastes.csv: OE1/principal/Reescritura --> | alta <!-- mapa_oe_contrastes.csv: OE1/principal/Reescritura --> | Sin indicador directo | Concatenación: +0,60 pp, n = 3 <!-- mapa_oe_contrastes.csv: OE1/principal/Concatenación --> | respaldo parcial |
| OE2 | Estado estructurado | Grafo: 9/72 (12,5 %) <!-- mapa_oe_indicadores.csv: OE2/Representación: grafo, principal --> | +3,50 pp, n = 11 <!-- mapa_oe_contrastes.csv: OE2/principal/Grafo --> | alta <!-- mapa_oe_contrastes.csv: OE2/principal/Grafo --> | Contexto creciente: 36/72 (50,0 %) <!-- mapa_oe_indicadores.csv: OE2/Coste crece, principal --> | SQL previo, edición o ventana: +5,08 pp, n = 12 <!-- mapa_oe_contrastes.csv: OE2/principal/SQL previo --> | respaldo parcial |
| OE3 | Rutas simbólicas de *join* | Caminos: 1/72 (1,4 %) <!-- mapa_oe_indicadores.csv: OE3/Joins por algoritmo de caminos, principal --> | No estimable, n = 0 <!-- mapa_oe_contrastes.csv: OE3/principal/Joins / FK / caminos --> | no evaluable <!-- mapa_oe_contrastes.csv: OE3/principal/Joins / FK / caminos --> | Errores de *join*: 10/72 (13,9 %) <!-- mapa_oe_indicadores.csv: OE3/Errores de join, principal --> | Vinculación de esquemas: +1,50 pp, n = 15 <!-- mapa_oe_contrastes.csv: OE3/principal/Vinculación --> | sin evidencia suficiente |
| OE4 | Autocorrección por ejecución | Error de ejecución: 10/72 (13,9 %) <!-- mapa_oe_indicadores.csv: OE4/Retroalimentación, principal --> | +2,08 pp, n = 10 <!-- mapa_oe_contrastes.csv: OE4/principal/Autocorrección --> | moderada <!-- mapa_oe_contrastes.csv: OE4/principal/Autocorrección --> | Sin indicador directo | Aclaración: +16,20 pp, n = 5 <!-- mapa_oe_contrastes.csv: OE4/principal/Aclaración --> | respaldo parcial |
| OE5 | Evaluación con historial predicho | 31/72 (43,1 %) <!-- mapa_oe_indicadores.csv: OE5/Historial predicho, principal --> | Pendiente: −7,0 pp/turno, n = 5 estudios <!-- slr/sintesis/PI5.md: degradación/PREDICHO --> | no asignada <!-- mapa_oe.json: oe/OE5/contrastes --> | Degradación reportada: 38/72 (52,8 %) <!-- mapa_oe_indicadores.csv: OE5/Degradación, principal --> | Solo preguntas: −10,96 pp/turno, n = 6 estudios <!-- slr/sintesis/PI5.md: degradación/SOLO_PREGUNTAS --> | respaldado |
| Transversal | Sin entrenamiento y multiagente | 21/72 (29,2 %) y 11/72 (15,3 %) <!-- mapa_oe_indicadores.csv: TRANSVERSAL/Sin entrenamiento; Agentes, principal --> | No estimable <!-- mapa_oe.json: oe/TRANSVERSAL/contrastes --> | no asignada <!-- mapa_oe.json: oe/TRANSVERSAL/contrastes --> | No hay indicador directo | *Prompting*: 17/72 (23,6 %) <!-- mapa_oe_indicadores.csv: TRANSVERSAL/LLM prompting, principal --> | sin evidencia suficiente |

## Direcciones que sugiere la evidencia y no vienen de la propuesta

- Comparar explícitamente la aclaración con el usuario frente a la autocorrección por ejecución.
- Incluir una línea base fuerte de edición o reutilización del SQL previo y otra de historial plano.
- Incorporar abstención y reordenamiento de candidatos como controles de seguridad y selección.
- Declarar siempre el tipo de historial y separar historial predicho, solo preguntas y *gold*.
- Controlar la dificultad de las preguntas por turno para no confundirla con profundidad conversacional.
- Medir latencia, tokens y coste monetario junto con exactitud y degradación.
- Evaluar contaminación del *benchmark*, transferencia entre dominios y cobertura lingüística, en especial datos en español.
- Reportar ablaciones negativas y nulas y mantener constante el modelo base al comparar componentes.
