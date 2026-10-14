"""Phase 11, step 4c: one LaTeX snippet per main-text figure (decision D2 b), caption from leyendas.json.

Figures wider than one IEEE column become figure*; captions are never typed by hand.
Output: latex/slr/figuras/tex/<nombre>.tex (label fig:<nombre>). Usage: make tablas
"""
import json
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
FIG = RAIZ / "latex" / "slr" / "figuras"
PRINCIPALES = ["busqueda_fuentes", "prisma_flujo", "pi0_anio_escenario", "d4_tendencia", "pi_efectos_componentes",
               "pi5_degradacion"]  # others: composite below or supplementary material (2026-10-14)
COLUMNA_PULG = 3.5
TEX = {"≥": r"$\geq$", "≤": r"$\leq$", "×": r"$\times$", "−": r"$-$", "→": r"$\rightarrow$", "Δ": r"$\Delta$",
       "%": r"\%", "&": r"\&", "_": r"\_", "#": r"\#"}


def ancho(pdf):
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    linea = next(l for l in info.splitlines() if l.startswith("Page size"))
    return float(linea.split()[2]) / 72


def main():
    ley = json.load(open(FIG / "leyendas.json", encoding="utf-8"))
    (FIG / "tex").mkdir(exist_ok=True)
    for n in PRINCIPALES:
        cap = ley[n]
        for a, b in TEX.items():
            cap = cap.replace(a, b)
        a = ancho(FIG / f"{n}.pdf")
        doble = a > COLUMNA_PULG + 0.05
        # full-width figures keep their designed size (fonts match the text); never stretched beyond it
        env, w = ("figure*", f"{min(a, 7.16):.2f}in") if doble else ("figure", r"\columnwidth")
        (FIG / "tex" / f"{n}.tex").write_text(
            f"% Generado por analysis/src/tablas/figuras_tex.py — no editar a mano.\n\\begin{{{env}}}[!tbp]\n\\centering\n"
            f"\\includegraphics[width={w},height=0.85\\textheight,keepaspectratio]{{{n}}}\n"
            f"\\caption{{{cap}}}\n\\label{{fig:{n}}}\n\\end{{{env}}}\n", encoding="utf-8")
    # composite (decisions 2026-10-14): IV-D bibliometrics as ONE float with four panels, to keep floats near their
    # mention; community (a), citation network (b), countries (c), base-model families (d)
    def sin_a6(c):
        return c.replace(" Análisis exploratorio (A6).", "").rstrip(".")
    cap = ("Panorama bibliométrico exploratorio (enmienda A6). (a) " + sin_a6(ley["bib_comunidad"]) + ". (b) "
           + sin_a6(ley["bib_red_citas"]) + ". (c) " + sin_a6(ley["bib_paises"]) + ". (d) " + sin_a6(ley["bib_modelos"]) + ".")
    for a, b in TEX.items():
        cap = cap.replace(a, b)
    (FIG / "tex" / "bib_panorama.tex").write_text(
        "% Generado por analysis/src/tablas/figuras_tex.py — no editar a mano.\n\\begin{figure*}[!tbp]\n\\centering\n"
        "\\begin{minipage}[b]{0.56\\textwidth}\\centering\n"
        "\\includegraphics[width=\\linewidth]{bib_comunidad}\\\\(a)\\\\[3pt]\n"
        "\\includegraphics[width=\\linewidth]{bib_red_citas}\\\\(b)\n\\end{minipage}\\hfill\n"
        "\\begin{minipage}[b]{0.42\\textwidth}\\centering\n"
        "\\includegraphics[width=0.82\\linewidth]{bib_paises}\\\\(c)\\\\[3pt]\n"
        "\\includegraphics[width=\\linewidth]{bib_modelos}\\\\(d)\n\\end{minipage}\n"
        f"\\caption{{{cap}}}\n\\label{{fig:bib_panorama}}\n\\end{{figure*}}\n", encoding="utf-8")
    print(f"{len(PRINCIPALES)} figuras + 1 compuesta → latex/slr/figuras/tex/")


if __name__ == "__main__":
    main()
