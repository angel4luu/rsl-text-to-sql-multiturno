Summary: 1 high, 3 medium, 0 low.

| id | severity | file:line | quoted text | problem | proposed replacement |
|---|---|---|---|---|---|
| F1 | high | `latex/slr/secciones/04-resultados.tex:15` | «E9 (4; informe secundario de un estudio ya incluido)» | The databases arm now has five E9 exclusions, not four: `slr/cribado/Screening_FT/FT_prisma_counts.json` reports E9 = 5, and Appendix B contains the five corresponding database-arm rows after R00278 was added. There is no existing macro for the total E9 count, so the shortest compliant correction is to omit the stale hand-typed count. | «E9 (informe secundario de un estudio ya incluido)» |
| F2 | medium | `latex/slr/secciones/04-resultados.tex:91` | «el \cref{app:caracteristicas} recoge el resultado principal de cada estudio» | Appendix E is limited to the 72 multiturn studies above the validity threshold, and 32 of its rows show `---` rather than a main result. The sentence therefore overstates both the population and the completeness of the appendix. | «el \cref{app:caracteristicas} recoge, cuando está disponible, el resultado principal de los estudios multiturno que alcanzan el umbral de validez» |
| F3 | medium | `latex/slr/secciones/08-declaraciones.tex:19` | «Los identificadores de los modelos, sus funciones y los ajustes de ejecución por etapa se documentan en la \cref{app:ia}. [...] Las plantillas de los \en{prompts} constan en la \cref{app:ia}; el repositorio contiene los \en{prompts} completos, salvo los que incorporan texto de los artículos» | Appendix G documents model identifiers, roles, settings, and five templates for screening and extraction only, although the declaration also reports drafting, simulated peer review, and citation/claim checking. In addition, `scripts/publicar.py` excludes every `HANDOFF*.md`, including executed prompts that do not necessarily contain article text. The two claims are broader than the appendix and public-snapshot contents. | «Los identificadores de los modelos, sus funciones y los ajustes de ejecución del cribado y la extracción se documentan en la \cref{app:ia}. [...] En el \cref{app:ia} constan plantillas de los \en{prompts} principales del cribado y la extracción; el repositorio contiene los \en{prompts} de estas etapas, salvo los que incorporan texto de los artículos, que no se publican por derechos de autor.» |
| F4 | medium | `latex/slr/secciones/09-apendices.tex:8` | «y todos los \en{prompts} ejecutados» | The public-snapshot builder deliberately excludes all `HANDOFF*.md`, although some are executed prompts for Codex review and checking tasks. Therefore the repository does not publish every executed prompt. | «y los \en{prompts} del cribado y la extracción que no incorporan texto de los artículos» |

## Checked, no issue

- Phase 12 repository/appendix substitutions in Sections 03, 04, 04b, 05, and 08 point to the intended repository material or appendix, apart from F2.
- The Phase 13 duplicate-detection sentence in `03-metodo.tex` matches `e9_duplicados_post_ft.csv`, and `\nDupVerifCitas` has the correct value.
- The extraction-run reconciliation in `03-metodo.tex` matches the generated set calculation: seven secondary reports, two studies run at both levels, and three Level-2-to-Level-1 reclassifications reconcile 317 + 78 runs to 389 studies.
- All newly used bibliometric, venue, pillar, source-contribution, PI3/PI4-contrast, D4-lax, and D4-bound macros match their current JSON/CSV sources and are used for the quantity their names denote.
- The three rewordings in Sections 01, 02, and 05 match the author-approved replacements recorded in `bib/afirmaciones/revision_afirmaciones.md`.
- Appendix order and letters are correct: A search, B full-text exclusions, C extraction form, D quality, E multiturn characteristics, F supplementary figures, and G AI use.
- Every scoped `\cref` resolves to the label whose content is described; the multi-label references in Sections 08 and 09 are also correct.
- Appendix A's caption and lead-in match `registro_busquedas.csv`, including the ACM date handling and the ACL checksum statement.
- Appendix B contains 100 exclusion rows (83 databases + 17 snowballing), and its caption and arm subtotals match the two full-text PRISMA records.
- Appendix C contains the stated 71 field rows and correctly identifies the Level 2-only blocks and fields.
- Appendix D's rubric, 77-study profile, 72-study threshold count, and 50% threshold agree with the quality records.
- Appendix E contains exactly the 72 multiturn studies above the validity threshold, and its code legend agrees with the table content.
- Appendix F's two captions agree with the current 389-study paradigm figure and the twelve-technique co-occurrence figure.
- Appendix G's model/role/settings rows and human-verification caption and values agree with the prompt indexes, model metadata, and `informe_acuerdo_extraccion.md`.
- The remaining AI declaration statements about tool/provider names, assigned research roles, human checks, limitations, cloud processing, reference verification, and author responsibility are supported by the method, Appendix G, threats section, and citation-verification report.
- All scoped citation keys are present, and the current log reports no undefined citations or cross-references.
- No broken/doubled words or concrete macro-spacing defects were found in the scoped edits.

## Optional style suggestions

None.
