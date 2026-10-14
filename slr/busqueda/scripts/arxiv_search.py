"""Official arXiv search (protocol §9–10; cadenas.md §4).

Step 1 (API): block A of string v4 on title OR abstract, submitted 2019-01-01..today,
         via the official API (export.arxiv.org/api/query), 3 s between calls.
Step 2 (local): keep records with at least one cs.* category and apply the FULL v4 string
         (A AND (B1 OR B2)) with the same code used for the ACL Anthology (v4.py).
Raw Atom pages are saved UNEDITED; selected records go to a CSV export (read by sr-screener)
plus a JSON log with every count.

Usage: python arxiv_search.py
"""
import csv
import datetime
import json
import os
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import v4

API = "http://export.arxiv.org/api/query"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "exports", "arxiv")
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
PAGE = 500

A_PHRASES = ['"text to SQL"', "text2sql", "nl2sql", '"NL to SQL"', '"natural language to SQL"',
             '"natural language interface to database"', '"natural language interfaces to databases"',
             '"natural language interface to relational database"',
             '"natural language interfaces to relational databases"', "NLIDB", "NLIDBs",
             '"SQL generation"', '"SQL query generation"', '"SQL synthesis"',
             '"question to SQL"', '"questions to SQL"', '"database question answering"',
             '"question answering over databases"', '"question answering over relational databases"']
SP_CONTEXT = ["SQL", "database", "databases", "SParC", "CoSQL", "Spider", "CHASE"]


def field_or(terms):
    return " OR ".join(f"ti:{t} OR abs:{t}" for t in terms)


def build_query(date_to):
    a = field_or(A_PHRASES)
    sp = f'(ti:"semantic parsing" OR abs:"semantic parsing") AND ({field_or(SP_CONTEXT)})'
    return f"(({a}) OR ({sp})) AND submittedDate:[201901010000 TO {date_to}2359]"


def fetch(query, start):
    params = urllib.parse.urlencode({"search_query": query, "start": start, "max_results": PAGE,
                                     "sortBy": "submittedDate", "sortOrder": "ascending"})
    req = urllib.request.Request(f"{API}?{params}", headers={"User-Agent": "SLR-thesis-UNMSM (mailto:angela.jara@unmsm.edu.pe)"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode("utf-8")


def main():
    today = datetime.date.today()
    tag = today.isoformat()
    raw_dir = os.path.join(OUT, f"{tag}_raw")
    os.makedirs(raw_dir, exist_ok=True)
    query = build_query(today.strftime("%Y%m%d"))

    entries, start, total = [], 0, None
    while True:
        xml = None
        for attempt in range(4):
            try:
                xml = fetch(query, start)
                break
            except Exception as e:  # transient API errors: back off and retry
                time.sleep(10 * (attempt + 1))
        if xml is None:
            raise SystemExit(f"API failed at start={start}")
        with open(os.path.join(raw_dir, f"page_{start:05d}.xml"), "w", encoding="utf-8") as fh:
            fh.write(xml)
        root = ET.fromstring(xml)
        if total is None:
            total = int(root.find("{http://a9.com/-/spec/opensearch/1.1/}totalResults").text)
        page = root.findall("a:entry", NS)
        if not page:
            break
        entries += page
        start += PAGE
        if start >= total:
            break
        time.sleep(3)

    rows, seen = [], set()
    for e in entries:
        aid = e.find("a:id", NS).text.rsplit("/", 1)[-1]
        base = aid.split("v")[0] if "v" in aid else aid
        if base in seen:
            continue
        seen.add(base)
        title = " ".join(e.find("a:title", NS).text.split())
        abstract = " ".join(e.find("a:summary", NS).text.split())
        cats = [c.get("term") for c in e.findall("a:category", NS)]
        doi_el = e.find("arxiv:doi", NS)
        jref = e.find("arxiv:journal_ref", NS)
        rows.append({"arxiv_id": aid, "title": title, "abstract": abstract,
                     "authors": "; ".join(a.find("a:name", NS).text for a in e.findall("a:author", NS)),
                     "year": e.find("a:published", NS).text[:4], "published": e.find("a:published", NS).text[:10],
                     "categories": "; ".join(cats), "doi": doi_el.text if doi_el is not None else f"10.48550/arXiv.{base}",
                     "journal_ref": jref.text if jref is not None else "", "source": "arXiv",
                     "document_type": "Preprint", "url": f"https://arxiv.org/abs/{aid}"})

    cs = [r for r in rows if any(c.startswith("cs.") for c in r["categories"].split("; "))]
    sel = [r for r in cs if v4.matches(r["title"], r["abstract"])[0]]

    cols = ["arxiv_id", "title", "authors", "year", "published", "source", "document_type",
            "doi", "journal_ref", "categories", "url", "abstract"]
    path = os.path.join(OUT, f"{tag}_arxiv_v4.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows({k: r[k] for k in cols} for r in sel)

    log = {"date": tag, "api": API, "query_block_A": query, "page_size": PAGE,
           "api_total_results": total, "unique_records": len(rows), "with_cs_category": len(cs),
           "selected_full_v4": len(sel), "export_csv": os.path.basename(path),
           "raw_pages_dir": os.path.basename(raw_dir)}
    json.dump(log, open(os.path.join(OUT, f"{tag}_arxiv_log.json"), "w"), indent=2)
    print(json.dumps({k: v for k, v in log.items() if k != "query_block_A"}, indent=2))


if __name__ == "__main__":
    main()
