"""Phase 12, step 3: build the public snapshot of the SLR repository (decision of 2026-10-14).

The working repository stays private (its history holds publisher records). This script copies the tracked SLR
files into <destino> and, on the way:
  1. leaves out non-SLR and working material (thesis context, registration form, agent handoffs);
  2. leaves out raw exports whose provider terms restrict redistribution (Scopus, IEEE Xplore, ACM DL pages,
     Semantic Scholar) and archives of unknown content; each is listed in MANIFIESTO_EXCLUIDOS.csv with SHA-256;
  3. removes abstracts (CSV columns, RIS AB fields, JSON keys, BibTeX fields) everywhere except the openly licensed
     arXiv and ACL Anthology exports, then drops any text file that still contains an abstract passage;
  4. rewrites absolute paths of the working copy as paths relative to the repository root;
  5. strips the thesis-only block of latex/comun/metadatos.tex and the `plan` target of the Makefile.
Everything in <destino> except .git is replaced, so the script can be re-run to update the public repository.

Usage (from the repo root): python3 scripts/publicar.py <destino>
"""
import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PLANTILLAS = RAIZ / "scripts" / "publico"

FUERA_DE_ALCANCE = ("00-contexto/", "plan-tesis/", "latex/plan-tesis/", "latex/tesis/", "CLAUDE.md", "README.md",
                    "PLAN_FASES.md")
TRABAJO = re.compile(r"(^|/)HANDOFF[^/]*\.md$")
RESTRINGIDOS = {  # path pattern -> reason (provider terms)
    r"^slr/busqueda/exports/scopus/": "Exportación de Scopus: los términos de Elsevier restringen su redistribución",
    r"^slr/busqueda/exports/ieee/": "Exportación de IEEE Xplore: los términos de IEEE restringen su redistribución",
    r"^slr/busqueda/exports/acm/[^/]+\.html$": "Páginas de resultados de ACM DL guardadas (contenido de ACM)",
    r"^slr/busqueda/exports/_dedup/[^/]*(scopus|ieee|acm)": "Copia para deduplicación de una exportación restringida",
    r"^slr/busqueda/exports/snowballing/[^/]*s2_raw": "Respuesta en bruto de la API de Semantic Scholar",
    r"\.tar\.gz$|\.zip$": "Archivo comprimido de trabajo (registros de ejecución con errores o anexos de OSF)",
}
ABIERTOS = re.compile(r"^slr/busqueda/exports/(arxiv|acl)/|^slr/busqueda/exports/_dedup/[^/]*(arxiv|acl)")
COLUMNAS_RESUMEN = {"abstract", "resumen"}
CLAVES_RESUMEN = {"abstract", "AB", "abstract_inverted_index", "Abstract", "resumen"}
TEXTO = {".py", ".md", ".txt", ".json", ".jsonl", ".csv", ".ris", ".bib", ".tex", ".yaml", ".yml", ".toml", ".js",
         ".sh", ".xml", ".html", "", ".gitkeep", ".gitignore"}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def corpus_resumenes():
    """Opening passages of every abstract seen in screening (to catch abstracts in free text)."""
    out = set()
    for f in ("slr/cribado/sr_work/raw_records.json", "slr/cribado/sr_work_bola/raw_records.json"):
        for r in json.load(open(RAIZ / f, encoding="utf-8")):
            ab = r.get("AB") or ""
            ab = re.sub(r"\s+", " ", " ".join(ab) if isinstance(ab, list) else ab).strip()
            if len(ab) >= 200:
                out.add(ab[40:120])  # skip the opening words, which are often generic
    return out


def sin_resumen_json(x):
    if isinstance(x, dict):
        return {k: sin_resumen_json(v) for k, v in x.items() if k not in CLAVES_RESUMEN}
    if isinstance(x, list):
        return [sin_resumen_json(v) for v in x]
    return x


def limpiar(ruta, texto):
    """Structural abstract removal; returns (new text, changed?)."""
    suf = Path(ruta).suffix
    if suf == ".csv":
        bom = texto.startswith("\ufeff")
        filas = list(csv.reader(io.StringIO(texto.lstrip("\ufeff"))))
        if not filas:
            return texto, False
        quitar = {i for i, c in enumerate(filas[0]) if c.strip().lower() in COLUMNAS_RESUMEN}
        if not quitar:
            return texto, False
        buf = io.StringIO()
        w = csv.writer(buf, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        for f in filas:
            w.writerow([c for i, c in enumerate(f) if i not in quitar])
        return ("\ufeff" if bom else "") + buf.getvalue(), True
    if suf == ".ris":
        lineas, out, en_ab = texto.splitlines(keepends=True), [], False
        for l in lineas:
            if re.match(r"^[A-Z][A-Z0-9]  -", l):
                en_ab = l.startswith("AB  -") or l.startswith("N2  -")
            if not en_ab:
                out.append(l)
        nuevo = "".join(out)
        return nuevo, nuevo != texto
    if suf == ".bib":
        nuevo = re.sub(r"^\s*abstract\s*=\s*\{(?:[^{}]|\{[^{}]*\})*\},?\s*\n", "", texto, flags=re.M | re.I)
        return nuevo, nuevo != texto
    if suf in (".json", ".jsonl"):
        try:
            if suf == ".jsonl":
                objs = [json.loads(l) for l in texto.splitlines() if l.strip()]
                nuevos = [sin_resumen_json(o) for o in objs]
                if nuevos == objs:
                    return texto, False
                return "".join(json.dumps(o, ensure_ascii=False) + "\n" for o in nuevos), True
            obj = json.loads(texto)
        except json.JSONDecodeError:
            return texto, False
        nuevo = sin_resumen_json(obj)
        if nuevo == obj:
            return texto, False
        return json.dumps(nuevo, ensure_ascii=False, indent=1) + "\n", True
    return texto, False


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    destino = Path(sys.argv[1]).resolve()
    assert RAIZ not in destino.parents and destino != RAIZ, "el destino debe estar fuera del repositorio"
    destino.mkdir(parents=True, exist_ok=True)
    for p in destino.iterdir():
        if p.name != ".git":
            shutil.rmtree(p) if p.is_dir() else p.unlink()

    archivos = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=RAIZ, capture_output=True, text=True,
                              check=True).stdout.split("\0")
    archivos = [a for a in archivos if a and not a.startswith(FUERA_DE_ALCANCE) and not TRABAJO.search(a)]
    ruta_abs = str(RAIZ) + "/"
    variantes = {ruta_abs, ruta_abs.replace("'", "\\u0027"), ruta_abs.replace("/", "\\/"),
                 ruta_abs.replace("'", "\\u0027").replace("/", "\\/")}
    resumenes = corpus_resumenes()
    manifiesto, limpiados, rutas_cambiadas = [], 0, 0

    for a in archivos:
        origen = RAIZ / a
        if not origen.exists():
            continue
        motivo = next((m for pat, m in RESTRINGIDOS.items() if re.search(pat, a)), None)
        if motivo:
            manifiesto.append((a, sha(origen), origen.stat().st_size, motivo))
            continue
        dest = destino / a
        dest.parent.mkdir(parents=True, exist_ok=True)
        if origen.suffix not in TEXTO and origen.name not in (".gitignore", ".gitkeep"):
            shutil.copy2(origen, dest)
            continue
        try:
            texto = origen.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            shutil.copy2(origen, dest)
            continue
        if not ABIERTOS.search(a):
            texto, cambio = limpiar(a, texto)
            limpiados += cambio
            plano = re.sub(r"\s+", " ", texto.replace("\\n", " "))
            if any(r in plano for r in resumenes):
                dest.unlink(missing_ok=True)
                manifiesto.append((a, sha(origen), origen.stat().st_size,
                                   "Texto libre que reproduce resúmenes de los registros (hojas de revisión o lotes "
                                   "de cribado); regenerable con los scripts a partir de las exportaciones"))
                continue
        nuevo = texto
        for v in variantes:
            nuevo = nuevo.replace(v, "")
        nuevo = nuevo.replace(str(Path.home()) + "/", "~/")  # other paths in the home folder (e.g. plugin cache)
        rutas_cambiadas += nuevo != texto
        if a == "latex/comun/metadatos.tex":
            nuevo = re.sub(r"% --- Tesis.*?(?=% --- RSL)", "", nuevo, flags=re.S)
        if a == "Makefile":
            nuevo = re.sub(r"\n## Compile the thesis registration form.*?\n(?=\n##|\Z)", "\n", nuevo, flags=re.S)
            nuevo = nuevo.replace(".PHONY: figs tablas slr plan clean", ".PHONY: figs tablas slr clean")
        dest.write_text(nuevo, encoding="utf-8")

    for p in PLANTILLAS.iterdir():  # README, licenses
        shutil.copy2(p, destino / p.name)
    with open(destino / "MANIFIESTO_EXCLUIDOS.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["archivo", "sha256", "bytes", "motivo"])
        w.writerows(sorted(manifiesto))

    # final checks on the snapshot
    restos = [str(p.relative_to(destino)) for p in destino.rglob("*") if p.is_file() and ".git" not in p.parts
              and str(Path.home()) in p.read_text(encoding="utf-8", errors="ignore")]
    print(f"copiados: {sum(1 for p in destino.rglob('*') if p.is_file() and '.git' not in p.parts)} archivos; "
          f"excluidos: {len(manifiesto)}; con resúmenes eliminados: {limpiados}; rutas reescritas: {rutas_cambiadas}")
    if restos:
        print("ATENCIÓN, rutas absolutas restantes en:", *restos[:20], sep="\n  ")


if __name__ == "__main__":
    main()
