# Paso 4a — Diálogo socrático (ARS `deep-research`, modo socrático), 2026-10-14

Registro del diálogo para la fusión en `desafio.md`. Las respuestas de la autora se redactaron con otro asistente de IA
y se pegaron en la sesión; Claude las contrastó con los datos del repositorio. Se indica el origen de cada elemento.

| # | Elemento | Estado | Fuente / verificación |
|---|---|---|---|
| 1 | Partiendo solo de la RSL, la autora señala DC (evaluación con historial predicho y reporte por turno), no OE2 | *Insight* | `latex/slr/secciones/07-conclusiones.tex` (primera brecha por solidez); estrato predicho: 6 curvas de 5 estudios (`04b-resultados.tex`) |
| 2 | Diseño DC: mismos diálogos con historial *gold* y predicho, delta por turno, estratos por dificultad SQL, tasa de recuperación tras un turno fallido | Adoptado (redactado con IA) | Corrección: «supuesto generalizado» y «hallazgo probado» exceden la evidencia (3 estudios citados en la introducción) |
| 3 | OE2 conserva los contrastes más consistentes (11 estudios, 10 positivos, mediana +3,50 pp, confianza alta) | *Insight* | `mapa_evidencia.md` §OE2; descartarlo solo por prevalencia es unilateral |
| 4 | Premisa «las ganancias del estado solo se observan con historial *gold*» | Refutada | `extraccion.csv` (`historial_eval`) de los 11 estudios: PREDICHO 6, NR 4, SOLO_PREGUNTAS 1, GOLD 0; codificación del historial verificada en 3 de 5 |
| 5 | Pregunta candidata: «¿El seguimiento explícito del estado estructurado reduce la pendiente de degradación por turno bajo historial predicho, o solo desplaza la exactitud global?» (OE2 × DC) | **Adoptada por la autora** (redactada con IA) | Sujeta a la verificación del ítem 7 |
| 6 | Motivo para mantener OE2 | Declaración de la autora: el impulso principal es el costo hundido y la inversión previa en la propuesta; las ganancias dentro del estudio existen, pero la RSL no dicta inequívocamente esa estructura | Nota: la respuesta menciona el «registro OSF»; OSF registra el protocolo de la RSL, no la tesis. Lo inscrito es el formulario de inscripción de la Escuela (Directiva 007, art. 7) |
| 7 | ¿Reportan los 6 estudios PREDICHO (R00099, R00117, R00435, R00438, R00499, R01029) resultados por turno con y sin el componente de estado? | Abierto | La extracción guarda un Δ global por contraste y curvas por estudio, no curvas por variante: «no extraído» ≠ «no reportado». Requiere lectura del texto completo |

Pendiente para el paso 5: decidir si la pregunta del ítem 5 sustituye, ajusta o se suma a OE1–OE5, a la luz del
ítem 6 (riesgo de costo hundido declarado) y del resultado del ítem 7.

## Refinamientos tras la revisión de Claude (2026-10-14)

Crítica de Claude a las respuestas de 4a, aceptada por la autora (respuesta redactada con IA y verificada contra el corpus).

| # | Refinamiento | Verificación |
|---|---|---|
| R1 | Encuadre de **estimación con intervalos** (pendientes de degradación, tamaños de efecto, IC 95 %), no contraste binario de hipótesis: los turnos 4+ de SParC/CoSQL tienen pocas preguntas y un resultado nulo de un contraste sin potencia no es informativo | Riesgo de resultado nulo alto: la ganancia global del estado es de mediana +3,50 pp (`mapa_evidencia.md` §OE2) y una diferencia de pendiente probablemente sea menor |
| R2 | La pregunta se plantea a **nivel de clase** (estado estructurado explícito, PI2). La implementación es una decisión aparte: sistemas existentes con código (p. ej., R00117 Cai2020IGSQL, R01029 Wang2021Tracking), un rastreador de estado por *prompting* o el grafo de dos capas propio (extensión opcional) | El grafo de dos capas no tiene evidencia propia en la RSL; solo la clase |
| R3 | Motivo para mantener un componente de estado, descompuesto en tres factores: (a) evidencia de la RSL para la clase; (b) costo hundido, que explica el apego al diseño específico de dos capas; (c) factibilidad institucional: cambiar el título inscrito exige modificación formal (Directiva 007, art. 7), un costo de factibilidad y no un sesgo | Sustituye la declaración del ítem 6 como lectura matizada; la declaración original se conserva arriba |
| R4 | Salvaguarda de **contaminación** (DD) para DC: al menos un *benchmark* posterior al corte de entrenamiento de cada modelo evaluado, verificado frente a la fecha de corte declarada, o una sonda explícita como SPENCE (R00029) | Contaminación discutida en 7 de 72 estudios (9,7 %) (`04b-resultados.tex`). BIRD-Interact (R00373, 2025) no es necesariamente posterior al corte de modelos de 2025–2026. Spider 2.0 se descarta: no es multiturno y es de 2024 |
| R5 | El diseño DC conserva los **estratos por dificultad SQL** (omitidos en la tabla resumen de la autora), necesarios para separar profundidad del turno y dificultad | Confusión señalada en `04b-resultados.tex` y `05-discusion.tex` |

Abierto para el paso 5: ítem 7 (verificación en texto completo) y la elección de implementación de R2.
