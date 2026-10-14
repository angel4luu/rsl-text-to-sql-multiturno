# Task: ARS academic-paper-reviewer, full mode — editorial synthesis

Read your role instructions: `~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper-reviewer/agents/editorial_synthesizer_agent.md` and `~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/academic-paper-reviewer/references/editorial_decision_standards.md`.
Inputs (relative to repo root, read only): the five independent seat reports
`latex/slr/plan/revision/informe_eic.md`, `informe_methodology.md`, `informe_domain.md`, `informe_perspective.md`,
`informe_devil.md` (same folder), and the manuscript `latex/slr/plan/revision/articulo.txt` to check claims.
The manuscript is a formal academic SLR for a course, written to be submittable later to an IEEE-style journal.

## Output (Markdown, English, return ONLY this)
1. Editorial decision (accept / minor / major / reject) with a 4–6 sentence rationale.
2. Consensus and disagreements among seats (short).
3. **Revision roadmap**: a table of consolidated items `E<n>` (merge duplicates across seats; keep the source ids,
   e.g. «RM-3, RD-1»), each with: priority (P1 must / P2 should / P3 could), location (section), the problem,
   the concrete fix, and effort (S/M/L). Mark items that need a decision by the author (scope, framing) with «[autora]».
   Mark items that are not feasible under the constraints (no new searches or data collection) as «no factible» with
   a one-line alternative (e.g. state it as a limitation). At most 20 items, P1 first.
