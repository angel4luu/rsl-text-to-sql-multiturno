# AI-use declaration compliance report

The declaration in `latex/slr/secciones/08-declaraciones.tex` was rendered against the PRISMA-trAIce policy anchor. ICMJE is used only for the human-responsibility field that PRISMA-trAIce does not address.

| Anchor | Field | Status | Where covered | Repository fact source(s) |
|---|---:|---|---|---|
| PRISMA-trAIce | 1. AI tool name | stated | First sentence: Claude Code, Academic Research Skills, and OpenAI Codex CLI | `PLAN_FASES.md`; `slr/HANDOFF_sesion_fase11.md`; `slr/HANDOFF_fase13.md`; `latex/slr/apendices/g_ia.tex` |
| PRISMA-trAIce | 2. AI tool version or identifier | cross-referenced | `\cref{app:ia}` | `latex/slr/apendices/g_ia.tex` |
| PRISMA-trAIce | 3. Developer or provider | stated | First sentence: Anthropic and OpenAI | `slr/HANDOFF_codex_declaracion_ia.md` |
| PRISMA-trAIce | 4. Stage or phase of use | stated | Screening, extraction, quality appraisal, drafting support, simulated peer review, and citation/claim checking | `latex/slr/secciones/03-metodo.tex`; `latex/slr/tablas/ia.tex`; `PLAN_FASES.md`; `slr/HANDOFF_fase13.md`; `bib/HANDOFF_codex_afirmaciones.md` |
| PRISMA-trAIce | 5. Specific task within stage | stated | Blinded assessments, adjudication, quality control, proposed coding/scoring, drafting support, simulated review, and checks | `latex/slr/secciones/03-metodo.tex`; `latex/slr/apendices/g_prompts.tex`; `PLAN_FASES.md`; `slr/HANDOFF_fase13.md`; `bib/HANDOFF_codex_afirmaciones.md` |
| PRISMA-trAIce | 6. Affected manuscript sections or content locator | not applicable | PRISMA-trAIce treats this field as implicit rather than requiring a per-task locator; the disclosure is in the dedicated AI-use section | `slr/HANDOFF_codex_declaracion_ia.md` |
| PRISMA-trAIce | 7. Date(s) of use | not applicable | The anchor does not address this field | `slr/HANDOFF_codex_declaracion_ia.md` |
| PRISMA-trAIce | 8. Prompts | cross-referenced | Prompt templates in `\cref{app:ia}` and complete prompts in the repository | `latex/slr/secciones/09-apendices.tex`; `latex/slr/apendices/g_prompts.tex` |
| PRISMA-trAIce | 9. Human oversight method | stated | Author verification is summarized and linked to `\cref{sec:met-seleccion,sec:met-extraccion,app:ia}` | `latex/slr/secciones/03-metodo.tex`; `latex/slr/apendices/g_ia.tex` |
| PRISMA-trAIce | 10. Human responsibility statement | not applicable | PRISMA-trAIce does not address this field; it is supplied under ICMJE field 10 below | `slr/HANDOFF_codex_declaracion_ia.md` |
| PRISMA-trAIce | 11. Performance evaluation method | cross-referenced | Agreement, calibrations, audits, and human checks; `\cref{tab:ia,app:ia}` | `latex/slr/secciones/03-metodo.tex`; `latex/slr/tablas/ia.tex`; `latex/slr/apendices/g_ia.tex` |
| PRISMA-trAIce | 12. Performance evaluation results | cross-referenced | `\cref{tab:ia,app:ia}` | `latex/slr/tablas/ia.tex`; `latex/slr/apendices/g_ia.tex` |
| PRISMA-trAIce | 13. Limitations or known failure modes | stated | Same-family screening reviewers, no fixed temperature, correlated-error risk, and limits of human verification; `\cref{sec:amenazas}` | `latex/slr/apendices/g_ia.tex`; `latex/slr/secciones/06-amenazas-validez.tex` |
| PRISMA-trAIce | 14. Disclosure location | stated | Dedicated “Declaración de uso de IA” section, with methodological and discussion cross-references | `latex/slr/secciones/08-declaraciones.tex` |
| PRISMA-trAIce | 15. Copyediting exemption predicate | not applicable | The anchor does not address a copyediting exemption, and the disclosed use was not limited to copyediting | `slr/HANDOFF_codex_declaracion_ia.md`; `PLAN_FASES.md` |
| PRISMA-trAIce | 16. Data handling, privacy, security, and rights | stated | Only published study texts were processed as study data; full texts are not redistributed | `slr/HANDOFF_codex_declaracion_ia.md`; `latex/slr/secciones/08-declaraciones.tex`; `latex/slr/secciones/09-apendices.tex` |
| ICMJE | 10. Human responsibility statement | stated | The author reviewed the final manuscript, assumes full responsibility, and AI tools are not authors; reference verification is also stated | `slr/HANDOFF_codex_declaracion_ia.md`; `slr/HANDOFF_fase13.md`; `bib/verificacion_citas_fase13.md` |

## Pending items

None. No `\pendiente` remains in the declaration. Fields marked “not applicable” are fields not addressed explicitly by the PRISMA-trAIce anchor, rather than missing repository facts.
