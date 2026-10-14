# Fase 1.6 — Plan de síntesis

Fecha: 2026-10-11 · Estado: **v1.1 — revisado tras el Checkpoint 1 (M1, M7, M8, menores); aprobado por la autora (2026-10-11)**
Insumos: `extraccion.csv`, `resultados.csv`, `contrastes.csv`, `calidad.csv`. Todos los números, tablas y figuras se generan con Python (`analysis/`).

## Principios
1. **Sin metaanálisis**; síntesis narrativa y temática estructurada según **SWiM**.
2. **Comparabilidad estricta:** solo se comparan valores dentro de la misma configuración (*benchmark* + versión + partición + métrica + historial + conocimiento externo).
3. **Niveles (D7):** Nivel 1 (todos) → PI0 e indicador D4 + contraste de técnicas PI3/PI4. Nivel 2 (multiturno, validez ≥ 50 %) → PI1–PI5 en profundidad.
4. **Hallazgos separados de implicaciones** (estas van a la Discusión).

## PI0 — Mapeo descriptivo (Nivel 1)
| Análisis | Salida |
|---|---|
| Estudios por año y escenario | Barras apiladas |
| Tipo de publicación y *venues* | Tabla + barras |
| `paradigma_principal` × año | Mapa de calor |
| Pilares centrales × escenario | Tabla de contingencia |
| *Training-free* vs. con entrenamiento, por año y pilar | Tabla |
| Informes no recuperados, por escenario (D6) | Tabla (detecta recuperación diferencial que sesgaría D4) |

### Indicador D4 (regla pre-especificada; detalle en `01_preguntas_picoc.md`)
- Proporción = multiturno ∧ (PI3 ∨ PI4 central) / (PI3 ∨ PI4 central). IC 95 % de **Wilson**.
- **Conclusión «considerablemente menos investigado» solo si el límite superior ≤ 30 %**; si el IC contiene el 30 %: no concluyente.
- Versión laxa (con `pilares_contenidos`) como sensibilidad.
- **Tendencia:** proporción anual 2019–2025 con prueba de Cochran–Armitage **exacta (permutación, 10 000 réplicas)** por los conteos pequeños; **2026 se excluye de la prueba** por ser año parcial y se reporta aparte.

## PI3–PI4 — Contraste un turno vs. multiturno (Nivel 1)
Frecuencia de cada código de técnica (`pi3_tecnica_linking`, `pi3_inferencia_joins`, `pi4_mecanismo`, `pi4_senal`) por escenario: ¿qué técnicas de un turno **no** se han llevado aún al escenario multiturno?

## PI1–PI5 — Síntesis en profundidad (Nivel 2)
Para cada PI:
1. **Taxonomía:** deductiva desde los vocabularios; las categorías `OTRA` se consolidan inductivamente y se reportan obligatoriamente.
2. **Tabla comparativa:** estudio, técnica, paradigma, *training-free*, *benchmark*, métrica, historial, resultado, Δ, validez.
3. **Efectos (SWiM):**
   - **Contrastes dentro del estudio** (`contrastes.csv`) como evidencia principal sobre el efecto de un componente (p. ej., reescritura vs. concatenación, con/sin grafo de estado, con/sin autocorrección): mediana, rango y dirección del efecto por componente.
   - **Δ sobre la línea base de referencia** (misma configuración y mismo modelo base; regla en el formulario) como evidencia secundaria: mediana, rango y conteo por dirección, solo dentro de grupos comparables.
   - Las comparaciones **entre estudios** se presentan como descriptivas, nunca como prueba de superioridad.
4. **Preguntas específicas:** PI1 rewriting vs. concatenación (contrastes); PI2 representaciones estructuradas y coste acotado; PI3 inferencia de *joins* implícita vs. algorítmica y escala; PI4 mecanismos aplicados a multiturno.

## PI5 — *Benchmarks*, métricas y degradación por turno (Nivel 2)
| Análisis | Salida |
|---|---|
| Uso de *benchmarks* y métricas | Tabla + figura |
| Tipo de historial en la evaluación (`GOLD` / `PREDICHO` / `SOLO_PREGUNTAS`) | Tabla — informa qué estudios miden realmente propagación de errores |
| **Curvas de degradación**, separadas por tipo de historial | Figura (valor absoluto y normalizado al turno 1) |
| **Pendiente** (pp por turno; regresión ponderada por `n_turno` cuando se reporta) | **Estratificada y nunca agrupada:** `PREDICHO` = degradación **con propagación de errores** (el sistema reutiliza sus propias salidas); `SOLO_PREGUNTAS` = degradación **sin *teacher forcing*** pero **sin** propagación de salidas previas; `GOLD` = referencia con *teacher forcing*. Solo el estrato `PREDICHO` se interpreta como propagación de errores |
Limitación declarada: los grupos de turno contienen preguntas distintas (composición y dificultad), por lo que la pendiente mezcla profundidad del turno y dificultad de las preguntas.

## Confianza en los hallazgos (operacionalizada, menor)
Enfoque inspirado en GRADE-CERQual, con cuatro componentes calificados como «sin / leves / importantes» limitaciones:
| Componente | Regla |
|---|---|
| Limitaciones metodológicas | Validez media de los estudios que sustentan el hallazgo: ≥ 75 % sin; 50–74 % leves; < 50 % importantes |
| Coherencia | Calculada sobre **contrastes dentro del estudio** (que pueden mostrar efectos nulos o negativos), no sobre Δ frente a la línea base propia: dirección concordante en ≥ 80 % de los contrastes: sin; 60–79 %: leves; < 60 %: importantes. Si hay < 3 contrastes, la coherencia se califica como «leves» como máximo |
| Suficiencia | ≥ 5 estudios: sin; 3–4: leves; ≤ 2: importantes |
| Pertinencia/comparabilidad | Todos en configuración comparable: sin; mayoría: leves; minoría: importantes |
**Nivel:** alto (ninguna limitación importante y ≤ 1 leve), moderado (≤ 1 importante), bajo (≥ 2 importantes).

## Criterio de reformulación de la brecha (M8)
Se evalúa y reporta según lo pre-especificado en `01_preguntas_picoc.md` («Qué contaría en contra de la brecha de la tesis»).

## Sesgos considerados
Sesgo de publicación; contaminación de datos (`contaminacion_discutida`); desfase de líneas base; sesgo de idioma (EX2); recuperación diferencial (D6).

## Análisis de sensibilidad
1. Reincorporar estudios bajo el umbral de validez.
2. Excluir preprints.
3. Indicador D4 en versión laxa.
4. Indicador D4 **solo con registros de las búsquedas en bases** (sin bola de nieve, que parte solo de estudios multiturno).
5. Si se activó la contingencia del Nivel 1 (decisiones de texto completo por la IA): D4 recalculado **solo con el subconjunto auditado** por la autora, y tasa de error de la auditoría reportada.
Se reporta si cambia alguna conclusión.

## Productos
Figuras en `analysis/src/figs/` → `latex/slr/figuras/`; tablas LaTeX generadas desde CSV; notas por PI en `slr/sintesis/PI0.md`…`PI5.md`.
