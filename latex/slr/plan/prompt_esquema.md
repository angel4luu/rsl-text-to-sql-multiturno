# Task: outline (ARS academic-paper, outline-only mode) for a PRISMA 2020 SLR article

You act as the ARS `structure_architect_agent`. First read its instructions:
`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/structure_architect_agent.md`
and, for structure patterns, `.../academic-paper/references/paper_structure_patterns.md` (same folder root).
This is outline-only mode: produce the Paper Outline + Evidence Map. Do NOT draft prose for the article.

All paths below are relative to the repo root (your working directory). Read only; do not write files.

## The article
- Title area/topic: Systematic literature review (Kitchenham & Charters, reported per PRISMA 2020) on
  *schema grounding / schema linking* in multi-turn (conversational) Text-to-SQL / NLIDBs. Thesis: "Stateful Schema
  Grounding in Multi-Turn NLIDBs". Registered on OSF (DOI 10.17605/OSF.IO/5USF3), protocol v1.2, amendments A1–A6.
- Target: full-length version (~15–20 pages, IEEEtran journal two-column) structured for **IEEE Latin America
  Transactions**; written in **Spanish**, English technical terms in italics on first use; **IEEE** citations.
  A shorter journal cut will be derived later, so mark which subsections are "core" vs "cut candidates".
- Fixed methodology: PICOC (not PICOS); Kitchenham-style quality checklist (not RoB); narrative/thematic synthesis
  (SWiM) + taxonomy; no meta-analysis; bibliometrics are exploratory (amendment A6).
- Existing section files (keep this order unless you argue for a change): `latex/slr/main.tex` and
  `latex/slr/secciones/00-resumen.tex … 08-declaraciones.tex` (resumen, introducción, trabajos relacionados,
  método, resultados, discusión, amenazas a la validez, conclusiones, declaraciones). Read them for the PRISMA-item
  comments already placed there.

## Inputs to read
- Protocol and questions: `slr/protocolo/protocolo_es.md`, `slr/protocolo/01_preguntas_picoc.md`,
  `slr/protocolo/03_criterios_elegibilidad.md`, `slr/protocolo/enmiendas.md` (A1–A6; A4–A6 still "Pendiente" in OSF
  — the article must state them), `slr/protocolo/02_estudios_semilla.md`.
- Search/selection: `slr/busqueda/registro_busquedas.csv`, `slr/sintesis/prisma_conteos.json`,
  `slr/cribado/Screening_TA/TA_methods_selection.md`, `slr/cribado/Screening_FT/FT_methods_selection.md`,
  `slr/cribado/Screening_TA_bola/TA_methods_selection.md`, `slr/cribado/Screening_FT_bola/FT_methods_selection.md`.
- Extraction/quality: `slr/extraccion/formulario_extraccion.md`, `slr/extraccion/informe_acuerdo_extraccion.md`,
  `slr/calidad/checklist_calidad.md` (do not read calidad.csv row by row).
- Synthesis (approved findings — the core evidence): `slr/sintesis/plan_sintesis.md`, `slr/sintesis/PI0.md` …
  `PI5.md`, `slr/sintesis/taxonomia_revision.md`, and the JSON outputs `pi0_resultados.json`,
  `pi15_resultados.json`, `sensibilidad.json`, `bibliometria_resultados.json` (skim keys).
- Figures: `latex/slr/figuras/leyendas.json` (15 generated figures; name → caption).
- Tables: list `slr/sintesis/tablas/*.csv` (33 files); read headers / first lines only.
- Bibliography currently available: `bib/referencias.bib` (16 entries only).
- Background/context only (not evidence): `00-contexto/` proposal.

## Hard rules
1. **No numbers typed in the outline.** Whenever a claim needs a number, cite its source as `file → key/column`
   (e.g. `prisma_conteos.json → incluidos_total`, `pi0_resultados.json → d4.ic95`). Never copy the value.
2. Never invent references. In the citation-needs list, name works by what they are (e.g. "Kitchenham & Charters
   2007 guidelines", "PRISMA 2020 statement", "SParC benchmark") and mark whether they are already in
   `bib/referencias.bib`; for included studies, refer to them by their study ID (R#####/B#####) where the synthesis
   files do.
3. Findings must come from PI0–PI5.md. The "Para la discusión" bullets of each PI file feed only the Discussion.
4. The Discussion will be written separately by a stronger model: give it a strong argument skeleton (claims,
   supporting evidence keys, implications for the thesis gap, comparison with prior reviews), not prose.

## Required output (in Spanish; return ONLY the Markdown document as your final answer, no preamble)
`# Esquema del artículo — RSL Text-to-SQL conversacional`
0. **Decisiones para la autora** (at the very top): only the non-obvious choices (≤ 6), each with lettered options,
   your recommendation, and a reply code (e.g. `D1: a`). Include at least: which tables go in the main text vs.
   supplementary material, and whether bibliometrics stays in Results or moves to a supplement.
1. **Árbol de secciones**: every section/subsection with label suggestion (`sec:…`), purpose (1–2 lines),
   PRISMA 2020 items covered (by item number), target length in words, core vs. cut-candidate.
   Total target must fit ~15–20 IEEE two-column pages including figures/tables.
2. **Ubicación de figuras y tablas**: each of the 15 figures and each proposed table → section, main/supplement,
   one-line reason; for tables, the source CSV(s) and proposed columns.
3. **Mapa de evidencia**: per Results/Discussion subsection, claim → source file → key/column/section.
4. **Esqueleto argumental de la Discusión** (principal findings, interpretation, comparison with prior reviews,
   implications for the thesis gap — M8 criterion — and for research/practice).
5. **Amenazas a la validez**: list of threats to cover (from PI*.md "Limitaciones", AI-assisted screening/extraction,
   amendments) with their source.
6. **Necesidades de citas**: table (work, where used, already in .bib yes/no, how to verify: DOI/DBLP/OpenAlex).
7. **Lista de verificación PRISMA 2020**: the 27 items (+ abstract checklist) → section, or "suplemento"/"N/A" with reason.
