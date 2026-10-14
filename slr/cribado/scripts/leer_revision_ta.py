"""Reads the reviewer's answers in revision_ta.md and writes overrides.csv (id,d,code,why,by)
for merge_decisions.py --overrides. Every answered record becomes a human decision (OK = the AI
suggestion, confirmed by the reviewer). Unanswered records are listed and nothing is written.
Usage (from slr/cribado): python scripts/leer_revision_ta.py
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "..")
LAB = {"I": ("include", "INC"), "U": ("unclear", "UNC")}


def main():
    text = open(os.path.join(C, "revision_ta.md"), encoding="utf-8").read()
    blocks = re.split(r"(?m)^### ", text)[1:]
    rows, missing = [], []
    for b in blocks:
        rid = re.search(r"\b(R\d{5})\b", b).group(1)
        sug = re.search(r"\*\*Sugerencia IA:\*\* (\S+)", b).group(1)
        m = re.search(r"\*\*Decisión:\*\*[ \t]*(\S*)[ \t]*(?:[—-][ \t]*(.*))?", b)
        ans = (m.group(1) if m else "").upper()
        note = (m.group(2) or "").strip() if m else ""
        if not ans:
            missing.append(rid)
            continue
        val = sug if ans == "OK" else ans
        if val in LAB:
            d, code = LAB[val]
        elif re.fullmatch(r"E[1-6]", val):
            d, code = "exclude", val
        else:
            sys.exit(f"{rid}: answer not understood: {ans!r}")
        why = note or ("Reviewer confirmed AI suggestion" if ans == "OK" else "Reviewer decision")
        rows.append([rid, d, code, why, "AJE"])
    if missing:
        sys.exit(f"unanswered ({len(missing)}): {', '.join(missing)}")
    with open(os.path.join(C, "overrides.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "d", "code", "why", "by"])
        w.writerows(rows)
    print(f"overrides.csv: {len(rows)} decisions")


if __name__ == "__main__":
    main()
