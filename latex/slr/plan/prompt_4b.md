# Task: draft section 3 (Método) of a PRISMA 2020 SLR article

You act as the ARS `draft_writer_agent`. First read its instructions:
`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/draft_writer_agent.md`
and `.../academic-paper/references/academic_writing_style.md` (same root). The hard rules below override them.
Paths are relative to the repo root (your working directory). Read only.

## Article and style
Systematic review (Kitchenham & Charters; reported per PRISMA 2020) on schema grounding in multi-turn Text-to-SQL,
for IEEE Latin America Transactions. **Spanish**, formal register, impersonal "se" + third person (never first-person plural; the author is «la autora»); English terms
in `\en{...}` on first use; IEEE citations `\cite{key}`. Sections 1–2 are already written: read
`latex/slr/secciones/01-introduccion.tex` for tone and to avoid repeating the questions (refer to them as PI0–PI5).

## Read
1. Outline `latex/slr/plan/esquema_articulo.md`: §0 «Decisiones tomadas», §1 rows 3.1–3.8 (purpose, PRISMA items,
   words, labels), §2.2 rows `tab:enmiendas` and `tab:ia`, §7.1 (PRISMA items 5–15, 24).
2. Protocol: `slr/protocolo/protocolo_es.md`, `slr/protocolo/01_preguntas_picoc.md`,
   `slr/protocolo/03_criterios_elegibilidad.md`, `slr/protocolo/enmiendas.md` (A1–A6; A4–A6 «Pendiente» in OSF).
3. Search: `slr/busqueda/registro_busquedas.csv` (rows marked OFICIAL), `slr/cribado/prisma_identificacion.json`.
4. Screening, for the *procedure only*: `slr/cribado/Screening_TA/TA_methods_selection.md` and
   `slr/cribado/Screening_FT/FT_methods_selection.md`. **Their numbers are stale or wrong (written before QC ran) and
   their `[TO COMPLETE]` passages must not be reproduced; take every number from the macros.**
5. Extraction and quality: `slr/extraccion/formulario_extraccion.md`, `slr/extraccion/informe_acuerdo_extraccion.md`
   (procedure), `slr/calidad/checklist_calidad.md`.
6. Synthesis: `slr/sintesis/plan_sintesis.md`.
7. Tables already generated (insert with `\input`, refer with `\cref`): `latex/slr/tablas/enmiendas.tex`
   (`tab:enmiendas`) and `latex/slr/tablas/ia.tex` (`tab:ia`). Read them so the text does not repeat their numbers.
8. Number macros: `latex/slr/numeros.tex` (read every line; the comment-free names are self-explanatory, and
   `slr/sintesis/cifras_metodo.json` shows what each Methods value means). Allowed keys: `latex/slr/plan/claves_permitidas_4a.txt`.

## Facts to report (all numbers via macros)
- Protocol PRISMA-P registered in OSF before the official search~\cite{OSF2026Protocolo}; amendments A1–A6 in
  \cref{tab:enmiendas}; A4–A6 will be updated in OSF before submission.
- Search: \nBases{} sources (Scopus, IEEE Xplore, ACM DL, ACL Anthology, arXiv), date \fechaBusqueda, per-source
  counts (\nBaseScopus …), capture method for ACM (A2) and arXiv (API + local filter); full strings go to the
  supplement (say «material suplementario»). Duplicates removed before screening: \nDupVersiones (versions of the
  same study), \nDupDOI (wrong DOI), \nDupHerramienta (tool, DOI or title+year). Search sensitivity against the
  reference set (A1): multi-turn \nRefMTHallados/\nRefMT (Wilson lower bound \refMTICinf~\%), single-turn
  \nRefUTHallados/\nRefUT. Snowballing (backward and forward) with OpenAlex~\cite{Priem2022OpenAlex} from
  \nBolaSemillas seed studies (\nBolaCandOA candidates), supplemented with Semantic Scholar for \nBolaSemillasSS seeds
  without OpenAlex references (\nBolaSemillasSSrefs with references; \nBolaCandSS candidates)~\cite{Wohlin2014Snowballing}.
- Selection: sr-screener (Academic Research Skills), two blinded AI reviewers (Claude Sonnet) with different personas,
  third AI reviewer (Claude Opus) for conflicts; the author reviewed all non-obvious cases (A3) and decided
  \nAutoraTR records at title/abstract and \nAutoraTC at full text. Blind pilot/validation sample of \nPiloto records
  labelled by the author before the AI (A3): the author advanced \nPilotoAvanzaAutora; the AI missed
  \nPilotoOmitidosIA; $\kappa$ = \pilotoKappa. Conflicts: \nConflictosTR (title/abstract), \nConflictosTC (full text,
  \nAdjTC resolved by the adjudicator). QC of joint exclusions: blinded second reading by Opus of \nQC records
  (\nQCCercanos near-miss + \nQCAleatorios random); \nQCAvanzados were advanced, and \nQCIncluidos of them were
  finally included. Full text: reviewers moved from Opus to Sonnet (A5a); reports without a prior decision were
  screened on an excerpt (pages 1–2 + experimental section), calibrated against the full text (Claude
  \nCalibClaude/\nCalibN, Codex \nCalibCodex/\nCalibN on include vs. not); part of Level 1 reviewed by GPT Codex
  (same model for A and B of a report), audited by Claude on \nAuditN of \nAuditPool Codex inclusions
  (\nAuditOK confirmed); Opus second reading of \nQCTCdudosos «unclear» reports and \nQCTCmt joint E6 exclusions with
  multi-turn signal. Agreement figures: point to \cref{tab:ia}, do not repeat them. Reports not retrieved: no contact
  with authors (A4); reported in PRISMA.
- Extraction: two levels (D7): Level 1 (mapping, all studies, pages 1–2) and Level 2 (multi-turn, full form).
  Double AI extraction with automatic comparison and pre-specified resolution rules (A5c as corrected in
  `enmiendas.md`: Level 1 Sonnet/Sonnet, tie-break Codex; Level 2 Sonnet/Codex, tie-break Sonnet on cited pages).
  Author verification samples (\verifC, \verifD, \verifB confirmed without changes) and blind sample of
  \nMuestraCiega studies. New variable `foro_nivel` (A5d). Outcomes: EX primary; EM/ESM, TS; QM/IM in multi-turn;
  per-turn degradation; within-study contrasts.
- Quality: Kitchenham-style checklist of \nItemsCalidad items (not RoB 2 / ROBINS-I), \nItemsValidez validity items
  define the score; threshold \umbralValidez~\% for the in-depth synthesis; traffic-light profile per item; reporting
  items are reported, not summed; calibration on \nCalibCalidad studies.
- Synthesis: SWiM~\cite{Campbell2020SWiM}, no meta-analysis; groups (Level 1/2, component classes); strict
  comparability; within-study contrasts as main evidence, Δ vs. baseline as secondary; D4 with Wilson CI~\cite{Wilson1927Probable}
  and the pre-specified rule (upper bound ≤ \umbralDcuatro~\%); trend test Cochran–Armitage~\cite{Cochran1954Methods,Armitage1955Tests}
  by permutation (\replicasTendencia{} replicas); stratification by evaluation history; sensitivity analyses
  (without preprints, below-threshold studies, lax D4, database arm only, top venues, non-retrieved reports);
  confidence per finding inspired by GRADE-CERQual~\cite{Lewin2018CERQual} (own rules); kappa~\cite{Cohen1960Coefficient}
  and PABAK~\cite{Byrt1993Bias}; exploratory bibliometrics (A6) labelled as such.

## Hard rules
1. No literal numbers in prose; macros only (`\num` is inside them). If a needed number has no macro, write
   `\pendiente{cifra: <qué>}`. Number words for counts are forbidden. Years and identifiers (PI0, D4, A5, CQ2, E6) are fine.
2. Cite only keys from `claves_permitidas_4a.txt`; otherwise `\pendiente{cita: <qué>}`. Cite Kitchenham~\cite{Kitchenham2007Guidelines},
   PRISMA 2020~\cite{Page2021PRISMA}, PRISMA-P~\cite{Moher2015PRISMAP}, PRISMA-S~\cite{Rethlefsen2021PRISMAS} where relevant;
   CQ10 uses Think. Check. Submit.~\cite{TCS2026}.
3. Do not mention the thesis (D5). Do not interpret results (that is sections 4–5).
4. Subsections and labels per the outline: `sec:met-protocolo`, `sec:met-picoc`, `sec:met-elegibilidad`,
   `sec:met-busqueda`, `sec:met-seleccion`, `sec:met-extraccion`, `sec:met-calidad`, `sec:met-sintesis`.
   ≈ 1 900 words excluding tables. Keep `% PRISMA ítems ...` comments per subsection. No `\textbf`; lists only for
   eligibility criteria if needed (compact `itemize`).
5. Insert `\input{tablas/enmiendas}` in 3.1 and `\input{tablas/ia}` in 3.5.

## Output (return ONLY this, no preamble, no Markdown fences)
```
%%%% FILE: 03-metodo.tex
\section{Método}
\label{sec:metodo}
...
```
