# Informe de acuerdo — extracción y calidad (fase 9)

Generado por `scripts/informe_acuerdo.py`. Diseño: doble extracción por IA (A, B), comparación automática, reglas preespecificadas (A5 c) y verificación de la autora por muestreo.

## Nivel 1 (317 estudios; A y B = Claude Sonnet)
- Acuerdo A–B por campo: 4131/4755 (86.9 %; IC95 85.9–87.8 %)
- Resolución: {'acuerdo': 4131, 'interseccion': 530, 'desempate_codex': 94}

## Nivel 2 (78 estudios; A = Claude Sonnet, B = GPT Codex salvo piloto y 2 reasignados)
- Acuerdo A–B en campos codificados (75 estudios no piloto): 1824/2478 (73.6 %; IC95 71.8–75.3 %)
- Acuerdo A–B en ítems de calidad: 567/750 (75.6 %; IC95 72.4–78.5 %)
- Resolución de campos: {'acuerdo': 1910, 'interseccion': 437, 'desempate_sonnet': 198, 'texto_A': 390, 'autora_A': 9, 'autora_B': 19, 'autora_valor': 3, 'acuerdo_NR': 1}
- Resolución de calidad: {'acuerdo': 597, 'desempate_sonnet': 180, 'autora_B': 2, 'autora_A': 1}

- Verificación de la autora, valores concordantes del Nivel 2 (muestra 10 %): confirmados sin cambios 182/182 (100.0 %; IC95 97.9–100.0 %)
- Verificación de la autora, estudios del Nivel 1 (muestra 10 %): confirmados sin cambios 32/32 (100.0 %; IC95 89.3–100.0 %)
- Verificación de la autora, ítems de validez cerca del umbral: confirmados sin cambios 95/95 (100.0 %; IC95 96.1–100.0 %)
- No decididos por el desempate y resueltos por la autora: 29 ({'A': 6, 'B': 15, 'OK': 8})

## Muestra independiente de la autora (5 estudios, a ciegas)
- escenario: 4/5 (80.0 %; IC95 37.6–96.4 %)
- historial_eval: 3/5 (60.0 %; IC95 23.1–88.2 %)
- calidad, ítem idéntico: 34/50 (68.0 %; IC95 54.2–79.2 %); a ≤ 0,5 puntos: 48/50 (96.0 %; IC95 86.5–98.9 %)
- resultados principales de la autora presentes en `resultados.csv`: 10/15 (66.7 %; IC95 41.7–84.8 %)
- Los demás campos de la muestra se anotaron en texto libre (no en el vocabulario controlado); se comparan cualitativamente.

  - discrepancia: R00298 escenario: autora UN_TURNO · IA MULTITURNO
  - discrepancia: R00920 historial_eval: autora SOLO_PREGUNTAS · IA PREDICHO
  - discrepancia: R00924 historial_eval: autora PREDICHO · IA SOLO_PREGUNTAS

Resolución final de estas discrepancias por la autora: Decisiones de la autora sobre discrepancias con su muestra independiente (2026-10-13). R00298 se mantiene en el Nivel 2; R00924 ya coincide (SOLO_PREGUNTAS). Taxonomía (2026-10-13): la autora aprobó la consolidación de OTRO/OTRA (taxonomia_revision.md) y la nueva categoría VALORES_BD de pi2_grafo_nodos. Valores aplicados: {"R00920": {"historial_eval": "SOLO_PREGUNTAS"}, "R00101": {"pi2_grafo_nodos": "TOKENS_PREGUNTA; ELEMENTOS_ESQUEMA; VALORES_BD"}, "R00936": {"pi2_grafo_nodos": "TOKENS_PREGUNTA; VALORES_BD; ELEMENTOS_ESQUEMA"}}
