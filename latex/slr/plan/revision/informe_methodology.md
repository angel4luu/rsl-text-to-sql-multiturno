## Methodology review (seat `methodology`)

### 1. Overall assessment

This is an unusually transparent PRISMA 2020 review. It has a registered protocol, pre-specified decision rules (D4, the reformulation criterion), a reconciled PRISMA flow and honest limitation sections. However, the headline claims rest on an asymmetric eligibility framework and an AI-only screening and extraction pipeline. That pipeline was validated with very small human samples, and no recall estimate is reported. Several comparisons (single-turn vs multi-turn technique frequencies, "high-confidence" component effects, the "zero" reformulation result) are not interpretable as stated. The prose already hedges many of these points, but the abstract, Table VI and Table VIII carry the stronger version. Most problems are repairable by reanalysis of existing data and rewriting. **Recommendation: major revision.**

### 2. Comments

**RM-1 (Major) — IV-I/IV-J, Table VIII, V-B: the single-turn vs multi-turn comparison is confounded by selection and by extraction depth**
- **Problem 1, selection.** Single-turn studies entered the corpus only if PI3/PI4 was their *central* contribution (IC2, EX6). The multi-turn arm is a census of any PI1–PI5 study. Frequencies of PI3/PI4 techniques are therefore higher in the single-turn arm by construction.
- **Problem 2, measurement depth.** Multi-turn studies (Level 2) received the full extraction form. Single-turn studies (Level 1) were coded from the first pages only, with Sonnet/Sonnet agreement.
- **Evidence:** "Su base son todos los estudios del Nivel 2 (77) y del Nivel 1 de un turno (313)". Execution feedback appears in 13.0 % of multi-turn studies and 31.6 % of single-turn. Implicit joins appear in 71.4 % of multi-turn and 22.7 % of single-turn. The text then reads this as "la ambigüedad se aborda más mediante la interacción que mediante la ejecución".
- **Fix:**
  - Restrict the multi-turn arm to studies with PI3/PI4 as a central pillar (13 and 22 studies) so both arms share the same selection rule.
  - Show "no reportado" rows for both arms.
  - State that Level 1 coding depth differs.
  - Drop or heavily qualify the interaction-vs-execution interpretation.
  - Add a Table VIII note: "no comparable sin igualar la selección".

**RM-2 (Major) — Abstract, III-G, IV-C, V-B: D4 and its "considerablemente menos investigado" label are weaker than they look**
- **Problem 1, asymmetric eligibility.** IC4 admits any evaluation (including proprietary data) for multi-turn but requires a public benchmark for single-turn. This pushes D4 in a direction the paper does not quantify.
- **Problem 2, threshold.** The 30 % threshold has no stated justification.
- **Problem 3, classification reliability.** D4 membership depends on a partly subjective judgement of "contribución central" from title and abstract. No agreement statistic is reported for that field, only overall extraction agreement (86.9 %).
- **Problem 4, the confidence interval.** The Wilson CI treats a census as a binomial sample and reflects neither misclassification nor search or retrieval error, which dominate the uncertainty.
- **Problem 5, reading.** The abstract's "considerablemente menos investigado" reads as a finding about the field despite the caveats in V-B.
- **Evidence:** "se concluye que el escenario es considerablemente menos investigado solo si el límite superior es de a lo sumo 30 %".
- **Fix:**
  - Justify the 30 % threshold, or present D4 only as a descriptive proportion with sensitivity analyses.
  - Report agreement (κ) on the D4-defining field from the existing double extraction.
  - Reword the abstract to "D4 = 11.3 % *dentro del marco de elegibilidad*".
  - Add a sentence saying the interval quantifies only sampling error.

**RM-3 (Major) — III-E, VI-A, Table IV: the AI screening and extraction pipeline is not validated well enough to support a recall claim**
- **Problem 1, correlated reviewers.** Reviewers A and B share a model family and the tiebreaker is another Claude model. Human validation covered 60 records (28 advanced) with no held-out sample. Human review covered only the non-obvious cases.
- **Problem 2, missed exclusions.** The blind re-read of joint exclusions (401 records) rescued 38 records, of which 14 were finally included. That is about 3.5 % of the sample. The paper never extrapolates this to the joint exclusions that were not re-read, nor states their total.
- **Problem 3, extraction.** Double-extraction agreement is 73.6 % (Level 2) with no per-field κ. The 182/182 and 95/95 checks sample *concordant* values, which cannot detect shared errors. The only fully independent check (5 studies) matched on the evaluation history in 3 of 5 (60 %). That field defines the PI5 strata.
- **Problem 4, reproducibility.** Prompts, model versions and temperature are in the supplement, which is not attached.
- **Evidence:** "el historial coincidió en 3 de 5 estudios (60,0 %)" and "pueden persistir omisiones no detectadas".
- **Fix:**
  - From the existing logs, report the number of unreviewed joint exclusions.
  - Extrapolate the rescue rate (with CI) to give an expected count of missed includes.
  - Give per-field κ or PABAK for the key extraction fields.
  - Present the PI5 stratification (Table IX) explicitly as conditional on a coding that was independently verified in only 3 of 5 cases.
  - Include prompts and settings in an appendix.

**RM-4 (Major) — IV-F, Table VI, V-B: effect synthesis relies on vote counting and cross-metric medians, and "alta" confidence is not credible**
- **Problem 1, mixed configurations.** Section III-H says only values within the same configuration are compared. Table VI then takes medians of pp differences across studies that use different benchmarks, metrics (EX, QM, IM) and histories.
- **Problem 2, clustering and unweighted votes.** Contrasts are clustered within studies (141 contrasts for 11 studies). Study direction is an unweighted vote count with no precision.
- **Problem 3, null effects.** The "Est. +/−/0" column always shows 0 nulls, and the text says "Ninguna clase registra estudios con efecto nulo". Yet the autocorrection range starts at 0,0 and others at −0,1/0,2. Either nulls were recoded or not extracted. This needs explaining.
- **Problem 4, confidence labels.** The CERQual-inspired rules are unvalidated. CERQual is designed for qualitative evidence, and the paper itself concedes that reporting bias inflates effects. Even so, 8 of 12 classes are labelled "alta".
- **Evidence:** "Ninguna clase registra estudios con efecto nulo"; ranges "0,3 a 33,2" and "0,5 a 32,0"; "Confianza: alta".
- **Fix:**
  - Report the threshold used to call a contrast null.
  - Report the share of nulls.
  - Drop cross-study medians from the main table, or label them explicitly as descriptive and cross-metric.
  - Rename "confianza" to "consistencia de la dirección" and downgrade by default for reporting bias (a GRADE-style rule).
  - Put the rules in an appendix.

**RM-5 (Major) — III-H, IV-C, VI: the exclusion of 2026 from the trend test is not justified for a proportion**
- **Problem:** Truncation of the year affects counts, not proportions, unless indexing lag differs by scenario. 2026 is the largest year (139 of 390) and has the *lowest* proportion (7/122 = 5.7 %). Excluding it removes the only evidence of a possible decline and underlies "no se detectó tendencia (p = 0,95)".
- **Evidence:** "2026 se reporta aparte por ser un año parcial".
- **Fix:**
  - Run the Cochran–Armitage test including 2026 as a sensitivity analysis and report both.
  - State whether indexing lag could differ by scenario.
  - Keep the "low power" caveat, but drop wording that implies stability.

**RM-6 (Major) — V-D, Abstract, VII: the "0 studies" reformulation result is uninformative as presented**
- **Problem 1, no null model.** The text gives (a) 14, (b) 13, (c) 46, (a)∩(c) 8, (b)∩(c) 7, (a)∩(b) 1, out of 77. Under independence the expected overlaps are about 8.4, 7.8 and 2.4. The observed pair counts match chance, and the (a)∩(b) count of 1 is not clearly below 2.4. So the data do not show that the combination is avoided. They show only low base rates.
- **Problem 2, hard to falsify.** The text itself concedes that "cuanto más específica es la combinación... menos probable es que un estudio la reúna". The registered criterion ("al menos 2 estudios") is close to unfalsifiable for a triple conjunction in 77 studies.
- **Problem 3, thesis-derived.** The criterion comes from the author's thesis gap, as the conflict-of-interest statement acknowledges.
- **Evidence:** "El número de estudios que reúnen los tres elementos es 0" (abstract headline).
- **Fix:**
  - Add expected-under-independence counts and an exact test (or at least the expected counts).
  - Present the null as "consistente con baja prevalencia conjunta".
  - Remove "0" as an abstract headline.
  - Justify the ≥ 2 threshold, or admit it is a weak test.

**RM-7 (Major) — III-D, IV-A, IV-C, V-D: unretrieved reports (about 28 % in the database arm) are handled only through one crude bound**
- **Problem 1, scale.** 164 of 595 reports (27.6 %) were not retrieved. In total 191 are unretrieved, of which 43 have a multi-turn signal (22.5 %). The retrieval failure is plausibly correlated with publisher and scenario.
- **Problem 2, the bound.** The D4 bound (77/493, upper limit 19.1 %) puts all 43 in the numerator and all 191 in the denominator. That is conservative for D4 but arbitrary, and it has no registered rule. Its numerator (34 + 43 = 77) coincides with the total multi-turn count, which confuses readers.
- **Problem 3, "signal".** How the single/multi signal was determined for unretrieved reports is not described.
- **Evidence:** "Los informes no recuperados fueron 164 en el brazo de bases y 27 en el de otros métodos".
- **Fix:**
  - Describe how the signal was determined.
  - Add a second, probabilistic bound (for example, applying the retrieved reports' observed rates of PI3/PI4-centrality).
  - Rename the bound to avoid the 77 coincidence.
  - Report retrieval rates by source and publisher.

**RM-8 (Major) — III-D, III-A, VI-A: search strategy and its sensitivity check are not independently verifiable**
- **Problem 1, circular reference set.** The sensitivity check used a reference set whose eligibility was decided by the same AI (A1). The set comes from the author's thesis context (the repository treats it as seed studies). The single-turn estimate (16/19 = 84 %) has a very wide CI, which is not given. The lower Wilson bound is about 62 %.
- **Problem 2, source handling.** ACM was captured from saved HTML pages with no date filter. arXiv was queried by API with a local filter on category and string. Neither is reproducible as a "search string" in the PRISMA-S sense.
- **Problem 3, missing material.** The exact search strings are absent from the manuscript ("se incluyen en el material suplementario"). The supplement is not attached.
- **Problem 4, source choice.** DBLP is used for related work but not as a source for a CS-centred review.
- **Evidence:** "16 de 19 estudios de un turno".
- **Fix:**
  - Put the strings in an appendix or a stable repository and cite it.
  - Report the CI for 16/19.
  - Describe how the reference set was assembled and by whom.
  - Justify omitting DBLP or Web of Science, or list it as a limitation.

**RM-9 (Major) — III-A, Table II, VI-A: protocol amendments after registration and registration timing**
- **Problem 1, amendments.** A4–A6 are not updated in OSF. A5 changes much of the pipeline (reviewer models, extracts instead of full text, AI-only double extraction, an extra snowballing source). All six amendments are dated 2026-10-11 to 2026-10-13, the same days as the search, screening and analysis.
- **Problem 2, timing.** Registration is dated 2026-10-11, the same day as the search. The article asserts registration "antes de la búsqueda oficial" with no timestamps.
- **Problem 3, data dependence.** The paper does not say whether each amendment was made before the relevant outcome data (D4, effects) were seen. A4 added a D4 sensitivity after the retrieval failures were known.
- **Evidence:** "La actualización de las enmiendas A4–A6 en OSF queda pendiente".
- **Fix:**
  - Update OSF before circulating the manuscript.
  - Add a column to Table II stating the data state at the time of each amendment (before or after seeing outcome data).
  - Give the OSF timestamps for registration versus the search.
  - Label A4's sensitivity as post hoc.

**RM-10 (Minor) — III-G, IV-E: the quality appraisal barely discriminates**
- **Problem 1, little discrimination.** The 50 % validity threshold excludes only 5 of 77 studies (median 70 %). The 5 "validity" items include reproducibility (CQ2, full in 18.2 %) and metrics/history reporting (CQ5, full in 24.7 %), which are reporting items.
- **Problem 2, scope and rater.** Quality was appraised for Level 2 only, so the 313 single-turn studies used in the contrasts have no appraisal. Scores were proposed by AI, with 75.6 % agreement.
- **Evidence:** "72 alcanzan el umbral de validez del 50 % y 5 quedan por debajo".
- **Fix:**
  - Justify the 50 % cut-off.
  - Move CQ2 and CQ5 to the reporting profile, or explain why they are validity items.
  - State that Level 1 studies were not appraised.
  - Use the sensitivity already run (reincorporating the 5) as the primary reading.

**RM-11 (Minor) — IV-A, Table IV, V-D and others: denominators are inconsistent across sections**
- **Problem 1, counts.** Table IV gives extraction n = 317 (Level 1) and 78 (Level 2) and quality n = 78. The text gives 313 and 77, which total 390. 317 + 78 = 395.
- **Problem 2, denominators.** Sections move among 77 (Level 2), 72 (above the validity threshold) and 78 (seeds) without always saying why. For example, V-D uses 77 and IV-F uses 72.
- **Problem 3, unfinished items.** The manuscript contains unfinished items ("[PENDIENTE: cita...]", "[PENDIENTE: enlace público del repositorio]", "[PENDIENTE: declaración completa...]") and internal annotations in reference entries ("Sin DOI; verificada por la autora (C1)").
- **Evidence:** "Extracción, Nivel 1 317"; "Calidad, Nivel 2 78".
- **Fix:**
  - Reconcile the counts.
  - Add a sentence for each denominator change.
  - Complete the pending items before any submission.
  - Remove internal notes from the reference list.

**RM-12 (Minor) — IV-K, Fig. 7, Table IX, V-B: the degradation evidence is thin and its comparison with the effect sizes is overinterpreted**
- **Problem 1, small k.** The strata have 5 and 6 studies (6 and 8 curves) and use only studies that report curves. The slope mixes turn depth and question difficulty, as the authors acknowledge.
- **Problem 2, scales.** The text juxtaposes slopes of −7.0 and −11.0 pp per turn with effects of a few pp, which come from different metrics and designs. The Fig. 7 axis runs above 100 % for accuracy relative to turn 1.
- **Evidence:** "pequeña al yuxtaponerla con las pendientes medianas de degradación".
- **Fix:**
  - Report ranges or IQRs per stratum in the text.
  - Remove or tone down the juxtaposition in V-B.
  - Explain the >100 % normalised values.
  - Use decimal commas consistently (the figure uses "-7.0").

### 3. What the manuscript does well

- **Pre-specified rules reported either way.** The D4 rule and the reformulation criterion were set in advance and reported regardless of result. Limitation sections (V-B, VI) are candid, for example about single-author work, AI reviewers from one family, and the "evidence is not a necessity" wording.
- **Mostly reconcilable PRISMA flow and arithmetic.** Counts reconcile for the database arm, which I rechecked: 1596 − 555 = 1041, 1041 − 446 = 595, 595 − 164 = 431, 431 − 82 = 349. The snowballing arm reconciles too, and D4 and the Wilson intervals recompute correctly (34/302 → 8.2–15.3 %).
- **Sensitivity analyses and stratification.** There are six D4 sensitivity analyses and several effect-synthesis sensitivities (without preprints, with the sub-threshold studies reincorporated, with the unretrieved bound). Degradation is stratified by evaluation history and never pooled.
- **Disclosed AI use with human checks and diagnostics.** The paper discloses AI use by phase, reports agreement (κ, PABAK) as a diagnostic rather than as independent-reviewer agreement, and includes a blind author-labelled sample.