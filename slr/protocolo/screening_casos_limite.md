# Boundary cases for the screening protocol (synthetic — agreed before the pilot)

All records below are **synthetic**, written to test the rules. Expected decisions **confirmed by the author on 2026-10-11** (all 7).

### Case 1 (synthetic) — clear include
TI: History-aware question rewriting for multi-turn text-to-SQL with large language models
AB: We rewrite each follow-up question in SParC and CoSQL into a self-contained question using the dialogue history, then generate SQL. Question match improves by 4.1 points on CoSQL.
Expected: **include (INC)**. Relational Text-to-SQL, multi-turn, context restoration, quantitative results.

### Case 2 (synthetic) — "multi-turn" that is really single-turn (tests B6)
TI: Multi-round agentic refinement for text-to-SQL on BIRD
AB: An LLM agent executes candidate SQL against the database over several rounds and repairs errors from the execution messages for each question. We report execution accuracy on BIRD dev.
Expected: **include (INC)** as **single-turn** with self-correction as the central contribution (not multi-turn). Tests that "multi-round" agent loops are not coded as multi-turn, but still pass via scope (b).

### Case 3 (synthetic) — single-turn without central linking/correction (tests E6)
TI: Parameter-efficient fine-tuning of small language models for text-to-SQL
AB: We study LoRA fine-tuning of 7B models on Spider and BIRD and compare prompt formats. Our model reaches 82% EX on Spider.
Expected: **exclude E6**. Relational Text-to-SQL, but single-turn and neither schema linking nor self-correction is a stated contribution.

### Case 4 (synthetic) — wrong formal language (tests E5)
TI: Conversational question answering over knowledge graphs with dynamic context graphs
AB: Users ask follow-up questions that are translated into SPARQL over Wikidata; we model ellipsis and coreference with a graph neural network.
Expected: **exclude E5**. Multi-turn and context modelling, but SPARQL over a knowledge graph, not SQL over a relational database.

### Case 5 (synthetic) — unclear, interactive wording (tests the multi-turn exception)
TI: An interactive natural language interface to enterprise databases
AB: We present an interactive NLIDB that translates user questions into SQL and lets users refine their requests. A user study and accuracy on an internal benchmark are reported.
Expected: **unclear (UNC)**. Task met; "interactive / refine their requests" may mean a multi-turn dialogue or single-question clarification — needs full text.

### Case 6 (synthetic) — relevant survey (tests E4 before E5/E6)
TI: A survey of conversational text-to-SQL: datasets, methods and challenges
AB: We review context-dependent text-to-SQL methods, SParC/CoSQL results and open problems.
Expected: **exclude E4** (not a primary study; goes to related work).

### Case 7 (synthetic) — date fails first (tests code order)
TI: Context-dependent semantic parsing for interactive database queries
AB: (2018) We parse sequences of user questions into SQL using the interaction history on ATIS.
Expected: **exclude E1** (published 2018), even though it is otherwise relevant.
