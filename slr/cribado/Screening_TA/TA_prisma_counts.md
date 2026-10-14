# PRISMA 2020 counts - title/abstract stage

```mermaid
flowchart TD
  I["Records identified from databases (n = 1457)<br/>ACL Anthology n = 133; ACM DL n = 146; arXiv n = 253; IEEE Xplore n = 368; Scopus n = 557"]
  R["Records removed before screening:<br/>duplicate records (n = 416)"]
  S["Records screened (n = 1041)"]
  X["Records excluded (n = 446)<br/>E1 Published before 2019: 43<br/>E2 Article written in a language other than English or Spanish: 11<br/>E3 Thesis, poster, abstract-only or extended abstract, <4 pages of content, editorial, proceedings front matter, complete book: 33<br/>E4 Not a primary study (survey, review, tutorial, position paper): 39<br/>E5 Not Text-to-SQL over relational databases (KGQA/SPARQL, Cypher, NoSQL, table QA without SQL, general code generation): 108<br/>E6 Single-turn and schema linking / join inference / execution feedback / self-correction is not a stated central contribution: 212"]
  F["Reports sought for retrieval (n = 595)"]
  I --> R
  I --> S
  S --> X
  S --> F
```

```json
{
 "stage": "ta",
 "tool": "sr-screener 1.0.0",
 "complete": true,
 "pending_records": 0,
 "state_problems": [],
 "identified_by_database": {
  "ACL Anthology": 133,
  "ACM DL": 146,
  "arXiv": 253,
  "IEEE Xplore": 368,
  "Scopus": 557
 },
 "identified_total": 1457,
 "duplicates_removed": 416,
 "records_screened": 1041,
 "records_to_screen": 1041,
 "records_excluded": 446,
 "excluded_by_code": {
  "E1": 43,
  "E2": 11,
  "E3": 33,
  "E4": 39,
  "E5": 108,
  "E6": 212
 },
 "reports_sought_for_retrieval": 595,
 "advanced_include": 343,
 "advanced_unclear": 252,
 "advanced_outside_allowed_languages": 0,
 "agreement": {
  "n": 1041,
  "both_advance": 532,
  "both_exclude": 477,
  "a_only_advance": 12,
  "b_only_advance": 20,
  "observed_agreement": 0.9693,
  "kappa": 0.938,
  "pabak": 0.939,
  "conflicts": 32,
  "resolved_by": {
   "AJE": 69,
   "A+B": 972
  }
 },
 "decided_by": {
  "AJE": 69,
  "A+B": 972
 }
}
```
