# Fase 1.5 — Formulario de extracción de datos

Fecha: 2026-10-11 · Estado: **v1.1 — revisado tras el Checkpoint 1 (M7, M8, menores); aprobado por la autora (2026-10-11)**
Vocabularios controlados en `MAYÚSCULAS`; listas con `;`; `NR` = no reportado; `NA` = no aplica. Toda celda extraída lleva su **ubicación** (página/sección/tabla) en el campo `*_ubic` correspondiente o en `ubicacion`.

## Alcance por nivel (D7)
| Bloque | Nivel 1 (todos los incluidos) | Nivel 2 (multiturno) |
|---|---|---|
| 0 Identificación | ✓ | ✓ |
| 1 Caracterización | ✓ | ✓ |
| 4–5 Códigos de técnica PI3/PI4 (solo campos `pi3_tecnica_linking`, `pi3_inferencia_joins`, `pi4_mecanismo`, `pi4_senal`) | ✓ | ✓ |
| 2–3 PI1–PI2, resto de 4–5, 5b, 6, 7 | — | ✓ |

## Tablas
1. **`extraccion.csv`** — una fila por estudio (bloques 0–5b).
2. **`resultados.csv`** — formato largo: estudio × *benchmark* × versión × partición × métrica × turno × sistema (bloque 6). Solo Nivel 2.
3. **`contrastes.csv`** — contrastes **dentro del mismo estudio** (componente activado vs. desactivado, mismo modelo base) (bloque 7). Solo Nivel 2.

---

## Bloque 0 — Identificación
| Campo | Contenido |
|---|---|
| `id_estudio` | E001… |
| `clave_bib` | Clave en `referencias.bib` |
| `informes` | DOI/arXiv de todos los informes vinculados (`;`) |
| `titulo`, `autores`, `anio`, `venue` | Del informe principal |
| `foro_tipo` | `CONGRESO`, `REVISTA`, `TALLER`, `PREPRINT` *(A5; ambos niveles)* |
| `foro_nivel` | CORE (`A*`, `A`, `B`, `C`) para congresos, cuartil SJR (`Q1`–`Q4`) para revistas, `SIN_RANKING`, `PREPRINT` *(A5; análisis de sensibilidad, no criterio de elegibilidad)* |
| `tipo_pub` | `REVISTA` · `CONFERENCIA` · `TALLER` · `PREPRINT` |
| `origen` | `SCOPUS` · `IEEE` · `ACM` · `ACL` · `ARXIV` · `BOLA_NIEVE` (`;`) |
| `nivel` | `1` · `2` |

## Bloque 1 — Caracterización (PI0)
| Campo | Vocabulario |
|---|---|
| `escenario` | `MULTITURNO` · `UN_TURNO` (definición revisada; caso B6) |
| `etiquetas` | `INTERACTIVO` (B1) · `USA_HISTORIAL` (B2) · `COMPONENTE` (B3) · `RONDAS_INTERNAS` (B6) · ninguna |
| `tipo_contribucion` | `TECNICA` · `BENCHMARK` · `ESTUDIO_EMPIRICO` (`;`) |
| `paradigma_principal` | **Un solo código**, con precedencia: `AGENTES` > `HIBRIDO_NEUROSIMBOLICO` > `LLM_FINETUNING` > `LLM_PROMPTING` > `PLM_FINETUNING` > `NEURONAL_PRE_PLM` > `REGLAS_SIMBOLICO` (se asigna el primero que aplique) |
| `paradigmas_secundarios` | Los demás que apliquen (`;`) |
| `modelos_base` | Normalizado (p. ej., `GPT-4o; T5-3B`) |
| `fecha_modelo` | Versión/fecha del modelo si se reporta (p. ej., `gpt-4o-2024-05-13`), si no `NR` |
| `pilares_centrales` | PI declarados como contribución central (`PI1`…`PI4`; `;`) |
| `pilares_contenidos` | PI presentes solo como componente (`;`) — para el indicador D4 laxo |
| `idioma_dataset` | `EN` · `ZH` · `ES` · `OTRO` (`;`) |
| `codigo_disponible` | `SI` · `NO` · `PARCIAL` |
| `requiere_entrenamiento` | `SI` · `NO` (*training-free*) · `PARCIAL` |

## Bloque 2 — PI1: restauración del contexto (Nivel 2)
| Campo | Vocabulario |
|---|---|
| `pi1_tecnica` | `CONCATENACION` · `REESCRITURA` · `RESOLUCION_EXPLICITA` · `CLASIFICACION_DISCURSO` · `OTRA:<descripción>` (`;`) |
| `pi1_insumos_historial` | `PREGUNTAS_PREVIAS` · `SQL_PREVIOS` · `RESPUESTAS_SISTEMA` · `RESULTADOS_EJECUCION` (`;`) |
| `pi1_resumen` | ≤ 2 frases + ubicación |

## Bloque 3 — PI2: estado del diálogo (Nivel 2)
| Campo | Vocabulario (nombres neutrales, M8) |
|---|---|
| `pi2_representacion` | `HISTORIAL_PLANO` · `VENTANA_DESLIZANTE` · `RESUMEN` · `SQL_PREVIO_EDICION` · `ARBOL_AST` · `GRAFO` · `MEMORIA_EXTERNA` · `ESTRUCTURA_EXPLICITA` · `OTRA:<descripción>` (`;`) |
| `pi2_grafo_nodos` | Si `GRAFO`: qué representan los nodos (`ELEMENTOS_ESQUEMA` · `TOKENS_PREGUNTA` · `TURNOS` · `OTROS:<descripción>`; `;`); si no `NA` |
| `pi2_grafo_dinamico` | `SI` (cambia por turno) · `NO` · `NA` |
| `pi2_actualizacion` | `IMPLICITA_NEURONAL` · `REGLAS_DETERMINISTAS` · `LLM_GENERATIVA` · `NR` |
| `pi2_coste_contexto` | `CRECE_CON_TURNOS` · `ACOTADO` · `NR` |
| `pi2_resumen` | ≤ 2 frases + ubicación |

## Bloque 4 — PI3: vinculación de esquemas e inferencia de *joins*
| Campo | Vocabulario |
|---|---|
| `pi3_tecnica_linking` | `COINCIDENCIA_CADENAS` · `EMBEDDINGS_RECUPERACION` · `CLASIFICADOR_ENTRENADO` · `LLM_PROMPTING` · `GRAFO_ESQUEMA` · `PODA_ESQUEMA` · `NINGUNA_EXPLICITA` (`;`) |
| `pi3_inferencia_joins` | `IMPLICITA_MODELO` · `ALGORITMICA_CAMINOS` · `GRAFO_FK_RESTRICCIONES` · `NR` |
| `pi3_algoritmo` | Si algorítmica (p. ej., `STEINER; DIJKSTRA`), si no `NA` *(Nivel 2)* |
| `pi3_escala_esquema` | Máximo de tablas/columnas evaluado *(Nivel 2)* |
| `pi3_metricas_linking` | Recall/precisión de *linking* *(Nivel 2)* |
| `pi3_resumen` | ≤ 2 frases + ubicación *(Nivel 2)* |

## Bloque 5 — PI4: retroalimentación de ejecución y autocorrección
| Campo | Vocabulario |
|---|---|
| `pi4_mecanismo` | `EJECUCION_FEEDBACK_ERRORES` · `AUTODEPURACION_LLM` · `AUTOCONSISTENCIA_VOTACION` · `VERIFICADOR_CRITICO` · `REPARACION_SIMBOLICA` · `ACLARACION_USUARIO` · `ABSTENCION` (`;`) |
| `pi4_senal` | `ERROR_DBMS` · `RESULTADO_VACIO` · `RESULTADO_EJECUCION` · `JUICIO_LLM` · `USUARIO` (`;`) |
| `pi4_rondas_max` | Número o `NR` *(Nivel 2)* |
| `pi4_aplicado_multiturno` | `SI` · `NO` |
| `pi4_resumen` | ≤ 2 frases + ubicación *(Nivel 2)* |

## Bloque 5b — Transversales (Nivel 2)
| Campo | Contenido |
|---|---|
| `historial_eval` | Se refiere **solo a las salidas del sistema en turnos previos** (SQL previo, reescrituras, estados), **no** a las preguntas anteriores del usuario, que siempre se dan. **`GOLD`** = el sistema recibe el SQL, la reescritura o el estado **de referencia** de los turnos previos (*teacher forcing*) · **`PREDICHO`** = recibe **sus propias** salidas previas (propagación de errores real) · **`SOLO_PREGUNTAS`** = solo usa las preguntas previas del usuario, sin salidas previas · `NR` |
| `degradacion_reportada` | `SI` · `NO` |
| `errores_join_reportados` | `SI` · `NO` |
| `coste_reportado` | `TOKENS` · `LATENCIA` · `MONETARIO` · `NINGUNO` (`;`) |
| `contaminacion_discutida` | `SI` · `NO` |
| `limitaciones_autores` | Texto breve + ubicación |
| `notas_revisora` | Observaciones de la autora (separadas de lo que dice el estudio) |
| `extraccion_independiente` | `SI` si pertenece a la muestra del 20 % extraída por la autora sin ver la IA |
| `verificado_por` | Quién verificó la fila |

## Bloque 6 — `resultados.csv`
| Campo | Contenido |
|---|---|
| `id_estudio` | E001… |
| `benchmark` | `SPIDER` · `BIRD` · `WIKISQL` · `SPARC` · `COSQL` · `CHASE` · `OTRO:<nombre>` |
| `version` | Versión del *benchmark* (p. ej., `SPIDER_1.0`, `SPIDER_2.0`, `BIRD_DEV_2024`) o `NR` |
| `particion` | `DEV` · `TEST` · `OTRA` |
| `metrica` | `EX` · `EM` · `ESM` · `TS` · `QM` · `IM` · `VES` · `LINKING_RECALL` · `OTRA:<nombre>` |
| `turno` | `TODOS` · `1` · `2` · `3` · `4+` · número mayor si se reporta por separado |
| `n_turno` | Número de preguntas en ese grupo de turno, si se reporta |
| `historial_eval` | `GOLD` · `PREDICHO` · `SOLO_PREGUNTAS` · `NR` (definición en el bloque 5b) |
| `conocimiento_externo` | `SI` (p. ej., *evidence* de BIRD) · `NO` · `NA` |
| `n_candidatos` | Número de candidatos / presupuesto de autoconsistencia, o `NR` |
| `valor` | Porcentaje tal como se reporta |
| `sistema` | `PROPUESTO` o nombre de la línea base |
| `es_linea_base_referencia` | `SI` para **una** línea base por configuración (regla abajo) |
| `modelo_base` | Modelo de esa fila |
| `ubicacion` | Tabla/página |

**Regla de línea base de referencia (M7e):** para calcular Δ se usa la **línea base más fuerte reportada por el propio estudio con el mismo modelo base**, misma configuración (*benchmark*, versión, partición, métrica, historial, conocimiento externo). Si no existe con el mismo modelo, Δ no se calcula para ese estudio.

## Bloque 7 — `contrastes.csv` (contrastes dentro del estudio)
| Campo | Contenido |
|---|---|
| `id_estudio` | E001… |
| `componente` | Qué se activa/desactiva (p. ej., `REESCRITURA`, `GRAFO_ESTADO`, `AUTOCORRECCION`) |
| `pilar` | `PI1` · `PI2` · `PI3` · `PI4` |
| `benchmark`, `version`, `particion`, `metrica`, `turno`, `historial_eval`, `conocimiento_externo`, `n_candidatos`, `modelo_base` | Configuración común (`turno` permite estudiar el efecto del componente a lo largo de los turnos, PI2) |
| `valor_con`, `valor_sin` | Resultado con y sin el componente |
| `ubicacion` | Tabla/página |
Permite responder preguntas como «¿la reescritura supera a la concatenación?» **sin comparar entre estudios distintos**.

## Procedimiento (revisado, M5; **sustituido por la enmienda A5 (c)**: doble extracción por IA + Opus en discrepancias; la autora revisa discrepancias, 10 % de concordantes del Nivel 2, validez 40–60 %, 10 % del Nivel 1; muestra independiente de 5 estudios en campos clave)
1. **Piloto:** 3 estudios extraídos por la IA y revisados por la autora; ajustes en `enmiendas.md`.
2. **Muestra independiente:** en un **20 % aleatorio** del Nivel 2 (mínimo 5), la autora extrae **sin ver** la propuesta de la IA; se reporta el acuerdo por campo.
3. **Resto:** la IA extrae con ubicación; la autora verifica cada fila.
4. Las categorías `OTRA:<…>` se consolidan inductivamente y **se reportan obligatoriamente**.
