r"""Integrity check of the narrative notes (CLAUDE.md: every number comes from a script output).

For each PI*.md, every number in a sentence that cites a source in brackets ([file.json], [tabla.csv]) must appear
in that source file (decimal comma or point; percentages also checked as proportions, e.g. 11,3 % -> 0.113).
Numbers that cannot be found are listed for correction.
Also checks the article sections (latex/slr/secciones/*.tex): numbers must come from the generated macros in
latex/slr/numeros.tex or from generated tables; any literal number in the prose is reported. Allowed: years,
identifiers such as PI0, D4, A5, M8, CQ2, R00123, and numbers inside \cite/\ref/\label/\en{...} arguments and comments.
Usage (from slr/sintesis): python scripts/verificar_numeros.py
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.abspath(os.path.join(HERE, ".."))
SLR = os.path.dirname(S)
BUSCAR = [S, os.path.join(S, "tablas"), os.path.join(SLR, "protocolo"), os.path.join(SLR, "extraccion"), os.path.join(SLR, "calidad"),
          os.path.join(SLR, "..", "latex", "slr", "figuras")]


def fuente(nombre):
    for d in BUSCAR:
        p = os.path.join(d, nombre)
        if os.path.exists(p):
            return open(p, encoding="utf-8").read()
    return None


def variantes(n):
    x = n.replace(",", ".")
    out = {n, x}
    try:
        f = float(x)
        out |= {f"{f:g}", f"{f:.1f}", f"{f:.2f}", f"{f / 100:.4f}".rstrip("0"), f"{f / 100:.3f}".rstrip("0"), f"{f / 100:.2f}".rstrip("0")}
        if f.is_integer():
            out.add(str(int(f)))
    except ValueError:
        pass
    return {v for v in out if v}


def main():
    problemas, total = [], 0
    for md in sorted(glob.glob(os.path.join(S, "PI*.md"))):
        for linea in open(md, encoding="utf-8"):
            fuentes = [f for b in re.findall(r"\[([^\]]*)\]", linea) for f in re.findall(r"[\w\-.]+\.(?:json|csv|md)", b)]
            if not fuentes:
                continue
            textos = [fuente(f) or "" for f in fuentes]
            texto = re.sub(r"\[[^\]]*\.(?:json|csv|md)[^\]]*\]", " ", linea)
            for n in re.findall(r"(?<![\w.])[-+−]?\d+(?:[.,]\d+)?", texto):
                n = n.replace("−", "-").lstrip("+")
                if re.fullmatch(r"(19|20)\d\d", n) or n.lstrip("-") in ("0", "1", "2", "3", "4", "5", "95"):
                    continue  # years, CI level and small ordinals are not data
                total += 1
                if not any(v in t for t in textos for v in variantes(n) | variantes(n.lstrip("-"))):
                    problemas.append(f"{os.path.basename(md)}: {n} [{', '.join(fuentes)}] :: {linea.strip()[:120]}")
    print(f"numbers checked: {total}; not found in their cited source: {len(problemas)}")
    for p in problemas:
        print("  -", p)



def redondeado_en(n, textos):
    """True if some number in the sources, rounded half-up to n's decimals, equals n (also as a percentage of a
    proportion: 0.1546 -> 15,5). Same rounding rule as the generated tables."""
    from decimal import ROUND_HALF_UP, Decimal
    x = n.replace(",", ".")
    dec = len(x.split(".")[1]) if "." in x else 0
    q = Decimal(1).scaleb(-dec)
    objetivo = Decimal(x)
    for t in textos:
        for m in re.findall(r"-?\d+(?:[.,]\d+)?", t):  # decimal commas appear in the .md notes
            v = Decimal(m.replace(",", "."))
            for c in (v, v * 100):
                if c.quantize(q, rounding=ROUND_HALF_UP) == objetivo:
                    return True
    return False


def verificar_tex():
    """Literal numbers are allowed only in a paragraph tagged '% fuente: a.csv, b.json' (same line or the next
    comment line), and only if each one is found in one of those sources; otherwise they must be macros."""
    sec = os.path.join(SLR, "..", "latex", "slr", "secciones")
    problemas, verificados = [], 0
    for f in sorted(glob.glob(os.path.join(sec, "*.tex"))):
        lineas = open(f, encoding="utf-8").read().split("\n")
        for i, linea in enumerate(lineas, 1):
            sig = lineas[i] if i < len(lineas) else ""
            etiqueta = " ".join(m for m in (linea, sig if sig.lstrip().startswith("%") else "") if "fuente:" in m)
            fuentes = re.findall(r"[\w\-.]+\.(?:json|csv|md)", etiqueta.split("fuente:", 1)[1]) if etiqueta else []
            textos = [fuente(x) or "" for x in fuentes]
            t = re.sub(r"(?<!\\)%.*", "", linea)
            t = re.sub(r"\\pendiente\{[^}]*\}", " ", t)
            t = re.sub(r"\\(?:cite|cref|Cref|ref|label|input|en|url|href|includegraphics|textit|emph)\*?(?:\[[^\]]*\])?\{[^}]*\}", " ", t)
            t = re.sub(r"\\[A-Za-z]+", " ", t)  # macros (numbers come from numeros.tex)
            t = re.sub(r"\b(?:[A-Z]{1,3}\d+[a-z]?|[RB]\d{5}|v\d+)\b", " ", t)  # identifiers: PI0, D4, A5, CQ2, R00123, arXiv v2
            t = re.sub(r"\b(?:Nivel|RoB)[~ ]\d\b", " ", t)  # design levels and tool names (RoB 2)
            t = re.sub(r"\b(?:19|20)\d\d\b", " ", t)  # years
            t = re.sub(r"\bIC[~ ]95|\b95[~ ]?\\%[~ ]?CI\b", " ", t)  # confidence level of the intervals (es/en)
            t = re.sub(r"\b10\.\d{4,9}/\S+", " ", t)  # DOIs
            t = re.sub(r"\\pendiente\{[^}]*\}", " ", t)  # placeholders (flagged separately)
            for n in re.findall(r"-?\d+(?:[.,]\d+)?", t):
                if fuentes and (any(v in x for x in textos for v in variantes(n) | variantes(n.lstrip("-")))
                                or redondeado_en(n, textos)):
                    verificados += 1
                    continue
                donde = f" [no está en {', '.join(fuentes)}]" if fuentes else " [sin macro ni % fuente]"
                problemas.append(f"{os.path.basename(f)}:{i}: {n}{donde} :: {linea.strip()[:90]}")
    # counts written as words escape the digit check: report them («dos estudios», «Diez informes»)
    pal = r"\b(dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|veinte|treinta)( y \w+)?\s+(estudios|registros|informes|curvas|revisiones|contrastes|fuentes)\b"
    for f in sorted(glob.glob(os.path.join(sec, "*.tex"))):
        for i, linea in enumerate(open(f, encoding="utf-8"), 1):
            if not linea.lstrip().startswith("%"):
                for m in re.finditer(pal, linea, re.I):
                    problemas.append(f"{os.path.basename(f)}:{i}: «{m.group(0)}» [cifra escrita en palabras: usar dígitos o macro]")
    print(f"article sections: numbers verified against their % fuente: {verificados}; problems: {len(problemas)}")
    for p in problemas:
        print("  -", p)
    return problemas


if __name__ == "__main__":
    main()
    verificar_tex()
