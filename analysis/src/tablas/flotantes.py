"""Layout check: page distance between each figure/table and its first mention in the text.

Float page from main.aux (\\newlabel); first mention = first page whose text contains the lowercase cleveref form
("figura 3", "tabla IV"; captions are capitalised, so they do not match). Usage: python3 analysis/src/tablas/flotantes.py
"""
import re
import subprocess
from pathlib import Path

SLR = Path(__file__).resolve().parents[3] / "latex" / "slr"


def main():
    aux = (SLR / "main.aux").read_text(encoding="utf-8", errors="replace")
    paginas = subprocess.run(["pdftotext", "-layout", str(SLR / "main.pdf"), "-"], capture_output=True,
                             text=True).stdout.split("\f")
    filas = []
    for tipo, num, pag, lab in re.findall(r"\\newlabel\{((fig|tab):[^}]+)\}\{\{([^}]+)\}\{(\d+)\}", aux) and \
            [(m.group(1)[:3], m.group(2), int(m.group(3)), m.group(1))
             for m in re.finditer(r"\\newlabel\{((?:fig|tab):[^}@]+)\}\{\{([^}]+)\}\{(\d+)\}", aux)]:
        palabra = "figura" if tipo == "fig" else "tabla"
        pat = re.compile(rf"\b{palabra}s?\s+(?:[IVX\d]+\s*(?:,|y)\s*)*{re.escape(num)}\b")
        primera = next((i + 1 for i, p in enumerate(paginas) if pat.search(p.replace("\n", " "))), None)
        filas.append((lab, num, pag, primera, None if primera is None else pag - primera))
    for lab, num, pag, primera, d in sorted(filas, key=lambda f: f[2]):
        print(f"{lab:32s} {num:>4s}  float p.{pag:<3d} first mention p.{primera}  distance {d}")
    ds = [abs(f[4]) for f in filas if f[4] is not None]
    print(f"mean |distance| {sum(ds) / len(ds):.2f} pages; >1 page: {sum(d > 1 for d in ds)} of {len(ds)}")


if __name__ == "__main__":
    main()
