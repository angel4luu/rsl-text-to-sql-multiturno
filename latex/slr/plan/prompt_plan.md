# Task: draft the FISI-UNMSM «Formulario de inscripción de tesis — Plan de tesis» (undergraduate thesis)

You act as the ARS `draft_writer_agent`. First read its instructions:
`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/draft_writer_agent.md`
and `.../academic-paper/references/academic_writing_style.md` (same root). The hard rules below override them.
Paths are relative to the repo root (your working directory). Read only.

## Context
The author (single tesista, **pregrado**, Escuela Profesional de Ingeniería de Software, FISI-UNMSM; adviser
Herrera Quispe, José Alfredo) registers her undergraduate thesis. The document follows the school's form (sections
1.1–2.7). A systematic literature review (SLR) on the topic is already drafted; it is the main evidence base.
Execution period: \TesisInicio–\TesisFin (Sept 2026 – Aug 2027; the SLR, Sept–Oct 2026, is its first phase).

## Read
1. Form layout already written (do not repeat it): `latex/plan-tesis/main.tex` (1.1–1.5, references, adviser, signatures).
2. The thesis idea: `00-contexto/TS Research Proposal.md` and `00-contexto/TS Blueprints.md` (objectives OE1–OE5,
   justification). **These are not evidence**: rephrase their promises («garantizar», «eliminar», «O(1)») as aims to
   be designed and evaluated.
3. Evidence: the SLR article sections `latex/slr/secciones/00-resumen.tex`, `01-introduccion.tex`,
   `02-trabajos-relacionados.tex`, `05-discusion.tex` (especially `sec:dis-brecha`: the five observed gaps),
   `07-conclusiones.tex`; outline `latex/slr/plan/esquema_articulo.md` §4.4.
4. Directive `plan-tesis/00-plantillas/DIRECTIVA 007 15 julio Estructura de Informe de Tesis (1) - copia-2.pdf`
   (title rules: Spanish, ≤ 20 words, no acronyms, three components qué / cómo / dónde-quién; avoid first person).
5. Macros: `latex/slr/numeros.tex` (verified SLR figures; includes \nDatasetES, \nDatasetEN, \nDatasetZH = included
   studies evaluating on Spanish / English / Chinese data) and `latex/comun/metadatos.tex`.
6. Allowed citation keys: `latex/slr/plan/claves_permitidas_4a.txt` and `bib/claves_estudios.csv` (included studies).
   Local context keys (verified, use only what their titles/abstracts state): QuinterosNavarro2025BI (BI and growth of
   525 SMEs in Lima Plaza; strong positive correlation), Leigh2024BIAdoption (BI adoption model for Peruvian SMEs,
   UTAUT2), MoranSantamaria2026BI (BI and export competitiveness of SMEs in northern Peru), PerezCampdesuner2025AI
   (limited AI adoption in Ecuadorian MSMEs, concentrated in marketing), Pazos2022Wizard (Spanish-language NLIDB work
   from Mexico: semantic views for multi-table queries). Methodology: Hevner2004DesignScience, Peffers2007DSRM,
   Kitchenham2007Guidelines, Page2021PRISMA. Benchmarks: Yu2019SParC, Yu2019CoSQL, Yu2018Spider, Li2023BIRD.

## Files to write (Spanish, impersonal «se» + third person, never first person; English terms in \en{...})
Citations with biblatex-apa: `\textcite{key}` (narrative) or `\parencite{key}`; only allowed keys, else
`\pendiente{cita: <qué>}`.

1. `../../plan-tesis/secciones/01-resumen.tex` — `\subsection{RESUMEN EJECUTIVO}`: one paragraph, 200–250 words:
   problem, gap (with SLR macros: \nEstudios, \DcuatroPct~\%, \nBrechaMocho), proposal (training-free multi-agent
   framework with graph-based dialogue state, symbolic join routing and execution-guided self-correction),
   evaluation plan (SParC, CoSQL; EX, QM/IM, per-turn degradation with predicted history), expected contribution.
   No results claimed for the framework (it does not exist yet).
2. `../../plan-tesis/secciones/02-descripcion.tex` — subsections in this order:
   - `\subsection{ANTECEDENTES Y FUNDAMENTACIÓN CIENTÍFICA, TÉCNICA O HUMANÍSTICA}` with run-in paragraphs
     «\textit{A nivel global:}» (SLR findings with macros and citations to benchmarks, prior reviews, a few included
     studies) and «\textit{A nivel local:}» (Peru/Latin America: BI in SMEs from the local keys; Spanish data is almost
     absent: \nDatasetES{} of \nEstudios{} included studies; Spanish NLIDB work exists regionally \parencite{Pazos2022Wizard}).
   - `\subsection{OBJETIVO GENERAL}` (one sentence) and `\subsubsection{OBJETIVOS ESPECÍFICOS}` (enumerate, 4–5,
     each starting with an infinitive verb, aligned with the SLR gaps; from OE1–OE5 without overclaiming).
   - `\subsection{JUSTIFICACIÓN}` with «\textit{Justificación teórica:}» and «\textit{Justificación práctica:}»
     (theory: SLR gap criterion met by \nBrechaMocho{} studies; practice: SMEs/BI in Peru, Spanish-speaking users,
     no fine-tuning cost — as aims, not guarantees).
   - `\subsection{METAS ESPECÍFICAS}` (itemize, 4–5 verifiable deliverables: completed SLR article; framework
     prototype; evaluation on SParC and CoSQL with turn-level and dialogue-level metrics and per-turn degradation with
     predicted history; comparison against a baseline with the same base LLM; thesis report and article). **Do not
     invent numeric targets**: where a threshold is needed write `\pendiente{meta numérica a acordar con el asesor}`.
   - `\subsection{METODOLOGÍA}` (enumerate phases, Design Science Research \parencite{Hevner2004DesignScience,Peffers2007DSRM}):
     (1) SLR per Kitchenham and PRISMA 2020 — completed; (2) problem identification and objectives from the SLR gaps;
     (3) design of the framework (context restoration, graph state, symbolic join routing, execution feedback);
     (4) implementation (training-free, open LLMs where possible); (5) experimental evaluation (benchmarks, metrics,
     ablations, baseline with the same base model, stratified by evaluation history); (6) communication (thesis report
     per Directive 007 and article).
3. `../../plan-tesis/secciones/03-calendario.tex` — `\subsection{CALENDARIO DE ACTIVIDADES}` (number it 2.7 by placing
   `\setcounter{subsection}{6}` before it) with a `tabularx` table (`\small`, vertical rules): first column «Actividad»,
   then 12 month columns S O N D | E F M A M J J A, header row spanning «2026» (S–D) and «2027» (E–A); 9–11 activities
   consistent with the methodology phases, marked with «X». SLR in Sept–Oct 2026; plan registration Oct 2026; design
   Nov 2026–Jan 2027; implementation Jan–Apr 2027; evaluation Apr–Jun 2027; writing and article Jun–Aug 2027.
4. `../../plan-tesis/titulos.md` — three title options in Spanish following Directive 007 (≤ 20 words, no acronyms —
   write «lenguaje natural», «bases de datos relacionales», «consultas SQL» only if SQL is acceptable as a common term;
   prefer avoiding it), each annotated with qué / cómo / dónde-quién and its word count; recommend one.

## Hard rules
- Numbers: only macros from `latex/slr/numeros.tex`; no other numbers except years, dates and list indices.
- Do not mention «doctoral». Do not claim the framework's performance. No «garantiza», «elimina», «demuestra».
- No `\textbf` in body text (headings already bold).

## Output (return ONLY this, no preamble, no Markdown fences)
```
%%%% FILE: ../../plan-tesis/secciones/01-resumen.tex
...
%%%% FILE: ../../plan-tesis/secciones/02-descripcion.tex
...
%%%% FILE: ../../plan-tesis/secciones/03-calendario.tex
...
%%%% FILE: ../../plan-tesis/titulos.md
...
```
