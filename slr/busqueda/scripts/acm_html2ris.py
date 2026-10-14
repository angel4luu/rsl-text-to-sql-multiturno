"""ACM DL results captured as saved HTML pages (export is premium-only) -> RIS for sr-screener.

The saved pages are the raw, unedited evidence of the ACM search. This script:
1. extracts each result item (DOI + title) from the pages, in page order;
2. completes metadata (authors, year, venue, abstract, type) from OpenAlex by DOI,
   falling back to Crossref; the ACM title is kept as the record title;
3. writes exports/acm/derived/<query>.ris and a JSON log with counts and any gaps.

Usage: python acm_html2ris.py 2026-10-11_acm1 2026-10-11_acm2
"""
import glob
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ACM = os.path.join(HERE, "..", "exports", "acm")
ITEM = re.compile(r'class="issue-item__title"[^>]*>.*?href="/doi/(?:abs/|full/|pdf/)?(10\.\d+/[^"?#]+)"[^>]*>(.*?)</a>', re.S)
UA = {"User-Agent": "SLR-thesis-UNMSM (mailto:angela.jara@unmsm.edu.pe)"}


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def inv(ai):
    if not ai:
        return ""
    return " ".join(w for p, w in sorted((p, w) for w, ps in ai.items() for p in ps))


def openalex(doi):
    try:
        w = get_json("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi))
    except Exception:
        return None
    src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
    return {"authors": [a["author"]["display_name"] for a in w.get("authorships", [])],
            "year": w.get("publication_year"), "venue": src, "abstract": inv(w.get("abstract_inverted_index")),
            "type": w.get("type") or "", "via": "OpenAlex"}


def crossref(doi):
    try:
        m = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
    except Exception:
        return None
    ab = re.sub(r"<[^>]+>", " ", m.get("abstract", "") or "")
    year = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
    return {"authors": [f"{a.get('family', '')}, {a.get('given', '')}".strip(", ") for a in m.get("author", [])],
            "year": year, "venue": (m.get("container-title") or [""])[0], "abstract": " ".join(ab.split()),
            "type": m.get("type", ""), "via": "Crossref"}


def ris(doi, title, md, db):
    ty = "CPAPER" if "proceedings" in (md.get("type") or "") or "conference" in (md.get("type") or "") else "JOUR"
    lines = [f"TY  - {ty}", f"TI  - {title}"]
    lines += [f"AU  - {a}" for a in md.get("authors", []) if a]
    if md.get("year"):
        lines.append(f"PY  - {md['year']}")
    if md.get("venue"):
        lines.append(f"T2  - {md['venue']}")
    lines.append(f"DO  - {doi}")
    if md.get("abstract"):
        lines.append(f"AB  - {md['abstract']}")
    if md.get("type"):
        lines.append(f"M3  - {md['type']}")
    lines += [f"DB  - {db}", f"UR  - https://dl.acm.org/doi/{doi}", "ER  - "]
    return "\n".join(lines)


def run(prefix):
    pages = sorted(glob.glob(os.path.join(ACM, f"{prefix}_p*.html")))
    items = []
    for p in pages:
        h = open(p, encoding="utf-8", errors="replace").read()
        for doi, t in ITEM.findall(h):
            items.append((doi, html.unescape(re.sub(r"<[^>]+>", "", t)).strip(), os.path.basename(p)))
    recs, gaps, via = [], [], {}
    for doi, title, page in items:
        md = openalex(doi) or crossref(doi) or {"via": "none"}
        if md["via"] == "OpenAlex" and not md.get("abstract"):
            cr = crossref(doi)
            if cr and cr.get("abstract"):
                md["abstract"], md["via"] = cr["abstract"], "OpenAlex+Crossref(abstract)"
        via[md["via"]] = via.get(md["via"], 0) + 1
        if not md.get("abstract"):
            gaps.append({"doi": doi, "title": title, "page": page})
        recs.append(ris(doi, title, md, "ACM Digital Library"))
        time.sleep(0.15)
    os.makedirs(os.path.join(ACM, "derived"), exist_ok=True)
    out = os.path.join(ACM, "derived", f"{prefix}.ris")
    open(out, "w", encoding="utf-8").write("\n\n".join(recs) + "\n")
    log = {"query": prefix, "pages": [os.path.basename(p) for p in pages], "items_in_pages": len(items),
           "metadata_source": via, "without_abstract": len(gaps), "without_abstract_list": gaps,
           "derived_ris": os.path.relpath(out, ACM)}
    json.dump(log, open(os.path.join(ACM, f"{prefix}_log.json"), "w"), indent=2, ensure_ascii=False)
    print(json.dumps({k: v for k, v in log.items() if k != "without_abstract_list"}, indent=2))


if __name__ == "__main__":
    for prefix in sys.argv[1:]:
        run(prefix)
