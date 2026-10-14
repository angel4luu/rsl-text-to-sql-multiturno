"""Final layout pass: move each float's \\input earlier in the source until it lands close to its first mention.

Target: single-column floats on the page of their first mention (distance 0); full-width floats (figure*/table*,
which LaTeX can never place on the calling page) on the next page (distance 1). Greedy loop: each iteration moves
every float that is later than its target one paragraph up (never above its own section heading), rebuilds and
re-measures; a move that does not improve the total distance is undone. Usage:
  python3 analysis/src/tablas/colocar_flotantes.py [latex_dir]   (default latex/slr; run after the text is final)
"""
import re
import subprocess
import sys
from pathlib import Path

SLR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3] / "latex" / "slr"
SEC = SLR / "secciones"


def compilar():
    subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"], cwd=SLR, capture_output=True)


def medir():
    aux = (SLR / "main.aux").read_text(encoding="utf-8", errors="replace")
    pags = subprocess.run(["pdftotext", "-layout", str(SLR / "main.pdf"), "-"], capture_output=True,
                          text=True).stdout.split("\f")
    out = {}
    for m in re.finditer(r"\\newlabel\{((fig|tab):[^}@]+)\}\{\{([^}]+)\}\{(\d+)\}", aux):
        lab, tipo, num, pag = m.group(1), m.group(2), m.group(3), int(m.group(4))
        pal = "figura" if tipo == "fig" else "tabla"
        pat = re.compile(rf"\b{pal}s?\s+(?:[IVX\d]+\s*(?:,|y)\s*)*{re.escape(num)}\b")
        prim = next((i + 1 for i, p in enumerate(pags) if pat.search(p.replace("\n", " "))), pag)
        out[lab] = (pag, prim)
    return out


def flotantes():
    """label -> (section file, input line text, wide?)"""
    res = {}
    for f in sorted(SEC.glob("0*.tex")):
        for i in re.findall(r"^\\input\{((?:figuras/tex|tablas)/[^}]+)\}\s*$", f.read_text(encoding="utf-8"), re.M):
            src = (SLR / (i + ".tex")).read_text(encoding="utf-8")
            lab = re.search(r"\\label\{([^}]+)\}", src).group(1)
            res[lab] = (f, "\\input{" + i + "}", "figure*" in src or "table*" in src)
    return res


def exceso(m, fl):
    return {lab: (m[lab][0] - m[lab][1]) - (1 if fl[lab][2] else 0) for lab in fl if lab in m}


def subir(f, linea):
    """Move `linea` one paragraph earlier, not above the last \\section heading before it. True if moved."""
    parr = re.split(r"\n\s*\n", f.read_text(encoding="utf-8"))
    k = next(j for j, p in enumerate(parr) if p.strip() == linea)
    if k == 0 or re.match(r"\s*\\section", parr[k - 1]):
        return False
    parr[k - 1], parr[k] = parr[k], parr[k - 1]
    f.write_text("\n\n".join(parr), encoding="utf-8")
    return True


def total(e):
    return sum(abs(v) for v in e.values())


def main():
    compilar()
    fl = flotantes()
    e = exceso(medir(), fl)
    print(f"start: total excess {total(e)}")
    for it in range(25):
        movido = False
        for lab in sorted(e, key=lambda x: -e[x]):
            if e[lab] <= 0:
                continue
            f, linea, _ = fl[lab]
            copia = f.read_text(encoding="utf-8")
            if not subir(f, linea):
                continue
            compilar()
            e2 = exceso(medir(), fl)
            if total(e2) < total(e):
                e, movido = e2, True
                print(f"it {it}: moved {lab} up → total excess {total(e)}")
            else:
                f.write_text(copia, encoding="utf-8")
        if not movido:
            break
    compilar()
    print(f"end: total excess {total(e)}; still late: {[k for k, v in e.items() if v > 0]}")


if __name__ == "__main__":
    main()
