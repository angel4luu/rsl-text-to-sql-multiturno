"""Phase 11, step 2: builds verified BibTeX for the SLR article.

Sources, in order: DBLP (title search, matched by DOI or title+year) -> doi.org content negotiation
(Crossref/DataCite) -> OpenAlex (title search, for records without DOI). Every entry is checked against the
expected title; low-similarity matches are not written and go to the review sheet.

Outputs:
  bib/estudios_incluidos.bib    the 390 included studies (skips those already in referencias.bib)
  bib/claves_estudios.csv       id_estudio -> clave_bib, source, status
  bib/referencias_metodo.bib    methods references and prior reviews (merged into referencias.bib after review)
  bib/verificacion_citas.csv    one row per reference: key, source, doi, title similarity, status
Usage (from repo root): python3 bib/scripts/construir_bib.py
"""
import csv
import difflib
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BIB = os.path.join(ROOT, "bib")
CACHE = os.path.join(BIB, ".cache")
UA = {"User-Agent": "slr-bib-builder/1.0 (mailto:ai.agent@probaar.co)"}
# DBLP (dblp.org) timed out and its mirrors serve a bot challenge on 2026-10-13: set DBLP=1 to re-enable.
MONTHS = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
USE_DBLP = os.environ.get("DBLP") == "1"
STOP = {"a", "an", "the", "on", "of", "for", "to", "in", "and", "with", "towards", "toward", "via", "is", "are",
        "how", "what", "do", "does", "can", "by", "from", "at", "as", "when", "why", "we", "your", "beyond", "not"}

# Methods references and prior reviews (outline §6). doi=None -> title search only.
MANUAL = [
    ("Page2021PRISMA", "10.1136/bmj.n71", "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews", 2021),
    ("Moher2015PRISMAP", "10.1186/2046-4053-4-1", "Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement", 2015),
    ("Rethlefsen2021PRISMAS", "10.1186/s13643-020-01542-z", "PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews", 2021),
    ("Campbell2020SWiM", "10.1136/bmj.l6890", "Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline", 2020),
    ("Lewin2018CERQual", "10.1186/s13012-017-0688-3", "Applying GRADE-CERQual to qualitative evidence synthesis findings: introduction to the series", 2018),
    ("Wilson1927Probable", "10.1080/01621459.1927.10502953", "Probable Inference, the Law of Succession, and Statistical Inference", 1927),
    ("Cochran1954Methods", "10.2307/3001616", "Some Methods for Strengthening the Common chi2 Tests", 1954),
    ("Armitage1955Tests", "10.2307/3001775", "Tests for Linear Trends in Proportions and Frequencies", 1955),
    ("Cohen1960Coefficient", "10.1177/001316446002000104", "A Coefficient of Agreement for Nominal Scales", 1960),
    ("Byrt1993Bias", "10.1016/0895-4356(93)90018-v", "Bias, prevalence and kappa", 1993),
    ("Wohlin2014Snowballing", "10.1145/2601248.2601268", "Guidelines for snowballing in systematic literature studies and a replication in software engineering", 2014),
    ("Priem2022OpenAlex", "10.48550/arXiv.2205.01833", "OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts", 2022),
    ("OSF2026Protocolo", "10.17605/OSF.IO/5USF3", None, 2026),
    ("Yu2018Spider", "10.18653/v1/D18-1425", "Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task", 2018),
    ("Li2023BIRD", None, "Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs", 2023),
    ("Zhong2017Seq2SQL", None, "Seq2SQL: Generating Structured Queries from Natural Language using Reinforcement Learning", 2017),
    ("Li2020ContextSurvey", "10.18653/v1/2020.coling-main.226", "Context Dependent Semantic Parsing: A Survey", 2020),
    ("Liu2026NLIDBReview", "10.1007/s11704-025-50592-w", "A systematic review of natural language interfaces for databases", 2026),
    ("Bui2026Survey", "10.7717/peerj-cs.3773", "A systematic survey of LLM-based text-to-SQL: methodologies, security vulnerabilities, and future challenges", 2026),
    ("Liu2025SurveyLLMs", "10.1109/TKDE.2025.3592032", "A Survey of Text-to-SQL in the Era of LLMs", 2025),
    ("Katsogiannis2023Survey", None, "A survey on deep learning approaches for text-to-SQL", 2023),
    ("Deng2022Recent", None, "Recent Advances in Text-to-SQL: A Survey of What We Have and What We Expect", 2022),
    ("Abbas2022NLIDB", "10.1109/ACCESS.2022.3147586", None, 2022),
    ("OrtizDelgado2026RAG", "10.17605/osf.io/qgr2x", None, 2026),
    # plan de tesis (2026-10-14): contexto local verificado por DOI (OpenAlex)
    ("QuinterosNavarro2025BI", "10.58861/tae.bm.2025.3.06", "Impact of business intelligence on the economic growth of small and medium-sized enterprises (SMEs): evidence from the Lima Plaza case", 2025),
    ("Leigh2024BIAdoption", "10.5220/0012894800003825", "Business Intelligence Solutions Adoption Model for Peruvians SMEs Based on UTAUT2", 2024),
    ("MoranSantamaria2026BI", "10.12688/f1000research.167062.1", "Business Intelligence and the export competitiveness of lambayecan SMEs in the north of Peru", 2026),
    ("PerezCampdesuner2025AI", "10.3390/info16060443", "Artificial Intelligence in Ecuadorian SMEs: Drivers and Obstacles to Adoption", 2025),
    ("Pazos2022Wizard", "10.61467/2007.1558.2022.v13i3.304", "Wizard for creating semantic views in a natural language interface to databases", 2022),
    ("Hevner2004DesignScience", "10.2307/25148625", "Design Science in Information Systems Research", 2004),
    ("Peffers2007DSRM", "10.2753/MIS0742-1222240302", "A Design Science Research Methodology for Information Systems Research", 2007),
    ("Kinney2023SemanticScholar", "10.48550/arXiv.2301.10140", "The Semantic Scholar Open Data Platform", 2023),
]


# Author decisions, bib/revision_citas.md (2026-10-13): C1 a, C2 a (Hong 2025 dropped), C3 a, C4 a.
STATIC = [
    """@techreport{Kitchenham2007Guidelines,
  author = {Barbara Kitchenham and Stuart Charters},
  title = {Guidelines for performing Systematic Literature Reviews in Software Engineering},
  institution = {Keele University and Durham University},
  type = {Informe t\\'{e}cnico},
  number = {EBSE-2007-01},
  year = {2007},
  note = {Versi\\'{o}n 2.3. Sin DOI; verificada por la autora (C1)}
}""",
    """@software{ARS2026,
  author = {{Imbad0202}},
  title = {Academic Research Skills (sr-screener)},
  version = {3.23.0},
  url = {https://github.com/Imbad0202/academic-research-skills},
  urldate = {2026-10-13},
  note = {Versi\\'{o}n usada seg\\'{u}n el protocolo registrado; URL verificada (HTTP 200) el 2026-10-13}
}""",
    """@online{TCS2026,
  author = {{Think. Check. Submit.}},
  title = {Think. Check. Submit.},
  url = {https://thinkchecksubmit.org/},
  urldate = {2026-10-13},
  note = {Verificada por HTTP 200 el 2026-10-13 (C4)}
}""",
]
EXPORT_OK = {"R00005", "R00039", "R00061", "R00065", "R00953"}  # C3 a: metadata from the official export
# OpenAlex matched a repository/arXiv copy with wrong venue or duplicated authors: use the export record (same rule as C3)
EXPORT_FORCE = {"R00935", "R00940"}
UNICODE_TEX = {"χ 2": "$\\chi^2$", "χ2": "$\\chi^2$", "χ": "$\\chi$", "\u2010": "-", "\u2011": "-", "\u00a0": " ",
               "\u2009": " ", "\u202f": " ", "²": "\\textsuperscript{2}"}


def from_export(r):
    journal = "journal" in r["venue"].lower()
    f = {"author": r["autores"].replace("; ", " and "), "title": r["titulo"],
         ("journal" if journal else "booktitle"): r["venue"], "year": r["anio"],
         "note": f"Sin DOI; metadatos de la exportaci\\'{{o}}n oficial de la b\\'{{u}}squeda ({r['id_cribado']})"}
    return "@%s{X,\n%s\n}" % ("article" if journal else "inproceedings",
                                ",\n".join(f"  {k} = {{{v}}}" for k, v in f.items()))


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", re.sub(r"[{}\\]", "", s)).strip()


def sim(a, b):
    if a and b and (norm(a).startswith(norm(b)) or norm(b).startswith(norm(a))) and min(len(norm(a)), len(norm(b))) > 25:
        return 1.0  # short title vs. same title with subtitle
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio() if a and b else 0.0


def get(url, accept=None, pause=0.0):
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, re.sub(r"[^A-Za-z0-9]+", "_", url)[-180:] + "_" + hashlib.md5(url.encode()).hexdigest()[:10])
    if os.path.exists(f):
        return open(f, encoding="utf-8").read()
    h = dict(UA)
    if accept:
        h["Accept"] = accept
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=30) as r:
                txt = r.read().decode("utf-8", "replace")
            break
        except urllib.error.HTTPError as e:
            if e.code in (404, 400):
                txt = ""
                break
            time.sleep(5 * (attempt + 1))
        except Exception:
            time.sleep(5 * (attempt + 1))
    else:
        return None  # network failure: not cached, retried on next run
    time.sleep(pause)
    open(f, "w", encoding="utf-8").write(txt)
    return txt


def dblp(title, doi, year):
    q = urllib.parse.quote(norm(title)[:200])
    txt = get(f"https://dblp.org/search/publ/api?q={q}&format=json&h=10", pause=1.2)
    try:
        hits = json.loads(txt)["result"]["hits"].get("hit", [])
    except Exception:
        return None
    best = None
    for h in hits:
        i = h["info"]
        if doi and i.get("doi", "").lower() == doi.lower():
            best = i
            break
        if sim(i.get("title", ""), title) > 0.93 and abs(int(i.get("year", 0)) - year) <= 1:
            # prefer the published version over CoRR when no DOI match
            if best is None or (best.get("venue") == "CoRR" and i.get("venue") != "CoRR"):
                best = i
    if not best:
        return None
    bib = get(f"https://dblp.org/rec/{best['key']}.bib", pause=1.2)
    return bib if bib and bib.lstrip().startswith("@") else None


def doi_bib(doi):
    bib = get("https://doi.org/" + urllib.parse.quote(doi, safe="/()"), accept="application/x-bibtex")
    return bib.strip() if bib and bib.strip().startswith("@") else None


def openalex(title, year):
    q = urllib.parse.quote(norm(title)[:200])
    txt = get(f"https://api.openalex.org/works?search={q}&per-page=5&mailto=ai.agent@probaar.co")
    try:
        res = json.loads(txt)["results"]
    except Exception:
        return None
    for w in res:
        if sim(w.get("title") or "", title) > 0.93 and abs((w.get("publication_year") or 0) - year) <= 1:
            return w
    return None


def oa_to_bib(w):
    au = " and ".join(a["author"]["display_name"] for a in w.get("authorships", []))
    src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
    typ = "inproceedings" if "proceed" in src.lower() or "conference" in src.lower() else "article"
    venue = "booktitle" if typ == "inproceedings" else "journal"
    f = {"author": au, "title": w["title"], venue: src, "year": str(w["publication_year"])}
    if w.get("doi"):
        f["doi"] = w["doi"].replace("https://doi.org/", "")
    f["note"] = "Metadatos de OpenAlex " + w["id"].rsplit("/", 1)[-1]
    return "@%s{X,\n%s\n}" % (typ, ",\n".join(f"  {k} = {{{v}}}" for k, v in f.items() if v))


def field(bib, name):
    """Brace-aware value of a BibTeX field ({...} or "...")."""
    m = re.search(r"(?:^|[,\s])" + name + r"\s*=\s*", bib or "", re.I)
    if not m:
        return ""
    i = m.end()
    if i < len(bib) and bib[i] == "{":
        d, j = 0, i
        while j < len(bib):
            d += {"{": 1, "}": -1}.get(bib[j], 0)
            if d == 0:
                break
            j += 1
        v = bib[i + 1:j]
    elif i < len(bib) and bib[i] == '"':
        v = bib[i + 1:bib.index('"', i + 1)]
    else:
        v = re.match(r"[^,}\n]*", bib[i:]).group(0)
    return re.sub(r"\s+", " ", v).strip()


def only_main(bib):
    """DBLP .bib may append crossref parents; keep the first entry only."""
    parts = re.split(r"\n(?=@)", bib.strip())
    return parts[0].strip()


def make_key(bib, used):
    au = field(bib, "author").split(" and ")[0]
    last = au.split(",")[0] if "," in au else (au.split()[-1] if au.split() else "Anon")
    last = re.sub(r"[^A-Za-z]", "", unicodedata.normalize("NFKD", re.sub(r"\{\\.\}|\\.", "", last))
                  .encode("ascii", "ignore").decode()) or "Anon"
    last = re.sub(r"\d+$", "", last)
    title = re.sub(r"[{}\\]", "", field(bib, "title"))
    head = title.split(":")[0].strip()
    word = head if ":" in title and len(head.split()) == 1 else next(
        (w for w in re.findall(r"[A-Za-z0-9\-]+", title) if w.lower() not in STOP), "X")
    word = re.sub(r"[^A-Za-z0-9]", "", word)
    word = word if any(c.isupper() for c in word[1:]) else word.capitalize()
    base = f"{last[0].upper()}{last[1:]}{field(bib, 'year')}{word}"
    k, n = base, 0
    while k in used:
        n += 1
        k = base + "abcdefghij"[n - 1]
    used.add(k)
    return k


def rekey(bib, key):
    bib = re.sub(r",?\s*(collection|series)\s*=\s*\{interspeech_\d+\}", "", bib)  # Crossref/ISCA internal ids
    bib = bib.replace("Systems Research1}", "Systems Research}")
    bib = re.sub(r"author\s*=\s*\{\s*and\s+", "author={", bib)  # Crossref group author with empty name (PRISMA-P)
    if key == "QuinterosNavarro2025BI":  # Crossref stores the title in capitals
        bib = re.sub(r"title=\{[^}]*\}", "title={Impact of business intelligence on the economic growth of small and "
                     "medium-sized enterprises ({SMEs}): Evidence from the {Lima Plaza} case}", bib, count=1)  # Crossref footnote marker (Hevner 2004)
    for a, b in UNICODE_TEX.items():
        bib = bib.replace(a, b)
    bib = bib.replace("&amp;", "\\&").replace("&lt;", "<").replace("&gt;", ">")
    bib = re.sub(r"^(@\w+\s*\{)[^,]*,", r"\g<1>" + key + ",", only_main(bib), count=1)
    bib = re.sub(r"month\s*=\s*\{?([A-Za-z]+)\.?\}?", lambda m: "month={%d}" % MONTHS[m.group(1)[:3].lower()]
                 if m.group(1)[:3].lower() in MONTHS else m.group(0), bib)
    return re.sub(r"\n\s*(timestamp|biburl|bibsource)\s*=\s*\{[^}]*\},?", "", bib)


def resolve(title, doi, year):
    """Returns (bib, source, similarity)."""
    if title and USE_DBLP:
        b = dblp(title, doi, year)
        if b:
            return b, "DBLP", sim(field(b, "title"), title)
    if doi:
        b = doi_bib(doi)
        if b:
            return b, "doi.org", sim(field(b, "title"), title) if title else 1.0
    if title:
        w = openalex(title, year)
        if w:
            return oa_to_bib(w), "OpenAlex", sim(w["title"], title)
    return None, "", 0.0


def main():
    existing = open(os.path.join(BIB, "referencias.bib"), encoding="utf-8").read()
    ex_keys = set(re.findall(r"^@\w+\{([^,]+),", existing, re.M))
    ex_doi = {}
    for ent in re.split(r"\n(?=@)", existing):
        k = re.match(r"\s*@\w+\{([^,]+),", ent)
        d = field(ent, "doi")
        if k and d:
            ex_doi[d.lower().replace("\\_", "_")] = k.group(1)
    used = set(ex_keys)
    studies = list(csv.DictReader(open(os.path.join(ROOT, "slr/extraccion/base_estudios.csv"), encoding="utf-8")))
    verif, claves, out = [], [], []
    for i, r in enumerate(studies, 1):
        doi = r["doi"].strip().lower() or None
        if doi and doi in ex_doi:
            claves.append([r["id_estudio"], ex_doi[doi], "referencias.bib", "", "1.00", "existente"])
            continue
        bib, src, s = (None, "", 0.0) if r["id_estudio"] in EXPORT_FORCE else resolve(r["titulo"], doi, int(r["anio"] or 0))
        if not bib and r["id_estudio"] in EXPORT_OK | EXPORT_FORCE:
            bib, src, s = from_export(r), "exportación", 1.0
        estado = "ok" if bib and s >= 0.90 else ("revisar" if bib else "no_resuelto")
        key = make_key(bib, used) if bib else ""
        if estado == "ok":
            out.append(rekey(bib, key))
        claves.append([r["id_estudio"], key if estado == "ok" else "", src, doi or "", f"{s:.2f}", estado])
        print(f"{i}/{len(studies)} {r['id_estudio']} {src or '-'} {s:.2f} {estado}", flush=True)
    new = []
    for key, doi, title, year in MANUAL:
        bib, src, s = resolve(title, doi, year)
        estado = "ok" if bib and s >= 0.90 else ("revisar" if bib else "no_resuelto")
        if bib:
            new.append((estado, rekey(bib, key)))
        verif.append([key, src, doi or "", field(bib, "title") if bib else "", f"{s:.2f}", estado])
        print(f"{key} {src or '-'} {s:.2f} {estado}", flush=True)
    open(os.path.join(BIB, "estudios_incluidos.bib"), "w", encoding="utf-8").write(
        "% Generado por bib/scripts/construir_bib.py — no editar a mano.\n\n" + "\n\n".join(out) + "\n")
    open(os.path.join(BIB, "referencias_metodo.bib"), "w", encoding="utf-8").write(
        "% Generado por bib/scripts/construir_bib.py. Entradas 'revisar' comentadas hasta confirmación.\n\n"
        + "\n\n".join(STATIC) + "\n\n"
        + "\n\n".join(b if e == "ok" else "% REVISAR\n" + re.sub(r"^", "% ", b, flags=re.M) for e, b in new) + "\n")
    with open(os.path.join(BIB, "claves_estudios.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id_estudio", "clave_bib", "fuente", "doi", "similitud_titulo", "estado"])
        w.writerows(claves)
    with open(os.path.join(BIB, "verificacion_citas.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["clave", "fuente", "doi", "titulo_recuperado", "similitud_titulo", "estado"])
        w.writerows(verif)
    verif += [[re.match(r"@\w+\{([^,]+)", b).group(1), "autora", "", field(b, "title"), "1.00", "ok"] for b in STATIC]
    from collections import Counter
    print("estudios:", dict(Counter(c[-1] for c in claves)), "| fuentes:", dict(Counter(c[2] for c in claves)))
    print("referencias:", dict(Counter(v[-1] for v in verif)))


if __name__ == "__main__":
    sys.exit(main())
