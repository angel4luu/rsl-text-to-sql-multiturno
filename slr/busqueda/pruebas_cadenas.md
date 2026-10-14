# Fase 1.3 — Registro de pruebas de la cadena de búsqueda

Fecha: 2026-10-11 · Herramientas: Scopus (API), arXiv (API), OpenAlex (estimación de volumen).
Estas pruebas calibran la cadena; **no** son las búsquedas oficiales (Fase 2).

## Estudios semilla (13)
S1–S6: `slr/protocolo/02_estudios_semilla.md`. S7–S13, elegidas por la autora antes de probar las cadenas:
S7 SParC (ACL 2019) · S8 CoSQL (EMNLP 2019) · S9 CHASE (ACL 2021) · S10 EditSQL (EMNLP 2019) · S11 IGSQL (EMNLP 2020) · S12 CQR-SQL (Findings EMNLP 2022) · S13 CoE-SQL (NAACL 2024).
**Limitación reconocida (M4b):** las semillas no son independientes de las cadenas (sus resúmenes contienen términos de B1), por lo que su recuperación prueba poco. La sensibilidad se medirá además con un **conjunto de referencia independiente** (abajo).

## Indexación de semillas
| Base | Semillas | Notas |
|---|---|---|
| Scopus | S1, S3, S4, S7–S13 (10) | S7 y S11 **sin DOI**; S12 con **DOI erróneo** (`…emnlp.374` = *BioNLI*; correcto `…emnlp.150`, verificado en ACL Anthology) → la deduplicación no puede basarse solo en DOI |
| ACM DL | S5, S6 (PACMMOD) | No indexadas en Scopus. **Pendiente** de verificar en la búsqueda oficial de ACM |
| arXiv | S2 | Preprint |

## Iteraciones
| Versión | Cambio | Resultado | Motivo |
|---|---|---|---|
| v1 | Cadena inicial | Scopus 9/10 | Falla S3 (DBTagger): sin resumen; «NLIDBs» no casa con `nlidb` |
| v2 | `nlidb*`; + `"keyword mapping"` | Scopus 10/10 | — |
| v2 | Comprobación de texto de resúmenes de S5, S6 (arXiv) | S5 contiene los términos; **S6 no** | S6 llama «Refinement» a su autocorrección |
| v3 | + `refinement` | Scopus 10/10; S5/S6 solo comprobadas por texto del resumen, **no** en ACM | **Ajuste a una semilla** (M4b): se reconoce; su justificación es que «refinement» es un término frecuente en autocorrección LLM, y su conteo marginal (+96) se registró |
| v3 | Prueba con casos externos sugeridos por el Checkpoint 1 | SCoRe (ICLR 2021) ✓; **R²SQL / *Dynamic Hybrid Relation Network* (AAAI 2021) ✗** | El resumen de R²SQL no contiene «SQL» suelto (solo «semantic parsing», «database schemas», «SParC», «CoSQL») |
| **v4** | Bloques ampliados (M3) y `"semantic pars*" AND (sql OR database* OR sparc OR cosql OR spider OR chase)` | **Scopus 12/12** (10 semillas + SCoRe + R²SQL) | — |

## Sensibilidad por base (estado actual; se completa en la Fase 2)
| Base | Semillas probadas | Recuperadas |
|---|---|---|
| Scopus (v4) | 10 semillas + 2 casos externos | 12/12 |
| ACM DL (v4 corregida) | S5, S6 | **2/2** (conteo previo al registro, 2026-10-11; C08) |
| arXiv | S2 | 1/1 (v2) — se reconfirma con v4 en la Fase 2 |
| IEEE Xplore | — (ninguna semilla es exclusiva de IEEE) | se mide con el conjunto de referencia |
| ACL Anthology | S1, S7–S10, S12, S13 (vía volcado) | pendiente (Fase 2) |

## Conteos marginales de los términos añadidos en v4 (OpenAlex, resumen, 2019+)
Solo registros **no** recuperados por v3:
| Grupo de términos nuevos | + registros | Muestra |
|---|---|---|
| Bloque A (text2sql, «semantic parsing» + BD/SParC/CoSQL/Spider, *database question answering*…) | +78 | R²SQL, SCoRe; algo de KGQA (lo filtra EX5) |
| Bloque B1 (multi-round, *rewriting*, correferencia, elipsis, DST, *session*, *chat*…) | +50 | algo de ruido por *chat*/*session* |
| Bloque B2 (*table selection*, *verifier*, *self-consistency*, *reflection*, Steiner…) | +192 | DBCopilot, SPSQL, CSR-RAG (PI3); ruido filtrado por EX6 |
Total estimado: v3 ≈ 848 → **v4 ≈ 1 170** (OpenAlex; cota inferior de una sola fuente). Se priorizó la exhaustividad sobre la precisión: el cribado título-resumen es asistido por IA y la regla EX6 filtra el ruido.

## Conjunto de referencia independiente (*quasi-gold standard*, M4; revisado en la ronda 1)
Procedimiento (Zhang, Babar y Tell, 2011), **independiente de las cadenas**, construido **antes** de ver los resultados de las búsquedas oficiales:

**Brazo multiturno (objetivo ≥ 30 estudios):**
- (a) estudios multiturno citados en Li, Qu y Haffari (2020), *Context Dependent Semantic Parsing: A Survey* (COLING, acceso abierto);
- (b) trabajos que **citan SParC o CoSQL** según OpenAlex y reportan resultados en esos *benchmarks*;
- (c) estudios multiturno citados en Yang et al. (2025), si se obtiene el PDF.

**Brazo de un turno (objetivo ≥ 20 estudios, cubriendo ambas épocas):** estudios de vinculación de esquemas y de autocorrección citados en las secciones correspondientes de (i) un *survey* de la era LLM, Hong et al. (2025, IEEE TKDE / arXiv 2406.08426), y (ii) un *survey* pre-LLM, Deng, Chen y Zhang (2022, COLING, acceso abierto), para medir la recuperación del denominador de D4 en todo el período 2019–2026.

**Elegibilidad de los miembros:** se aplican IC1–IC7 y EX1–EX9; título-resumen y, cuando haga falta, texto completo. Solo los elegibles forman el conjunto.

**Medidas:**
1. Sensibilidad = proporción del conjunto recuperada por la **unión** de las búsquedas oficiales, por **brazo** y por **base**, con IC 95 % de Wilson.
2. **Control de circularidad:** la sensibilidad del brazo multiturno se reporta también **solo para los miembros cuyo resumen no contiene «SParC» ni «CoSQL»** (términos que la cadena incluye).
3. **Umbral:** si la sensibilidad global de algún brazo es **< 80 %**, se analizan los no recuperados, se ajusta la cadena (enmienda registrada) y se repite la búsqueda.
4. Los miembros del conjunto se usan también como **positivos conocidos** para probar a ciegas a los revisores IA (protocolo §11c).

Cubre además los foros de aprendizaje automático (ICLR, NeurIPS, AAAI, IJCAI).

### Construcción realizada (2026-10-11, antes de las búsquedas oficiales)
Archivo: `conjunto_referencia.csv` (congelado con el commit de la Fase 1; no se modifica tras ver los resultados de las búsquedas).
- **Brazo multiturno — 32 candidatos.** Fuente (b): 214 trabajos que citan SParC o CoSQL en OpenAlex (desde 2019), cribados por la IA con IC/EX sobre título y resumen; solo se retuvieron los **claramente** elegibles (casos dudosos como GAZP quedaron fuera). Incluye 5 semillas (S1, S8, S9, S10, S12), marcadas en la columna `semilla`; la sensibilidad se reportará también **sin** ellas. Fuente (a), Li et al. (2020): no aportó miembros nuevos de 2019 en adelante (sus citas SQL de ese período, EditSQL, SParC y CoSQL, ya estaban). Fuente (c), Yang et al. (2025): sin PDF.
- **Brazo de un turno — 25 candidatos.** 10 pre-LLM (Deng et al., 2022, secciones de *encoding*/*schema linking* y *decoding*/*execution-guided*; y citas de SParC/CoSQL) y 15 de la era LLM (Hong et al., 2025, categorías C1 *decomposition* con módulos de *schema linking*, *schema augmentation* y C4 *execution refinement*). Títulos exactos y DOI se resuelven en DBLP/OpenAlex antes de medir.
- **Limitación observada:** OpenAlex no registra todas las citas: IGSQL (S11), que cita SParC, no aparece entre los 214. La fuente (b) es por tanto incompleta, lo que no sesga la medida de sensibilidad (los miembros se eligen sin usar la cadena), pero reduce el tamaño del conjunto.
- **Hallazgo colateral:** DIR (Li et al., 2023, *Applied Sciences*), que se había declarado «no encontrado» en la verificación de semillas, apareció aquí; se corrigió `02_estudios_semilla.md`.
- **Verificación pendiente antes de medir:** confirmación ciega de la elegibilidad de cada candidato (título-resumen y, si hace falta, texto completo) por la autora.

## Sensibilidad de las búsquedas oficiales (Fase 2.4, 2026-10-11)
Cálculo: `scripts/sensibilidad.py` → `sensibilidad_fase2.json`. Coincidencia por DOI normalizado o título normalizado (similitud ≥ 0,93), sobre las exportaciones oficiales leídas con los parsers de sr-screener. Elegibilidad del conjunto de referencia determinada por IA (enmienda A1).

| Medida | Resultado | IC 95 % (Wilson) | Umbral registrado |
|---|---|---|---|
| Semillas (13) | **13/13** | — | todas |
| Brazo multiturno — elegibles | **24/24 (100 %)** | 86,2–100 % | ≥ 80 % ✓ |
| Brazo multiturno — elegibles + probables | 31/31 (100 %) | 89,0–100 % | — |
| Brazo multiturno — control de circularidad (resumen sin «SParC»/«CoSQL») | 5/5 (100 %) | 56,6–100 % | — |
| Brazo multiturno — sin semillas | 19/19 (100 %) | 83,2–100 % | — |
| Brazo de un turno — elegibles | **16/19 (84,2 %)** | 62,4–94,5 % | ≥ 80 % ✓ |

**Por base (multiturno, elegibles + probables):** Scopus 31, arXiv 12, IEEE 9, ACL 9, ACM 2. **(Un turno):** arXiv 15, Scopus 10, ACL 6, IEEE 0, ACM 0.

**No recuperados (un turno):** MAC-SQL («refine erroneous SQL queries», «acquire smaller sub-databases»), CHESS («Schema Selector… prunes», «refines queries») y Bertrand-DR («discriminative re-ranker»). **Causa común:** la cadena v4 contiene las formas nominales («refinement», «schema selection», «candidate selection») pero no las verbales («refine», «prune») ni «re-rank». 

**Decisión de la autora (2026-10-11):** ambos brazos cumplen el umbral registrado → **no se realiza búsqueda suplementaria** (opción a). Se reporta como limitación: la omisión es sistemática y afecta al brazo de un turno (denominador de D4); su efecto sobre D4 es **conservador** (reduce el denominador y eleva la proporción multiturno, en contra de la conclusión «≤ 30 %»). El límite inferior del IC del brazo de un turno (62 %) se declara.
