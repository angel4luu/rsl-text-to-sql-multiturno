"""Search string v4 (registered protocol, OSF 10.17605/OSF.IO/5USF3) as local Boolean logic.

Used for sources without a Boolean search engine (ACL Anthology dump) and to apply the
full string to arXiv API results. Mirrors `slr/busqueda/cadenas.md`:

    A (task) AND (B1 (multi-turn) OR B2 (pillars 3-4)), over title + abstract.

Records without an abstract: block A on the title only (rule M4e of the protocol).
Matching is case-insensitive; hyphens/spaces in phrases are interchangeable, as in Scopus.
"""
import re

SEP = r"[\s\-]*"  # "multi-turn" == "multi turn" == "multiturn"


def _p(phrase):
    """Phrase -> regex with flexible separators and word boundaries."""
    words = [re.escape(w) for w in re.split(r"[\s\-]+", phrase.strip())]
    return r"\b" + SEP.join(words) + r"\b"


# ---- Block A: task --------------------------------------------------------------
A_TERMS = [
    _p("text to SQL"), r"\btext2sql\b", r"\bnl2sql\b", _p("NL to SQL"),
    _p("natural language to SQL"),
    r"\bnatural language interfaces?" + SEP + r"to" + SEP + r"(relational" + SEP + r")?databases?\b",
    r"\bnlidbs?\b",
    _p("SQL generation"), _p("SQL query generation"), _p("SQL synthesis"),
    r"\bquestions?" + SEP + r"to" + SEP + r"sql\b",
    _p("database question answering"),
    r"\bquestion answering over" + SEP + r"(relational" + SEP + r")?databases?\b",
]
SEMPARSE = r"\bsemantic" + SEP + r"pars\w*"
SEMPARSE_CONTEXT = r"\b(sql|databases?|sparc|cosql|spider|chase)\b"

# ---- Block B1: multi-turn -----------------------------------------------------------
B1_TERMS = [
    _p("multi turn"), _p("multi round"), r"\bconversational\b",
    _p("context dependent"), _p("context aware"), r"\bdialog\w*",
    _p("follow up"), r"\binteractive\b", r"\bsessions?\b",
    r"\bchat\b", r"\bchatbots?\b", _p("chat based"),
    r"\bcoreference\w*", r"\bellipsis\b", r"\banaphor\w*",
    r"\b(query|question|utterance)" + SEP + r"rewriting\b",
    r"\bsparc\b", r"\bcosql\b",
]

# ---- Block B2: schema linking / joins / self-correction -----------------------------------
B2_TERMS = [
    r"\bschema" + SEP + r"(linking|pruning|selection|retrieval|grounding|filtering|routing)\b",
    _p("keyword mapping"),
    r"\b(table|column)" + SEP + r"(selection|retrieval)\b",
    r"\bvalue" + SEP + r"(linking|retrieval)\b",
    r"\bjoin" + SEP + r"(paths?|inference)\b", r"\bmulti" + SEP + r"hop" + SEP + r"joins?\b",
    r"\bforeign" + SEP + r"keys?\b", r"\bsteiner\b",
    r"\bself" + SEP + r"(correct\w*|debug\w*|refin\w*|consistency)\b",
    r"\bdebugging\b", r"\brefinement\b", r"\breflection\b",
    r"\bverifiers?\b", r"\bverification\b", _p("candidate selection"),
    _p("execution feedback"), _p("execution guided"),
    _p("error correction"), _p("SQL correction"), _p("SQL repair"), _p("query repair"),
]

_A = re.compile("|".join(A_TERMS), re.I)
_SP = re.compile(SEMPARSE, re.I)
_SPC = re.compile(SEMPARSE_CONTEXT, re.I)
_B1 = re.compile("|".join(B1_TERMS), re.I)
_B2 = re.compile("|".join(B2_TERMS), re.I)


def block_a(text):
    return bool(_A.search(text)) or (bool(_SP.search(text)) and bool(_SPC.search(text)))


def matches(title, abstract):
    """Return (selected, reason). reason in {'v4', 'v4_title_only', ''}."""
    title = title or ""
    abstract = (abstract or "").strip()
    if not abstract:
        return (block_a(title), "v4_title_only" if block_a(title) else "")
    text = f"{title} {abstract}"
    ok = block_a(text) and (bool(_B1.search(text)) or bool(_B2.search(text)))
    return (ok, "v4" if ok else "")


if __name__ == "__main__":  # quick self-test on seed-like strings
    tests = [
        ("CoSQL: A Conversational Text-to-SQL Challenge", "dialogue with a database", True),
        ("Dynamic Hybrid Relation Network for Cross-Domain Context-Dependent Semantic Parsing",
         "contextual information of natural language utterance and database schemas; SParC and CoSQL", True),
        ("Reliable Text-to-SQL with Adaptive Abstention", "focuses on the critical schema linking phase", True),
        ("OpenSearch-SQL", "Text-to-SQL task into Preprocessing, Extraction, Generation, and Refinement", True),
        ("DBTagger: Multi-Task Learning for Keyword Mapping in NLIDBs", "", True),
        ("LoRA fine-tuning for text-to-SQL", "We study parameter-efficient fine-tuning on Spider.", False),
        ("Conversational QA over knowledge graphs", "SPARQL queries over Wikidata with dialogue context", False),
        ("ChatGPT for text-to-SQL", "We evaluate ChatGPT zero-shot on Spider.", False),
    ]
    for t, a, exp in tests:
        got = matches(t, a)[0]
        print("OK " if got == exp else "FAIL", got, "|", t)
