# Registro OSF — *Generalized Systematic Review Registration* (texto para pegar)

Plantilla: Generalized Systematic Review Registration Form v1 (van den Akker et al., 2023, *Systematic Reviews* 12, DOI 10.1186/s13643-023-02281-7). Idioma: español. Visibilidad: **pública**.
Commit de referencia del protocolo: `1a4c6ab3e9d3c9e76eb0848bd84ef8d783563cce` (2026-10-11).
Archivos a adjuntar: el paquete `osf_anexos_1a4c6ab.zip` (misma carpeta).

---

## METADATOS

**Title**
Text-to-SQL conversacional: restauración del contexto, estado del diálogo, vinculación de esquemas y autocorrección — una revisión sistemática de la literatura

**Description** *(campo de metadatos propio de OSF; no forma parte de los 66 ítems de la plantilla)*
Esta revisión sistemática de la literatura examina cómo los sistemas Text-to-SQL —interfaces que traducen preguntas en lenguaje natural a consultas SQL sobre bases de datos relacionales— manejan el escenario conversacional o multiturno, en el que cada pregunta del usuario depende de las anteriores mediante elipsis, correferencia o cambios de tema. Aunque existen numerosos *surveys* de Text-to-SQL, ninguno aplica un protocolo sistemático al escenario multiturno ni analiza conjuntamente sus cuatro desafíos técnicos principales: (1) la restauración del contexto conversacional, (2) la representación y actualización del estado del diálogo, (3) la vinculación de esquemas y la inferencia de rutas de *join*, y (4) la autocorrección mediante retroalimentación de ejecución.

La revisión sigue las guías de Kitchenham y Charters y se reportará según PRISMA 2020. Se buscará en Scopus, IEEE Xplore, ACM Digital Library, ACL Anthology y arXiv (2019–2026), con una cadena validada mediante estudios semilla y un conjunto de referencia independiente. Tiene un diseño en dos niveles: un mapeo sistemático de todos los estudios incluidos (estadísticas por año, paradigma técnico y escenario, y la proporción de investigación dedicada al escenario multiturno) y una revisión en profundidad de los estudios multiturno, con evaluación de calidad, extracción detallada y síntesis narrativa estructurada según SWiM. El cribado se apoya en dos revisores de IA cegados y un tercer revisor de IA, con decisión final humana y validación humana ciega del rendimiento de la IA.

Resultados esperados: (a) una taxonomía de las técnicas de cada uno de los cuatro desafíos y su comparación con las técnicas equivalentes de un solo turno; (b) una síntesis de los resultados reportados, incluida la degradación del rendimiento a lo largo de los turnos, distinguiendo evaluaciones con historial de referencia y con historial predicho; (c) una estimación descriptiva, con un umbral pre-especificado, de cuánto se ha investigado el escenario multiturno y su tendencia; y (d) la identificación de brechas de investigación. La revisión fundamentará el diseño de un *framework* multiagente para el seguimiento del estado del diálogo en una tesis de pregrado de Ingeniería de Software (Universidad Nacional Mayor de San Marcos, Perú), y se publicará como artículo en español.

**Contributors**
Angela Lucia Jara Espinoza (Universidad Nacional Mayor de San Marcos, Lima, Perú; ORCID 0009-0007-8716-0988)

**Subjects**
Engineering → Computer Engineering; Physical Sciences and Mathematics → Computer Sciences (Artificial Intelligence and Robotics; Databases and Information Systems)

**Tags** *(metadatos de OSF, si los pide)*
text-to-SQL; NL2SQL; NLIDB; conversational text-to-SQL; multi-turn; dialogue state tracking; schema linking; self-correction; systematic review; PRISMA 2020; revisión sistemática

**License** *(metadatos de OSF, si los pide)*
CC-By Attribution 4.0 International

**Tasks and roles**
Angela Lucia Jara Espinoza: conceptualización, diseño del protocolo, búsqueda, cribado (decisión final humana), extracción y evaluación de calidad (verificación humana), síntesis y redacción. Asistencia de IA declarada en «Software» y «Screening».

---

## MÉTODOS DE LA REVISIÓN

**Type of review**
Revisión sistemática (Kitchenham y Charters, 2007) con un nivel previo de mapeo sistemático; reporte según PRISMA 2020; protocolo según PRISMA-P 2015. Sin metaanálisis.

**Review stages**
(1) Búsqueda; (2) deduplicación; (3) piloto y validación del cribado; (4) cribado título-resumen; (5) recuperación de texto completo; (6) cribado de texto completo; (7) bola de nieve (una iteración); (8) evaluación de calidad; (9) extracción de datos; (10) síntesis; (11) redacción.

**Current review stage**
Protocolo finalizado (v1.2). **La búsqueda oficial no ha comenzado.** Antes del registro se realizaron únicamente: búsquedas exploratorias de revisiones existentes; pruebas de sensibilidad de la cadena con 13 estudios semilla; y consultas de solo conteo en Scopus, IEEE Xplore y ACM DL (sin exportar ni leer registros; documentadas en `registro_busquedas.csv`). Se construyó un conjunto de referencia independiente antes de las búsquedas oficiales.

**Start date**
2026-10-11

**End date**
2027-03-31 (tentativa)

**Background**
Los sistemas Text-to-SQL permiten consultar bases de datos relacionales en lenguaje natural. Existen numerosos *surveys* generales, pero ninguna revisión sistemática dedicada al escenario conversacional o multiturno, donde la interpretación de cada pregunta depende de las anteriores. El único *survey* específico localizado (Yang et al., 2025) es narrativo y, según su resumen, no trata como ejes la vinculación de esquemas, la inferencia de *joins* ni la autocorrección; dos revisiones sistemáticas de 2026 (Liu et al.; Bui et al.) no analizan el escenario multiturno. Esta revisión alimenta una tesis de pregrado (UNMSM) sobre seguimiento del estado del diálogo en Text-to-SQL multiturno. Detalle: `00_analisis_brecha.md`.

**Primary research question(s)**
¿Qué técnicas emplean los sistemas Text-to-SQL conversacionales (multiturno) para (PI1) restaurar el contexto conversacional, (PI2) representar y actualizar el estado del diálogo, (PI3) vincular el esquema e inferir rutas de *join* y (PI4) autocorregirse mediante retroalimentación de ejecución, y qué resultados reportan?

**Secondary research question(s)**
PI0: ¿cómo se distribuyen los estudios por año, tipo de publicación, paradigma técnico y escenario (uno vs. varios turnos), y cómo evoluciona la proporción multiturno? PI5: ¿qué *benchmarks* y métricas se usan y qué degradación del rendimiento por turno se reporta? PI3–PI4 incluyen el contraste con las técnicas equivalentes de un solo turno.

**Expectations / hypotheses**
Indicador descriptivo pre-especificado D4: proporción = estudios multiturno que abordan PI3 o PI4 como contribución central / todos los estudios que abordan PI3 o PI4 como contribución central. Se concluirá que el escenario multiturno está «considerablemente menos investigado» solo si el límite superior del IC 95 % de Wilson es ≤ 30 %; si el IC contiene el 30 %, el resultado es no concluyente. Es una referencia descriptiva condicionada al marco de elegibilidad. Criterio pre-especificado de reformulación de la brecha de la tesis: si ≥ 2 estudios del nivel en profundidad ya combinan estado del diálogo estructurado explícito, inferencia algorítmica de *joins* o autocorrección por ejecución, y evaluación multiturno con historial predicho, la brecha se reformulará (correspondencia con códigos en `01_preguntas_picoc.md`).

**Dependent variable(s) / outcome(s) / main variables**
Execution Accuracy (EX, primaria); Exact/Exact-Set Match (EM/ESM); test-suite accuracy (TS); Question Match e Interaction Match (QM/IM) en multiturno; degradación por turno (pendiente en puntos porcentuales por turno, solo con historial predicho); errores de *join*; coste computacional.

**Independent variable(s) / intervention(s) / treatment(s)**
Técnicas de restauración del contexto (concatenación, reescritura, resolución explícita de elipsis/correferencia), representación del estado (historial plano, edición de SQL previo, grafos, estructuras explícitas, memoria externa), vinculación de esquemas e inferencia de *joins* (implícita vs. algorítmica), y retroalimentación de ejecución / autocorrección.

**Additional variable(s) / covariate(s)**
Escenario (uno vs. varios turnos), paradigma técnico, requiere entrenamiento o no (*training-free*), modelo base y fecha, *benchmark* y versión, partición, tipo de historial en la evaluación (gold / predicho / solo preguntas), conocimiento externo, número de candidatos, año y tipo de publicación.

**Software**
Python 3.12 (scripts de búsqueda en arXiv/ACL y de análisis; matplotlib, pandas, numpy); Academic Research Skills v3.23.0 (sr-screener) en Claude Code, con modelos Claude Sonnet 5.5 (revisores A y B) y Claude Opus 5.5 (tercer revisor, recomprobación QC y texto completo) de Anthropic; Mendeley (gestión de referencias); git (control de versiones); LaTeX.

**Funding**
Sin financiamiento.

**Conflicts of interest**
Ninguno.

**Overlapping authorships**
La autora no es autora de ningún estudio potencialmente elegible.

---

## ESTRATEGIA DE BÚSQUEDA

**Databases**
Scopus; IEEE Xplore; ACM Digital Library (ACM Full-Text Collection); ACL Anthology; arXiv.

**Interfaces**
Scopus: búsqueda avanzada web. IEEE Xplore: *Command Search*, campo *All Metadata* (4 consultas). ACM DL: búsqueda avanzada web (2 consultas; sin filtro de fecha disponible en la cuenta de la autora, los registros previos a 2019 se eliminan por metadatos). ACL Anthology: volcado oficial `anthology+abstracts.bib.gz` filtrado por script con la misma lógica. arXiv: API oficial mediante script versionado.

**Grey literature**
Preprints de arXiv (incluidos si no existe versión revisada a la fecha de búsqueda; marcados; deduplicados frente a versiones publicadas; análisis de sensibilidad sin preprints).

**Inclusion and exclusion criteria**
Inclusión (todos): IC1 estudio primario (técnica o *benchmark*) de Text-to-SQL sobre bases de datos relacionales; IC2 multiturno que aborde cualquiera de PI1–PI5, o de un turno con PI3/PI4 como contribución central declarada en título o resumen; IC3 evaluación cuantitativa; IC4 un turno: *benchmark* público (multiturno: cualquier evaluación); IC5 publicado desde 2019-01-01; IC6 en inglés o español; IC7 artículo completo revisado por pares (≥ 4 páginas, incluidas *demo tracks*) o preprint de arXiv. Exclusión ordenada (se registra la primera): E1 < 2019; E2 idioma; E3 tipo (tesis, póster, solo resumen, < 4 páginas, editorial, libro); E4 no primario (*survey*, revisión, posición); E5 no es SQL relacional (SPARQL, Cypher, NoSQL, QA sobre tablas sin SQL); E6 un turno sin PI3/PI4 central; E7 sin evaluación cuantitativa; E8 un turno sin *benchmark* público; E9 informe secundario. «Multiturno» = preguntas sucesivas del usuario dependientes de turnos previos; las rondas internas de un sistema sobre una sola pregunta son de un turno. Detalle y casos límite B1–B6: `03_criterios_elegibilidad.md`.

**Query strings**
Cadena v4: (tarea) AND (multiturno OR vinculación de esquemas/joins OR autocorrección), en título, resumen y palabras clave, 2019–2026. Cadenas exactas por base, tabla de equivalencia y reglas de sintaxis en `cadenas.md` (anexo). Ejemplo (Scopus): TITLE-ABS-KEY("text-to-SQL" OR "text to SQL" OR text2sql OR nl2sql OR … OR ("semantic pars*" AND (sql OR database* OR sparc OR cosql OR spider OR chase))) AND (TITLE-ABS-KEY("multi-turn" OR … OR cosql) OR TITLE-ABS-KEY("schema linking" OR … OR "query repair")) AND PUBYEAR > 2018 AND PUBYEAR < 2027.

**Search validation procedure**
(1) 13 estudios semilla (9 multiturno, 4 de un turno): Scopus 12/12 incluidos 2 casos externos (SCoRe, R²SQL; la versión v3 omitía R²SQL y se corrigió); ACM 2/2; arXiv 1/1; ACL pendiente. (2) Conjunto de referencia independiente construido sin usar la cadena (32 candidatos multiturno a partir de trabajos que citan SParC/CoSQL; 25 de un turno a partir de dos *surveys*, pre-LLM y LLM), congelado antes de las búsquedas oficiales; umbral de sensibilidad ≥ 80 % por brazo, con control de circularidad. Si no se alcanza, se ajusta la cadena mediante enmienda. Detalle: `pruebas_cadenas.md`, `conjunto_referencia.csv`.

**Other search strategies**
Bola de nieve: una iteración hacia atrás y hacia adelante desde los estudios multiturno incluidos, mediante OpenAlex; los candidatos se filtran con el bloque de tarea de la cadena y pasan por el mismo cribado; se reportan en la rama «otros métodos» de PRISMA.

**Procedures to contact authors**
Se contactará por correo electrónico a los autores de estudios cuyo texto completo no pueda obtenerse por acceso abierto, repositorios o biblioteca; un recordatorio a las dos semanas.

**Results of contacting authors**
No aplica todavía; se reportará.

**Search expiration and repetition**
Si transcurren más de 6 meses entre la búsqueda y el envío del artículo, se repetirá con las mismas cadenas para el intervalo nuevo.

**Search strategy justification**
Las bases cubren los foros principales de Text-to-SQL: PLN (ACL Anthology: ACL, EMNLP, NAACL, COLING, EACL), bases de datos (ACM: SIGMOD, PACMMOD, VLDB/PVLDB vía Scopus), IEEE y la indexación multidisciplinar de Scopus (incluidos ICLR y AAAI); arXiv recoge literatura gris muy relevante en el área. Se priorizó la exhaustividad sobre la precisión.

**Miscellaneous search strategy details**
Se observaron DOI ausentes o erróneos en Scopus (p. ej., CQR-SQL), por lo que la deduplicación usa DOI y título normalizado. Conteos previos al registro (sin exportar): Scopus 563; IEEE 107, 51, 84 y 96; ACM 122 y 24.

---

## CRIBADO

**Screening stages**
(1) Título y resumen; (2) texto completo. Ambos con dos revisores IA independientes y cegados y un tercer revisor IA para conflictos; decisión final humana.

**Screened fields / masking**
Título, resumen, palabras clave, año, fuente y tipo de publicación. Los revisores IA no ven las decisiones de los otros revisores (solo el tercer revisor ve ambas). La autora realiza a ciegas la muestra de validación y la auditoría de exclusiones, sin ver las decisiones de la IA.

**Used exclusion criteria**
E1–E9 en el orden indicado en «Inclusion and exclusion criteria». E7, E8, E9 y el límite de páginas solo se aplican en texto completo. Regla de incertidumbre: ante la duda, el registro pasa a texto completo.

**Screener instructions**
Protocolo de cribado en inglés `screening_protocol.md` v1.0 (traducción fiel de los criterios, confirmada por la autora el 2026-10-11), con definiciones operativas de «multiturno» y «contribución central» y 7 casos límite sintéticos acordados (`screening_casos_limite.md`). El texto se inserta literalmente en las instrucciones de los revisores.

**Screening reliability**
Medida principal: acuerdo humano–IA (kappa de Cohen, PABAK y acuerdo observado) en una muestra de validación de 100 registros aleatorios, distinta del piloto, cribada por la autora a ciegas. Acuerdo entre los dos revisores IA: solo diagnóstico (comparten familia de modelo; no se consideran independientes). Prueba de sensibilidad de la IA con el conjunto de referencia (objetivo ≥ 95 %).

**Screening reconciliation procedure**
Conflictos entre revisores A y B: tercer revisor IA (desempate a favor de avanzar si los criterios centrales son plausibles); la autora revisa todos los conflictos y puede anular cualquier decisión (registro de anulaciones). Recomprobación QC de exclusiones conjuntas por un revisor sénior IA (muestra de 150 y casos cercanos por palabras clave). Auditoría humana ciega de máx(10 %, 150) exclusiones por consenso: si la sensibilidad implícita estimada es < 95 % o hay un patrón sistemático de falsos negativos, se aclaran criterios, se re-pilota y se vuelven a cribar las exclusiones.

**Sampling and sample size**
Piloto de ajuste: 50–100 registros etiquetados por la autora. Validación: 100 registros aleatorios. Auditoría: máx(10 %, 150). Contingencia pre-especificada: si los textos completos de un turno superan 400, sus decisiones las toman los revisores IA con auditoría humana del 20 % y de todos los conflictos.

**Screening procedure justification**
Revisora humana única sin segunda revisora disponible; la doble revisión IA cegada con adjudicación, la validación humana reservada y la auditoría de exclusiones compensan parcialmente esa limitación, que se declara.

**Data management and sharing**
Registros, decisiones de cada revisor, registros de ejecución, anulaciones y conteos PRISMA se conservan en el repositorio git del proyecto y se publicarán en este proyecto OSF al finalizar.

**Miscellaneous screening details**
La crítica del protocolo (abogado del diablo, 1 verificación + 2 rondas de revisión) fue realizada por un agente de IA de la misma familia de modelos; no constituye revisión por pares independiente (`04_critica_abogado_diablo_cp1.md`).

---

## EXTRACCIÓN

**Entities to extract**
Nivel 1 (todos los incluidos): identificación, escenario, tipo de contribución, paradigma, modelos, pilares centrales y contenidos, idioma del *dataset*, código, *training-free*, códigos de técnica PI3/PI4. Nivel 2 (multiturno): además, campos de PI1–PI4, tipo de historial en la evaluación, degradación, errores de *join*, coste, contaminación, limitaciones; resultados en formato largo (*benchmark*, versión, partición, métrica, turno, historial, conocimiento externo, candidatos, valor, sistema, modelo); contrastes dentro del estudio. Formulario: `formulario_extraccion.md`.

**Extraction stages**
Piloto con 3 estudios; extracción del Nivel 1; extracción completa del Nivel 2.

**Extractor instructions**
Vocabularios controlados, valores `NR`/`NA`, ubicación (página/tabla) obligatoria para cada dato; regla de línea base de referencia (la más fuerte con el mismo modelo base); categorías inductivas `OTRA` de reporte obligatorio.

**Extractor blinding**
En un 20 % aleatorio del Nivel 2 la autora extrae sin ver la propuesta de la IA.

**Extraction reliability**
Acuerdo por campo entre la extracción independiente de la autora y la propuesta de la IA en esa muestra.

**Extraction reconciliation procedure**
La IA propone y la autora verifica cada fila; ante discrepancia decide la autora con el texto del estudio.

**Extraction procedure justification**
Asistencia de IA para el volumen; verificación humana completa y muestra independiente para medir el sesgo de automatización.

**Data management and sharing**
`extraccion.csv`, `resultados.csv`, `contrastes.csv` en el repositorio; se publicarán en OSF.

**Miscellaneous extraction details**
Unidad de análisis: estudio (varios informes vinculados); se extrae del informe más completo.

---

## SÍNTESIS Y EVALUACIÓN DE CALIDAD

**Planned data transformations**
Δ en puntos porcentuales frente a la línea base de referencia; normalización de curvas por turno al turno 1; pendientes por estudio (regresión ponderada por número de preguntas por turno).

**Missing data**
Se registra `NR`; no se imputan valores; los análisis usan los estudios con datos disponibles y se indica el número.

**Data validation**
Verificación humana de cada fila; comprobaciones automáticas de vocabularios y rangos en Python.

**Quality assessment**
Lista de 10 ítems adaptada de Kitchenham (`checklist_calidad.md`), aplicada al Nivel 2; umbral ≥ 50 % calculado solo con los ítems de validez (reproducibilidad, líneas base con el mismo modelo, métricas y tipo de historial, ablación o análisis de errores, robustez); ítems de reporte y apertura informados por ítem; 20 % puntuado de forma independiente por la autora.

**Synthesis plan**
Sin metaanálisis (heterogeneidad de *benchmarks*, métricas y modelos). Síntesis narrativa y temática según SWiM: taxonomías por PI; tablas comparativas; contrastes dentro del estudio como evidencia principal; Δ sobre la línea base de referencia solo dentro de grupos comparables (mediana, rango, dirección del efecto); PI0 descriptivo con IC de Wilson y prueba de tendencia de Cochran–Armitage exacta (2019–2025; 2026 aparte); curvas y pendientes de degradación estratificadas por tipo de historial. Plan: `plan_sintesis.md`.

**Criteria for conclusions / inference criteria**
Indicador D4 y criterio de reformulación de la brecha como se describen en «Expectations / hypotheses». Confianza en cada hallazgo (alta/moderada/baja) con reglas inspiradas en GRADE-CERQual: limitaciones metodológicas, coherencia (sobre contrastes dentro del estudio), suficiencia y pertinencia.

**Synthesist masking**
No aplicable (autora única).

**Synthesis reliability**
Los números, tablas y figuras se generan por *script* a partir de los datos verificados; no se transcriben a mano.

**Synthesis reconciliation procedure**
No aplicable (autora única).

**Publication bias analyses**
No se aplican pruebas formales (sin metaanálisis); se discute el predominio de resultados positivos, la contaminación de *benchmarks* y el desfase de líneas base; la inclusión de preprints busca mitigar el sesgo de publicación.

**Sensitivity analyses / robustness checks**
(1) Reincorporar estudios bajo el umbral de calidad; (2) excluir preprints; (3) D4 en versión laxa; (4) D4 sin registros de bola de nieve; (5) D4 con el subconjunto auditado si se activa la contingencia; (6) recuento del criterio de reformulación incluyendo los grafos neuronales tipo IGSQL.

**Synthesis procedure justification**
SWiM es la guía recomendada cuando no es posible un metaanálisis.

**Synthesis data management and sharing**
Scripts de análisis y datos en el repositorio; se publicarán en OSF con el artículo.

**Miscellaneous synthesis details**
Las enmiendas posteriores al registro se documentan en `enmiendas.md` y en OSF.
