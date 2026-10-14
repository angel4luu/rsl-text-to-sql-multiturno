.PHONY: figs tablas slr clean

FIGS := $(wildcard analysis/src/figs/*.py)
FIGS := $(filter-out analysis/src/figs/estilo.py,$(FIGS))

## Generate every figure (each script saves its own PDF)
figs:
	@for f in $(FIGS); do echo "→ $$f"; uv run --project analysis python $$f || exit 1; done

## Generate the LaTeX tables (and the quality aggregation) from the synthesis outputs
tablas:
	uv run --project analysis python analysis/src/tablas/revision_4f.py
	uv run --project analysis python analysis/src/tablas/tablas.py
	uv run --project analysis python analysis/src/tablas/cifras_metodo.py
	uv run --project analysis python analysis/src/tablas/numeros.py
	uv run --project analysis python analysis/src/tablas/figuras_tex.py
	uv run --project analysis python analysis/src/tablas/apendices.py

## Compile the SLR article
slr:
	cd latex/slr && latexmk main.tex


## Remove LaTeX auxiliary files (keeps PDFs)
clean:
	cd latex/slr && latexmk -c main.tex
