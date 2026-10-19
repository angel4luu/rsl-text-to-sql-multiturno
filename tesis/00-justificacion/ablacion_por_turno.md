# Ablación de estado y resultados por turno

| ID | Ablación de estado | Por turno, sistema | Por turno, variantes ablacionadas |
|---|---|---|---|
| R00099 | sí | sí | no |
| R00117 | sí | sí | no |
| R00435 | sí | sí | sí |
| R00438 | sí | no | no |
| R00499 | sí | parcial | no |
| R01029 | sí | sí | no |

**R00099 — Hu2022InContext.** Se compara el uso de contexto completo, turno único y estado previo más turno único en MultiWOZ 2.4 (Tabla 3, §5, p. 7). Se muestra JGA por turno en la Figura 5 para el sistema de la fila 5 y para la predicción directa de estado de la fila 2, pero ambas configuraciones reciben el estado previo; no se muestra por turno la variante sin esa representación. Los valores exactos de las curvas no están impresos, por lo que quedan **no claros**. Se afirma: “Because states have increasing numbers of slots with more turns, JGA [...] of the full state decreases for later turns” (§5, p. 7).

**R00117 — Cai2020IGSQL.** Se ablan las capas de grafo de interacción de esquema en la Tabla 6 (§6.3, p. 8), con resultados agregados de desarrollo de SParC y CoSQL. La Tabla 4 (§6.2, p. 7) sí presenta exact match por turnos 1/2/3/4/>4 para IGSQL —SParC 63.2/50.8/39.0/26.1/0; CoSQL 53.1/42.6/39.3/43.0/31.0— y para EditSQL —62.2/45.1/36.1/19.3/0; 50.0/36.7/34.8/43.0/23.9—, pero EditSQL es un baseline, no una variante de la ablación. Se señala: “In CoSQL, performances on interaction with two turns and larger than four turns improve the most” (§6.2, p. 7).

**R00435 — Tummalapenta2026Memory.** Se comparan cinco condiciones de memoria en las Tablas 6 y 8 (§6.1–6.2, pp. 10–11). La Tabla 7 (p. 11) imprime EX% para cada T1–T10 bajo A (sin estado) y B (memoria de trabajo de dos turnos) en los cinco modelos: Sonnet 4.5 A 69.7/4.3/0/10.5/1.1/2.2/0/8.9/0/15.0 y B 70.7/84.3/92.9/97.1/68.9/98.9/81.1/98.9/96.7/45.0; Sonnet 4.6 A 68.0/0.5/0/5.2/1.1/1.1/0/7.8/0/5.0 y B 68.0/52.4/95.2/78.1/66.7/83.3/80.0/85.6/83.3/30.0; Opus 4.6 A 67.0/2.4/0/1.9/1.1/2.2/0/1.1/0/0 y B 67.7/66.7/87.6/89.5/62.2/90.0/76.7/94.4/81.1/40.0; GPT-5 mini A 68.7/5.7/0/7.6/1.1/7.8/0/10.0/0/15.0 y B 68.3/76.2/100.0/91.4/70.0/91.1/83.3/91.1/96.7/45.0; GPT-5.2 A 73.0/5.2/0/7.6/1.1/13.3/0/6.7/1.1/0 y B 73.0/90.0/100.0/96.2/70.0/96.7/81.1/100.0/74.4/50.0. Se advierte que T10 usa 20 sesiones. El texto resume: “Condition A drops to near-zero by Turn 3 and stays there; Condition B recovers to 60–95%” (§6.1, p. 10). No se dan curvas por turno para B_wm5, C o D.

**R00438 — Wang2026Learning.** Se eliminan por separado la memoria de episodio, la memoria de turno y la optimización por RL en la Tabla 3 (§6.2, p. 8) de BIRD-Interact. Se informan Success Rate por fase y Avg. #Turns, pero no exactitud por índice ni por grupo de turno; Avg. #Turns es una medida de coste de interacción. Se indica: “[T]urn-level hints complement episode-level by supporting decisions as the interaction state evolves” (§6.2, p. 8).

**R00499 — Yang2026GitHarness.** Se ablan la selección de versión histórica, INSPECT, la reutilización de estado exacto y los modos de ejecución en la Tabla 2 (§5.3, p. 8), incluidos resultados agregados de BIRD SQL. La Tabla 4 (p. 9) agrupa sesiones por H = 10/15/20/25/30, pero solo para Math y Research y frente a baselines: GitHarness obtiene 92.0/90.0/87.0/85.0/84.0 en Math y 49.53/49.27/48.71/47.52/47.32 en Research. No se desglosan por horizonte las variantes de la Tabla 2 ni se incluye SQL, por lo que el resultado por turno del sistema se clasifica como parcial. Se informa: “From H = 10 to H = 30, its Research score decreases by only 2.21 points” (§5.3, p. 9).

**R01029 — Wang2021Tracking.** Se eliminan schema-states y SQL-states en la Tabla 4 (p. 7), donde solo se dan QM e IM agregadas. La Tabla 6 (Analysis—Turn Index, p. 7) presenta QM por turnos 1/2/3/4/>4 para IST-SQL, 56.2/41.0/41.0/41.2/26.8, y para Edit-Net, 52.1/39.6/37.3/36.0/25.4; Edit-Net es un baseline, no una de las variantes ablacionadas. Se afirma: “These results demonstrate the ability of our model on dealing with deep turns by tracking the interaction process with schema-states and SQL-states” (p. 7).
