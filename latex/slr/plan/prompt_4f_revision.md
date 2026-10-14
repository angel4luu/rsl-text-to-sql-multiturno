# Task: apply the accepted peer-review revisions (step 4f) to a PRISMA 2020 SLR article (Spanish)

You act as the ARS `draft_writer_agent` in revision mode
(`~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper/agents/draft_writer_agent.md`).
The rules below override it. Paths are relative to the repo root. Read only.

## Read first
- Accepted decisions: `latex/slr/plan/revision/hoja_decisiones_4f.md` (author answered «OK» to every ★ option).
- The two reviews: `latex/slr/plan/revision/informe_methodology.md`, `informe_devil.md`.
- New results: `slr/sintesis/revision_4f.json` and their macros at the end of `latex/slr/numeros.tex`
  (`\nCentralMT`, `\nCentralUT`, `\espMochoAB`, `\espMochoAC`, `\espMochoBC`, `\espMochoABC`, `\tendenciaConP`,
  `\nulosUmbral`, `\nEstClase`, `\nConfAlta`, `\nConjuntas`, `\nNoReleidas`, `\nAleatRel`, `\nRescAleat`, `\tasaRescate`,
  `\tasaRescateInf`, `\tasaRescateSup`, `\omisEsp`, `\omisEspInf`, `\omisEspSup`, `\kappaCentral`, `\pabakCentral`,
  `\nKappaCentral`, `\DcuatroProbPct`, `\sensUTInf`, `\sensUTSup`, `\degPredMin`, `\degPredMax`, `\degSoloMin`,
  `\degSoloMax`, `\acuerdoCampoPilaresCentrales`, `\acuerdoCampoTecnicaContexto`, `\acuerdoCampoRepresentacion`,
  `\acuerdoCampoInferenciaJoins`, `\acuerdoCampoMecanismo`, `\acuerdoCampoHistorial`).
- Regenerated tables (already updated, do not edit; read their captions): `latex/slr/tablas/contraste-pi34.tex`
  (now both arms restricted to PI3/PI4-central studies, with «no reportado» rows), `efectos.tex` (new columns: nulls with
  |Δ| < 0,5 pp and confidence penalized one level for reporting bias), `enmiendas.tex` (new column «Momento respecto de
  los datos»).
- The sections to revise: `latex/slr/secciones/00-resumen.tex`, `03-metodo.tex`, `04-resultados.tex`,
  `04b-resultados.tex`, `05-discusion.tex`, `06-amenazas-validez.tex`, `07-conclusiones.tex`.

## Changes (only these; keep every other sentence, macro, \input, label and «% fuente:» line verbatim)
- **A1** (`04b-resultados.tex` IV-I/IV-J, `05-discusion.tex` V-B): the technique contrast now compares
  \nCentralMT{} multi-turn vs \nCentralUT{} single-turn studies, both PI3/PI4-central. Update the sentences and numbers to
  the new table (read `slr/sintesis/tablas/pi34_tecnicas_central.csv`; cite it in `% fuente:`): execution feedback is
  closer between arms than before; user clarification and the user signal remain far more frequent in multi-turn; join
  inference is **not comparable** (single-turn «no reportado» is much higher because Level 1 was extracted from the
  first pages). Delete the sentence «Este patrón sugiere que en el escenario conversacional la ambigüedad se aborda más
  mediante la interacción que mediante la ejecución» and its follow-up explanation.
- **A2** (`05-discusion.tex` V-D, `00-resumen.tex`, `07-conclusiones.tex`): add the expected counts under independence
  (a+b \espMochoAB, a+c \espMochoAC, b+c \espMochoBC, triple \espMochoABC) next to the observed ones; say the observed
  pairs are close to what independence predicts, so the data show low base rates, not an avoided combination; replace
  «lo que casi no aparece es el estado estructurado junto con…» accordingly; state that the (a)/(b)/(c) definitions
  were registered (protocol v1.2, M8a). In both abstracts remove the sentence reporting the number of studies meeting
  the reformulation criterion; adjust the conclusions' gap paragraph.
- **A3** (`04-resultados.tex` IV-C, `05-discusion.tex` V-B, `03-metodo.tex` III-H): sensitivity trend test including
  2026: $p$ = \tendenciaConP{} (decreasing direction, not significant at 0,05). Keep the registered test as primary;
  drop wording that implies stability.
- **A4** (`04-resultados.tex` IV-F, `05-discusion.tex` V-B): replace «Ninguna clase registra estudios con efecto nulo»
  with the threshold result (\nulosUmbral{} of \nEstClase{} study-class results have |Δ| < 0,5 pp); the registered
  confidence is «alta» in \nConfAlta{} classes and drops to «moderada» when penalized for reporting bias (\cref{tab:efectos});
  rewrite «efectos positivos y modestos»-type claims as «las ablaciones de los autores rara vez reportan perjuicio».
  In III-H say the penalized reading is an added sensitivity, the registered rule unchanged.
- **A5** (`03-metodo.tex` III-E, `06-amenazas-validez.tex`): of \nConjuntas{} joint exclusions, \nNoReleidas{} were not
  re-read; in the random re-read stratum \nRescAleat{} of \nAleatRel{} were finally included (\tasaRescate~\%, IC
  \tasaRescateInf--\tasaRescateSup~\%), which extrapolates to \omisEsp{} expected missed studies (IC \omisEspInf--\omisEspSup).
  Per-field A–B agreement in Level 2 before resolution: central pillars \acuerdoCampoPilaresCentrales, context-restoration
  technique \acuerdoCampoTecnicaContexto, state representation \acuerdoCampoRepresentacion, join inference
  \acuerdoCampoInferenciaJoins, PI4 mechanism \acuerdoCampoMecanismo, evaluation history \acuerdoCampoHistorial (report in
  III-F and discuss the low ones in VI-B). In Results/Discussion phrase «no reportado» shares as «no reportado o no
  extraído» at first use, and say the PI5 strata depend on a coding independently verified in 3 of 5 sample studies.
- **A6** (`00-resumen.tex`, `03-metodo.tex` III-H, `04-resultados.tex` IV-C): D4 presented as a descriptive proportion
  «dentro del marco de elegibilidad»; the 30 % threshold is a reference chosen by the author in the protocol, without
  external grounding — say so; agreement on the D4-defining field (PI3/PI4 central) in Level 1: $\kappa$ = \kappaCentral{}
  (PABAK \pabakCentral, $n$ = \nKappaCentral); the Wilson interval covers only sampling error.
- **A7** (`03-metodo.tex` III-D, `04-resultados.tex` IV-C, `05-discusion.tex`): describe the «señal» of unretrieved
  reports (multi-turn keywords in title/abstract); call the existing bound «cota extrema» (avoid presenting 77 as if it
  were the multi-turn total); add the probabilistic estimate applying the rates observed among retrieved reports:
  D4 ≈ \DcuatroProbPct~\%.
- **A8** (`03-metodo.tex` III-D, `06-amenazas-validez.tex`): single-turn sensitivity \nRefUTHallados/\nRefUT{} (IC
  \sensUTInf--\sensUTSup~\%); present the multi-turn lower bound \refMTICinf~\% as optimistic because of the circular
  reference set; limitation: no independent reference set; DBLP and Web of Science not searched.
- **A9** (`04b-resultados.tex` IV-K, `05-discusion.tex` V-B): ranges per stratum (predicted \degPredMin{} to
  \degPredMax{}, questions-only \degSoloMin{} to \degSoloMax{} pp/turn); discuss that the predicted stratum degrades less
  than the questions-only one, contrary to the error-propagation expectation (few curves, mixed benchmarks/metrics,
  depth confounded with difficulty); explain that relative values above 100 % mean some later-turn groups score higher
  than turn 1; remove the juxtaposition of component effects with degradation slopes; present the claim that gold history
  overestimates robustness as a hypothesis.
- **B1** (`03-metodo.tex`, `04-resultados.tex`): one sentence explaining that extraction runs (Level 1 and Level 2,
  table IV) sum more than the studies because 5 reclassified studies were extracted at both levels; final split
  \nUnTurno{} / \nMultiturno; complete the venue categories in IV-B with the remaining types from `slr/sintesis/tablas/pi0_foros.csv`
  (sum to \nEstudios); justify each denominator change (77 Level 2 vs 72 above the threshold) at first use.
- **B2** (`05-discusion.tex` agenda): state the ordering rule (direct report data > extraction coding > rarity) and add
  to the Spanish-data item that the search strings were in English (Spanish-language publications may be missed;
  Spanish datasets reported in English papers would still be found).
- **B3** (`03-metodo.tex` III-G, `04-resultados.tex` IV-E): the 50 % threshold was registered; it excludes few studies,
  so the reading with all studies (sensitivity already run) is equally informative; single-turn (Level 1) studies were
  not appraised, so single-turn contrasts are unappraised.
- **B4** (`03-metodo.tex` III-A): the OSF registration preceded the official searches (pre-registration counts are
  logged as such in the search log); point to the new «Momento» column of \cref{tab:enmiendas}; the A4 sensitivity is
  post hoc.

## Hard rules
- Numbers: macros, or values copied exactly from a source file with a `% fuente:` comment on the paragraph. No
  computing new numbers. Number words for counts are forbidden.
- Spanish, impersonal «se» + third person; no first person; no «demuestra», «prueba que», «garantiza».
- Cite only keys in `latex/slr/plan/claves_permitidas_4a.txt` or `bib/claves_estudios.csv`.
- Keep the article length roughly stable: offset additions by tightening nearby sentences.

## Output (ONLY this; each file COMPLETE; no preamble, no Markdown fences)
```
%%%% FILE: 00-resumen.tex
...
%%%% FILE: 03-metodo.tex
...
%%%% FILE: 04-resultados.tex
...
%%%% FILE: 04b-resultados.tex
...
%%%% FILE: 05-discusion.tex
...
%%%% FILE: 06-amenazas-validez.tex
...
%%%% FILE: 07-conclusiones.tex
...
```
