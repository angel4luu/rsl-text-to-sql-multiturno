# Task: anti-bias refactor of the interpretive layer of a PRISMA 2020 SLR article (Spanish)

You act as the ARS `draft_writer_agent` in revision mode. Read
`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/draft_writer_agent.md`
and `.../academic-paper/references/academic_writing_style.md` (same root). The rules below override them.
Paths are relative to the repo root. Read only.

## Why this revision
The author asked for an honest audit: the review must not read as built to justify her planned thesis. Verified facts:
1. The research questions PI1–PI4 were derived from the author's prior thesis proposal (they map 1:1 to its
   objectives). The protocol's own devil's-advocate critique flagged this as a confirmation-bias risk
   (`slr/protocolo/04_critica_abogado_diablo_cp1.md`, item 8: «the surviving gap may be only a conjunction»). The
   article does not disclose it.
2. M8 was registered as a **falsification / reformulation rule** («qué contaría en contra de la brecha de la tesis»:
   reformulate the thesis if ≥ 2 Level-2 studies already combine (a)+(b)+(c); `slr/protocolo/01_preguntas_picoc.md`).
   Its null result (\nBrechaMocho) only shows the **combination was not found in the corpus**; it says nothing about
   necessity, value or effectiveness. New counts over the \nMultiturno{} Level-2 studies: (a) explicit structured state
   \nMochoA, (b) algorithmic joins or execution-based correction \nMochoB, (c) predicted / questions-only history
   \nMochoC; pairs a+c \nMochoAC, b+c \nMochoBC, a+b \nMochoAB; triple \nBrechaMocho. So each component exists and most
   pairs exist; what is nearly absent is (a) together with (b). Components also exist separately in the literature
   (graph interaction state \cite{Cai2020IGSQL}; non-implicit join inference in multi-turn \cite{Dou2023UniSAr,Wang2020PGGSQL};
   algorithmic join paths in single-turn \cite{Safdarian2026SchemaGraphSQL}).
3. The research agenda in V-D lists, in the thesis's own order, the thesis's own five components. Rarity is not need:
   the review itself cannot tell whether implicit join inference is insufficient. Gaps supported by the data but not
   aligned with the thesis are missing: user clarification/interaction is proportionally far more frequent in multi-turn
   (ACLARACION_USUARIO and signal USUARIO in `slr/sintesis/tablas/pi34_tecnicas_escenario.csv`) — an alternative route;
   only \nDatasetES{} of \nEstudios{} included studies evaluate on Spanish data (\nDatasetEN{} English, \nDatasetZH{} Chinese);
   benchmark contamination is rarely discussed (`slr/sintesis/tablas/pi5_historial.csv`, contaminacion_discutida);
   reporting is weak (non-reported values; quality items CQ2, CQ5 in `slr/sintesis/CALIDAD.md`).

## Files to rewrite (return each COMPLETE file; change ONLY the passages listed; keep every other sentence, macro,
## comment, label, \input and «% fuente:» line verbatim)
1. `06-amenazas-validez.tex` — in `sec:am-seleccion` add one paragraph (construct validity): the questions and taxonomy
   derive from the author's thesis proposal, risk of privileging those components; mitigations actually applied (the
   multi-turn arm was not restricted to the pillars — any of PI1–PI5 qualified; inductive «otros» classes and OTRA codes
   reported; M8 pre-registered as a reformulation rule and reported regardless of outcome; conflict of interest declared);
   residual risk (categories and agenda may still be framed by the proposal). Also replace «criterio de brecha» wording if present.
2. `05-discusion.tex` —
   - In `sec:dis-hallazgos`, the seventh finding: say no study met the pre-specified **reformulation criterion**, and
     that the null result reflects mainly the near-absence of (a)+(b) (macros above), not that the components are absent.
   - Rewrite the first paragraph of `sec:dis-brecha` (keep the label; retitle the subsection «Criterio de reformulación y
     brechas de cobertura»): what M8 tested (novelty of a conjunction, registered as what would count against the thesis
     gap); the component and pair counts; why a null conjunction is weak evidence (conjunctions of specific features are
     rarely satisfied); it says nothing about necessity or effectiveness; the three conditional reasons already in the
     text (coding, non-retrieved reports, extraction agreement) stay.
   - Rewrite the agenda as «brechas de cobertura observadas», **ordered by strength of evidence, not by the thesis**,
     each item stating what the evidence shows and what it cannot show. Include: evaluation with predicted history and
     per-turn reporting (strongest: data on reporting); weak reporting (NR, CQ2/CQ5); Spanish and multilingual data;
     user clarification/interaction as an under-compared alternative route; the near-absence of structured state combined
     with algorithmic joins or execution feedback (rarity, not demonstrated need); training-free work not characterized
     by scenario; contamination. 6–8 items, enumerate.
   - Keep the conflict-of-interest silence (D5): do not mention the thesis in the body.
3. `00-resumen.tex` — in both the Spanish and English abstracts, change only the sentence about the gap criterion and the
   conclusion sentence that lists gaps, so they match the new V-D (reformulation criterion; coverage gaps, not needs;
   include Spanish data and evaluation practice). Keep length within ±15 words.
4. `07-conclusiones.tex` — align the gap paragraph and the future-work sentence with the new agenda.
5. `01-introduccion.tex` — the fifth contribution: «la evaluación de un criterio pre-especificado de reformulación, que
   examina si la combinación … ya se había evaluado».

## Hard rules
- Numbers only as macros (listed above and in `latex/slr/numeros.tex`) or copied from a source with `% fuente: <file>`.
- Cite only keys in `latex/slr/plan/claves_permitidas_4a.txt` or `bib/claves_estudios.csv`.
- Spanish, impersonal «se» + third person; no first person; no «demuestra», «prueba que», «garantiza».
- Honest but not self-flagellating: the descriptive results stand; the change is in what they are said to imply.

## Output (ONLY this, no preamble, no Markdown fences)
```
%%%% FILE: 06-amenazas-validez.tex
...
%%%% FILE: 05-discusion.tex
...
%%%% FILE: 00-resumen.tex
...
%%%% FILE: 07-conclusiones.tex
...
%%%% FILE: 01-introduccion.tex
...
```
