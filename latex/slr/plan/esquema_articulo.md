# Esquema del artículo — RSL Text-to-SQL conversacional

Modo: solo esquema y mapa de evidencia. No se redactó prosa del artículo ni se escribió ningún archivo. Patrón elegido: revisión sistemática PRISMA 2020. Es un híbrido de IMRaD (método y resultados por pregunta de investigación) con revisión temática (PI1–PI5).

---

## Decisiones tomadas (autora, 2026-10-13)

D1: a (9 tablas en el texto; versión corta → b) · D2: b (bibliometría: un párrafo + `bib_comunidad` y `bib_coocurrencia_tecnicas`; resto al suplemento) · D3: a (subsección transversal de efectos §4.6) · D4: a (sección propia de trabajos relacionados con tabla) · D5: a (criterio M8 neutral; conflicto declarado) · D6: a (enviar antes de cumplir 6 meses desde la búsqueda, es decir antes de 2027-04-11; sin repetir la búsqueda).

Cambios posteriores (autora, 2026-10-14): D1 y D2 revisadas para acercar las figuras a su mención — la tabla de calidad, la figura de paradigma por año y la de coocurrencia pasan al material suplementario; la bibliometría (IV-D) se amplía con una figura compuesta de cuatro paneles (comunidad, red de citas, países, modelos). Criterios de elegibilidad en tabla del texto principal. D5: proyecto de tesis de pregrado (no doctoral). D6 suspendida: sin revista de destino; el manuscrito es un trabajo académico de curso con formato IEEEtran. Título: opción 2.

## 0. Decisiones para la autora

**Responde con los códigos, por ejemplo `D1: a, D2: b, …`**

**D1. Qué tablas van en el texto principal y cuáles en el suplemento** (lista completa en §2)
- a) **9 tablas en el texto:** revisiones previas, IA y verificación humana por fase, enmiendas, D4 con sensibilidades, calidad agregada, efectos con confianza, taxonomías PI1–PI2, contraste un turno/multiturno PI3–PI4 y PI5. El resto va al suplemento. Si se pasa de 20 páginas, se degradan primero las tres marcadas «corte».
- b) **5 tablas en el texto** (IA, D4, efectos con confianza, contraste PI3–PI4, PI5). Las demás pasan al suplemento y las enmiendas quedan en prosa.
- c) Todas las tablas de resultados en el texto. Excede el límite de páginas.
- **Recomiendo a.** Las tablas de IA, enmiendas y revisiones previas son lo que más escrutinan los revisores de una RSL con IA. La versión corta se obtiene con b.

**D2. Bibliometría (A6, exploratoria): ¿Resultados o suplemento?**
- a) Subsección completa en Resultados, con las 9 figuras `bib_*`.
- b) Un párrafo corto en Resultados (§4.4) con `bib_comunidad`, más `bib_coocurrencia_tecnicas` dentro de PI3. Las otras 7 figuras y todas las tablas `bib_*` van al suplemento.
- c) Todo al suplemento, con una sola frase en Resultados.
- **Recomiendo b.** Es exploratoria y no pre-registrada, y no modifica ninguna conclusión. Esas dos figuras sí apoyan la Discusión (comunidad que produce multiturno; combinación de técnicas).

**D3. Dónde presentar los efectos de los componentes (contrastes dentro del estudio)**
- a) Una subsección transversal (§4.6) con `pi_efectos_componentes` y la tabla de efectos con confianza. Cada subsección PI1–PI4 conserva su taxonomía y su pregunta específica, y remite a §4.6.
- b) Una tabla y una figura por PI.
- **Recomiendo a.** La figura y las clases «Otros componentes» son compartidas, y ahorra aproximadamente una página. Cambia respecto del orden de los archivos actuales, porque añade una subsección.

**D4. Trabajos relacionados**
- a) Sección propia, corta, con una tabla comparativa de revisiones.
- b) Fusionarla con la Introducción.
- **Recomiendo a.** El posicionamiento frente a Yang 2025, Liu 2026 y Bui 2026 es la justificación del ítem 3 y debe poder citarse como tabla. En la versión corta se funde con la Introducción.

**D5. Postura sobre la brecha de la tesis y el conflicto de intereses**
- a) Reportar el criterio M8 como «criterio pre-especificado de brecha de investigación», sin nombrar la tesis en el cuerpo, y declarar en «Conflictos de interés» que la autora desarrolla una tesis de pregrado (título profesional) relacionada.
- b) Nombrar la tesis en la Discusión.
- c) No mencionar la relación.
- **Recomiendo a.** Hay sesgo de lealtad: la autora tiene interés en que la brecha exista, y M8 y D4 fueron fijados por ella. Declararlo protege la credibilidad. El criterio ya está registrado en OSF.

**D6. Fecha de envío y actualización de la búsqueda**
- a) Enviar antes de que se cumplan 6 meses desde la búsqueda (2026-10-11, ver `registro_busquedas.csv`) y no repetirla.
- b) Prever repetir las cadenas v4 en el intervalo nuevo (regla de `protocolo_es.md` §5b), con costo de cribado y de extracción.
- **Recomiendo decidir la fecha objetivo ahora.** El cronograma del protocolo prevé redacción hasta marzo de 2027, justo en el límite. Si se elige b, el artículo debe reportar la segunda búsqueda como actualización.

### 0b. Alertas de consistencia (resolver en los scripts antes de redactar; los números del texto deben salir de scripts)

1. **Marcadores `[TO COMPLETE]` abiertos.** Están en los cuatro `*_methods_selection.md`: verificación humana, fechas, rondas del piloto y prueba de sensibilidad con conocidos de la bola de nieve. En la bola de nieve, el texto de sensibilidad con conocidos es contradictorio («0 of 13 retrieved»). Eso exige revisar el script y quizá eliminar la frase.
2. **Conteos por base.** `TA_methods_selection.md` (arXiv, Scopus, duplicados) no coincide con `prisma_conteos.json → bases.identificados`, `bases.duplicados_eliminados` ni con `registro_busquedas.csv` (B02, B03). Hay que unificar la fuente, y debe ser el JSON.
3. **Total de estudios.** Comparar `informe_acuerdo_extraccion.md` (encabezados «Nivel 1» y «Nivel 2») con `pi0_resultados.json → n_estudios, n_multiturno` y con `prisma_conteos.json → incluidos` (bases) más `otros_metodos.incluidos`. Aparentan no cuadrar. Verificar con `verificar_numeros.py`.
4. **Nivel 2: base ≥ umbral frente a todos.** Las taxonomías PI1–PI5 usan los estudios del Nivel 2 sobre el umbral de validez (`pi15_resultados.json → nivel2_umbral`). El contraste PI3–PI4 (`pi34_tecnicas_escenario.csv`) usa todos los multiturno (`nivel2`). Hay que declarar la base en cada tabla o usar una sola.
5. **No recuperados.** `enmiendas.md` A4 informa solo el brazo de bases. `pi0_resultados.json → no_recuperados_por_senal` suma ambos brazos. El texto debe separar los brazos, como en el PRISMA.
6. **Calidad sin archivo de hallazgos.** No existe `PIx.md` aprobado para §4.5. Falta un `calidad_resultados.json` (distribución por ítem CQ, validez, estudios bajo el umbral) y que la autora lo apruebe, porque la regla 3 exige hallazgos aprobados.
7. **Redondeos.** Los textos de `confianza_hallazgos.csv` (hallazgo) redondean la mediana distinto de `pi_efectos_componentes.csv`. `PI5.md` muestra el artefacto de punto flotante en `valor_turno1` de R01031/SQA. Corregir en el generador.
8. **Pendientes de forma.** Faltan el título, la revista y el título corto en `main.tex` (`\pendiente`). La figura de prueba de `01-introduccion.tex` debe eliminarse. Verificar la guía de autores vigente de IEEE Latin America Transactions (límite de páginas y formato del resumen); no la he podido verificar aquí.

---

## 1. Árbol de secciones

Objetivo total: unas 9 700 palabras de cuerpo, más resumen, 8 figuras, 9 tablas y referencias. Es el objetivo de la versión larga: en el límite superior de las 15–20 páginas con dos columnas. Para llegar a ~15 páginas, aplicar los «corte».

| Sección (label) | Propósito | Ítems PRISMA | Palabras | Tipo |
|---|---|---|---|---|
| **Título y metadatos** (`main.tex`) | Identificar el trabajo como revisión sistemática PRISMA 2020. Título provisional en `protocolo_es.md` §1. | 1 | — | Núcleo |
| **Resumen** (`sec:resumen`) | Estructurado: Contexto, Objetivo, Método, Resultados, Conclusiones. Añadir líneas de Limitaciones, Financiamiento y Registro (OSF). Palabras clave. | Resumen 1–12 | ~220 (fuera del total) | Núcleo |
| **1. Introducción** (`sec:introduccion`) | Problema, brecha y preguntas. | | 800 | |
| 1.1 `sec:intro-contexto` | Text-to-SQL/NLIDB y por qué el multiturno añade dependencia de contexto (elipsis, correferencia, propagación de errores). Citar SParC/CoSQL. | 3 | 250 | Núcleo |
| 1.2 `sec:intro-justificacion` | Revisiones existentes y ausencia de una RSL multiturno. Pilares PI1–PI4. | 3 | 300 | Núcleo |
| 1.3 `sec:intro-objetivos` | Objetivo, PI0–PI5, contribuciones y organización. | 4 | 250 | Núcleo |
| **2. Trabajos relacionados** (`sec:relacionados`) | Posicionar frente a revisiones previas. Sirve a la justificación. | | 700 | |
| 2.1 `sec:rel-generales` | Revisiones generales de Text-to-SQL/NLIDB que tratan lo multiturno como subtema. | 3 | 250 | Corte |
| 2.2 `sec:rel-conversacional` | Revisiones centradas en contexto/conversacional (Yang 2025; Li-Qu-Haffari 2020). Revisiones sistemáticas de 2026 (Liu; Bui), con lo verificado en `00_analisis_brecha.md`. | 3 | 250 | Núcleo |
| 2.3 `sec:rel-brecha` | Diferencias de esta RSL (método, PICOC, ejes) y tabla comparativa. | 3 | 200 | Núcleo |
| **3. Método** (`sec:metodo`) | Reproducibilidad. Kitchenham y Charters, reportado por PRISMA 2020. | | 1 900 | |
| 3.1 `sec:met-protocolo` | Protocolo PRISMA-P, registro OSF, enmiendas A1–A6 y su estado (A4–A6 pendientes en OSF). Tabla de enmiendas. | 24a, 24b, 24c | 250 | Núcleo |
| 3.2 `sec:met-picoc` | PICOC, PI0–PI5, diseño en dos niveles (D7) e indicador D4 con su regla. | 4 | 150 | Corte (fusionar con 3.1) |
| 3.3 `sec:met-elegibilidad` | IC/EX, definición de multiturno, contribución central, casos B1–B6, reglas de versiones. Tabla completa en el suplemento. | 5 | 200 | Núcleo |
| 3.4 `sec:met-busqueda` | Cinco fuentes y su forma de captura (A2 para ACM). Cadena v4 y sensibilidad con el conjunto de referencia (A1). Fecha de la búsqueda. Cadenas completas en suplemento. Bola de nieve (OpenAlex y Semantic Scholar). | 6, 7 | 250 | Núcleo |
| 3.5 `sec:met-seleccion` | Cribado dual con IA, tercer revisor, QC, verificación humana reducida (A3), cribado de texto completo con extractos (A5a), segundo espacio de cribado en la bola de nieve (A5b). Tabla IA y verificación. | 8 | 350 | Núcleo |
| 3.6 `sec:met-extraccion` | Formulario, dos niveles, doble extracción por IA y resolución, muestra independiente (A5c), `foro_nivel` (A5d). Resultados primarios y variables. | 9, 10a, 10b | 200 | Núcleo |
| 3.7 `sec:met-calidad` | Lista de calidad de 10 ítems, perfil tipo semáforo, umbral solo con ítems de validez. | 11 | 150 | Núcleo |
| 3.8 `sec:met-sintesis` | SWiM. Comparabilidad estricta. Contrastes dentro del estudio y Δ frente a la línea base. Wilson y Cochran–Armitage. Estratificación por historial. Sesgos, sensibilidad y confianza inspirada en GRADE-CERQual. | 12, 13a–f, 14, 15 | 350 | Núcleo |
| **4. Resultados** (`sec:resultados`) | Hallazgos aprobados de PI0–PI5. Sin interpretación. | | 3 300 | |
| 4.1 `sec:res-seleccion` | Flujo PRISMA y motivos de exclusión por código. Informes no recuperados. | 16a, 16b | 300 | Núcleo |
| 4.2 `sec:res-caracteristicas` | PI0: año × escenario, tipo de foro, paradigma por año, pilares centrales por escenario, sin entrenamiento, no recuperados por escenario. | 17, 20a | 350 | Núcleo |
| 4.3 `sec:res-d4` | Indicador D4, tendencia 2019–2025, 2026 aparte, sensibilidades. Tabla D4. | 20b, 20d | 300 | Núcleo |
| 4.4 `sec:res-bibliometria` | Panorama bibliométrico exploratorio (A6), etiquetado como tal. | 17 | 200 | Corte |
| 4.5 `sec:res-calidad` | Distribución de calidad (perfil por ítem), estudios bajo el umbral, acuerdo de la IA con la autora. | 18 | 300 | Núcleo |
| 4.6 `sec:res-efectos` | Contrastes dentro del estudio por clase de componente. Confianza por hallazgo. Δ frente a la línea base (secundaria). | 19, 20b, 20c, 22 | 250 | Núcleo |
| 4.7 `sec:res-pi1` | PI1: técnicas, insumos y reescritura frente a concatenación. | 19, 20a | 250 | Núcleo |
| 4.8 `sec:res-pi2` | PI2: representación, actualización, coste del contexto, grafo y estado estructurado. | 19, 20a | 280 | Núcleo |
| 4.9 `sec:res-pi3` | PI3: vinculación de esquemas e inferencia de joins en multiturno frente a un turno. Coocurrencia. | 19, 20a | 280 | Núcleo |
| 4.10 `sec:res-pi4` | PI4: mecanismos de autocorrección, aclaración y señales. Contraste con un turno. | 19, 20a | 250 | Núcleo |
| 4.11 `sec:res-pi5` | PI5: benchmarks, métricas, tipo de historial y degradación por turno, estratificada. | 19, 20c | 340 | Núcleo |
| 4.12 `sec:res-sesgos` | Sesgos de notificación y sensibilidades no tratadas en otras subsecciones. | 20d, 21 | 200 | Corte (fusionar con 4.3 y 4.6) |
| **5. Discusión** (`sec:discusion`) | Redactada aparte con el esqueleto de §4 de este documento. | | 1 800 | |
| 5.1 `sec:dis-hallazgos` | Síntesis de hallazgos principales. | 23a | 250 | Núcleo |
| 5.2 `sec:dis-interpretacion` | Interpretación: multiturno menos investigado, técnicas no trasladadas, estado, efectos, degradación. | 23a, 23b | 600 | Núcleo |
| 5.3 `sec:dis-comparacion` | Comparación con revisiones previas. | 23a | 300 | Núcleo |
| 5.4 `sec:dis-brecha` | Criterio M8 y agenda de investigación. | 23d | 400 | Núcleo |
| 5.5 `sec:dis-practica` | Implicaciones para práctica y evaluación. | 23d | 250 | Corte |
| **6. Amenazas a la validez** (`sec:amenazas`) | Lista de §5. Convención en RSL de computación. | | 650 | |
| 6.1 `sec:am-seleccion` | Constructo y selección, incluida la IA. | 23c | 250 | Núcleo |
| 6.2 `sec:am-interna` | Extracción, calidad y síntesis. | 23c | 250 | Núcleo |
| 6.3 `sec:am-externa` | Externa y de conclusión. | 23b, 23c | 150 | Núcleo |
| **7. Conclusiones** (`sec:conclusiones`) | Respuestas breves a PI0–PI5 y trabajo futuro. | 23d | 300 | Núcleo |
| **Declaraciones** (`08-declaraciones`, sin numerar) | Registro, financiamiento, conflictos (incluida la lealtad, D5), disponibilidad de datos y código, declaración de uso de IA. | 24, 25, 26, 27 | 250 | Núcleo |
| **Total del cuerpo** | | | ~9 700 | |

Estimación de páginas con 2 columnas: 9 700 palabras ≈ 10 páginas, más figuras ≈ 3,5, tablas ≈ 3,5 y referencias ≈ 2,5. Total ≈ 19–20 páginas. Es una estimación a verificar al compilar.

**Transiciones**
- **1 → 2:** la brecha identificada en la Introducción se contrasta con lo que cubren las revisiones previas.
- **2 → 3:** lo que no cubren las revisiones previas define el diseño de una RSL con PICOC.
- **3 → 4:** el diseño en dos niveles estructura los Resultados (mapeo, luego profundidad).
- **4 → 5:** cada «Para la discusión» de PI0–PI5 alimenta la interpretación, y solo ahí.
- **5 → 6:** las interpretaciones se acotan con las amenazas.
- **6 → 7:** las conclusiones se limitan a lo que las amenazas permiten.

---

## 2. Ubicación de figuras y tablas

### 2.1 Figuras (15)

| Figura | Sección | Lugar | Motivo |
|---|---|---|---|
| `prisma_flujo` | 4.1 | Texto | Exigida por PRISMA 2020 (16a). |
| `pi0_anio_escenario` | 4.2 | Texto | Evolución anual por escenario; base de D4. |
| `pi0_paradigma_anio` | 4.2 | Texto (corte) | Contexto de la transición pre-LLM a LLM; candidata a suplemento. |
| `d4_tendencia` | 4.3 | Texto | Indicador primario de PI0. |
| `pi_efectos_componentes` | 4.6 | Texto | Evidencia principal de PI1–PI4 en una sola figura. |
| `pi5_degradacion` | 4.11 | Texto | Resultado central de PI5; estratos separados. |
| `bib_comunidad` | 4.4 | Texto (corte) | Sustenta la Discusión sobre qué comunidades producen multiturno. |
| `bib_coocurrencia_tecnicas` | 4.9 | Texto (corte) | Combinaciones PI3/PI4; apoya M8. |
| `bib_red_citas` | Suplemento | Suplemento | Exploratoria; se menciona en una frase de 4.4. |
| `bib_paises` | Suplemento | Suplemento | Exploratoria. |
| `bib_modelos` | Suplemento | Suplemento | El Nivel 1 solo registró modelos de las páginas 1–2 (subestima). |
| `bib_autores` | Suplemento | Suplemento | Exploratoria; poco valor para PI0–PI5. |
| `bib_autores_red` | Suplemento | Suplemento | Ídem. |
| `bib_terminos_barras` | Suplemento | Suplemento | Apoyo léxico. |
| `bib_terminos_nube` | Suplemento | Suplemento | Ilustrativa; la propia leyenda lo dice. Opcional omitirla. |

### 2.2 Tablas propuestas

| Tabla (label) | Sección | Lugar | Fuente CSV/archivo | Columnas propuestas | Motivo |
|---|---|---|---|---|---|
| `tab:relacionados` | 2.3 | Texto | `00_analisis_brecha.md` (verificar en el texto de cada revisión) | Revisión; año; tipo (sistemática/narrativa); protocolo documentado; multiturno (sí/subtema/no); ejes PI1–PI4 cubiertos | Diferencia explícita frente a lo existente. |
| `tab:enmiendas` | 3.1 | Texto (corte) | `enmiendas.md` | N.º; fecha; fase afectada; cambio (una línea); estado OSF | Ítem 24c. Resumir A4–A6 como «Pendiente». |
| `tab:ia` | 3.5 | Texto | `Screening_*/*_methods_selection.md` (4), `informe_acuerdo_extraccion.md`, `enmiendas.md` A3, A5 | Fase; herramienta; modelo (ID exacto); roles; verificación humana; acuerdo (kappa o %) | Ítem 8 y transparencia de IA. Cifras generadas por script. |
| `tab:d4` | 4.3 | Texto | `pi0_resultados.json`, `sensibilidad.json` | Análisis; k; n; proporción; IC 95 % de Wilson; conclusión según la regla | Indicador primario más sensibilidades. |
| `tab:calidad` | 4.5 | Texto (corte) | `calidad.csv` agregado (nuevo script) | Ítem CQ; tipo (validez/reporte); proporción en 1 / 0,5 / 0 | Resumen del perfil por ítem. |
| `tab:efectos` | 4.6 | Texto | `pi_efectos_componentes.csv` ⨝ `confianza_hallazgos.csv` | Pilar; clase; estudios; contrastes; mediana; rango; estudios +/−/nulos; % de contrastes positivos; validez media; confianza | Núcleo de PI1–PI4. |
| `tab:taxo-pi12` | 4.7–4.8 | Texto (corte) | `pi1_tecnicas.csv`, `pi2_representacion.csv` | Campo; código; estudios; % | Taxonomía de PI1 y PI2. Excluir `pi2_grafo_*` (van al suplemento). |
| `tab:contraste-pi34` | 4.9–4.10 | Texto | `pi34_tecnicas_escenario.csv` | Campo; código; multiturno (n, %); un turno (n, %); no trasladado | Respuesta a «comparación con un turno». Declarar la base. |
| `tab:pi5` | 4.11 | Texto | `pi5_historial.csv`, `pi15_resultados.json → degradacion` | Estrato; estudios (n, %); curvas; pendiente mediana | Estratos de historial y degradación. |
| S1 | Suplemento | Supl. | `registro_busquedas.csv`, `cadenas.md` | Base; fecha; campos; cadena exacta; filtros; resultados | Ítem 7: cadenas completas. |
| S2 | Suplemento | Supl. | `03_criterios_elegibilidad.md` | Código; criterio | Ítem 5 completo. |
| S3 | Suplemento | Supl. | `prisma_conteos.json` (motivos), `ft_map.csv` | Estudio; motivo de exclusión | Ítem 16b. |
| S4 | Suplemento | Supl. | `formulario_extraccion.md` | Bloque; campo; vocabulario | Ítems 9–10. |
| S5 | Suplemento | Supl. | `checklist_calidad.md` | Ítem; rúbrica 1 / 0,5 / 0 | Ítem 11. |
| S6 | Suplemento | Supl. | `calidad.csv` | Estudio × ítem (semáforo) | Perfil por estudio exigido por el protocolo. |
| S7 | Suplemento | Supl. | `pi_tabla_comparativa.csv` | Estudio; año; pilares; paradigma; sin entrenamiento; PI1–PI4; historial; benchmark; métrica; Δ; validez | Ítem 19. |
| S8 | Suplemento | Supl. | `pi3_joins.csv`, `pi4_mecanismos.csv`, `pi1_tecnicas.csv` (insumos), `pi2_representacion.csv` (grafo) | Campo; código; estudios; % | Taxonomías sobre la base del umbral. |
| S9 | Suplemento | Supl. | `pi5_benchmarks.csv`, `pi5_metricas.csv`, `taxonomia_otra.csv` | Familia; estudios | Taxonomía de benchmarks y métricas, y consolidación de `OTRA`. |
| S10 | Suplemento | Supl. | `pi5_pendientes.csv` | Estudio; benchmark; métrica; historial; turnos; pendiente; valor del turno 1 | Pendientes individuales. |
| S11 | Suplemento | Supl. | `pi_deltas_linea_base.csv` | Estudio; benchmark; métrica; turno; historial; propuesto; línea base; Δ | Evidencia secundaria. |
| S12 | Suplemento | Supl. | `sensibilidad.json`, `pi0_training_free.csv` | Análisis; clase; mediana; estudios | Sensibilidades completas. |
| S13 | Suplemento | Supl. | `pi0_foros.csv`, `pi0_venues_top.csv`, `pi0_pilares_escenario.csv`, `pi0_no_recuperados_escenario.csv` | Según archivo | Descriptivas de PI0. |
| S14 | Suplemento | Supl. | `bib_*.csv` | Según archivo | Respaldo de la bibliometría exploratoria (A6). |
| S15 | Suplemento | Supl. | `informe_acuerdo_extraccion.md`, `muestra_independiente.json` | Verificación; n; confirmados/total; IC 95 % | Transparencia del proceso con IA. |

---

## 3. Mapa de evidencia

Notación: `archivo → clave/columna`. Ningún valor está copiado. Los «Para la discusión» de cada `PIx.md` alimentan solo §5.

### 3.1 Resultados

| Sección | Afirmación | Fuente → clave/sección |
|---|---|---|
| 4.1 | Registros identificados por base y total | `prisma_conteos.json → bases.identificados.*` |
| 4.1 | Duplicados, cribados, buscados, no recuperados, evaluados, incluidos (bases) | `prisma_conteos.json → bases.{duplicados_eliminados, cribados, buscados, no_recuperados, evaluados, incluidos}` |
| 4.1 | Excluidos por código y motivo | `prisma_conteos.json → bases.excluidos_cribado_por_codigo`, `bases.excluidos_texto_completo_por_motivo` |
| 4.1 | Brazo «otros métodos» | `prisma_conteos.json → otros_metodos.*` |
| 4.1 | Acuerdo entre revisores IA (TA y FT) | `Screening_*/*_methods_selection.md` (extraer por script) |
| 4.2 | Estudios por año y escenario | `pi0_anio_escenario.csv`, `pi0_resultados.json → n_estudios, n_multiturno` |
| 4.2 | Tipo y nivel de foro | `pi0_foros.csv` (`foro_tipo`, `foro_nivel`) |
| 4.2 | Foros más frecuentes | `pi0_venues_top.csv` |
| 4.2 | Paradigma por año | `pi0_paradigma_anio.csv` |
| 4.2 | Pilares centrales por escenario | `pi0_pilares_escenario.csv` |
| 4.2 | Sin entrenamiento por año y pilar | `pi0_training_free.csv` |
| 4.2 | No recuperados por escenario | `pi0_no_recuperados_escenario.csv`, `pi0_resultados.json → no_recuperados_por_senal` |
| 4.3 | D4 estricto y laxo, IC y conclusión | `pi0_resultados.json → D4.{estricto, laxo}.{k, n, p, ic95, conclusion}` |
| 4.3 | Tendencia 2019–2025 | `pi0_resultados.json → D4.tendencia_2019_2025`, `d4_tendencia.csv` |
| 4.3 | 2026 parcial | `pi0_resultados.json → D4.anio_2026_parcial` |
| 4.3 / 4.12 | Sensibilidades | `sensibilidad.json → 2_sin_preprints_D4, 3_D4_laxo, 4_D4_solo_busqueda_en_bases, A5_D4_foros_de_primer_nivel, A4_D4_con_no_recuperados_segun_senal, 5_contingencia_nivel1` |
| 4.4 | Red de citas y afiliación | `bibliometria_resultados.json → red.*, citas_mediana_por_anio, tipo_afiliacion, no_resueltos` |
| 4.4 | Comunidad del foro | `bib_comunidad.csv` |
| 4.4 | Países, más citados, términos | `bib_paises.csv`, `bib_mas_citados_multiturno.csv`, `bib_terminos.csv` |
| 4.5 | Validez por estudio, estudios sobre el umbral y bajo el umbral | `calidad.csv → validez_pct, supera_umbral`; `pi15_resultados.json → nivel2, nivel2_umbral` |
| 4.5 | Perfil por ítem | `calidad.csv → CQ1…CQ10` |
| 4.5 | Acuerdo IA–autora en calidad | `informe_acuerdo_extraccion.md → «ítems de calidad», «calidad, ítem idéntico»` |
| 4.6 | Efecto por clase de componente | `pi_efectos_componentes.csv → mediana_pp, min_pp, max_pp, estudios_positivos/negativos/nulos, pct_contrastes_positivos` |
| 4.6 | Confianza por hallazgo | `confianza_hallazgos.csv → limitaciones_metodologicas, coherencia, suficiencia, pertinencia, confianza` |
| 4.6 | Δ frente a la línea base (secundaria) | `pi15_resultados.json → deltas_linea_base`; `pi_deltas_linea_base.csv` |
| 4.7 | Técnicas de PI1 e insumos | `pi1_tecnicas.csv`; `PI1.md → Taxonomía` |
| 4.7 | Reescritura frente a concatenación | `pi_efectos_componentes.csv → pilar=PI1, clase`; `PI1.md → «Pregunta específica»` |
| 4.7 | Ejemplos de reescritura y concatenación | `PI1.md` (R00033, R00086, R00097, R00924, R00950, R01034; R00072, R00100) |
| 4.8 | Representación, actualización, coste | `pi2_representacion.csv → pi2_representacion, pi2_actualizacion, pi2_coste_contexto` |
| 4.8 | Grafo: nodos y dinamismo (con NR alto) | `pi2_representacion.csv → pi2_grafo_nodos, pi2_grafo_dinamico`; `PI2.md → Limitaciones` |
| 4.8 | Efecto de grafo/estado estructurado y de SQL previo | `pi_efectos_componentes.csv → pilar=PI2` |
| 4.9 | Técnicas de vinculación e inferencia de joins | `pi3_joins.csv`; `PI3.md → Taxonomía` |
| 4.9 | Estudios con inferencia no implícita | `PI3.md` (R00981, R00120) |
| 4.9 | Un turno frente a multiturno | `pi34_tecnicas_escenario.csv → campo=pi3_*, multiturno, un_turno, pct_*` |
| 4.9 | Efecto de la vinculación de esquemas | `pi_efectos_componentes.csv → pilar=PI3` |
| 4.9 | Coocurrencia de técnicas | `bib_coocurrencia_multiturno.csv`, `bib_coocurrencia_un_turno.csv` |
| 4.10 | Mecanismos y señales | `pi4_mecanismos.csv → pi4_mecanismo, pi4_senal, pi4_aplicado_multiturno` |
| 4.10 | Contraste y técnica no trasladada | `pi34_tecnicas_escenario.csv → campo=pi4_*, no_trasladado`; `pi0_resultados.json → tecnicas_un_turno_no_trasladadas` |
| 4.10 | Efecto por clase | `pi_efectos_componentes.csv → pilar=PI4` |
| 4.11 | Benchmarks y métricas | `pi5_benchmarks.csv`, `pi5_metricas.csv`, `taxonomia_otra.csv` |
| 4.11 | Tipo de historial | `pi5_historial.csv → campo=historial_eval` |
| 4.11 | Degradación reportada, errores de join, contaminación | `pi5_historial.csv → degradacion_reportada, errores_join_reportados, contaminacion_discutida` |
| 4.11 | Pendientes por estrato | `pi15_resultados.json → degradacion`; `pi5_pendientes.csv` |
| 4.11 | Muestra independiente de la autora (historial_eval) | `informe_acuerdo_extraccion.md → historial_eval, discrepancias` |
| 4.12 | Sensibilidad al umbral y a los preprints | `sensibilidad.json → 1_reincorporar_bajo_umbral, 2_sin_preprints_efectos` |
| 4.12 | Recuperación diferencial | `pi0_no_recuperados_escenario.csv`; `sensibilidad.json → A4_*` |

### 3.2 Discusión (por argumento)

Ver §4.

---

## 4. Esqueleto argumental de la Discusión

Para el modelo que la redacta. No hay prosa: afirmación, evidencia, salvedad.

### 4.1 Hallazgos principales (5.1)
- **H1.** El escenario multiturno es una fracción minoritaria de los estudios que abordan vinculación de esquemas o autocorrección como contribución central.
  - Evidencia: `pi0_resultados.json → D4`, `sensibilidad.json → todas las variantes`.
- **H2.** No hay tendencia temporal detectable en esa proporción.
  - Evidencia: `D4.tendencia_2019_2025`, `d4_tendencia.csv`.
- **H3.** El historial plano domina la representación del estado. Las representaciones estructuradas son minoritarias.
  - Evidencia: `pi2_representacion.csv`.
- **H4.** Los contrastes dentro del estudio van, en su gran mayoría, en dirección positiva y de magnitud moderada.
  - Evidencia: `pi_efectos_componentes.csv`, `confianza_hallazgos.csv`.
- **H5.** La inferencia de joins es mayoritariamente implícita en multiturno.
  - Evidencia: `pi3_joins.csv`, `pi34_tecnicas_escenario.csv`.
- **H6.** El tipo de historial usado en la evaluación varía mucho y a menudo no se reporta. Solo un subconjunto permite observar propagación de errores.
  - Evidencia: `pi5_historial.csv`, `pi15_resultados.json → degradacion`.
- **H7.** No hay estudios que cumplan a la vez (a), (b) y (c) del criterio M8.
  - Evidencia: `pi15_resultados.json → brecha_M8`.

### 4.2 Interpretación (5.2)

| # | Argumento | Evidencia | Salvedad obligatoria |
|---|---|---|---|
| I1 | «Considerablemente menos investigado» se cumple por la regla registrada, no por una prueba de hipótesis. | `D4.*.conclusion`, `sensibilidad.json` | El indicador depende del marco de elegibilidad, que sesga hacia más multiturno (PI0.md, Limitaciones). No se generaliza a todo el campo. |
| I2 | La ausencia de tendencia convive con IC anuales amplios. Se descarta «el campo se está cerrando». | `d4_tendencia.csv`, `D4.tendencia_2019_2025` | Potencia baja en los años tempranos. 2026 es parcial y queda fuera de la prueba. |
| I3 | Las técnicas de un turno aparecen en multiturno con frecuencias distintas. La autoconsistencia es la única ausente. Aclaración con usuario y señal de usuario son proporcionalmente más frecuentes en multiturno. Ejecución y verificación, menos. | `pi34_tecnicas_escenario.csv` | Son frecuencias, no resultados. Las bases difieren de las del Nivel 2 con validez (alerta 4). |
| I4 | La inferencia algorítmica de joins es casi inexistente en multiturno. | `pi3_joins.csv` | Con 2 estudios, el contraste implícito/algorítmico dentro del estudio es imposible (`PI3.md → Limitaciones`). No se analizó escala. |
| I5 | El estado estructurado y el grafo muestran efecto positivo consistente sobre la línea base propia. | `pi_efectos_componentes.csv → PI2`, `confianza_hallazgos.csv` | **Sesgo de notificación:** las ablaciones se reportan para justificar el componente. Los contrastes negativos son raros por construcción. Citar `estudios_negativos` y la sensibilidad a preprints. La clase «Otros componentes» es heterogénea. |
| I6 | Los efectos de componentes (pocos pp) son pequeños frente a las pendientes de degradación por turno. | `pi_efectos_componentes.csv`, `pi5_pendientes.csv` | Interpretación descriptiva. Métricas, benchmarks e historiales distintos; no inferir causalidad. |
| I7 | Mucha información crítica no se reporta (técnica de restauración, mecanismo de PI4, historial, campos de grafo). | `pi1_tecnicas.csv → NR`, `pi4_mecanismos.csv → NR`, `pi5_historial.csv → NR` | El NR puede deberse a la extracción de la IA. Se verificó por muestreo (`informe_acuerdo_extraccion.md`). |
| I8 | La evaluación con historial gold sobreestima la robustez. Solo PREDICHO mide propagación de errores, y hay pocas curvas. | `pi5_historial.csv`, `pi15_resultados.json → degradacion` | Las pendientes mezclan profundidad del turno y dificultad de las preguntas. No se agrupan los estratos. |
| I9 | Los estudios multiturno se concentran en la comunidad de PLN. La de bases de datos tiene presencia menor. | `bib_comunidad.csv` | Exploratorio (A6). Depende de la clasificación del foro y de OpenAlex. |

### 4.3 Comparación con revisiones previas (5.3)
- Contraste de alcance y método con Yang 2025 (única centrada en conversacional), Liu 2026 y Bui 2026 (sistemáticas generales), y con las generales (Shi 2026, Quamar 2022 y otras de `00_analisis_brecha.md`). Fuente: `00_analisis_brecha.md` y los textos completos.
- **Pendiente de verificación:** lo que se afirme sobre Yang 2025 debe basarse en su texto completo, no en el resumen (`protocolo_es.md` §6, `00_analisis_brecha.md`). Lo mismo para Liu 2026 (la versión publicada puede diferir de arXiv v2).
- Aportes diferenciales: registro y protocolo; PICOC; contraste explícito entre un turno y multiturno; degradación por turno con estratos de historial; contrastes dentro del estudio.
- No afirmar superioridad de método sobre los *surveys*: tienen objetivos distintos.

### 4.4 Implicaciones para la brecha (M8) y la agenda (5.4)
- **Resultado:** el criterio de reformulación no se activó. No se encontraron estudios que combinen (a) estado estructurado explícito, (b) inferencia algorítmica de joins o autocorrección por ejecución y (c) historial predicho o solo preguntas. Se confirma con la sensibilidad de grafos neuronales. Fuente: `pi15_resultados.json → brecha_M8`.
- **Redacción:** «no se encontró ningún estudio en el corpus que…», no «nadie lo ha hecho». Depende de la codificación de la extracción, de los no recuperados y del acuerdo entre extractores.
- **Agenda derivada de la evidencia:**
  1. Estado estructurado e inspeccionable con coste de contexto acotado.
  2. Inferencia algorítmica de joins en multiturno.
  3. Autocorrección por ejecución en multiturno, hoy proporcionalmente menos frecuente que en un turno.
  4. Evaluación con historial predicho y reporte por turno.
  5. Trabajo sin entrenamiento (`pi0_training_free.csv`).
- Cada punto se marca como «brecha observada», no como solución.
- Declarar la lealtad (D5): la autora desarrolla una propuesta en esta línea.

### 4.5 Implicaciones para práctica y evaluación (5.5)
- Reportar siempre: tipo de historial, resultados por turno, técnica de restauración, mecanismo y señal de autocorrección y coste.
- Preferir QM/IM junto con EX en multiturno (`formulario_extraccion.md`), y declarar el historial.
- Cuidado con la contaminación de benchmarks: `contaminacion_discutida` es poco discutida (`pi5_historial.csv`).

### 4.6 Lo que no se puede afirmar
- Superioridad entre estudios (comparaciones descriptivas).
- Que el estado estructurado cause la mejora (contrastes dentro del estudio, con sesgo de notificación).
- Que el multiturno sea poco investigado en todo el campo.
- Interacción paradigma × escenario: no hay tabla cruzada en los archivos. Si se quiere afirmar, hay que generarla.

---

## 5. Amenazas a la validez

| Amenaza | Sentido del sesgo | Fuente | Dónde |
|---|---|---|---|
| Revisora humana única, con asistencia de IA | Errores de cribado/extracción no detectados | `protocolo_es.md` §3 | 6.1 |
| Los revisores A/B comparten familia de modelo (no independientes) | Sesgos correlacionados | `protocolo_es.md` §11c; `*_methods_selection.md` | 6.1 |
| Diseño reducido de verificación humana (muestra pequeña de validación; sin muestra reservada) | Estimaciones de sensibilidad imprecisas | `enmiendas.md` A3 | 6.1 |
| Crítica del protocolo por un agente de la misma familia | No es revisión por pares independiente | `protocolo_es.md` §11c | 6.1 |
| Cribado de texto completo con extractos y con modelos distintos (Sonnet; Codex en parte del Nivel 1) | Variación entre modelos | `enmiendas.md` A5(a) | 6.1 |
| Conjunto de referencia elegido por la IA (circularidad) | Sensibilidad de búsqueda sobreestimada | `enmiendas.md` A1; `sensibilidad_fase2.json` | 6.1 |
| Cinco fuentes; ACM sin filtro de fecha; arXiv por API más filtro local | Cobertura incompleta | `registro_busquedas.csv` | 6.1 |
| Sesgo de idioma: sin chino, sin bases hispanas | Pierde literatura (CHASE, grupos chinos) | `03_criterios_elegibilidad.md` | 6.3 |
| Informes no recuperados, con posible sesgo de disponibilidad (editoriales de pago, IEEE) | D4 y síntesis sesgados | `enmiendas.md` A4; `pi0_no_recuperados_escenario.csv`; `sensibilidad.json → A4` | 6.1 |
| Marco de elegibilidad asimétrico entre escenarios | Aumenta la proporción multiturno en D4 | `PI0.md → Limitaciones`; `01_preguntas_picoc.md` | 6.1 |
| «Contribución central» juzgada por título/resumen | Clasificación subjetiva | `03_criterios_elegibilidad.md` | 6.1 |
| Doble extracción por IA con acuerdo moderado en campos codificados del Nivel 2 | Error de extracción | `informe_acuerdo_extraccion.md` | 6.2 |
| Muestra independiente de la autora muy pequeña | Estimación de acuerdo imprecisa | `informe_acuerdo_extraccion.md`; `enmiendas.md` A5(c) | 6.2 |
| Verificaciones de la autora que confirmaron el 100 % | Posible sesgo de automatización o confirmación | `informe_acuerdo_extraccion.md` | 6.2 |
| Nivel 1 extraído de las páginas 1–2 | Modelos y detalles subestimados | `PI0.md → Limitaciones`; `leyendas.json → bib_modelos` | 6.2 |
| Calidad puntuada por IA, con ítems de validez y umbral | Clasificación errónea de estudios cercanos al umbral | `checklist_calidad.md`; `informe_acuerdo_extraccion.md` | 6.2 |
| Sesgo de notificación en contrastes dentro del estudio | Efectos sobreestimados | `pi_efectos_componentes.csv`; `PI1–PI4.md` | 6.2 |
| Clase «Otros componentes» heterogénea | Efecto no interpretable | `PI1–PI4.md → Limitaciones` | 6.2 |
| Pocos estudios en algunas clases (aclaración, autoconsistencia, concatenación) | Confianza limitada | `confianza_hallazgos.csv`; `PI1.md`, `PI4.md` | 6.2 |
| Comparaciones entre estudios solo descriptivas | Sin inferencia entre estudios | `plan_sintesis.md` | 6.2 |
| Pendiente de degradación mezcla turno y dificultad; pocas curvas; ninguna en GOLD | Interpretación acotada | `PI5.md → Limitaciones`; `leyendas.json → pi5_degradacion` | 6.2 |
| Confianza «inspirada en GRADE-CERQual»: reglas propias, no validadas | Niveles de confianza no equivalentes a CERQual | `plan_sintesis.md` | 6.2 |
| Contaminación de benchmarks y desfase de líneas base | Resultados inflados | `plan_sintesis.md → Sesgos`; `pi5_historial.csv` | 6.3 |
| Enmiendas posteriores al registro (A1–A6), A4–A6 pendientes en OSF | Desviación del protocolo | `enmiendas.md` | 6.1 y Declaraciones |
| Bibliometría exploratoria: 6 estudios sin resolver en OpenAlex; clasificación de foros | Sesgo de cobertura | `bibliometria_resultados.json → no_resueltos` | 6.3 |
| Año 2026 parcial | Tendencia truncada | `leyendas.json` | 6.3 |
| Fecha de búsqueda y posible actualización (D6) | Búsqueda desactualizada | `protocolo_es.md` §5b | 6.3 |
| Lealtad de la autora al resultado M8 | Interpretación sesgada | D5 | Declaraciones |

---

## 6. Necesidades de citas

«En .bib» significa que ya figura en `bib/referencias.bib` (16 entradas). Los estudios incluidos se citan por ID (R#####/B#####) hasta resolver la clave.

| Obra | Dónde se usa | En .bib | Verificación |
|---|---|---|---|
| Kitchenham y Charters 2007 (guías SLR en ingeniería de software) | 3 (método), 3.7 | no | DOI/DBLP |
| Declaración PRISMA 2020 (Page et al.) | 3, Declaraciones | no | DOI (BMJ) |
| PRISMA-P 2015 | 3.1 | no | DOI |
| PRISMA-S (extensión de búsqueda) | 3.4 | no | DOI |
| SWiM (Campbell et al. 2020) | 3.8 | no | DOI |
| GRADE-CERQual (Lewin et al.) | 3.8 | no | DOI |
| Guía RAISE sobre IA en síntesis de evidencia | 3.5, Declaraciones | no | Fuente primaria (verificar nombre y año) |
| Wilson 1927 (intervalo) | 3.8, 4.3 | no | DOI/JSTOR |
| Cochran–Armitage (Cochran 1954; Armitage 1955) | 3.8, 4.3 | no | DOI |
| Cohen 1960 (kappa); Byrt 1993 (PABAK) | 3.5, 4.1 | no | DOI |
| Wohlin 2014 (bola de nieve) | 3.4 | no | DOI/DBLP |
| *Think. Check. Submit.* | 3.7 | no | URL oficial |
| Think. (sr-screener / ARS, versión usada) | 3.5 | no | Repositorio y versión |
| OpenAlex (Priem et al. 2022) | 3.4, 4.4 | no | arXiv/DOI |
| OSF Registries (registro del protocolo) | 3.1 | no | DOI 10.17605/OSF.IO/5USF3 |
| SParC (Yu et al. 2019) | 1.1, 4.11 | **sí** (`Yu2019SParC`) | — |
| CoSQL (Yu et al. 2019) | 1.1, 4.11 | **sí** (`Yu2019CoSQL`) | — |
| CHASE (Guo et al. 2021) | 4.11 | **sí** (`Guo2021Chase`) | — |
| Spider (Yu et al. 2018) | 1.1, 4.11 | no | DBLP |
| BIRD (Li et al. 2023) | 4.11 | no | DBLP |
| WikiSQL (Zhong et al. 2017) | 4.11 | no | DBLP/arXiv |
| EditSQL (R00131) | 4.8 | **sí** (`Zhang2019EditSQL`) | — |
| IGSQL (R00117) | 4.8, 4.11 | **sí** (`Cai2020IGSQL`) | — |
| CQR-SQL (R00097) | 4.7 | **sí** (`Xiao2022CQRSQL`) | — |
| CoE-SQL (R00072) | 4.7, 4.8 | **sí** (`Zhang2024CoESQL`) | — |
| Decoupled (Chen 2021) | 4.7 | **sí** (`Chen2021Decoupled`) | — |
| Memory Architectures (R00435) | 4.11 | **sí** (`Tummalapenta2026Memory`) | — |
| DBTagger, SchemaGraphSQL, Chen 2025 (abstención), OpenSearch-SQL (semillas de un turno) | 3.4 (semillas), 4.9–4.10 | **sí** (`Usta2021DBTagger`, `Safdarian2026SchemaGraphSQL`, `Chen2025Abstention`, `Xie2025OpenSearchSQL`) | — |
| PICARD (R00109) | 4.10 | no | DBLP/DOI |
| Rose-SQL (R00033), ACT-SQL (R00086), DIR (R00924), QURG (R00950), FANDA (R01034) | 4.7 | no | DBLP/OpenAlex (DIR: DOI 10.3390/app13042262) |
| PG-GSQL (R00120), UniSAr (R00981) | 4.9 | no | DBLP/OpenAlex |
| R00160, R00508, R00123, R00311, R00312 | 4.10 | no | DBLP/OpenAlex |
| R01029, R00936, R01037, R00480, R00099 | 4.8 | no | DBLP/OpenAlex |
| R00868 (MIGA), R00994, R01031 (SCORE), R00100, R00920 (SUQL), R00298 (SQLformer) | 4.11 | no | DBLP/OpenAlex |
| Yang et al. 2025 (conversacional) | 2.2, 5.3 | **sí** (`Yang2025Conversational`) | Leer texto completo antes de afirmar |
| Shi et al. 2026 (LLM para Text-to-SQL) | 2.1, 5.3 | **sí** (`Shi2026SurveyLLM`) | — |
| Quamar et al. 2022 | 2.1 | **sí** (`Quamar2022NLI`) | — |
| Liu et al. 2026 (NLIDB, Front. Comput. Sci.) | 2.2, 5.3 | no | DOI 10.1007/s11704-025-50592-w |
| Bui et al. 2026 (PeerJ CS) | 2.2, 5.3 | no | DOI 10.7717/peerj-cs.3773 |
| Li, Qu y Haffari 2020 | 2.2 | no | DOI 10.18653/v1/2020.coling-main.226 |
| Hong et al. 2025; Liu et al. 2025 (TKDE); Katsogiannis-Meimarakis y Koutrika 2023; Deng et al. 2022; Abbas et al. 2022; Ortiz-Delgado et al. 2026 | 2.1 | no | DBLP/DOI de `00_analisis_brecha.md` |

Regla: nada se añade a `referencias.bib` sin verificación por DOI, DBLP u OpenAlex. Toda cita de `00-contexto/TS Blueprints.md` queda fuera mientras no se verifique la fuente.

---

## 7. Lista de verificación PRISMA 2020

### 7.1 Los 27 ítems

| Ítem | Sección | Nota |
|---|---|---|
| 1 Título | Título (`main.tex`) | Incluir «revisión sistemática». |
| 2 Resumen | `00-resumen` | Ver 7.2. |
| 3 Justificación | 1.2, 2 | |
| 4 Objetivos | 1.3, 3.2 | |
| 5 Criterios de elegibilidad | 3.3, S2 | |
| 6 Fuentes de información | 3.4 | |
| 7 Estrategia de búsqueda | 3.4, S1 | Cadenas completas en suplemento. |
| 8 Proceso de selección | 3.5, Tab. IA | Detalla IA, revisores y verificación humana. |
| 9 Recogida de datos | 3.6 | |
| 10a Resultados (outcomes) | 3.6 | EX, EM/ESM, TS, QM/IM, degradación. |
| 10b Otras variables | 3.6, S4 | |
| 11 Riesgo de sesgo | 3.7, S5, S6 | Lista Kitchenham adaptada, no RoB 2 ni ROBINS-I. |
| 12 Medidas de efecto | 3.8 | Diferencias en pp, Δ, pendiente, proporciones con Wilson. |
| 13a Grupos de síntesis | 3.8 | Niveles 1/2 y clases de componente. |
| 13b Preparación de datos | 3.8 | Consolidación de `OTRA`, NR. |
| 13c Tablas y figuras | 3.8, 4.x | |
| 13d Métodos de síntesis | 3.8 | SWiM, sin metaanálisis. |
| 13e Heterogeneidad | 3.8, 4.6, 4.11 | Estratificación por historial, comparabilidad estricta. |
| 13f Sensibilidad | 3.8, 4.12, S12 | |
| 14 Sesgo de notificación (método) | 3.8 | |
| 15 Certeza (método) | 3.8 | Inspirada en GRADE-CERQual. |
| 16a Selección de estudios | 4.1 | |
| 16b Estudios excluidos | 4.1, S3 | Lista con motivo. |
| 17 Características de los estudios | 4.2, S7 | |
| 18 Riesgo de sesgo en estudios | 4.5, S6 | |
| 19 Resultados individuales | 4.6–4.11, S7, S11 | |
| 20a Características y calidad por síntesis | 4.2, 4.7–4.10 | |
| 20b Resultados de las síntesis | 4.3, 4.6–4.11 | |
| 20c Causas de heterogeneidad | 4.6, 4.11 | |
| 20d Sensibilidad | 4.3, 4.12 | |
| 21 Sesgos de notificación | 4.12 | |
| 22 Certeza de la evidencia | 4.6 | |
| 23a Interpretación | 5.1–5.3 | |
| 23b Limitaciones de la evidencia | 5.2, 6.3 | |
| 23c Limitaciones del proceso | 6.1, 6.2 | |
| 23d Implicaciones | 5.4, 5.5, 7 | |
| 24a Registro | 3.1, Declaraciones | OSF y DOI. |
| 24b Acceso al protocolo | 3.1, Declaraciones | Enlace OSF; protocolo en el repositorio. |
| 24c Enmiendas | 3.1, Declaraciones | A1–A6; declarar A4–A6 pendientes en OSF. |
| 25 Financiamiento | Declaraciones | Comprobar la macro `\RSLFinanciamiento`. |
| 26 Conflictos de interés | Declaraciones | Incluir la lealtad (D5). |
| 27 Disponibilidad de datos y código | Declaraciones | Repositorio con exportaciones, registros de cribado y extracción. PDFs no se comparten (copyright). N/A parcial: textos extraídos y prompts con texto de artículos están en `.gitignore`. |

### 7.2 Resumen (PRISMA 2020 para resúmenes)

| Ítem | Dónde |
|---|---|
| 1 Título | Título |
| 2 Objetivos | «Objetivo» |
| 3 Criterios de elegibilidad | «Método» |
| 4 Fuentes de información | «Método» |
| 5 Riesgo de sesgo | «Método» (lista de calidad) |
| 6 Métodos de síntesis | «Método» |
| 7 Estudios incluidos | «Resultados» (número e indicador D4) |
| 8 Resultados de la síntesis | «Resultados» |
| 9 Limitaciones de la evidencia | Añadir línea «Limitaciones» |
| 10 Interpretación | «Conclusiones» |
| 11 Financiamiento | Añadir línea |
| 12 Registro | Añadir línea (OSF) |

Los números del resumen deben salir de un script, igual que los del cuerpo.