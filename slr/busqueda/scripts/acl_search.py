"""Official ACL Anthology search (protocol §9–10; cadenas.md §5).

1. Downloads the official dump `anthology+abstracts.bib.gz`, records date, URL and SHA-256.
2. Keeps entries from 2019-2026 that match search string v4 on title + abstract
   (entries without an abstract: block A on the title only).
3. Writes the matching entries UNEDITED to exports/acl/<date>_acl_v4.bib,
   a derived RIS for sr-screener, and a JSON log with all counts.

Usage: python acl_search.py            (run from any folder)
"""
import datetime
import gzip
import hashlib
import json
import os
import urllib.request

import bib2ris
import v4

URL = "https://aclanthology.org/anthology+abstracts.bib.gz"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "exports", "acl")
YEARS = range(2019, 2027)


def main():
    today = datetime.date.today().isoformat()
    os.makedirs(os.path.join(OUT, "derived"), exist_ok=True)
    raw_gz = os.path.join(OUT, f"{today}_anthology+abstracts.bib.gz")
    if not os.path.exists(raw_gz):
        urllib.request.urlretrieve(URL, raw_gz)
    sha = hashlib.sha256(open(raw_gz, "rb").read()).hexdigest()
    text = gzip.open(raw_gz, "rt", encoding="utf-8").read()

    total = in_years = sel_full = sel_title = 0
    kept = []
    for etype, key, fields in bib2ris.split_entries(text):
        if etype == "proceedings":      # volume front matter, not papers
            continue
        total += 1
        f = bib2ris.parse_fields(fields)
        try:
            year = int(f.get("year", "0")[:4])
        except ValueError:
            continue
        if year not in YEARS:
            continue
        in_years += 1
        ok, why = v4.matches(f.get("title", ""), f.get("abstract", ""))
        if ok:
            sel_full += why == "v4"
            sel_title += why == "v4_title_only"
            kept.append(f"@{etype}{{{key},{fields}}}")

    bib_out = os.path.join(OUT, f"{today}_acl_v4.bib")
    with open(bib_out, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(kept) + "\n")
    ris_out = os.path.join(OUT, "derived", f"{today}_acl_v4.ris")
    recs = bib2ris.convert(open(bib_out, encoding="utf-8").read(), "ACL Anthology")
    with open(ris_out, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(recs) + "\n")

    log = {"date": today, "source_url": URL, "dump_file": os.path.basename(raw_gz), "sha256": sha,
           "entries_papers": total, "entries_2019_2026": in_years,
           "selected_v4_title_abstract": sel_full, "selected_title_only_no_abstract": sel_title,
           "selected_total": len(kept), "export_bib": os.path.basename(bib_out),
           "derived_ris": os.path.relpath(ris_out, OUT)}
    json.dump(log, open(os.path.join(OUT, f"{today}_acl_log.json"), "w"), indent=2)
    print(json.dumps(log, indent=2))


if __name__ == "__main__":
    main()
