# Fase 1.7 — Crítica del abogado del diablo (ARS, Checkpoint 1)

Fecha: 2026-10-11 · Ejecutado por un agente independiente (sin el contexto de la conversación), con el rol `deep-research/agents/devils_advocate_agent.md` de ARS v3.23.0, sobre la versión 1.0 del protocolo.
**Veredicto: REVISE** (0 críticos, 9 mayores, 10 menores). Informe en inglés, condensado fielmente (sin cambiar hallazgos, severidades ni recomendaciones):

---
## Devil's Advocate Report — Checkpoint 1

### Verdict: REVISE
No fatal flaw; the protocol is substantially above the norm for a single-author thesis SLR. But several Major issues must be fixed before the official searches are run.

Strengths acknowledged: seed verification (discarded 5 unfindable blueprint citations and a wrong year); ordered exclusion codes and documented borderline cases B1–B5; DOI + normalized-title deduplication after observing Scopus DOI errors; reproducible ACL Anthology dump procedure; long-format results table and strict comparability rule; correct handling of D6; separation of findings from thesis implications. CS adaptations judged justified: PICOC (Kitchenham), Kitchenham-style quality checklist instead of RoB 2/ROBINS-I, SWiM without meta-analysis. Weak spot: §17 confidence ratings.

### Critical Issues
No critical issues identified.

### Major Issues
1. **D4 indicator is ill-defined and largely determined by the review's own design** (Bias/Method; `01_preguntas_picoc.md`, `protocolo_es.md` §7, `plan_sintesis.md`, IC2/IC4/EX6/EX8). (a) Numerator not restricted to multi-turn ∧ (PI3 ∨ PI4); (b) no coding rule for when a multi-turn study "addresses PI3/PI4" — researcher degree of freedom; (c) the ratio measures the sampling frame (single-turn filtered three times), not the field — note the asymmetry raises the multi-turn share, working against the hypothesis; (d) ~9 % preliminary estimate makes the outcome near-certain; 30 % unjustified; (e) no decision rule when the Wilson CI straddles 30 %; (f) OSF registration optional, so pre-specification is only provable via git. **Rec.:** formal numerator; one coding rule for both scenarios (or strict + liberal ratios fixed now); CI rule (e.g., upper bound ≤ 30 %); justify 30 % or reframe as descriptive benchmark; limitation that the ratio is frame-conditional; make OSF registration mandatory before Phase 2.
2. **"Multi-turn" and "central contribution" ambiguous and partly unusable at TA stage** (`03_criterios_elegibilidad.md`). (a) Agent↔DBMS / self-refinement rounds can be coded MULTITURNO; (b) the "evaluated separately (e.g., ablation)" arm is only verifiable at full text and swallows the rule; (c) no "uncertain → full text" rule. **Rec.:** restrict multi-turn to user-initiated successive NL questions; add B6 (agent/self-refinement rounds on one question = single-turn); tighten or drop the ablation arm; explicit uncertainty rule; pilot it.
3. **Search strings miss common synonyms and are not equivalent across databases** (`cadenas.md`). Missing in A: text2sql, "natural language interface(s) to relational database(s)", "natural language quer* … SQL", "question(s) to SQL", "SQL synthesis", database question answering. In B1: multi-round, context-aware, session, coreference/ellipsis/anaphora, query/question/utterance rewriting, "dialogue state tracking", chat. In B2: table/column selection, table retrieval, schema filtering, value linking/retrieval, verif*/verifier, "SQL repair", debug*, self-consistency, reflection, candidate selection, join inference / multi-hop join / Steiner. ACM and IEEE strings drop some A/B2 terms; ACM Full-Text restriction should be justified. No Spanish terms although IC6 admits Spanish. **Rec.:** add terms with marginal counts logged; cross-database equivalence table; freeze v4 before registration.
4. **Sensitivity testing is circular and overstated** (`pruebas_cadenas.md`, `protocolo_es.md` §10). (a) "13/13" overclaims (Scopus 10/10; S5/S6 only abstract-checked; S6 not yet confirmed in ACM); (b) seeds S7–S13 are canonical papers whose abstracts contain B1 terms; `refinement` added to rescue S6 is seed-fitting; (c) few single-turn and LLM-era multi-turn seeds; (d) ICLR/NeurIPS/AAAI/IJCAI coverage untested (e.g., SCoRe ICLR 2021, R²SQL AAAI 2021 — to verify); (e) ACL dump entries without abstracts make the filter title-only; (f) DBLP step undefined. **Rec.:** independent quasi-gold standard (Zhang, Babar & Tell 2011) from hand-search/reference lists; per-database sensitivity; more seeds; OpenAlex or Semantic Scholar as supplementary source; title-only rule for abstract-less ACL records; define or drop DBLP step.
5. **AI-assisted screening validity insufficiently demonstrated; "independent" overstated** (`protocolo_es.md` §11). (a) Pilot stopping rule weak and overfits, no held-out set; (b) AI-consensus exclusions never audited by the human → unknown false-negative rate; (c) two instances of the same model are not independent raters; (d) automation/anchoring bias in AI-proposed quality and extraction; small calibration sets; (e) translated English criteria are an unversioned instrument. **Rec.:** held-out blind validation sample; blind human audit of a random sample (≥ 10 % or sized) of AI-consensus exclusions with estimated false-negative rate; human–AI agreement as primary reliability statistic; author scores/extracts 10–20 % independently before seeing AI output; second human if possible; version and back-check the English criteria; disclose model IDs, prompts, dates, override counts.
6. **Feasibility for one reviewer not checked against real counts** (`01_preguntas_picoc.md`, `pruebas_cadenas.md`, `protocolo_es.md` §9). OpenAlex-only estimates are a lower bound; the corpus may reach hundreds; snowballing is unbounded. **Rec.:** count-only queries per database now; pre-registered contingency rule if the corpus exceeds N; define snowballing (one iteration, forward only from included multi-turn studies, same criteria, PRISMA "other methods").
7. **Extraction form cannot support planned comparisons and degradation analysis** (`formulario_extraccion.md` Bloque 6, `plan_sintesis.md`). (a) No benchmark version field; (b) missing gold vs predicted interaction history, BIRD evidence on/off, number of candidates/self-consistency budget, model snapshot date; (c) SParC/CoSQL report turn "≥ 4"; (d) per-study slopes confounded by turn-bucket composition; (e) cross-study rewriting-vs-concatenation comparison invalid without within-study contrasts; no rule for which baseline defines Δ. **Rec.:** add `version`, `historial_eval` (GOLD/PREDICHO/NR), `conocimiento_externo`, `n_candidatos`, `fecha_modelo`, turn code `4+`, a within-study contrast sub-table; baseline rule (strongest same-base-model baseline); slopes only for predicted-history rows; add metric `TS`.
8. **Questions, vocabulary and gap narrative shaped by the thesis design (confirmation-bias risk)**. PI1–PI4 map 1:1 to SO1–SO4; `BIPARTITO_INTENCION_ESQUEMA` echoes the unfindable "ReDST" citation; §6 states as fact what rests on Yang et al.'s abstract; the blueprint contained fabricated citations; "stateful" title vs inclusion of stateless single-turn studies. Graph-based multi-turn state (IGSQL) and algorithmic joins (SchemaGraphSQL) already exist; the surviving gap may be only a conjunction. **Rec.:** read Yang et al. 2025 in full before registration and hedge §6; pre-register what would count against the thesis gap; mandatory reporting of inductive `OTRA` categories; neutral code names; retitle or justify "con estado".
9. **Quality threshold double-penalizes preprints and may drop key LLM-era multi-turn evidence** (`checklist_calidad.md`). CQ10 already scores preprints 0.5, then threshold 60 %; CQ3/CQ8/CQ10 score openness/venue, not validity; summed-score cut-offs are a known weakness (Jüni et al., 1999). **Rec.:** drop the separate preprint threshold (or drop CQ10 and rely on the preprint sensitivity analysis); base the threshold on validity items (CQ2, CQ4–CQ7); report per-item quality profiles.

### Minor Issues
- `01_preguntas_picoc.md` stale text (empirical-evaluation criterion "to decide in Phase 1"; header says draft).
- IC7 (≥ 4 pages) has no exclusion code; EX3 "demo" excludes peer-reviewed ACL/EMNLP demos without justification.
- Spanish admitted (IC6) but no Spanish strings or Spanish-language database — search or state "Spanish only if retrieved".
- Chinese-language literature excluded (EX2) — state as language-bias limitation.
- §17 confidence ratings not operationalized (suggest CERQual-like rules).
- `paradigma` codes not mutually exclusive — precedence rule or multi-coding.
- Cochran–Armitage test: partial 2026 and small early counts — state handling; consider exact/permutation version.
- PRISMA-P items missing: timeline, search-update plan, contact/registration placeholder.
- CQ10 "predatory" judgement needs named criteria/list.
- Clarify that single-turn B4 benchmarks enter via PI3/PI4 and are only also tabulated in PI5.

### Observations
- A two-tier design (systematic *mapping* of single-turn PI3/PI4 + in-depth *review* of multi-turn) would ease feasibility and clarify the single-turn role, consistent with D3.
- The DOI-error finding (S12 → *BioNLI*) and the discarded blueprint citations are worth reporting in Methods.
- Git history supports, but does not replace, registration.
- Report "not retrieved" counts by scenario; differential non-retrieval would bias D4.

### Strongest Counter-Argument
"The headline claim (multi-turn ≤ 30 %) is an artefact of an eligibility frame the author built; the qualitative 'gap' is a conjunction of existing components (graph-structured state, rewriting, algorithmic joins, execution-guided correction) chosen to match the thesis, scoped from a blueprint with fabricated citations; the evidence was screened by two instances of the same AI whose shared exclusions no human audited; and per-turn degradation figures mix gold- and predicted-history evaluations."

### What's Missing
Independent quasi-gold standard and per-database recall; human audit of AI-consensus exclusions and held-out pilot; pre-search counts and contingency rule; snowballing rules; extraction fields for history type, benchmark version, external knowledge, sampling budget, model date, within-study contrasts; coding rule for multi-turn PI3/PI4 and CI decision rule for D4; full reading of Yang et al. 2025; pre-stated disconfirmation criteria; mandatory OSF registration; coverage check for ICLR/NeurIPS/ICML/AAAI/IJCAI.

### Stress Test Results
| Test | Result |
|---|---|
| Remove strongest source | Partially — "no SLR on multi-turn Text-to-SQL" survives; "no review treats the pillars jointly" unverified until Yang et al. is read in full |
| Flip the question | Yes — multi-turn may be studied proportionately to its scope; no baseline for what ≤ 30 % means |
| Different context | No/Partially — D4 holds only within this frame; transfer to enterprise schemas weakly supported |
| "So what?" | Yes, conditionally — useful if the gap is stated narrowly and AI-screening validity is demonstrated |

---

## Ronda 1 de revisión (protocolo v1.1) — Veredicto: REVISE (acotado)
Concedidos con 5/5: M1, M9 y 9 de 10 menores. Con 4/5 (resueltos con residuos): M3, M6, M8. Mantenidos: M2 (4/5, aclaraciones tipo CoSQL), M4 (4/5, conjunto de referencia solo multiturno y parcialmente circular), **M5 (3/5, regla de auditoría con el denominador equivocado)**, **M7 (3/5, definición GOLD/PREDICHO errónea para SParC/CoSQL)**. Nuevo mayor **N1** (no se verificó la cobertura multiturno de las revisiones sistemáticas de 2026). Nuevos menores N2 (`chat*` captura «ChatGPT»), N3, N4, N5 (archivos sin commit), N6. La pausa por tasa de concesiones > 50 % se aplicó; el umbral subió a 5/5.

## Ronda 2 de revisión (protocolo v1.2) — Veredicto: **PASS** (condicionado a la lista previa al registro)
Concedidos con 5/5: M5, M2, M8a, M3/N2/N6, N1, N3/N4/§17. Con 4/5 (menores, no bloquean): M7 (estratificar `PREDICHO` y `SOLO_PREGUNTAS`; corregido tras el informe) y M4 (añadir una fuente pre-LLM al brazo de un turno; corregido tras el informe). Verificación de *frame-lock*: la crítica fue hecha por IA de la misma familia que el cribado → declararlo (añadido en §11c).

**Lista previa al registro OSF (Fase 1.8):** (1) correcciones menores de texto — hechas; (2) conteos reales por base; (3) lectura completa de Bui et al. 2026 y, si es posible, Yang et al. 2025; (4) `screening_protocol.md` en inglés y su contraste con el original; (5) construir el conjunto de referencia (ambos brazos) antes de las búsquedas oficiales; commit en git; (6) registro OSF citando el hash del commit; (7) declaración de que la crítica fue realizada por IA.
