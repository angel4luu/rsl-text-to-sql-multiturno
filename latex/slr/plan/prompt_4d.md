# Task: draft section 5 (Discusión) of a PRISMA 2020 SLR article

You act as the ARS `draft_writer_agent`. First read its instructions:
`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/draft_writer_agent.md`
and `.../academic-paper/references/academic_writing_style.md` (same root). The hard rules below override them.
Paths are relative to the repo root (your working directory). Read only.

## Article and style
PRISMA 2020 systematic review on schema grounding in multi-turn (conversational) Text-to-SQL, IEEE Latin America
Transactions. **Spanish**, formal register, **impersonal "se" + third person (never first-person plural; the author is
«la autora»)**, varied with active third-person sentences. English terms in `\en{...}` on first use. IEEE citations.

## Read first (in this order)
1. Sections already written — the Discussion must build on them, not repeat them:
   `latex/slr/secciones/01-introduccion.tex`, `02-trabajos-relacionados.tex`, `03-metodo.tex`, `04-resultados.tex`,
   `04b-resultados.tex`, and the generated tables/figures they `\input` (for labels and captions).
2. The argument skeleton: `latex/slr/plan/esquema_articulo.md` §0 (D5), §1 rows 5.1–5.5, **§4 entirely** (H1–H7,
   I1–I9 with their mandatory caveats, §4.3 comparison, §4.4 gap and agenda, §4.5 practice, **§4.6 what cannot be
   claimed**), §5 (threats — do not discuss them here, section 6 does; at most one sentence pointing to
   `\cref{sec:amenazas}`).
3. The «Para la discusión» bullets of `slr/sintesis/PI0.md` … `PI5.md` (this is the only section that uses them).
4. `slr/protocolo/00_analisis_brecha.md` (what was verified about each prior review and on which text).
5. Figure 1 data: `slr/sintesis/tablas/busqueda_fuentes.csv` (`\cref{fig:busqueda_fuentes}`): IEEE Xplore yielded few
   included studies relative to its records (consistent with the retrieval bias of A4: paywalled publishers are
   under-represented among retrieved full texts); arXiv made the largest unique contribution (supports including preprints).
6. `slr/sintesis/pi15_resultados.json → brecha_M8` and `latex/slr/numeros.tex`.

## Content (subsections and labels per the outline)
- 5.1 `sec:dis-hallazgos`: principal findings (H1–H7) in a compact paragraph, by reference to Results subsections.
- 5.2 `sec:dis-interpretacion`: I1–I9; every interpretation carries the caveat listed in §4.2 of the outline.
  Distinguish what the evidence shows from what it suggests; descriptive comparisons only across studies.
- 5.3 `sec:dis-comparacion`: scope and method vs. prior reviews (\cref{tab:relacionados}); Yang 2025 only «según su
  resumen»; no claim of superiority over surveys (different aims).
- 5.4 `sec:dis-brecha`: the pre-specified gap criterion M8 (\nBrechaMocho{} studies meet it): wording «no se encontró
  en el corpus ningún estudio que…», never «nadie lo ha hecho»; why the result is conditional (coding, non-retrieved
  reports, extraction agreement). Then the research agenda as «brechas observadas» (outline §4.4 items 1–5), not as
  solutions. **Decision D5: do not mention the thesis or the author's own project** (the conflict of interest is
  declared in the Declaraciones section, not here).
- 5.5 `sec:dis-practica`: reporting and evaluation recommendations for primary studies (outline §4.5).
≈ 1 800 words.

## Hard rules
1. Numbers: macros from `latex/slr/numeros.tex` when they exist; otherwise copy a value exactly as it appears in a
   source and end the paragraph with `% fuente: <file(s)>` (decimal comma in the text; same one-decimal rounding as the
   Results). Never compute new numbers. Prefer few numbers: the Discussion points to Results and tables.
2. Cite only keys in `latex/slr/plan/claves_permitidas_4a.txt` or `bib/claves_estudios.csv` (included studies by
   key); otherwise `\pendiente{cita: <qué>}`. Never invent references or facts about cited works.
3. No causal language for within-study contrasts or cross-study comparisons; no «demuestra», «prueba que», «causa»,
   «garantiza». Respect every item of §4.6 of the outline.
4. Keep `% PRISMA ítems ...` comments (23a, 23b, 23d). No `\textbf`; at most one enumerated list (the agenda).
5. No new figures or tables.

## Output (return ONLY this, no preamble, no Markdown fences)
```
%%%% FILE: 05-discusion.tex
\section{Discusión}
\label{sec:discusion}
...
```
