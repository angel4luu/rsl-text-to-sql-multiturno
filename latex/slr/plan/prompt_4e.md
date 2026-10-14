# Task: complete the article — threats to validity, conclusions, bilingual abstract, declarations, expanded IV-D, title options

You act as the ARS `draft_writer_agent` and, for the abstracts, the ARS `abstract_bilingual_agent`. Read:
`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/draft_writer_agent.md`,
`.../academic-paper/agents/abstract_bilingual_agent.md`, `.../academic-paper/references/abstract_writing_guide.md` and
`.../academic-paper/references/academic_writing_style.md` (same root). The hard rules below override them.
Paths are relative to the repo root (your working directory). Read only.

## Article and style
PRISMA 2020 systematic review on schema grounding in multi-turn (conversational) Text-to-SQL, IEEE Latin America
Transactions (IEEEtran). **Spanish** for everything except the English abstract/keywords/titles. **Impersonal "se" +
third person (never first-person plural; the author is «la autora»)**. English terms in `\en{...}` on first use.

## Read first
1. All written sections, in order: `latex/slr/secciones/01-introduccion.tex`, `02-trabajos-relacionados.tex`,
   `03-metodo.tex`, `04-resultados.tex`, `04-bibliometria.tex`, `04b-resultados.tex`, `05-discusion.tex`, and the
   generated tables/figures they `\input` (labels, captions). New text must agree with them and not repeat them.
2. Outline `latex/slr/plan/esquema_articulo.md`: §0 (D5, D6), §1 rows for sections 6, 7, Resumen, Declaraciones,
   **§5 (threats table)**, §7.2 (PRISMA 2020 for Abstracts, 12 items).
3. `latex/slr/numeros.tex` (macros), `latex/comun/metadatos.tex` (\RSLFinanciamiento), `slr/protocolo/enmiendas.md`.
4. For IV-D: `slr/sintesis/bibliometria_resultados.json`, `slr/sintesis/tablas/bib_*.csv`, `slr/sintesis/PI0.md`
   (section Bibliometría), and the figure snippets `latex/slr/figuras/tex/bib_comunidad.tex` and
   `latex/slr/figuras/tex/bib_panorama.tex` (composite: (a) citation network, (b) countries, (c) base-model families).

## Files to write
1. `04-bibliometria.tex` — rewrite subsection «Panorama bibliométrico exploratorio» (`\label{sec:res-bibliometria}`,
   keep its PRISMA comment) to ≈ 350–400 words: first sentence states it is exploratory (enmienda A6) — neutral
   wording, do not say «no pre-registrado»; then community of venue (`\input{figuras/tex/bib_comunidad}`), citation
   network, countries and base-model families (`\input{figuras/tex/bib_panorama}`, referred to as
   `\cref{fig:bib_panorama}` with panels «(a)», «(b)», «(c)»), with the caveats in the captions (Level 1 models from
   pages 1–2 only; OpenAlex coverage). Put each `\input` **before** the paragraph that first mentions it. Mention that
   authorship and term analyses are in the supplementary material. Findings only, no interpretation.
2. `06-amenazas-validez.tex` — `\section{Amenazas a la validez}\label{sec:amenazas}` (≈ 650 words), subsections
   `sec:am-seleccion`, `sec:am-interna`, `sec:am-externa` (PRISMA 23b, 23c), from outline §5 plus: search sensitivity
   lower for single-turn (\nRefUTHallados{} of \nRefUT{} vs. \nRefMTHallados{} of \nRefMT{}); the blinded QC re-read
   advanced \nQCAvanzados{} joint exclusions of which \nQCIncluidos{} were included (A and B together missed eligible
   studies; the QC only covered a sample of joint exclusions); excerpt calibration of Codex (\nCalibCodex{} of
   \nCalibN{}); the low yield of IEEE Xplore (\cref{fig:busqueda_fuentes}) and non-retrieved reports; Level 2
   extraction agreement \acuerdoNivelDos~\%; author verification samples all confirmed (possible automation bias);
   blind sample of \nMuestraCiega{} studies; same-family AI reviewers; language bias (no Chinese, no Hispanic
   databases); reporting bias in within-study contrasts; partial 2026; amendments A4–A6 pending in OSF.
   For each threat: what it is, direction of the possible bias, and the mitigation applied. Do not repeat the
   Discussion's interpretations.
3. `07-conclusiones.tex` — `\section{Conclusiones}\label{sec:conclusiones}` (≈ 300 words, PRISMA 23d): one short
   answer per PI0–PI5 (macros only, no new numbers), then future work aligned with `sec:dis-brecha`. No new claims.
   **Do not mention the thesis (D5).**
4. `00-resumen.tex` — keep the PRISMA comment; then, in this order:
   `\begin{abstract} ... \end{abstract}` (Spanish, ≈ 220–250 words, structured with run-in labels written as
   `\textit{Contexto:}`, `\textit{Objetivo:}`, `\textit{Método:}`, `\textit{Resultados:}`, `\textit{Limitaciones:}`,
   `\textit{Conclusiones:}`, `\textit{Financiamiento y registro:}` — cover the 12 PRISMA-A items),
   `\begin{IEEEkeywords} ... \end{IEEEkeywords}` (5–6 keywords, Spanish),
   `\begin{abstracten} ... \end{abstracten}` (English, a faithful translation with the same structure and labels in
   English: Background, Objective, Methods, Results, Limitations, Conclusions, Funding and registration),
   `\begin{keywordsen} ... \end{keywordsen}` (Index Terms, same keywords in English).
   Numbers only as macros (they render correctly in both languages). No citations in the abstracts.
5. `08-declaraciones.tex` — unnumbered `\section*{...}` blocks: «Registro y protocolo» (OSF, DOI, \cite{OSF2026Protocolo},
   amendments A1–A6 and that A4–A6 will be updated before submission), «Financiamiento» (`\RSLFinanciamiento`),
   «Conflictos de interés» (decision D5: the author is developing an undergraduate thesis project (professional degree) on a related topic;
   the gap criterion and D4 rule were registered before the data were examined), «Disponibilidad de datos y código»
   (repository with search exports, screening logs, extraction and quality files, synthesis scripts and figures;
   full texts are not shared for copyright reasons), «Declaración de uso de IA» (one sentence:
   `\pendiente{declaración completa con /ars-disclosure (fase 13)}` after a brief factual summary that AI models were
   used for screening, extraction and drafting under the author's verification, as described in \cref{sec:met-seleccion}).
6. `../plan/titulos.md` — three title options, each in Spanish and English, each including «revisión sistemática» /
   «systematic review» (PRISMA item 1), ≤ 20 words, plus a short running title (≤ 50 characters) for each. Plain Markdown.

## Hard rules
1. Numbers: macros from `latex/slr/numeros.tex` whenever they exist; otherwise copy a value exactly as it appears in a
   source and end that paragraph with `% fuente: <file(s)>` (decimal comma; one decimal). Never compute new numbers.
   No literal numbers in the abstracts, conclusions or declarations (macros only).
2. Cite only keys from `latex/slr/plan/claves_permitidas_4a.txt` or `bib/claves_estudios.csv`; otherwise
   `\pendiente{cita: <qué>}`. No citations in the abstracts.
3. No causal claims; no «demuestra», «prueba que». Respect outline §4.6.
4. No `\textbf`. Lists only if indispensable.

## Output (return ONLY this, no preamble, no Markdown fences)
```
%%%% FILE: 04-bibliometria.tex
...
%%%% FILE: 06-amenazas-validez.tex
...
%%%% FILE: 07-conclusiones.tex
...
%%%% FILE: 00-resumen.tex
...
%%%% FILE: 08-declaraciones.tex
...
%%%% FILE: ../plan/titulos.md
...
```
