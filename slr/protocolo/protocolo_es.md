# Protocolo de revisión sistemática (PRISMA-P 2015)

**Versión:** 1.2 (revisada tras la ronda 1 del Checkpoint 1) · **Fecha:** 2026-10-11
**Repositorio:** este directorio (`slr/`) contiene todos los anexos citados. Control de versiones con git.

---

## INFORMACIÓN ADMINISTRATIVA

### 1. Identificación
**Título provisional:** Text-to-SQL conversacional: restauración del contexto, estado del diálogo, vinculación de esquemas y autocorrección — una revisión sistemática de la literatura.
Tipo: revisión sistemática (Kitchenham y Charters, 2007) con un nivel previo de mapeo sistemático (D7), reportada según PRISMA 2020.

### 2. Registro
**Obligatorio** en **OSF Registries** antes de la búsqueda oficial (D8). **Registrado el 2026-10-11** en OSF Registries (plantilla *Generalized Systematic Review Registration*, pública): https://osf.io/5usf3/ · DOI [10.17605/OSF.IO/5USF3](https://doi.org/10.17605/OSF.IO/5USF3). Versión registrada del protocolo: v1.2, commit `1a4c6ab`. PROSPERO no admite revisiones de computación. El historial de git complementa, no sustituye, el registro.

### 3. Autoría y contacto
Angela Lucia Jara Espinoza — Escuela Profesional de Ingeniería de Software, Facultad de Ingeniería de Sistemas e Informática, Universidad Nacional Mayor de San Marcos, Lima, Perú. ORCID 0009-0007-8716-0988. Contacto: angela.jara@unmsm.edu.pe. Revisora humana única, con asistencia de IA (ítem 11c). No hay segunda revisora humana disponible: se declara como limitación y se compensa con la validación del ítem 11c.

### 4. Enmiendas
Tras el registro, todo cambio se documenta en `enmiendas.md` (fecha, sección, cambio, motivo), se actualiza en OSF y se reporta en el artículo.

### 5. Financiamiento
Sin financiamiento. Sin conflictos de interés.

### 5b. Cronograma tentativo
| Fase | Período |
|---|---|
| Registro OSF (1.8) | octubre 2026 |
| Búsqueda oficial y deduplicación (2–3) | octubre–noviembre 2026 |
| Piloto, validación y cribado título-resumen (4–5) | noviembre–diciembre 2026 |
| Texto completo y bola de nieve (6–8) | diciembre 2026 – enero 2027 |
| Calidad, extracción y síntesis (9–10) | enero–febrero 2027 |
| Redacción y revisión (11–13) | marzo 2027 |
**Actualización de la búsqueda:** si pasan más de 6 meses entre la búsqueda y el envío del artículo, se repite con las mismas cadenas para el intervalo nuevo.

---

## INTRODUCCIÓN

### 6. Justificación
Existen numerosos *surveys* de Text-to-SQL, pero la búsqueda exploratoria (`00_analisis_brecha.md`) no encontró ninguna revisión sistemática dedicada al escenario conversacional o multiturno. Las dos revisiones de 2026 que se denominan sistemáticas no lo cubren: Liu et al. (2026), en su versión arXiv, no documenta un protocolo de búsqueda y no trata SParC, CoSQL ni el escenario multiturno; Bui et al. (2026), una revisión sistemática de 187 estudios sobre Text-to-SQL con LLM y su seguridad, trata el escenario multiturno solo como categoría de *datasets* y no analiza la restauración del contexto, el estado del diálogo ni la degradación por turno. El *survey* más cercano (Yang et al., 2025) **parece**, según su resumen, ser narrativo y no tratar como ejes la vinculación de esquemas, la inferencia de *joins* ni la retroalimentación de ejecución; **esta afirmación se verificará con su texto completo antes del registro** y, si no es posible, se mantendrá matizada como basada en el resumen. Las estimaciones preliminares sugieren que el escenario multiturno es una fracción pequeña de la literatura. Falta una revisión reproducible que analice conjuntamente la restauración del contexto, la representación del estado, la vinculación de esquemas y la autocorrección en multiturno, contrastándolas con el escenario de un turno y examinando la degradación por turno.

### 7. Objetivos
**Objetivo:** identificar, clasificar y analizar críticamente las técnicas de Text-to-SQL conversacional para la restauración del contexto, la representación del estado del diálogo, la vinculación de esquemas / inferencia de *joins* y la autocorrección; contrastarlas con las de un turno; comparar los resultados reportados y señalar brechas.

**Preguntas** (detalle, PICOC y decisiones D1–D9 en `01_preguntas_picoc.md`):
- **PI0** (Nivel 1) — Distribución por año, tipo de publicación, paradigma y escenario; evolución de la proporción multiturno.
- **PI1** (Nivel 2) — Restauración del contexto conversacional.
- **PI2** (Nivel 2) — Representación y actualización del estado del diálogo.
- **PI3** (Nivel 2 + contraste Nivel 1) — Vinculación de esquemas e inferencia de *joins*.
- **PI4** (Nivel 2 + contraste Nivel 1) — Retroalimentación de ejecución y autocorrección.
- **PI5** (Nivel 2) — *Benchmarks*, métricas y degradación por turno.

**Indicador descriptivo D4 (pre-especificado):** proporción = multiturno ∧ (PI3 ∨ PI4 central) / (PI3 ∨ PI4 central), con IC 95 % de Wilson. Se concluye «escenario multiturno considerablemente menos investigado» **solo si el límite superior del IC ≤ 30 %**; si el IC contiene el 30 %, el resultado es no concluyente. Es una referencia descriptiva condicionada al marco de elegibilidad, no una afirmación sobre todo el campo.

**Criterio de reformulación de la brecha (pre-especificado):** ver `01_preguntas_picoc.md`.

---

## MÉTODOS

### 8. Criterios de elegibilidad
Detalle, definiciones y casos límite B1–B6: `03_criterios_elegibilidad.md`.
- **Multiturno** = preguntas sucesivas del **usuario** cuya interpretación depende de turnos anteriores; las rondas internas de un sistema sobre una sola pregunta son de un turno (B6).
- **Contribución central** = la técnica de PI3/PI4 se declara como contribución en el título o el resumen (misma regla en ambos escenarios).
- **Inclusión:** IC1–IC7. **Exclusión ordenada:** EX1–EX9. **Regla de incertidumbre:** en título-resumen, ante la duda, pasa a texto completo.
- **Niveles (D7):** Nivel 1 = todos los incluidos (mapeo); Nivel 2 = incluidos multiturno (revisión en profundidad).

### 9. Fuentes de información
| Fuente | Modo |
|---|---|
| Scopus | Búsqueda avanzada web |
| IEEE Xplore | *Command search* (4 consultas) |
| ACM Digital Library (Full-Text Collection) | Búsqueda avanzada web |
| ACL Anthology | Volcado BibTeX oficial + script |
| arXiv (literatura gris) | API oficial + script |
| Bola de nieve | OpenAlex (ítem 11f) |

### 10. Estrategia de búsqueda
Cadena **v4** (tarea AND (multiturno OR pilares 3–4)), con tabla de equivalencia entre bases: `slr/busqueda/cadenas.md`. Pruebas y conteos marginales: `slr/busqueda/pruebas_cadenas.md` (Scopus 12/12 con 10 semillas + 2 casos externos; ACM y ACL pendientes de la búsqueda oficial). **Sensibilidad independiente:** conjunto de referencia construido sin las cadenas (*quasi-gold standard*); umbral de sensibilidad global ≥ 80 %, reportada también por base. Antes del registro se registran los **conteos reales por base** en `registro_busquedas.csv`.

### 11. Registro y manejo de estudios
**a) Gestión de datos.** Exportaciones sin editar en `slr/busqueda/exports/`; deduplicación con sr-screener por DOI **y título normalizado** (DOI ausentes o erróneos observados en Scopus). Biblioteca en Mendeley; bibliografía en `bib/referencias.bib`; git.

**b) Selección.** Título-resumen y texto completo con los criterios traducidos al inglés en `screening_protocol.md`; la traducción se versiona en git y la autora la contrasta con el original en español antes del piloto.

**c) Uso de IA y su validación (D9).**
- **Herramienta:** sr-screener (Academic Research Skills v3.23.0), con dos revisores IA cegados y un tercer revisor IA para conflictos, perfil **«quality»**: revisores A y B con Claude Sonnet 5.5; tercer revisor, recomprobación QC y todo el cribado de texto completo con Claude Opus 5.5 (Anthropic). Se registran **ID exacto del modelo, *prompts* (generados por la herramienta), fechas de ejecución y número de anulaciones humanas**. Los dos revisores IA comparten familia de modelo: **no se consideran revisores independientes** en el sentido de Kitchenham; su acuerdo se reporta solo como diagnóstico.
- **Piloto de ajuste:** 50–100 registros etiquetados por la autora; sirve para aclarar criterios.
- **Muestra de validación reservada:** **100 registros aleatorios distintos del piloto**, cribados por la autora **a ciegas** antes de conocer las decisiones de la IA. Se calculan sensibilidad y especificidad de la IA frente a la autora y el **acuerdo humano–IA (kappa, PABAK, % de acuerdo)**, que es la **medida principal de fiabilidad**.
- **Auditoría de exclusiones por consenso de la IA (revisada en la ronda 1):** la autora revisa a ciegas una muestra aleatoria de las exclusiones en que ambos revisores IA coinciden, de tamaño **máx(10 %, 150 registros)**. Con la tasa de falsos negativos observada (*p̂*) y el número total de exclusiones por consenso (*N*), se estima el número de estudios elegibles perdidos (*p̂·N*) y la **sensibilidad implícita** = incluidos / (incluidos + *p̂·N*). **Regla:** si la sensibilidad implícita es **< 95 %**, o si se detecta algún falso negativo con un patrón sistemático, se aclaran criterios, se re-pilota y se vuelven a cribar las exclusiones. Se reportan *p̂*, su IC 95 % y la cota inferior de la sensibilidad implícita.
- **Prueba de sensibilidad con positivos conocidos:** los registros del **conjunto de referencia independiente** (ítem 10) se pasan a ciegas por los revisores IA; se reporta la proporción incluida en título-resumen, con IC 95 % de Wilson. Objetivo: ≥ 95 %; si es menor, se analizan los fallos antes del cribado completo.
- **Crítica del protocolo:** el Checkpoint 1 (abogado del diablo) lo realizó un agente de IA de la misma familia de modelos que los revisores de cribado; **no es una revisión por pares independiente** y así se declara en el artículo (posibles puntos ciegos compartidos).
- **Decisiones finales:** la autora resuelve todos los conflictos, puede anular cualquier decisión (`overrides.csv`) y verifica todas las inclusiones del Nivel 2.
- **Calidad y extracción:** la IA propone con cita o página y la autora verifica cada fila; además, en un **20 % aleatorio** del Nivel 2 la autora puntúa y extrae **antes de ver** la propuesta de la IA, y se reporta el acuerdo.

**d) Recogida de datos.** Formulario y vocabularios: `slr/extraccion/formulario_extraccion.md` (extracción ligera en Nivel 1, completa en Nivel 2; piloto con 3 estudios).

**e) Regla de contingencia por volumen (pre-especificada).**
- Si el **Nivel 2** supera **150 estudios** tras texto completo, la tabla de resultados (bloque 6) se limita a SParC, CoSQL y CHASE y a las métricas EX, QM e IM; el resto de la extracción se mantiene.
- Si los registros que pasan a **texto completo en el Nivel 1** (un turno) superan **400**, sus decisiones de texto completo las toman los revisores IA y la autora audita una muestra aleatoria del **20 %** más todos los conflictos; en el Nivel 2 la autora verifica todas las decisiones.
- Ninguna otra restricción se aplicará *ad hoc*; cualquier otra requiere enmienda registrada.

**f) Bola de nieve.** **Una iteración**, hacia atrás (referencias) y hacia adelante (citas) desde los estudios incluidos del **Nivel 2**, mediante OpenAlex. Los candidatos se filtran automáticamente con el bloque A de la cadena sobre título y resumen y luego pasan por el mismo cribado. Se reportan en la rama «otros métodos» del diagrama PRISMA.

### 12. Elementos de datos
Identificación y nivel; caracterización (escenario, etiquetas B1–B3/B6, tipo de contribución, paradigma principal y secundarios, modelos y fecha del modelo, pilares centrales y contenidos, idioma del *dataset*, código, *training-free*); códigos de técnica PI3/PI4 (ambos niveles); en Nivel 2, campos de PI1–PI4, tipo de historial en la evaluación (gold/predicho), degradación, errores de *join*, coste, contaminación, limitaciones; resultados en formato largo (con versión del *benchmark*, historial, conocimiento externo, número de candidatos) y contrastes dentro del estudio.

### 13. Resultados y priorización
Métrica primaria: **EX**; secundarias: EM/ESM, TS; en multiturno, **QM e IM**. Degradación por turno: pendiente en pp/turno **solo con historial predicho**. Efecto de componentes: **contrastes dentro del estudio** como evidencia principal. Indicador primario de PI0: D4.

### 14. Evaluación de calidad
`slr/calidad/checklist_calidad.md`: 10 ítems; el umbral (≥ 50 %) se calcula solo con los **ítems de validez** (CQ2, CQ4–CQ7); los ítems de reporte y apertura se informan por ítem (perfil tipo semáforo). Aplica al Nivel 2. Indicios de prácticas depredadoras según *Think. Check. Submit.* No se usan RoB 2 ni ROBINS-I (diseñados para ensayos clínicos).

### 15. Síntesis de datos
Sin metaanálisis. SWiM: taxonomías, tablas comparativas, contrastes dentro del estudio, Δ sobre la línea base de referencia (mismo modelo base) solo en grupos comparables; PI0 descriptivo con IC de Wilson y Cochran–Armitage exacta (2019–2025; 2026 aparte); curvas de degradación separadas por tipo de historial. Detalle: `slr/sintesis/plan_sintesis.md`.

### 16. Meta-sesgos
Sesgo de publicación, contaminación de *benchmarks*, desfase de líneas base, sesgo de idioma (exclusión del chino; sin bases hispanas) y recuperación diferencial por escenario. Análisis de sensibilidad sin preprints, con estudios bajo el umbral y con D4 laxo.

### 17. Confianza en la evidencia
Enfoque inspirado en GRADE-CERQual con cuatro componentes y reglas explícitas (`plan_sintesis.md`): alto / moderado / bajo.

---

## ANEXOS
| Anexo | Archivo |
|---|---|
| A. Análisis de brecha | `00_analisis_brecha.md` |
| B. Preguntas, PICOC, decisiones, D4 y criterio de reformulación | `01_preguntas_picoc.md` |
| C. Estudios semilla | `02_estudios_semilla.md` |
| D. Criterios de elegibilidad | `03_criterios_elegibilidad.md` |
| E. Crítica del abogado del diablo (Checkpoint 1) | `04_critica_abogado_diablo_cp1.md` |
| F. Cadenas y pruebas | `../busqueda/cadenas.md`, `../busqueda/pruebas_cadenas.md` |
| G. Lista de calidad | `../calidad/checklist_calidad.md` |
| H. Formulario de extracción | `../extraccion/formulario_extraccion.md` |
| I. Plan de síntesis | `../sintesis/plan_sintesis.md` |

## Registro de revisiones
| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-11 | Borrador inicial (Fases 0–1.6) |
| 1.1 | 2026-10-11 | Revisión completa tras el Checkpoint 1 (veredicto REVISE, 0 críticos / 9 mayores / 10 menores). **M1** D4 formalizado (numerador, regla común, IC, limitación); **M2** definición de multiturno, B6, se elimina la vía «ablación», regla de incertidumbre; **M3** cadena v4 + tabla de equivalencia; **M4** sensibilidad por base, R²SQL recuperado, conjunto de referencia independiente, regla para registros ACL sin resumen, se elimina el paso DBLP; **M5** validación reservada, auditoría de exclusiones, acuerdo humano–IA, muestras independientes del 20 %, divulgación; **M6** diseño en dos niveles (D7), regla de contingencia, bola de nieve acotada; **M7** campos de versión, historial, conocimiento externo, candidatos, fecha de modelo, turno 4+, TS, tabla de contrastes, regla de línea base; **M8** título, códigos neutrales, §6 matizado, criterio de reformulación de la brecha; **M9** umbral sobre ítems de validez, se elimina el 60 % para preprints, perfil por ítem. **Menores:** texto obsoleto, IC7/EX3, idioma, confianza operacionalizada, precedencia de paradigmas, tendencia con año parcial, cronograma, actualización de la búsqueda, criterios de revista depredadora, ruta de B4 |
| 1.2 | 2026-10-11 | Ronda 1 del Checkpoint 1 (REVISE acotado): **M5** auditoría con regla de **sensibilidad implícita ≥ 95 %** (máx(10 %, 150)) y prueba ciega de la IA con el conjunto de referencia; **M7** `historial_eval` redefinido sobre salidas previas del sistema (GOLD / PREDICHO / SOLO_PREGUNTAS), `turno` y configuración en `contrastes.csv`; **M2** aclaraciones dentro de diálogos tipo CoSQL = multiturno; **M4** conjunto de referencia con tamaño, etapa y brazo de un turno, control de circularidad; **M8** criterio de reformulación mapeado a códigos (grafos neuronales tipo IGSQL no cuentan; sensibilidad que sí los cuenta); **M3/N2** `chat*` → `chat OR chatbot* OR "chat-based"`, IEEE completado, ACM expandido; **N1** verificación de Liu et al. 2026 (sin protocolo, sin multiturno) y §6 actualizado; **N3/N4** sensibilidades de D4 sin bola de nieve y con subconjunto auditado; **N6** S5/S6 como aprobado/fallido; coherencia CERQual basada en contrastes dentro del estudio |
