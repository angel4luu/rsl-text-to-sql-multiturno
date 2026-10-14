# Task: draft section 4, part 2 (Resultados 4.7–4.12) of a PRISMA 2020 SLR article

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
1. Outline `latex/slr/plan/esquema_articulo.md`: §0 «Decisiones tomadas», §1 rows 4.7–4.12, §2, §3.1 rows 4.7–4.12.
2. Approved findings: `slr/sintesis/PI1.md` … `PI5.md` (taxonomy, specific question, limitations sections — not
   «Para la discusión»), `slr/sintesis/PI0.md` section Sensibilidad, `slr/sintesis/sensibilidad.json`.
3. Generated items to insert: tables `taxo-pi12` (in 4.7), `contraste-pi34` (in 4.9), `pi5` (in 4.11); figures
   `bib_coocurrencia_tecnicas` (4.9, exploratory A6), `pi5_degradacion` (4.11). The component-effect figure and table
   (`fig:pi_efectos_componentes`, `tab:efectos`) are inserted in subsection `sec:res-efectos` (written separately):
   refer to them, do not insert them, and do not repeat their numbers beyond one sentence per PI.

## Content
- 4.7 `sec:res-pi1` (19, 20a): PI1 techniques and history inputs; rewriting vs. concatenation (the PI1 specific question);
  example studies cited by key. Table taxo-pi12 (shared with 4.8).
- 4.8 `sec:res-pi2`: representation, update, context cost; graph nodes/dynamics with the high not-reported rate.
- 4.9 `sec:res-pi3`: schema-linking techniques and join inference, multi-turn vs. single-turn (table contraste-pi34,
  state its base); studies with non-implicit join inference; exploratory co-occurrence figure.
- 4.10 `sec:res-pi4`: mechanisms and signals vs. single-turn (same table); the single-turn technique not transferred.
- 4.11 `sec:res-pi5` (19, 20c): benchmarks and metrics families, evaluation history, degradation by stratum (never
  pooled), reporting practices; table pi5, figure pi5_degradacion.
- 4.12 `sec:res-sesgos` (20d, 21): reporting bias and sensitivity analyses not covered in 4.3/4.6 (below-threshold
  studies, without preprints, differential retrieval by scenario).

## Output
```
%%%% FILE: 04b-resultados.tex
\subsection{PI1: restauración del contexto}
\label{sec:res-pi1}
...
```
