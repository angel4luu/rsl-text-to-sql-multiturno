"""Shared figure style for the SLR and the thesis.

Usage (from any script in this folder):
    from estilo import aplicar_estilo, guardar, PALETA, ANCHO_COLUMNA
    aplicar_estilo()
    fig, ax = plt.subplots(figsize=(ANCHO_COLUMNA, 2.2))
    ...
    guardar(fig, "nombre")   # -> latex/slr/figuras/nombre.pdf
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

RAIZ = Path(__file__).resolve().parents[3]  # repo root (TH/)
DIR_FIGURAS = {
    "slr": RAIZ / "latex" / "slr" / "figuras",
    "tesis": RAIZ / "latex" / "tesis" / "figuras",
}

# IEEEtran two-column journal: column 3.5 in, full text width 7.16 in
ANCHO_COLUMNA = 3.5
ANCHO_PAGINA = 7.16

# Okabe–Ito: colour-blind-safe categorical palette
PALETA = [
    "#0072B2",  # azul
    "#E69F00",  # naranja
    "#009E73",  # verde
    "#D55E00",  # bermellón
    "#CC79A7",  # púrpura
    "#56B4E9",  # celeste
    "#F0E442",  # amarillo
    "#000000",  # negro
]

# Times-metric TrueType clone, matches IEEEtran body text. TrueType (not OpenType/CFF)
# so embedded fonts pass IEEE PDF eXpress checks.
_FUENTES = [
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
]


def aplicar_estilo(tamano_base: float = 8.0) -> None:
    """Apply the shared rcParams. 8 pt matches IEEE figure text."""
    for f in _FUENTES:
        if Path(f).exists():
            font_manager.fontManager.addfont(f)
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Liberation Serif", "Times New Roman", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "font.size": tamano_base,
        "axes.titlesize": tamano_base,
        "axes.labelsize": tamano_base,
        "xtick.labelsize": tamano_base - 1,
        "ytick.labelsize": tamano_base - 1,
        "legend.fontsize": tamano_base - 1,
        "axes.prop_cycle": mpl.cycler(color=PALETA),
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.linewidth": 0.5,
        "axes.linewidth": 0.6,
        "lines.linewidth": 1.2,
        "figure.dpi": 150,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,  # embed TrueType: editable text, accepted by IEEE PDF checks
        "axes.formatter.use_locale": False,
        "figure.constrained_layout.use": True,  # no clipped labels, consistent spacing
        "legend.frameon": False,
        "axes.axisbelow": True,                 # grid behind the marks
        "grid.color": "#B0B0B0",
        "xtick.direction": "out",
        "ytick.direction": "out",
        "image.cmap": "Blues",                  # sequential = one hue, light -> dark
    })


def guardar(fig: plt.Figure, nombre: str, destino: str = "slr", leyenda: str | None = None) -> Path:
    """Save `fig` as PDF in the LaTeX figures folder of `destino` ('slr' or 'tesis').

    `leyenda` = the figure caption (title + reading note). IEEE puts the title in the caption, not inside the
    image; captions are collected in <figuras>/leyendas.json so the LaTeX text uses exactly these words.
    """
    import json
    carpeta = DIR_FIGURAS[destino]
    carpeta.mkdir(parents=True, exist_ok=True)
    ruta = carpeta / f"{nombre}.pdf"
    fig.savefig(ruta)
    plt.close(fig)
    if leyenda:
        f = carpeta / "leyendas.json"
        d = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
        d[nombre] = leyenda
        f.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
    return ruta
