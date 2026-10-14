# Devil's advocate report (seat `devil`)

## 1. Overall assessment

The manuscript is a careful, well-hedged mapping exercise. Its headline claims, though, rest on constructs the review built itself. The "considerably under-researched" verdict compares two arms with different eligibility rules and different extraction depth. The "reformulation criterion = 0" result is a three-way conjunction whose boundaries are drawn by the author's own thesis framing. The "modest positive, high-confidence" effects come from author-reported ablations, which are the stream most exposed to selective reporting. The extraction layer under all of this is AI-generated with modest agreement (73.6 %) and weak independent confirmation (3/5 on the key stratifier). Most hedges are present, but the abstract and conclusions still carry the stronger readings. I recommend **major revision**. Most fixes need only reanalysis and rewriting, not new data.

## 2. Comments

**Rdevil-1 · Major · IV-C, III-F, Abstract: the D4 verdict is a product of design, not evidence about the field**
- Problem:
  - D4 is the share of multi-turn studies in a population the review itself defined. Multi-turn studies enter with any of PI1–PI5 and any evaluation, including proprietary data. Single-turn studies enter only if schema linking or self-correction is central and a public benchmark is used (IC2/IC4). The manuscript concedes this "tiende a aumentar la proporción multiturno".
  - The 30 % threshold is never justified, and no reference share exists for what "adequately researched" would look like. The verdict is therefore a rule applied to a self-constructed ratio.
  - Single-turn search sensitivity was only 16/19 (about 84 %, with a wide interval), against 24/24 for multi-turn.
- Evidence: "la regla registrada arroja la conclusión «considerablemente menos investigado»"; the abstract repeats it as a result.
- Fix:
  - Justify the 30 % threshold, or state plainly that it is arbitrary.
  - Report D4 as a descriptive share only, not a verdict, in the abstract and conclusions.
  - Add a sensitivity that applies the same entry filters to both arms (for example, multi-turn restricted to PI3/PI4-central studies; Table V already uses 34/302 for this).
  - Report the sensitivity interval implied by the 16/19 single-turn recall.
- Confidence: 4/5 (design logic is visible in the text).
- Norm basis: PRISMA 2020 item 13e and Kitchenham both ask that conclusions follow from the evidence. I take this as a reporting norm, not a quantitative threshold norm.

**Rdevil-2 · Major · IV-I, IV-J (Table VIII), V-D: the single-turn vs multi-turn technique contrast is confounded by construction**
- Problem:
  - Single-turn studies are in the corpus *because* PI3/PI4 is central, so they contain more schema-linking and feedback techniques than a multi-turn arm that includes PI1/PI2-centred papers. That alone produces "retroalimentación de ejecución 13,0 % vs 31,6 %".
  - Level 1 (single-turn) was extracted from "las páginas iniciales", while Level 2 (multi-turn) used the full form. Unreported cells are therefore not comparable across arms. For example, only 93 of 313 single-turn studies have any join code, versus 57 of 77 multi-turn.
  - V-D nonetheless interprets the pattern: "la ambigüedad se aborda más mediante la interacción que mediante la ejecución".
- Evidence: "Este patrón sugiere que en el escenario conversacional la ambigüedad se aborda más mediante la interacción".
- Fix:
  - Recompute Table VIII percentages among PI3/PI4-central studies only, in both arms.
  - Show "no reportado" explicitly per row, so the extraction-depth asymmetry is visible.
  - Drop or heavily qualify the interpretive sentence.
- Confidence: 4/5.

**Rdevil-3 · Major · V-D, Abstract, VII: the "reformulation criterion = 0" result is close to guaranteed and is framed through the author's thesis**
- Problem:
  - The criterion needs at least 2 studies combining (a) explicit structured state, (b) algorithmic joins or execution self-correction, and (c) predicted or question-only history. The text admits that "un resultado nulo sobre una conjunción es evidencia débil".
  - The boundaries are drawn in the direction of the gap. Graph-based interaction encoders such as IGSQL are excluded from (a) ("como codificador neuronal no cuentan para (a)"). The "sensibilidad con grafos neuronales" is reported only in passing.
  - The elements mirror the thesis proposal ("Stateful Schema Grounding"). The conflict of interest is acknowledged, and the pre-registration mitigates it.
  - Yet "resultado nulo" is the seventh headline finding and sits in the abstract and conclusions.
- Evidence: "El número de estudios que reúnen los tres elementos es 0, y la sensibilidad prevista con grafos neuronales tampoco identificó ninguno."
- Fix:
  - Report the full 2×2×2 cross-tabulation of (a)/(b)/(c) with the pairs already computed (8, 7, 1).
  - Report the result under alternative operationalizations of (a), including neural graph state.
  - Move the finding out of the abstract headline, or present it as "no study combines X; pairs exist".
  - Make explicit which definitions were fixed in the registered protocol and which were set at extraction.
- Confidence: 4/5.

**Rdevil-4 · Major · IV-F, VI-B: the effect synthesis is rated "alta" confidence despite acknowledged reporting bias and heterogeneity**
- Problem:
  - Within-study contrasts come from ablations authors run to justify their own components. Nine of the twelve classes are rated "alta", including the heterogeneous "otros componentes" buckets (e.g., 17 studies, range −0.2 to 25.0 pp).
  - The confidence rule is home-made and unvalidated, as the manuscript says.
  - It also conflicts with the quality profile: only 14/77 studies describe the technique reproducibly (CQ2), and only 19/77 report metric and history (CQ5).
  - The statement "Ninguna clase registra estudios con efecto nulo" sits beside Table VI ranges starting at 0,0 and the paper's own "no se registran nulos" caveat. The "+/−/0" column reports zero null studies in every class.
  - A near-universal positive direction (the +/−/0 counts are almost all +) is the signature of selective ablation reporting, not evidence of general efficacy.
- Evidence: "La confianza en el hallazgo es alta para las clases «otros componentes» de los cuatro pilares".
- Fix:
  - Cap confidence at "moderada" wherever the class is heterogeneous or the sole source is author-run ablations.
  - Add a downgrade for reporting bias, per CERQual's own "adequacy" logic.
  - Add a funnel-style or small-study check even without meta-analysis (e.g., direction vs study size or venue level).
  - Rewrite "modest positive effects" as "authors' ablations rarely report harm".
- Confidence: 4/5.

**Rdevil-5 · Major · III-E, III-F, VI-B, Table IV: AI-generated screening and extraction are verified too weakly to carry the "not reported" findings**
- Problem:
  - Reviewers A and B share a model family, which the paper concedes. The human validation uses one 60-record sample that served as both pilot and validation, with no held-out set.
  - Extraction agreement is 73.6 % (Level 2) and 86.9 % (Level 1). The author's blind sample on the key variable (history type) matched only 3/5.
  - The author's verification covered values the AI already agreed on (182/182, 32/32, 95/95). A 100 % confirmation rate on pre-agreed values is weak evidence of accuracy and may reflect automation bias.
  - Yet the central PI1/PI2/PI5 findings are shares of "no reportado" (34.7 %, 63.9 %, 27.8 %), and the manuscript admits these could be extraction artefacts ("una fracción de los valores no reportados podría deberse a la extracción asistida por IA").
  - PRISMA 2020 items 8–9 require reporting how many reviewers worked independently and what automation was used. The manuscript discloses this but offers no estimate of how large the error is.
- Evidence: "una muestra aleatoria de los valores concordantes del Nivel 2 (182/182 confirmados sin cambios)".
- Fix:
  - Report the author's verification on the *discordant* cells and on a random sample regardless of agreement. Report error rates per field with intervals.
  - For "no reportado" figures, give a bounded range (for example, re-check a random sample of unreported cells against the PDF).
  - Phrase the "not reported" findings as "not extracted" unless validated.
- Confidence: 5/5.

**Rdevil-6 · Major · IV-K, V-B (Table IX, Fig. 7): the degradation analysis cannot support the interpretation attached to it**
- Problem:
  - The only gold-vs-predicted claim ("plausible... sobreestime la robustez") has no data behind it, since there are zero gold curves.
  - The data run against the expectation. The predicted-history stratum (error propagation) degrades *less* (−7.0 pp/turn, 6 curves from 5 studies) than the question-only stratum (−11.0 pp/turn, 8 curves from 6 studies). This is not discussed.
  - Stratum assignment is unreliable: the author's independent check agreed on 3/5, and two discrepancies were found in the sample (SUQL, DIR).
  - Fig. 7 normalizes to turn 1 on an axis reaching 140 %, which indicates later turns are sometimes *easier*. The paper itself says the slope mixes depth with difficulty.
  - V-B still juxtaposes −7/−11 pp per turn with +2–3 pp component effects to conclude the latter are "pequeña".
- Evidence: "la magnitud de estos efectos, de pocos puntos porcentuales, resulta pequeña al yuxtaponerla con las pendientes medianas de degradación".
- Fix:
  - Remove the effect-size juxtaposition, or restrict it to studies reporting both quantities.
  - Discuss the counter-intuitive ordering.
  - Report slopes with their range and n, and flag the stratum assignment as unreliable.
  - Treat the gold-history claim as speculation.
- Confidence: 4/5.

**Rdevil-7 · Major · III-A, III-D, Table II, VI-A: protocol integrity and the circular search-sensitivity check**
- Problem:
  - The paper presents a "frozen, pre-registered" protocol, but A4–A6 were made after the search and are not yet in OSF. A5 changes screening models, extraction design and adds a snowballing supplement. A6 adds unregistered analyses.
  - The search-sensitivity figure (24/24 multi-turn) uses a reference set whose eligibility the AI determined (A1), and which derives from the author's seed studies. This is circular, as VI-A partly admits, but the Wilson lower bound (86.2 %) is still quoted as a strength.
  - The baseline for the multi-turn recall figure is the author's own list, so it cannot detect systematic blind spots.
- Evidence: "La búsqueda recuperó 24 de 24 estudios multiturno del conjunto de referencia (límite inferior de Wilson de 86,2 %)".
- Fix:
  - Update OSF with A4–A6 before circulating the manuscript, as the text itself promises.
  - Add a table that separates what was pre-registered from what was added.
  - Report the sensitivity using an independent reference set (e.g., references of the two closest surveys, or studies found only via snowballing).
  - Label the 86.2 % as an upper bound on true sensitivity.
- Confidence: 4/5.
- Norm basis: PRISMA 2020 item 24 (registration and protocol amendments) and PRISMA-S.

**Rdevil-8 · Minor · V-D (gaps list): gaps are "ranked by evidential solidity" with no stated rule, and two are artefacts of the review's own design**
- Problem:
  - Gap 4 (Spanish-language data: 3 of 390) follows from IC6 and the English-only search strings. The review states "no hay cadena específica en español", so the scarcity is partly manufactured.
  - Gap 6 repeats the thesis hypothesis.
  - The ordering criteria are not given.
- Evidence: "ordenadas de mayor a menor solidez de la evidencia que las sustenta".
- Fix:
  - State the ranking rule, or drop the ranking.
  - Mark gap 4 as "not testable with this search".
- Confidence: 4/5.

**Rdevil-9 · Minor · Table IV, III-F, IV-E, IV-B, Fig. 5: unexplained numerical inconsistencies**
- Problem:
  - Table IV reports Level 1 extraction n = 317 and Level 2 n = 78, but the text counts 313 single-turn and 77 multi-turn studies. The snowballing uses "78 estudios semilla".
  - IV-B lists 146 preprints + 91 CORE A* + 34 Q1 = 271 of 390, with no category for the remaining 119.
  - The Fig. 5 caption repeats "(a)" with two meanings.
  - Table III names codes EXn while Fig. 2 uses En.
- Evidence: "Extracción, Nivel 1 317"; "los 390 estudios... 77 son multiturno y 313 son de un turno".
- Fix: reconcile or explain each count (one sentence each). Fix the caption and code labels.
- Confidence: 5/5.

**Rdevil-10 · Minor · IV-C, V-B: the partial year 2026 is excluded exactly where the share is lowest**
- Problem:
  - 2026 holds 139/390 studies (36 % of the corpus) but only 7/122 (5.7 %) in D4. This is the lowest annual share and is set aside as "parcial".
  - A partial year biases counts, not proportions, so the exclusion is not self-evidently justified. The conclusion "los datos no respaldan... que la diferencia se esté reduciendo" is therefore stated cautiously, but the 2026 point arguably suggests widening.
- Evidence: "El año 2026, parcial y fuera de la prueba, registra 7 de 122 estudios (5,7 %)".
- Fix: add a sensitivity trend test including 2026 and discuss whether the LLM/agent shift explains the drop.
- Confidence: 3/5 (the original exclusion may be pre-registered).

**Rdevil-11 · Minor · III-G, IV-E: the quality appraisal filters almost nothing and covers only one arm**
- Problem:
  - The 50 % validity threshold excludes 5 of 77 studies, so "quality" hardly shapes the synthesis. The scores were AI-proposed with 75.6 % agreement and calibrated on 5 studies.
  - The 313 single-turn studies, which serve as the comparison set, receive no appraisal at all.
- Evidence: "72 alcanzan el umbral de validez del 50 % y 5 quedan por debajo".
- Fix: justify the threshold. State that single-turn contrasts are unappraised and limit the claims accordingly.
- Confidence: 4/5.

**Rdevil-12 · Minor · Abstract, II, Reference list, front matter: novelty and completeness**
- Problem:
  - Seven of ten related reviews were checked only on abstracts. The novelty claim ("no se identificó una revisión...") rests on them, including the closest one, [10].
  - Placeholders remain in the text: [PENDIENTE: cita...], [PENDIENTE: enlace público], and the AI-use declaration.
  - The supplement (strings, criteria, per-study tables), on which the PRISMA-S claims depend, is not attached.
  - Reference artefacts remain: "Metadatos de OpenAlex W…", "(C1)", "(C4)", and a malformed author in [22].
- Evidence: "[PENDIENTE: cita: propagación de errores entre turnos en Text-to-SQL multiturno]".
- Fix:
  - Obtain the full text of [10] or soften the novelty claim.
  - Resolve every placeholder.
  - Attach the supplement.
  - Clean the reference entries.
- Confidence: 5/5.

## 3. What the manuscript does well

- It consistently separates what the data show from what they do not ("brechas de cobertura, no necesidades"). It pre-states a null-result rule and reports it regardless of outcome.
- It stratifies degradation by evaluation-history type and refuses to pool slopes across strata. It also reports sensitivity analyses (without preprints, with sub-threshold studies, with unretrieved reports).
- PRISMA flow numbers reconcile (349 + 41 = 390; 431 − 82 = 349; 58 − 17 = 41), and the limitations are candidly stated (same-family AI reviewers, single author, unretrieved reports, conflict of interest).
- The related-work table states which text each descriptor was verified against (abstract vs full text), which is an unusually honest provenance practice.