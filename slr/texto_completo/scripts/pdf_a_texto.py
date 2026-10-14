"""Phase 7 prep — converts the retrieved PDFs to plain text for full-text screening (cheaper than
page images; same content for eligibility decisions).

- pdftotext (poppler), page by page; each page starts with "=== página N ===" so reviewers can cite pages.
- The reference list and anything after it (appendices) are dropped, but only when the last
  "References"/"Bibliography" heading is in the second half of the text.
- Texts shorter than 3,000 characters (scanned or broken PDFs) fall back to the PDF itself.
Writes texto/<id>.txt (gitignored with the PDFs), ft_map.csv (id,pdf -> file the reviewers read,
for prepare_fulltext.py --map) and conversion_log.csv.
Usage (from slr/texto_completo): python scripts/pdf_a_texto.py
"""
import csv
import os
import re
import argparse
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.abspath(os.path.join(HERE, ".."))
PDF, TXT = os.path.join(T, "pdf"), os.path.join(T, "texto")
MIN_CHARS = 3000


def main():
    global PDF, TXT
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-dir", default="pdf")
    ap.add_argument("--txt-dir", default="texto")
    ap.add_argument("--map", default="ft_map.csv")
    ap.add_argument("--log", default="conversion_log.csv")
    a = ap.parse_args()
    PDF, TXT = os.path.join(T, a.pdf_dir), os.path.join(T, a.txt_dir)
    os.makedirs(TXT, exist_ok=True)
    log, mapping = [], []
    for f in sorted(x for x in os.listdir(PDF) if re.fullmatch(r"R\d{5}\.pdf", x)):
        rid, src = f[:-4], os.path.join(PDF, f)
        raw = subprocess.run(["pdftotext", "-enc", "UTF-8", src, "-"], capture_output=True, text=True).stdout
        pages = raw.split("\f")
        if pages and not pages[-1].strip():
            pages = pages[:-1]
        body = "\n".join(f"=== página {i} ===\n{re.sub(r'[ \t]+', ' ', p).strip()}" for i, p in enumerate(pages, 1))
        body = re.sub(r"\n{3,}", "\n\n", body)
        heads = list(re.finditer(r"(?im)^\s*(\d+\.?\s*)?(references|bibliography)\s*$", body))
        cut = heads[-1].start() if heads and heads[-1].start() > len(body) / 2 else None
        text = body[:cut] + "\n\n=== [lista de referencias y apéndices omitidos] ===\n" if cut else body
        if len(text) < MIN_CHARS:
            target, note = src, "texto insuficiente: se usa el PDF"
        else:
            target, note = os.path.join(TXT, rid + ".txt"), "referencias omitidas" if cut else "sin encabezado de referencias"
            open(target, "w", encoding="utf-8").write(f"[Texto extraído de {f} con pdftotext para el cribado]\n\n{text}")
        mapping.append({"id": rid, "pdf": target})
        log.append({"id": rid, "pages": len(pages), "chars_total": len(body), "chars_used": len(text),
                    "file": os.path.relpath(target, T), "note": note})
    for name, rows in ((a.map, mapping), (a.log, log)):
        with open(os.path.join(T, name), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    n_pdf = sum(r["file"].endswith(".pdf") for r in log)
    print(f"converted {len(log) - n_pdf}; PDF fallback {n_pdf}; "
          f"chars used {sum(r['chars_used'] for r in log) / 1e6:.1f} M of {sum(r['chars_total'] for r in log) / 1e6:.1f} M")


if __name__ == "__main__":
    main()
