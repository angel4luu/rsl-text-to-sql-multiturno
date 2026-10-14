"""Minimal, dependency-free BibTeX -> RIS converter for sr-screener (which does not read BibTeX).

The raw .bib export is kept unedited; the .ris is a derived file written next to it under
`derived/`. Usage:  python bib2ris.py input.bib output.ris --db "ACM DL"
"""
import argparse
import re

TYPES = {"article": "JOUR", "inproceedings": "CPAPER", "conference": "CPAPER",
         "proceedings": "CONF", "book": "BOOK", "incollection": "CHAP", "inbook": "CHAP",
         "phdthesis": "THES", "mastersthesis": "THES", "techreport": "RPRT", "misc": "GEN"}


def split_entries(text):
    """Yield (type, key, body) for each @type{key, ...} entry, brace-aware."""
    i = 0
    n = len(text)
    while True:
        m = re.compile(r"@(\w+)\s*\{").search(text, i)
        if not m:
            return
        etype = m.group(1).lower()
        depth, j = 1, m.end()
        while j < n and depth:
            c = text[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        body = text[m.end():j - 1]
        i = j
        if etype in ("comment", "string", "preamble"):
            continue
        key, _, fields = body.partition(",")
        yield etype, key.strip(), fields


def parse_fields(fields):
    """Parse `name = {value}` / `name = "value"` / `name = 123` pairs, brace-aware."""
    out = {}
    i, n = 0, len(fields)
    while i < n:
        m = re.compile(r"\s*,?\s*([A-Za-z_\-]+)\s*=\s*").match(fields, i)
        if not m:
            break
        name = m.group(1).lower()
        j = m.end()
        if j >= n:
            break
        if fields[j] == "{":
            depth, k = 1, j + 1
            while k < n and depth:
                if fields[k] == "{":
                    depth += 1
                elif fields[k] == "}":
                    depth -= 1
                k += 1
            val = fields[j + 1:k - 1]
        elif fields[j] == '"':
            k = j + 1
            while k < n and not (fields[k] == '"' and fields[k - 1] != "\\"):
                k += 1
            val = fields[j + 1:k]
            k += 1
        else:
            k = j
            while k < n and fields[k] not in ",\n":
                k += 1
            val = fields[j:k]
        out[name] = clean(val)
        i = k
    return out


def clean(v):
    v = re.sub(r"\\[a-zA-Z]+\s*\{([^{}]*)\}", r"\1", v)   # \emph{x} -> x
    v = re.sub(r"\\['`^\"~=.uvHtcdbk]\s*\{?([A-Za-z])\}?", r"\1", v)  # accents -> base letter
    v = v.replace("{", "").replace("}", "").replace("\\&", "&").replace("~", " ")
    return re.sub(r"\s+", " ", v).strip()


def entry_to_ris(etype, key, f, db):
    lines = [f"TY  - {TYPES.get(etype, 'GEN')}"]
    if f.get("title"):
        lines.append(f"TI  - {f['title']}")
    for a in re.split(r"\s+and\s+", f.get("author", "")):
        if a.strip():
            lines.append(f"AU  - {a.strip()}")
    if f.get("year"):
        lines.append(f"PY  - {f['year']}")
    src = f.get("journal") or f.get("booktitle")
    if src:
        lines.append(f"T2  - {src}")
    if f.get("doi"):
        lines.append(f"DO  - {f['doi']}")
    if f.get("url"):
        lines.append(f"UR  - {f['url']}")
    if f.get("abstract"):
        lines.append(f"AB  - {f['abstract']}")
    for kw in re.split(r"[;,]\s*", f.get("keywords", "")):
        if kw.strip():
            lines.append(f"KW  - {kw.strip()}")
    if f.get("pages"):
        lines.append(f"SP  - {f['pages']}")
    if f.get("language"):
        lines.append(f"LA  - {f['language']}")
    lines.append(f"DB  - {db}")
    lines.append(f"ID  - {key}")
    lines.append("ER  - ")
    return "\n".join(lines)


def convert(text, db):
    recs = []
    for etype, key, fields in split_entries(text):
        f = parse_fields(fields)
        recs.append(entry_to_ris(etype, key, f, db))
    return recs


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--db", required=True)
    a = ap.parse_args()
    recs = convert(open(a.inp, encoding="utf-8").read(), a.db)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(recs) + "\n")
    print(f"{len(recs)} records -> {a.out}")
