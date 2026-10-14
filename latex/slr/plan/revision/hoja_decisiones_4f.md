# Hoja de decisiones — revisión simulada (paso 4f)

**Cómo responder:** «OK» = aceptar todas las recomendaciones (marcadas ★). Para cambiar una, escriba su código y la
opción, p. ej. `A4: b` o `C1: no`. Fuentes: `informe_methodology.md` (RM-n) e `informe_devil.md` (Rd-n), ambos con
veredicto «revisión mayor». Ninguna decisión exige nuevas búsquedas ni nueva recolección de datos.

**Opciones válidas:** `a`/`b`/`c` donde se indiquen · `sí`/`no` en las tareas opcionales · «OK».

---

###### A — Reanálisis con los datos existentes (scripts, $0; los números salen del código)

**A1 · Contraste un turno / multiturno (tabla VIII, IV-I/J, V-B) — RM-1, Rd-2.** Está sesgado por construcción: los de
un turno entran solo si PI3/PI4 es central; además se extrajeron con menos profundidad.
`a ★` recalcular la tabla con ambos brazos restringidos a estudios con PI3/PI4 central, mostrar filas «no reportado» y
eliminar la frase «la ambigüedad se aborda más mediante la interacción» · `b` igual, pero conservar la frase como
hipótesis explícita · `c` dejar como está.

**A2 · Criterio de reformulación M8 (V-D, resumen, VII) — RM-6, Rd-3.** Los pares observados (8, 7, 1) coinciden con lo
esperable por azar (8,4; 7,8; 2,4): no hay «evitación» de la combinación, solo prevalencias bajas.
`a ★` añadir los conteos esperados bajo independencia, reportar la variante con grafos neuronales en (a), aclarar que
las definiciones (a)/(b)/(c) estaban registradas (protocolo v1.2, M8a), reescribir como «consistente con baja
prevalencia conjunta» y quitar el «0» del resumen · `b` solo quitarlo del resumen.

**A3 · Tendencia de D4 con 2026 (IV-C, V-B) — RM-5, Rd-10.** 2026 tiene la proporción más baja y quedó fuera.
`a ★` añadir la prueba de tendencia incluyendo 2026 como sensibilidad y reportar ambas · `b` no.

**A4 · Efectos y «confianza alta» (tabla VI, IV-F) — RM-4, Rd-4.** Los nulos se contaban solo si el efecto era
exactamente 0; 8–9 de 12 clases figuran como «alta» pese al sesgo de notificación.
`a ★` mantener las etiquetas registradas pero añadir: sensibilidad con umbral de nulidad (|Δ| < 0,5 pp), y una columna o
nota «con penalización por sesgo de notificación» (baja un nivel); reescribir «efectos positivos y modestos» como «las
ablaciones de los autores rara vez reportan perjuicio» · `b` sustituir directamente las etiquetas por las penalizadas
(desviación del plan de síntesis → nueva enmienda) · `c` solo el umbral de nulidad.

**A5 · Fiabilidad del cribado y la extracción con IA (III-E, VI) — RM-3, Rd-5.** `a ★` reportar cuántas exclusiones
conjuntas no se releyeron y extrapolar la tasa de rescate (con IC) a omisiones esperadas; acuerdo por campo (κ/PABAK)
en los campos clave de la doble extracción; redactar los porcentajes «no reportado» como «no reportado o no extraído»;
declarar que la estratificación de PI5 depende de una codificación verificada de forma independiente en 3 de 5 casos.

**A6 · D4 como veredicto (resumen, III-H, IV-C) — RM-2, Rd-1.** `a ★` presentar D4 como proporción descriptiva «dentro
del marco de elegibilidad» con la regla registrada (umbral del 30 % = referencia elegida por la autora, sin
fundamento externo, dicho así); acuerdo en el campo que define D4; aclarar que el IC solo cubre el error muestral.

**A7 · Informes no recuperados (III-D, IV-A, V-D) — RM-7.** `a ★` describir cómo se asignó la «señal» por título y
resumen; renombrar la cota (evitar el 77 que coincide con el total multiturno); añadir una cota probabilística con las
tasas observadas en los recuperados; tasa de recuperación por fuente.

**A8 · Sensibilidad de la búsqueda (III-D, VI-A) — RM-8, Rd-7.** `a ★` dar el IC de 16/19, presentar el 86,2 % como
cota optimista por la circularidad del conjunto de referencia, y declarar como limitación la falta de un conjunto
independiente y de DBLP / Web of Science como fuentes.

**A9 · Degradación por turno (IV-K, V-B, fig. 7) — RM-12, Rd-6.** `a ★` eliminar la yuxtaposición efectos/pendientes;
discutir que el estrato predicho se degrada *menos* que el de solo preguntas (contraintuitivo); dar rangos y n por
estrato; explicar los valores > 100 %; presentar la afirmación sobre historial *gold* como hipótesis.

###### B — Redacción y consistencia (una ejecución de revisión, ≈ $1–1,5)

**B1 · Cifras sin conciliar — RM-11, Rd-9.** `a ★` nota en la tabla IV (317/78 = ejecuciones de extracción, con 5
estudios reclasificados; finales 313/77); completar las categorías de foro (146 + 91 + 34 no suman 390); corregir la
leyenda de la fig. 5 con dos «(a)»; justificar cada cambio de denominador (77 / 72).

**B2 · Agenda de brechas (V-D) — Rd-8.** `a ★` declarar la regla de ordenación (solidez = datos directos de los informes
> codificación de la extracción > rareza) y matizar la brecha de datos en español: las cadenas eran en inglés.

**B3 · Calidad (III-G, IV-E) — RM-10, Rd-11.** `a ★` explicar el umbral del 50 % (registrado), declarar que los estudios
de un turno no se evaluaron y que el umbral apenas filtra (lectura principal = con todos).

**B4 · Enmiendas y registro (tabla II, III-A) — RM-9, Rd-7.** `a ★` añadir a la tabla II una columna «momento» (antes o
después de ver datos de resultado) y precisar que el registro OSF precedió a las búsquedas oficiales (los recuentos
previos al registro constan en `registro_busquedas.csv`); etiquetar la sensibilidad de A4 como *post hoc*.

**B5 · Bibliografía — RM-11, Rd-12.** `a ★` ocultar las notas internas («Metadatos de OpenAlex…», «(C1)», «(C4)») y
corregir el autor mal formado de [22].

###### C — No factibles en esta ronda (se declaran como limitación) y tareas opcionales para la autora

**C1 · Tarea opcional (≈ 30–40 min):** revisar a ciegas 20 celdas «no reportado» elegidas al azar contra el PDF, para
acotar el error de extracción (Rd-5). `sí` / `no ★` (si `no`, se declara como limitación).
**C2 · Tarea opcional:** conseguir el texto completo de Yang et al. 2025 (revisión más cercana; Rd-12) — `sí` / `no ★`.
**C3 ★ Fases posteriores:** material suplementario (Fase 12), actualización OSF de A4–A6 y declaración de IA (Fase 13),
cita pendiente de propagación de errores (se resuelve en este paso con un estudio incluido).

Respuesta:
