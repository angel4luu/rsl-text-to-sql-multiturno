# Fase 1.4 — Lista de verificación de calidad (CQ)

Fecha: 2026-10-11 · Estado: **v1.1 — revisada tras el Checkpoint 1 (M9, M5); aprobada por la autora (2026-10-11)**
Base: Kitchenham y Charters (2007), §6.3, adaptada a Text-to-SQL.
**Alcance (D7):** se aplica a los estudios del **Nivel 2** (multiturno incluidos tras texto completo). Los estudios de un turno (Nivel 1) no se puntúan.

## Puntuación
Cada pregunta: **1** = sí / completo · **0,5** = parcial · **0** = no.

## Preguntas
### A. Validez (determinan el umbral)
| # | Pregunta | 1 | 0,5 | 0 |
|---|---|---|---|---|
| CQ2 | ¿Se describe la técnica (o la construcción del *benchmark*) con detalle suficiente para reproducirla? (arquitectura, *prompts*, modelos y versiones, hiperparámetros / proceso de anotación) | Completo | Faltan elementos importantes | Insuficiente |
| CQ4 | ¿Se compara con líneas base competitivas del momento, **con el mismo modelo base** cuando aplica? | Sí | Solo líneas base débiles, antiguas o con otro modelo base | Sin comparación |
| CQ5 | ¿Se reportan y definen métricas estándar (EX, EM/ESM, TS; QM/IM en multiturno) **y el tipo de historial usado en la evaluación** (gold vs. predicho)? | Ambos | Uno de los dos | Ninguno |
| CQ6 | ¿Se analiza la contribución de cada componente (ablación) o se hace un análisis de errores? *(Benchmarks: análisis de dificultad o de errores de las líneas base)* | Ablación o análisis sistemático | Análisis cualitativo breve | Ninguno |
| CQ7 | ¿Se evalúa la robustez? (varias ejecuciones o semillas, varianza, significancia, o varios *datasets*/modelos) | Sí | Parcial | Una ejecución, un *dataset* |

### B. Reporte y apertura (se reportan, no determinan el umbral)
| # | Pregunta | 1 | 0,5 | 0 |
|---|---|---|---|---|
| CQ1 | ¿Se definen claramente el objetivo, el problema y el escenario? | Explícitos | Vagos | Ausentes |
| CQ3 | ¿Se evalúa en *benchmarks* públicos reconocidos? | ≥ 1 público | Solo datos propios descritos | Datos propios no descritos |
| CQ8 | ¿Están disponibles el código o los datos? | Públicos | Parcial / «bajo petición» | No |
| CQ9 | ¿Se discuten las limitaciones o amenazas a la validez? | Explícito | Breve | No |
| CQ10 | Foro de publicación | Revisado por pares e indexado (Scopus, DBLP o ACL Anthology) | Preprint | Foro no indexado **con indicios de prácticas depredadoras** según la lista *Think. Check. Submit.* (thinkchecksubmit.org): revisión por pares no verificable, comité editorial no identificable, cobro sin servicios declarados, alcance desmesurado |

## Umbral y uso (revisado, M9)
1. **Puntuación de validez** = (CQ2 + CQ4 + CQ5 + CQ6 + CQ7) / 5 × 100 %.
2. **Umbral único:** validez ≥ **50 %** → entra a la síntesis en profundidad (PI1–PI5). **Se elimina el umbral especial del 60 % para preprints** (doble penalización); los preprints se tratan con el análisis de sensibilidad «sin preprints».
3. Los ítems de reporte y apertura (CQ1, CQ3, CQ8–CQ10) se **reportan por ítem**, no suman al umbral.
4. **Perfil por ítem:** se publica una tabla tipo semáforo (estudio × ítem), no solo el porcentaje.
5. Estudios bajo el umbral: permanecen en PI0 y en el anexo; análisis de sensibilidad reincorporándolos.

## Procedimiento (revisado, M5)
1. **Calibración:** autora e IA puntúan por separado **5 estudios**; se precisan descriptores (cambios → `enmiendas.md`).
2. **Muestra independiente:** en un **20 % aleatorio** del Nivel 2 (mínimo 5), la autora puntúa **antes de ver** la propuesta de la IA; se reporta el acuerdo (kappa ponderado y % de acuerdo por ítem).
3. **Resto:** la IA propone puntuación por ítem con cita o página; la autora verifica cada fila.
4. **Registro:** `slr/calidad/calidad.csv`.
