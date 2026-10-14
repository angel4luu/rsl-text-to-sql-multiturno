"""Phase 10 — exploratory bibliometrics (amendment A6): OpenAlex metadata of the 396 included studies.

Resolves each study by DOI (else exact normalised title) and stores, unedited, the fields needed for the
citation network, citation counts, countries/institutions and versions. Raw responses ->
slr/sintesis/datos/openalex_estudios.jsonl (one line per study, with the collection date).
Usage (from slr/sintesis): python scripts/openalex_bibliometria.py
"""
import csv
import datetime
import json
import os
import re
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.abspath(os.path.join(HERE, ".."))
SLR = os.path.dirname(S)
UA = {"User-Agent": "SLR-thesis-UNMSM (mailto:angela.jara@unmsm.edu.pe)"}
API = "https://api.openalex.org/works"
SEL = "id,doi,title,publication_year,publication_date,cited_by_count,counts_by_year,authorships,referenced_works,locations,ids,type"


def get(url):
    for k in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 * (k + 1))
    return None


def nt(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def main():
    base = list(csv.DictReader(open(os.path.join(SLR, "extraccion", "base_estudios.csv"), encoding="utf-8")))
    os.makedirs(os.path.join(S, "datos"), exist_ok=True)
    out = open(os.path.join(S, "datos", "openalex_estudios.jsonl"), "w", encoding="utf-8")
    hoy, ok = datetime.date.today().isoformat(), 0
    for n, b in enumerate(base, 1):
        w, how = None, "no_encontrado"
        if b["doi"]:
            w = get(f"{API}/doi:{urllib.parse.quote(b['doi'])}?select={SEL}")
            how = "doi" if w else how
        if not w and b["titulo"]:
            q = urllib.parse.quote(re.sub(r"[^\w\s-]", " ", b["titulo"])[:200])
            for x in (get(f"{API}?filter=title.search:{q}&per-page=10&select={SEL}") or {}).get("results", []):
                if nt(x.get("title")) == nt(b["titulo"]):
                    w, how = x, "titulo"
                    break
        out.write(json.dumps({"id_estudio": b["id_estudio"], "resuelto": how, "fecha": hoy, "work": w}, ensure_ascii=False) + "\n")
        ok += bool(w)
        if n % 50 == 0:
            print(f"{n}/{len(base)} resolved {ok}", flush=True)
        time.sleep(0.12)
    out.close()
    print(f"resolved {ok}/{len(base)}")


if __name__ == "__main__":
    main()
