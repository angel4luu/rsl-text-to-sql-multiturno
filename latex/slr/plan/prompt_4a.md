# Task: draft sections 1 (Introducción) and 2 (Trabajos relacionados) of a PRISMA 2020 SLR article

You act as the ARS `draft_writer_agent`. First read its instructions:
`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/draft_writer_agent.md`
and the style guide `.../academic-paper/references/academic_writing_style.md` (same root). Apply them, but the
hard rules below override them. Paths below are relative to the repo root (your working directory). Read only.

## Article
Systematic review (Kitchenham & Charters, reported per PRISMA 2020) on schema grounding in multi-turn
(conversational) Text-to-SQL. Target journal: IEEE Latin America Transactions (IEEEtran, two columns). Language:
**Spanish** (formal academic register, impersonal "se" + third person; never first-person plural), English technical terms in italics with
the macro `\en{...}` on first use (e.g. `\en{schema linking}`). IEEE citations with `\cite{key}`.

## Read
1. The approved outline: `latex/slr/plan/esquema_articulo.md` — §0 «Decisiones tomadas», §1 rows for sections 1
   and 2 (purpose, PRISMA items, word budget, subsection labels), §2.2 row `tab:relacionados`, §4.3 and §6.
2. Protocol: `slr/protocolo/protocolo_es.md` (title, background, objectives), `slr/protocolo/01_preguntas_picoc.md`
   (PICOC and the exact questions PI0–PI5).
3. Gap analysis of prior reviews: `slr/protocolo/00_analisis_brecha.md` (what was verified and on which text).
4. Prior-reviews table already generated: `latex/slr/tablas/relacionados.tex` (reference it as
   `\cref{tab:relacionados}` and insert it with `\input{tablas/relacionados}` in section 2) and its source
   `slr/sintesis/tablas/revisiones_previas.csv`.
5. Findings for the contributions paragraph only: the first section of `slr/sintesis/PI0.md` (Mapeo general,
   Indicador D4) and `slr/sintesis/pi15_resultados.json → brecha_M8` (meaning only).
6. Number macros: `latex/slr/numeros.tex`. Allowed citation keys: `latex/slr/plan/claves_permitidas_4a.txt`.

## Hard rules
1. **No literal numbers in the prose.** Every count, percentage or interval must be a macro from
   `latex/slr/numeros.tex` (e.g. `\nEstudios`, `\DcuatroPct~\%`, IC `\DcuatroICinf--\DcuatroICsup~\%`). If a number
   you need has no macro, write `\pendiente{cifra: <qué>}` instead. Years, and identifiers like PI0–PI5 or D4, are allowed.
   Number words for counts («cinco bases») are also forbidden: use the macro.
2. **Cite only keys from `claves_permitidas_4a.txt`.** Never invent a key or a reference. If a claim needs a source
   that is not in the list, write `\pendiente{cita: <qué>}`.
3. Describe each prior review only with what `00_analisis_brecha.md` / `revisiones_previas.csv` verified, and say on
   which text it was verified when it was only the abstract (e.g. «según su resumen»). Do not claim superiority over
   surveys; they have different aims (outline §4.3).
4. Decision D5: present the gap criterion neutrally as a pre-specified criterion; **do not mention the thesis**.
5. The Introduction states the objective, PI0–PI5 and the contributions; it may state headline results only through
   macros (`\nEstudios`, `\nMultiturno`, `\DcuatroPct`, `\DcuatroConclusion`), without interpretation (that belongs
   to the Discussion).
6. Follow the outline's subsections and labels (`sec:intro-contexto`, `sec:intro-justificacion`, `sec:intro-objetivos`,
   `sec:rel-generales`, `sec:rel-conversacional`, `sec:rel-brecha`); use `\subsection`. Word budget ≈ 800 (sección 1)
   and ≈ 700 (sección 2), excluding the table. End section 1 with a short paragraph on the article's organization
   using `\cref{sec:...}` labels of sections 2–7 (`sec:relacionados`, `sec:metodo`, `sec:resultados`, `sec:discusion`,
   `sec:amenazas`, `sec:conclusiones`).
7. Keep the PRISMA item comments at the top of each section (`% PRISMA ítems 3 (justificación) y 4 (objetivos)`).
   No figures. Do not use `\textbf` for emphasis; no bullet lists in section 1 except the list of questions PI0–PI5
   (use `enumerate` or `description`).

## Output (return ONLY this, no preamble, no Markdown fences)
```
%%%% FILE: 01-introduccion.tex
\section{Introducción}
\label{sec:introduccion}
...
%%%% FILE: 02-trabajos-relacionados.tex
\section{Trabajos relacionados}
\label{sec:relacionados}
...
```
