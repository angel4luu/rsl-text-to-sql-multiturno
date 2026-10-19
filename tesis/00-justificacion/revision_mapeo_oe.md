# Revisión — correspondencia OE → códigos de la RSL (Fase 14, paso 1a)

**Cómo responder:** debajo de cada decisión escriba `OK`, o una de las opciones indicadas (p. ej., `B`), o un texto libre.
Solo se listan las decisiones no obvias; el resto de la correspondencia está en `MAPEO` de
`analysis/src/tesis/mapa_oe.py` y las cifras en `datos/mapa_oe_indicadores.csv` (generadas por el *script*).

Roles de cada indicador: **propuesta** (lo que plantea el OE), **alternativa** (enfoque competidor con evidencia propia),
**problema** (evidencia de que el problema existe), **contexto**.

---

**D1. OE2 — ¿qué cuenta como «estado estructurado»?** Se cuentan `GRAFO` y `ESTRUCTURA_EXPLICITA` (como el
componente *a* del criterio M8). A: ambos (propuesto) · B: solo `GRAFO`.
**Decisión:** A — aprobado por la autora (2026-10-14)

**D2. OE3 — vinculación por grafo de esquema (`pi3_tecnica_linking = GRAFO_ESQUEMA`, 41 estudios).** Codifica el esquema
como grafo, pero no enruta *joins*. A: rol «contexto» (propuesto) · B: rol «propuesta».
**Decisión:** A — aprobado por la autora (2026-10-14)

**D3. OE4 — `AUTODEPURACION_LLM` (reflexión del LLM)** forma parte del OE4 (bucle neuronal guiado por errores del DBMS).
`VERIFICADOR_CRITICO` y `AUTOCONSISTENCIA_VOTACION` se tratan como alternativas. A: OK (propuesto) · B: los tres como «propuesta».
**Decisión:** A — aprobado por la autora (2026-10-14)

**D4. OE5 — evaluación con historial *gold*** como indicador de «problema» (sobrestima la exactitud multiturno).
A: OK (propuesto) · B: «contexto».
**Decisión:** A — aprobado por la autora (2026-10-14)

**D5. Premisa multiagente** medida solo con `paradigma_principal = AGENTES` (los secundarios no registran agentes).
A: OK (propuesto) · B: excluir la premisa del mapa (se discute en el paso 2).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D6. Población de los contrastes:** principal = nivel 2 que supera el umbral de calidad (72); sensibilidad = todo el nivel 2
(77). Igual que la síntesis de la RSL. A: OK (propuesto).
**Decisión:** A — aprobado por la autora (2026-10-14)

**D7. Clases de los componentes de los contrastes** (336 pares OE–componente, asignados hoy por expresión regular): Codex
propone la clase de cada uno con motivo; Claude verifica una muestra; usted solo revisa los casos dudosos en una hoja
aparte. A: OK (propuesto) · B: revisarlos todos usted.
**Decisión:** A — aprobado por la autora (2026-10-14)

---

## Casos dudosos de la clasificación de componentes (D7, propuesta de Codex)

**D8. `QUESTION_DETECTOR`, `ANALISIS_DIFERENCIA(S)_ENTRE_PREGUNTAS` → OE1 «Reescritura / reformulación / discurso».**
Detectan ambigüedad o cambios entre preguntas; no reescriben por sí mismos. A: OK (dentro de la clase amplia) · B: `NINGUNA`.
**Decisión:** A — aprobado por la autora (2026-10-14)

**D9. `TSP`, `CSP`, `TSP+CSP` (tareas auxiliares que predicen cambios de SQL/esquema entre turnos) → OE2 `NINGUNA`.**
No son una representación explícita del estado, pero sí lo modelan implícitamente. A: OK (`NINGUNA`) · B: «Grafo / estado / memoria estructurada».
**Decisión:** A — aprobado por la autora (2026-10-14)

**D10. `HUMAN_IN_THE_LOOP` (el usuario corrige restricciones extraídas) → OE4 «Aclaración / interacción con el usuario».**
A: OK · B: `NINGUNA`.
**Decisión:** A — aprobado por la autora (2026-10-14)
