# Task: draft section 4, part 1 (Resultados 4.1–4.6) of a PRISMA 2020 SLR article

You act as the ARS `draft_writer_agent`. First read its instructions:
`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/draft_writer_agent.md`
and `.../academic-paper/references/academic_writing_style.md` (same root). The hard rules below override them.
Paths are relative to the repo root (your working directory). Read only.

## Article and style
PRISMA 2020 systematic review on schema grounding in multi-turn Text-to-SQL, IEEE Latin America Transactions.
**Spanish**, formal register, **impersonal "se" + third person (never first-person plural; the author is «la autora»)**,
varied with active third-person sentences (e.g. «La \cref{fig:x} muestra…», «Los estudios multiturno usan…»).
English terms in `\en{...}` on first use. IEEE citations `\cite{key}`. Read `latex/slr/secciones/03-metodo.tex` first
for terminology (Nivel 1/2, D4, contrastes dentro del estudio, historial GOLD/PREDICHO/SOLO_PREGUNTAS) and tone.
Results report findings only: **no interpretation, no causal language, no recommendations** (those go to the
Discussion). Never use the «Para la discusión» bullets of the PI files.

## Numbers (hard rule, checked by a script)
1. Use a macro from `latex/slr/numeros.tex` whenever one exists (counts, D4, quality, PRISMA).
2. Otherwise copy the number exactly as it appears in an approved source and end that paragraph with a comment line
   `% fuente: <file1>, <file2>` naming the file(s) where each number appears verbatim (e.g. `pi1_tecnicas.csv`,
   `pi0_resultados.json`, `PI3.md`, `CALIDAD.md`, `prisma_conteos.json`, `cifras_metodo.json`). Decimal comma in the
   text (48,6), the script accepts it. Percent sign as `~\%`.
3. Never compute new numbers (no sums, differences or new percentages); if a value you need is not in a source,
   write `\pendiente{cifra: <qué>}`.
4. Do not repeat in prose every value of a table or figure: point to it (`\cref{tab:...}`, `\cref{fig:...}`) and state
   only the main values.
5. Study IDs: cite included studies by key using `bib/claves_estudios.csv` (column clave_bib for id_estudio R#####/B#####);
   cite only keys present there or in `latex/slr/plan/claves_permitidas_4a.txt`. Never invent a key.

## Figures and tables (generated; insert, never edit)
Insert each with `\input{figuras/tex/<name>}` or `\input{tablas/<name>}` near its first mention, and reference it with
`\cref`. Read each file to know its caption and label so the text agrees with it.

## Format
`\subsection` with the outline labels; keep a `% PRISMA ítems ...` comment per subsection. No `\textbf`; no bullet
lists. Return ONLY the file content(s) with the `%%%% FILE: <name>` markers, no preamble, no Markdown fences.


## Read
1. Outline `latex/slr/plan/esquema_articulo.md`: §0 «Decisiones tomadas» (D1–D3), §1 rows 4.1–4.6, §2, §3.1 rows 4.1–4.6.
2. Approved findings: `slr/sintesis/PI0.md` (sections Mapeo general, Indicador D4, Técnicas no trasladadas,
   Bibliometría, Sensibilidad — not «Para la discusión»), `slr/sintesis/CALIDAD.md`, and for 4.6 the component-effect
   paragraphs of `slr/sintesis/PI1.md`–`PI4.md` plus `slr/sintesis/tablas/pi_efectos_componentes.csv` and
   `confianza_hallazgos.csv`. Counts: `slr/sintesis/prisma_conteos.json`.
3. Generated items to insert: figures `prisma_flujo`, `pi0_anio_escenario`, `pi0_paradigma_anio`, `d4_tendencia`,
   `bib_comunidad`, `pi_efectos_componentes` (in `latex/slr/figuras/tex/`); tables `d4`, `calidad`, `efectos`
   (in `latex/slr/tablas/`).

## Content
- 4.1 `sec:res-seleccion` (PRISMA 16a, 16b): flow with macros (\nIdentificados … \nEstudios, both arms),
  main exclusion reasons by code (from prisma_conteos.json), reports not retrieved (\nNoRecuperados) and that they
  are described by scenario in 4.2. Figure prisma_flujo.
- 4.2 `sec:res-caracteristicas` (17, 20a): year × scenario, venue types, paradigm by year, central pillars by scenario,
  training-free work, not-retrieved by scenario. Figures pi0_anio_escenario, pi0_paradigma_anio.
- 4.3 `sec:res-d4` (20b, 20d): D4 strict with macros (\DcuatroK, \DcuatroN, \DcuatroPct, CI, \DcuatroConclusion),
  trend test (\DcuatroTendenciaP), 2026 partial, sensitivity variants via \cref{tab:d4}. Figure d4_tendencia, table d4.
- 4.4 `sec:res-bibliometria` (17; decision D2 b): ONE short paragraph, explicitly labelled exploratory and not
  pre-registered (A6); figure bib_comunidad; say the other bibliometric figures are in the supplementary material.
- 4.5 `sec:res-calidad` (18): from CALIDAD.md and table calidad (\nUmbral, \nBajoUmbral, \validezMediana); AI–author
  agreement on quality is already in Methods — do not repeat.
- 4.6 `sec:res-efectos` (19, 20b, 20c, 22; decision D3 a): within-study contrasts by component class across
  PI1–PI4, confidence per finding, Δ vs. baseline only as secondary; figure pi_efectos_componentes, table efectos.
  Subsections 4.7–4.10 (written separately) will refer back here.
- End the file with the line `\input{secciones/04b-resultados}`.

## Output
```
%%%% FILE: 04-resultados.tex
\section{Resultados}
\label{sec:resultados}
...
\input{secciones/04b-resultados}
```
