# Fase 0c — Preguntas de investigación y PICOC

Fecha: 2026-10-11 · Estado: **v1.1 — revisada tras la crítica del abogado del diablo (Checkpoint 1); aprobada por la autora (2026-10-11)**
Origen: pilares OE1–OE4 de la propuesta de tesis + decisiones de la autora en el diálogo socrático (Fase 0c) + revisión de la Fase 1.7 (`04_critica_abogado_diablo_cp1.md`).

## Título provisional de la revisión
**Text-to-SQL conversacional: restauración del contexto, estado del diálogo, vinculación de esquemas y autocorrección — una revisión sistemática de la literatura** *(cambio M8: el título anterior, «anclaje de esquemas con estado», no reflejaba la inclusión de estudios de un turno)*.

## Decisiones de la autora (registro)
| # | Decisión | Palabras de la autora (resumen fiel) |
|---|---|---|
| D1 | Se incluyen estudios de **un solo turno** solo si abordan los pilares 3–4 como contribución central | «b» |
| D2 | La **reescritura de consultas** cuenta como seguimiento del estado del diálogo **si usa el historial conversacional** | «Count it as dialogue state track… whenever they use conversational history» |
| D3 | ~~Un único conjunto de estudios analizado en profundidad~~ → **sustituida por D7** (diseño en dos niveles). Se mantiene la intención: foco principal en profundidad; la estadística actúa como introducción | «both goals together but the strongest focus on depth… statistics just like the introduction» |
| D4 | Umbral fijado **antes** de ver los datos: **≤ 30 %** → escenario multiturno **considerablemente menos investigado**; además se analiza la **tendencia temporal**. Operacionalización formal abajo (revisada, M1) | «30% or less… considerably less investigated»; «track growth will be interesting» |
| D5 | Tipo de revisión: **revisión sistemática** (PRISMA 2020 + Kitchenham) | elegido desde el inicio del proyecto |
| D6 | **Acceso limitado a texto completo:** el acceso abierto **no es criterio de elegibilidad**; los informes no recuperados se reportan (PRISMA 2020, ítem 16a), **desglosados por escenario** | «we will only have access to open access papers…» |
| D7 | **Diseño en dos niveles (M6/Observación):** **Nivel 1 — mapeo sistemático** de todos los estudios incluidos (PI0 e indicador D4; extracción ligera). **Nivel 2 — revisión sistemática en profundidad** de los estudios **multiturno** (PI1–PI5; calidad, extracción completa y síntesis). Los estudios de un turno de PI3/PI4 se caracterizan en el Nivel 1 y sirven de contraste en PI3–PI4 | acepta la recomendación (2026-10-11) |
| D8 | **Registro en OSF obligatorio** antes de la búsqueda oficial (M1f) | acepta la recomendación |
| D9 | **Validación humana de la IA** (M5): auditoría ciega de exclusiones, muestra de validación reservada, extracción/calidad independiente en una muestra | acepta la recomendación |

## Objetivo de la RSL
Identificar, clasificar y analizar críticamente las técnicas de Text-to-SQL conversacional (multiturno) para la restauración del contexto, la representación del estado del diálogo, la vinculación de esquemas / inferencia de *joins* y la autocorrección; contrastarlas con las técnicas equivalentes de un solo turno; comparar los resultados reportados y señalar brechas.

## Preguntas de investigación (PI)
| PI | Pregunta | Nivel |
|---|---|---|
| **PI0** (descriptiva) | ¿Cómo se distribuyen los estudios por año, tipo de publicación, paradigma técnico y escenario (uno vs. varios turnos), y cómo evoluciona la proporción de estudios multiturno? | 1 (mapeo) |
| **PI1** | ¿Qué técnicas se usan para restaurar el contexto conversacional (resolución de elipsis y correferencia, reescritura de consultas con historial) y qué resultados reportan? | 2 |
| **PI2** | ¿Cómo se representa y actualiza el estado del diálogo y cómo influye en el rendimiento a lo largo de los turnos? | 2 |
| **PI3** | ¿Qué técnicas de vinculación de esquemas e inferencia de rutas de *join* se emplean en el escenario multiturno, y cómo se comparan con las de un solo turno? | 2 (multiturno) + 1 (contraste un turno) |
| **PI4** | ¿Qué mecanismos de retroalimentación de ejecución y autocorrección se han aplicado al escenario multiturno, y cómo se comparan con los de un solo turno? | 2 + 1 |
| **PI5** | ¿Qué *benchmarks* y métricas se emplean en el escenario multiturno y qué degradación del rendimiento por turno se reporta? | 2 |

## Indicador D4 (operacionalización pre-especificada, revisada M1)
- **Población del indicador:** estudios incluidos que abordan PI3 o PI4 **como contribución central** (misma regla en ambos escenarios; ver `03_criterios_elegibilidad.md`).
- **Numerador:** estudios **multiturno ∧ (PI3 ∨ PI4 central)**. **Denominador:** todos los estudios **(PI3 ∨ PI4 central)**, de uno o varios turnos.
- **Versión laxa (sensibilidad):** igual, pero contando en el numerador y el denominador los estudios multiturno que solo *contienen* un componente de PI3/PI4.
- **Regla de decisión:** se concluye «considerablemente menos investigado» **solo si el límite superior del IC 95 % de Wilson es ≤ 30 %**. Si el IC contiene el 30 %, el resultado se declara no concluyente.
- **Justificación del 30 %:** valor de referencia elegido por la autora como umbral de «proporción minoritaria clara» (menos de un tercio). Se presenta como **referencia descriptiva**, no como prueba de hipótesis.
- **Limitación declarada:** el indicador está condicionado por el marco de elegibilidad (los estudios de un turno deben cumplir más requisitos que los multiturno, lo que tiende a **aumentar** la proporción multiturno, en contra de la conclusión esperada). No se generaliza a «todo el campo Text-to-SQL».
- **Tendencia:** proporción anual 2019–2025 (año completo); 2026 se reporta aparte como año parcial.

## Qué contaría en contra de la brecha de la tesis (pre-especificado, M8)
La brecha de la tesis (estado del diálogo estructurado y explícito + inferencia algorítmica de *joins* + autocorrección, sin entrenamiento, en multiturno) se **reformulará** si en el Nivel 2 se encuentran **≥ 2 estudios** que ya combinen: (a) representación estructurada explícita del estado del diálogo, **y** (b) inferencia algorítmica de *joins* o autocorrección por ejecución, **y** (c) evaluación multiturno con historial **predicho**. En ese caso la contribución de la tesis se replanteará como mejora o evaluación comparativa, no como novedad de componentes. El resultado se reporta sea cual sea.

**Correspondencia con los códigos de extracción (ronda 1, M8a):**
- (a) **Estado estructurado explícito** = `pi2_representacion` contiene `ESTRUCTURA_EXPLICITA`, **o** contiene `GRAFO` con `pi2_actualizacion` ∈ {`REGLAS_DETERMINISTAS`, `LLM_GENERATIVA`} (estado inspeccionable fuera del modelo). **No cuentan** los grafos usados solo como codificador neuronal (`GRAFO` + `IMPLICITA_NEURONAL`, p. ej., IGSQL o R²SQL) ni `SQL_PREVIO_EDICION`.
- (b) = `pi3_inferencia_joins` ∈ {`ALGORITMICA_CAMINOS`, `GRAFO_FK_RESTRICCIONES`} **o** `pi4_mecanismo` contiene `EJECUCION_FEEDBACK_ERRORES` o `REPARACION_SIMBOLICA`.
- (c) = `historial_eval` ∈ {`PREDICHO`, `SOLO_PREGUNTAS`}.
- **Sensibilidad:** se reporta también el recuento contando como (a) los grafos neuronales tipo IGSQL, para que la decisión de excluirlos no determine por sí sola la conclusión.

## PICOC
| Elemento | Definición |
|---|---|
| **P**oblación | Estudios primarios sobre interfaces de lenguaje natural a bases de datos relacionales (Text-to-SQL / NLIDB) |
| **I**ntervención | Técnicas de restauración de contexto, representación del estado del diálogo, vinculación de esquemas / rutas de *join*, y retroalimentación de ejecución / autocorrección |
| **C**omparación | Entre enfoques (un turno vs. multiturno; simbólico vs. neuronal; pre-LLM vs. LLM; con vs. sin entrenamiento) |
| **O**utcomes | EX, EM/ESM, *test-suite accuracy* (TS), QM/IM, degradación por turno, errores de *join*, coste computacional |
| **C**ontexto | Investigación académica e industrial, 2019–2026, estudios en inglés o español, evaluados en *benchmarks* o bases de datos reales |

## Volumen esperado
Estimación OpenAlex (solo resúmenes, 2019+): v3 ≈ 850 registros; v4 ≈ 1 170. Las búsquedas oficiales devolverán más. Los conteos reales por base se registran antes del registro OSF (`slr/busqueda/registro_busquedas.csv`), y se aplica la regla de contingencia del protocolo (§11e).
