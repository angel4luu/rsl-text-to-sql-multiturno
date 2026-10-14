"""Option 2 (cost) — screening excerpts of the full texts, for reports no reviewer has decided yet.

Excerpt = pages 1-2 (title, abstract, introduction, contributions) + the first page whose text has an
Experiments / Evaluation / Results / Experimental setup heading and the page after it (datasets,
benchmarks, metrics, results). At most 5 pages; if no such heading is found, pages 1-4. Page markers
are kept, so reviewers still cite real page numbers; omitted pages are marked.
Modes:
  --pending  : reports without ANY reviewer decision (sr_work/runs/*_ft) get the excerpt in texto/<id>.txt;
               the full text is moved first to texto_full/<id>.txt (prompt files keep pointing to texto/).
               Reports with at least one decision keep their full text, so A and B of a report always
               see the same version.
  --calib IDS: excerpts written to texto_calib/<id>.txt only (calibration; texto/ is not touched).
Writes/updates conversion_log_extracto.csv. Usage (from slr/texto_completo):
  python scripts/acortar_textos.py --pending        |  python scripts/acortar_textos.py --calib R00003,R00128
"""
import argparse
import csv
import glob
import json
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.abspath(os.path.join(HERE, ".."))
RUNS = os.path.join(T, "..", "cribado", "sr_work", "runs")
HEAD = re.compile(r"(?im)^\s*(\d+(\.\d+)*\.?\s*)?(experiments?|experimental (setup|settings?|results)|evaluation|"
                  r"results( and (discussion|analysis))?|empirical (study|evaluation))\s*$")
NOTE = ("[Extracto para el cribado de texto completo: contiene las páginas con título, resumen, introducción "
        "y contribuciones, y las páginas de la sección experimental (datos, benchmarks, métricas y resultados) "
        "del informe. Las demás páginas no se incluyen en este archivo.]")


def decided_ids(runs=None):
    runs = runs or RUNS
    ids = set()
    for d in ("manual_ft", "cli_ft", "codex_ft"):
        for f in glob.glob(os.path.join(runs, d, "FT[AB]_R*.json")):
            if not f.endswith(".error.json"):
                ids.add(re.search(r"(R\d{5})", os.path.basename(f)).group(1))
    return ids


def excerpt(full):
    parts = re.split(r"(?m)^=== página (\d+) ===\n", full)
    header, pages = parts[0], {int(parts[i]): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
    n = max(pages) if pages else 0
    exp = next((p for p in sorted(pages) if p > 2 and HEAD.search(pages[p])), None)
    keep = [1, 2] + ([exp, exp + 1] if exp else [3, 4])
    keep = sorted({p for p in keep if p in pages})[:5]
    out, prev = [NOTE, ""], 0
    for p in keep:
        if p > prev + 1:
            out.append(f"=== [páginas {prev + 1}–{p - 1} no incluidas en el extracto] ===\n")
        out.append(f"=== página {p} ===\n{pages[p].strip()}\n")
        prev = p
    if n > prev:
        out.append(f"=== [páginas {prev + 1}–{n} no incluidas en el extracto] ===")
    return header.strip() + "\n\n" + "\n".join(out), keep, n


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pending", action="store_true")
    g.add_argument("--calib")
    ap.add_argument("--txt-dir", default="texto")
    ap.add_argument("--full-dir", default="texto_full")
    ap.add_argument("--runs-dir", default=RUNS)
    ap.add_argument("--log", default="conversion_log_extracto.csv")
    a = ap.parse_args()
    txt, full_dir = os.path.join(T, a.txt_dir), os.path.join(T, a.full_dir)
    if a.calib:
        ids, dest = a.calib.split(","), os.path.join(T, "texto_calib")
    else:
        done = decided_ids(os.path.abspath(os.path.join(T, a.runs_dir)))
        ids = sorted(f[:-4] for f in os.listdir(txt) if f.endswith(".txt") and f[:-4] not in done)
        dest = txt
    os.makedirs(dest, exist_ok=True)
    os.makedirs(full_dir, exist_ok=True)
    log_path = os.path.join(T, a.log)
    log = {r["id"]: r for r in csv.DictReader(open(log_path, encoding="utf-8"))} if os.path.exists(log_path) else {}
    before = after = 0
    for rid in ids:
        backup = os.path.join(full_dir, rid + ".txt")
        src = backup if os.path.exists(backup) else os.path.join(txt, rid + ".txt")
        if not os.path.exists(src):
            continue  # PDF fallback (no text): reviewers read the PDF
        full = open(src, encoding="utf-8").read()
        short, keep, n = excerpt(full)
        if not a.calib and not os.path.exists(backup):
            shutil.copy2(src, backup)
        open(os.path.join(dest, rid + ".txt"), "w", encoding="utf-8").write(short)
        before, after = before + len(full), after + len(short)
        log[rid] = {"id": rid, "uso": "calibración" if a.calib else "cribado", "paginas_total": n,
                    "paginas_extracto": " ".join(map(str, keep)), "chars_completo": len(full), "chars_extracto": len(short)}
    with open(log_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "uso", "paginas_total", "paginas_extracto", "chars_completo", "chars_extracto"])
        w.writeheader()
        w.writerows(log[k] for k in sorted(log))
    print(f"{len(ids)} reports -> {dest}; chars {before / 1e6:.2f} M -> {after / 1e6:.2f} M "
          f"({100 * (1 - after / max(before, 1)):.0f}% less)")


if __name__ == "__main__":
    main()
