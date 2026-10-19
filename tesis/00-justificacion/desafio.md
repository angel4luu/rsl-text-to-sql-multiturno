# Paso 4 — Desafío independiente a la decisión (Fase 14)

Fecha: 2026-10-14. Fusiona dos fuentes, que se conservan íntegras:

- **4a** — diálogo socrático (ARS `deep-research`), `desafio_socratico.md`. Las respuestas de la autora se redactaron
  con otro asistente de IA y se contrastaron con el repositorio.
- **4b** — abogado del diablo en Codex (`gpt-6.1-sol`), `desafio_codex.md`, sin recomendación.

## 1. Verificación de `desafio_codex.md` por Claude

Se comprobaron por *script* las 16 parejas ID/`clave_bib` contra `bib/claves_estudios.csv`, sin discrepancias.
También se comprobaron todas las cifras de sensibilidad (D17, D18b, D19, D20) contra `datos/matriz_alternativas.csv`,
las puntuaciones y rangos de E3 contra `datos/matriz_decision.csv`, los recuentos citados contra `mapa_evidencia.md` y
`direcciones_alternativas.md`, la regla C1 de DC contra `matriz_decision.md`, y HE2 y el indicador «curva de
decaimiento por turno» contra `00-contexto/TS Blueprints.md`. Se corrigió una comparación imprecisa de rangos de DG
(se contrastaba E2 con E3). El documento declara 7 `[FALTA]`, todas por análisis inexistentes, no por datos omitidos.

## 2. Hallazgos principales

| # | Hallazgo | Origen | Consecuencia para el paso 5 |
|---|---|---|---|
| H1 | Partiendo solo de la RSL, la autora señaló DC (evaluación con historial predicho y reporte por turno), no OE2 | 4a, ítem 1 | DC es la brecha que la RSL ordena primero por solidez |
| H2 | OE2 conserva los contrastes más consistentes para la **clase** de estado estructurado (11 estudios, mediana +3,50 pp, confianza alta), no para la doble capa | 4a, ítem 3; 4b §2 | El apoyo es a la clase; el diseño concreto carece de contraste propio |
| H3 | La pregunta adoptada en 4a (pendiente frente a desplazamiento bajo historial predicho) **reproduce HE2** de `TS Blueprints.md` §5 («reduciendo el decaimiento de la precisión en diálogos extensos en comparación con los historiales de chat planos») y su indicador «curva de decaimiento por turno» (§6) | 4b §6; verificado | La pregunta no nació solo de la RSL: es la hipótesis previa reformulada. No la invalida, pero debe declararse |
| H4 | La autora declaró el costo hundido como motivo principal para mantener OE2 (R3 lo matiza en evidencia, apego y trámite) | 4a, ítem 6 y R3 | 4b: el trámite (Directiva 007) es una restricción, no evidencia; separar el juicio epistémico del operativo |
| H5 | La diferencia de pendientes puede no ser estimable: solo hay Δ globales y curvas de sistemas completos; los turnos tardíos son escasos y la estratificación por dificultad los fragmenta más | 4a, R1 y R5; 4b §6 | Hace falta un análisis de precisión antes de comprometer la pregunta |
| H6 | La clasificación «técnica/evaluación» gobierna buena parte del orden: C5 = 3 por tipo (D20) y la renormalización de C2 en E3 (D13) favorecen a DC y a las combinaciones de evaluación | 4b §2–3 | La posición de DC depende en parte de convenciones aprobadas |
| H7 | D19 (media en combinaciones) protege la posición de OE2: con máximos, DE+DF+DG pasa a rango 1 en los cuatro escenarios y DA+DC de 12 a 3 en E0 | 4b §3 y §5 | Ningún candidato tiene una posición estable frente a reglas igualmente discutibles |
| H8 | El universo de candidatos se construyó sobre OE1–OE5 y las decisiones D1, D3 y D8 ampliaron clases ligadas a la propuesta; su efecto no es cuantificable con las salidas actuales | 4b §3 | Sesgo de encuadre declarado, no medido |
| H9 | R2 (nivel de clase) se bifurca: reejecutar sistemas existentes no identifica el efecto de la clase, y una ablación propia limita la conclusión a esa implementación | 4b §6 | Definir de antemano el aporte propio y el alcance de la inferencia |
| H10 | R4 (contaminación) documenta el riesgo, pero no lo controla: los cortes de entrenamiento no son observables y SPENCE (R00029) es correlacional | 4b §6 | No se dispone de un *benchmark* multiturno inequívocamente posterior en el corpus |

## 3. Cuestiones abiertas para el paso 5

Se unifican las preguntas de 4a y 4b, sin respuestas sugeridas.

1. ¿La pregunta OE2 × DC se mantiene sabiendo que reproduce HE2 (H3)? Si se mantiene, ¿cómo se declara su origen?
2. ¿Se conservaría OE2 si el título inscrito pudiera modificarse sin coste? (4b, pregunta 8)
3. ¿Qué decisión se tomaría si el estado elevara la exactitud global pero dejara igual o empeorara la pendiente?
   La disyunción adoptada solo contempla resultados favorables. (4b §6)
4. ¿Qué precisión mínima debe tener la diferencia de pendientes y cómo se modelará la dependencia dentro del diálogo,
   la dificultad y el *benchmark*? (H5)
5. Implementación (R2): sistemas existentes, rastreador por *prompting* o grafo propio. ¿Cuál es el aporte propio en
   cada caso? (H9)
6. ¿Qué evidencia observable permitiría a R4 distinguir ausencia de contaminación de ausencia de información? (H10)
7. Verificación en texto completo: ¿reportan R00099, R00117, R00435, R00438, R00499 o R01029 resultados por turno
   con y sin el componente de estado? (4a, ítem 7)
8. ¿Qué criterio justificaría descartar DA+DC o DE+DF+DG si su posición cambia tanto con D19? (H7)
9. ¿Qué parte de DE+DF+DG es la relación principal y qué partes son condiciones de evaluación? (4b, pregunta 9)

## 4. Límites de este desafío

Las respuestas de 4a se redactaron con otro asistente de IA; tres afirmaciones no resistieron la verificación contra
el repositorio (`desafio_socratico.md`). Por ello, el razonamiento propio de la autora sobre la decisión aún no está
registrado de forma independiente. El paso 5 (`decision.md`) debe recogerlo.
