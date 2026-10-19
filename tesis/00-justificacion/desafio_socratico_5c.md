# Desafío socrático, segunda ronda (paso 5c) — EN PAUSA

Fechas: 2026-10-14 a 2026-10-16. Objeto: `decision.md` («ajustar»). Modo: ARS `deep-research` socrático.
Estado: pausado tras la ronda 5 (sin respuesta), a petición de la autora, para volver a la verificación de la RSL.
Las respuestas de la autora se dieron en inglés con sus propias palabras; aquí se resumen en español sin añadir contenido.

## Insumo previo (5b)
Verificación Codex de ablaciones por turno (`ablacion_por_turno.md`, `datos/ablacion_por_turno.csv`), comprobada contra
los PDF: todos los valores y citas coinciden; se corrigió una mayúscula en la cita de R00438. Alcance: los 6 contrastes
de estado estructurado con historial predicho. Ninguno de ellos informa resultados por turno de ambas variantes
(con y sin estado) salvo R00435, cuya comparación es «sin memoria» frente a «memoria de trabajo de 2 turnos», no estado
estructurado frente a historial plano. Los demás estudios multiturno no se revisaron para esta pregunta.

## Insights registrados
1. El grafo debe conservar el contexto del esquema (tablas, atributos) entre turnos para completar preguntas elípticas.
2. Cada nodo guarda ranuras tipadas (tablas, atributos, filtros); una pregunta nueva cambia una ranura y conserva el
   resto; los turnos son operaciones (añadir, retroceder…). Precedentes más cercanos: R01029 (estados explícitos
   actualizados por reglas desde el último SQL predicho) y R00499 (grafo versionado con retroceso).
3. La operación sobre el grafo la infiere el LLM, no reglas.
4. La autora identifica la corrección del usuario como disparador natural del retroceso; reconoce que en SParC no ocurre
   (preguntas fijas) y que no dispone de usuarios reales.
5. Prefiere un disparador interno al sistema (componente) y validación solo con *benchmarks* existentes sin usuarios.
6. Propuesta: confianza del LLM por ranura/operación con umbral como señal de error. Crítica (abogado del diablo, a
   petición): posible mala calibración (riesgo a medir, sin cita verificada), coste según método, umbral a fijar en
   train/dev, acción tras la señal ≈ reintento del turno; precedente lejano R00088 (clasificador de confianza →
   aclaración, basado en reglas). La autora queda **no segura** de esta opción.
7. La autora propone fijar primero los *benchmarks* de evaluación y después el manejo de errores.

## Pregunta abierta (ronda 5)
Entre SParC, CoSQL, SPLASH y BIRD-Interact: ¿cuál prueba el fallo que el grafo debe corregir, cuál permite que el
retroceso se dispare sin usuarios reales y cuál es el principal?

## Pendiente al reanudar
Respuesta a la ronda 5 → cierre del diálogo → 5d (abogado del diablo, Codex) → 5e (actualizar `decision.md`, incl. ítem 2
de «Verificaciones pendientes», ya resuelto por 5b). Las descripciones de SParC y CoSQL usadas en el diálogo provienen
del conocimiento del modelo: sus artículos originales deben añadirse y verificarse en `bib/referencias.bib` antes de citarse.
