# Task: ARS academic-paper-reviewer, full mode — seat `perspective`

Read your role instructions: `~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper-reviewer/agents/perspective_reviewer_agent.md`, and `~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper-reviewer/references/review_criteria_framework.md`, `~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper-reviewer/references/quality_rubrics.md`. Apply them to the manuscript below. Iron rule: write your report independently; you do not see other reviewers' reports. Paths are relative to the repo root. Read only.

## Manuscript under review
`latex/slr/plan/revision/articulo.txt` — text extracted from the compiled PDF (Spanish; IEEEtran journal layout,
about 21 pages including figures, tables and references). Title: «Anclaje al esquema en Text-to-SQL multiturno:
revisión sistemática PRISMA 2020 de técnicas, efectos y brechas». Single author (undergraduate, UNMSM). It is a
formal academic manuscript for a course, written to be submittable later to an IEEE-style journal (no venue chosen;
IEEE Latin America Transactions is the reference). Figures appear only as captions in the text file; their images
were generated from the data and are not available to you.

## Field context (replaces the field-analyst phase)
Field: NLP / databases — conversational (multi-turn) Text-to-SQL, natural language interfaces to databases.
Paper type: systematic literature review (Kitchenham & Charters; reported per PRISMA 2020; registered on OSF;
synthesis without meta-analysis, SWiM; Kitchenham-style quality checklist). Relevant reporting standards: PRISMA
2020 (27 items + abstract checklist), PRISMA-S, SWiM. AI tools (Claude, GPT Codex) were used for screening,
extraction and drafting under the author's verification; this is disclosed in Methods (an AI-use statement is
pending). Supplementary material (search strings, full criteria, per-study tables) is referenced but not attached.

## Constraints you should know (do not ask to undo them; you may flag consequences)
- The protocol and its amendments A1–A6 are fixed; every number in the text comes from scripts.
- No new searches or data collection are possible in this revision round; reanalysis of existing data and rewriting are possible.

## Output (Markdown, English, return ONLY the report)
1. Overall assessment (3–5 sentences) and your recommendation (accept / minor / major / reject).
2. Numbered comments `R<seat>-<n>`: severity (Major/Minor), location (section number and heading, e.g. «IV-F»),
   the problem, the evidence (short quote from the manuscript), and a concrete, feasible fix.
   At most 12 comments; prioritise what most changes the paper's credibility or clarity.
3. What the manuscript does well (≤ 4 bullets).
