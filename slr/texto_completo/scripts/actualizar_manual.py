"""Applies the author's manual retrieval (pendientes_recuperacion.md + pdf/) to retrieval_log.csv, offline.

A record counts as retrieved only if pdf/<id>.pdf exists and starts with %PDF; the sheet's note must
then say "retrieved" (any mismatch stops the script). Notes for the rest: "withdrawn" -> retirado,
"not found" -> no encontrado, "no access" or empty -> sin acceso (the author's convention).
Usage (from slr/texto_completo): python scripts/actualizar_manual.py
"""
import argparse
import csv
import datetime
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "..")
REASON = {"withdrawn": "retirado (según la autora)", "not found": "no encontrado (búsqueda manual de la autora)"}


def local_path(value):
    return value if os.path.isabs(value) else os.path.abspath(os.path.join(T, value))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", default="pendientes_recuperacion.md")
    ap.add_argument("--pdf-dir", default="pdf")
    ap.add_argument("--log", default="retrieval_log.csv")
    args = ap.parse_args()
    sheet, pdf_dir, path = map(local_path, (args.sheet, args.pdf_dir, args.log))
    notes = {}
    for line in open(sheet, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) > 2 and re.fullmatch(r"R\d{5}", cells[1]):
            notes[cells[1]] = cells[-1].lower()
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    problems, today = [], datetime.date.today().isoformat()
    for r in rows:
        if r["status"] == "recuperado" or r["id"] not in notes:
            continue
        note = notes[r["id"]]
        pdf = os.path.join(pdf_dir, f"{r['id']}.pdf")
        has = os.path.exists(pdf) and open(pdf, "rb").read(4) == b"%PDF"
        if has != (note == "retrieved"):
            problems.append(f"{r['id']}: note={note!r} pdf={'yes' if has else 'no'}")
            continue
        if has:
            r.update(status="recuperado", route="manual (autora)", version="por verificar", url="",
                     reason="", date=today, bytes=os.path.getsize(pdf))
        else:
            r.update(reason=REASON.get(note, "sin acceso (autora: biblioteca UNMSM / editorial)"), date=today)
    if problems:
        sys.exit("mismatch between sheet and pdf/:\n" + "\n".join(problems))
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    got = sum(r["status"] == "recuperado" for r in rows)
    print(f"retrieved {got}/{len(rows)}; not retrieved {len(rows) - got}")


if __name__ == "__main__":
    main()
