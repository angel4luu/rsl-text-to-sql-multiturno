# Fase 1.1 — Verificación de estudios semilla (citas del *blueprint*)

Fecha: 2026-10-11 · Fuentes de verificación: DBLP (volcado 2026-09-01), OpenAlex, arXiv, Scopus.
Regla aplicada: una cita que no puede confirmarse tras ≥ 3 búsquedas distintas se marca **NO ENCONTRADA** y no se usa (zona gris = FALLO).

**Uso de las semillas:** comprobar la sensibilidad de las cadenas de búsqueda (Fase 1.3) y la calibración del cribado (sr-screener). Una semilla solo sirve para probar la búsqueda si está indexada en las bases oficiales.

## A. Verificadas — candidatas a semilla (estudios primarios)
| # | Estudio verificado | Publicación | Pilar / PI | Observaciones |
|---|---|---|---|---|
| S1 | Chen, Z. et al. — *Decoupled Dialogue Modeling and Semantic Parsing for Multi-Turn Text-to-SQL* | Findings ACL-IJCNLP 2021 (DBLP `conf/acl/ChenCLCMWY21`) | PI1–PI2 (multiturno) | Coincide con el *blueprint* |
| S2 | Tummalapenta, R. K. y Addanki, S. — *Memory Architectures for Multi-Turn Text-to-SQL: A Benchmark and Empirical Study* | arXiv 2605.26394 (2026) — **preprint** | PI2, PI5 (multiturno) | La cita del *blueprint* («collapses… by the third turn») concuerda con el resumen. Literatura gris |
| S3 | Usta, A., Karakayali, A. y Ulusoy, Ö. — *DBTagger: Multi-Task Learning for Keyword Mapping in NLIDBs…* | PVLDB 2021 (DBLP `journals/pvldb/UstaKU21`) | PI3 (un turno) | **Año corregido:** el *blueprint* dice 2023; es 2021 |
| S4 | Safdarian, A. et al. — *SchemaGraphSQL: Efficient Schema Linking with Pathfinding Graph Algorithms for Text-to-SQL on Large-Scale Databases* | Findings EACL 2026; arXiv 2505.18363 (2025) | PI3 (un turno) | Coincide con «Safdarian et al. (2025)». Ver nota sobre «Wang et al. (2025)» en C |
| S5 | Chen, K., Chen, Y., Koudas, N. y Yu, X. — *Reliable Text-to-SQL with Adaptive Abstention* | PACMMOD 2025 (DBLP `journals/pacmmod/ChenCKY25`) | PI3–PI4 (un turno) | Coincide con «Chen et al. (2025)» (abstención / *schema linking*) |
| S6 | Xie, X. et al. — *OpenSearch-SQL: Enhancing Text-to-SQL with Dynamic Few-shot and Consistency Alignment* | PACMMOD 2025 (DBLP `journals/pacmmod/XieXZG25`) | PI4 (un turno) | **Coincidencia probable, a confirmar por la autora** («Xie et al. (2025)», guardas de consistencia multiagente) |

## B. Verificadas — pero no aptas como semilla
| Estudio | Motivo |
|---|---|
| Jain, P. y Lapata, M. — *Conversational Semantic Parsing using Dynamic Context Graphs*, EMNLP 2023 | **Dominio distinto:** grafos de conocimiento (SPARQL sobre Wikidata), no bases de datos relacionales. El *blueprint* lo presenta como Text-to-SQL. Su elegibilidad depende de la decisión de la Fase 1.2 sobre análisis semántico conversacional no-SQL |
| Li, Y. (2023) — *Execution-Feedback and Retrieval-Augmented Generation for Conversational Text-to-SQL…*, *Journal of Advanced Computing Systems*, DOI 10.69987/jacs.2023.30201 | Encontrado solo en OpenAlex; **no indexado** en DBLP ni Scopus; revista sin trayectoria verificable → **posible revista depredadora** (se evaluará en calidad). No sirve para probar la búsqueda. Fuente de las citas «Li (2023)» y «Yunhe Li (2023), EFRAG» |
| Quamar, A. et al. — *Natural Language Interfaces to Data*, Found. Trends Databases 2022 | Monografía/*survey* → carpeta 9 (trabajos relacionados) |
| Shi, L. et al. — *A Survey on Employing Large Language Models for Text-to-SQL Tasks*, ACM Comput. Surv. | *Survey* → carpeta 9. La frase citada en el *blueprint* aún debe verificarse en el texto |

## C. NO ENCONTRADAS (≥ 3 búsquedas en DBLP, OpenAlex y arXiv)
| Cita del *blueprint* | Búsquedas realizadas | Hipótesis |
|---|---|---|
| Liao et al. (2021), «ReDST», grafo bipartito | DBLP «ReDST», autor+tema; OpenAlex; arXiv DST + text-to-SQL | Sin rastro |
| ~~Jieyu Li et al. (2023), dataset «DIR» de reescritura~~ **CORRECCIÓN (2026-10-11): SÍ EXISTE** | DBLP autora; DBLP/arXiv reescritura + elipsis | **Error de verificación:** *DIR: A Large-Scale Dialogue Rewrite Dataset for Cross-Domain Conversational Text-to-SQL*, Li, J., Chen, Z., Chen, L., Zhu, Z., Li, H., Cao, R. y Yu, K., *Applied Sciences* 13(4), 2262, 2023, DOI 10.3390/app13042262. No estaba en DBLP (que no indexa *Applied Sciences*) y no se buscó con estos términos en OpenAlex. Se halló al construir el conjunto de referencia independiente. Lo recuperará la búsqueda sistemática; las demás citas de C siguen sin encontrarse |
| Tzitzikas y Marketos (2025), árboles de dependencias + grafo de esquema | DBLP coautoría; publicaciones de Tzitzikas 2024–2026; OpenAlex | Tzitzikas no tiene trabajos de NL→SQL; el nombre «Marketos» no aparece (existe «Marketakis») |
| «Dynamic-SQL» (2026), autocorrección multironda | DBLP título; arXiv; OpenAlex | Sin rastro |
| Wang et al. (2025), esquema como grafo no dirigido + BFS/Dijkstra, *zero-shot* | DBLP título/autor; búsqueda de *schema graph* 2025+ | La descripción coincide con **SchemaGraphSQL (Safdarian et al.)** → posible atribución errónea |

**Decisión de la autora (2026-10-11):** las fuentes originales no están disponibles → las citas de C **se descartan**. Si alguno de esos trabajos existe y es pertinente, lo recuperará la búsqueda sistemática de la Fase 2. S6 aceptada como semilla.

## Observación para la autora
Los números entre corchetes del *blueprint* (p. ej., [159], [867]) sugieren que se generó con una herramienta de IA sobre un conjunto de fuentes (p. ej., NotebookLM). Si esas fuentes (PDF) existen, permitirían resolver las citas de C. **Ninguna cita de C se usará como evidencia** hasta localizar su fuente original.
