# Anclaje al esquema en Text-to-SQL multiturno: revisión sistemática PRISMA 2020

Datos, *scripts* y fuentes LaTeX de la revisión sistemática de la literatura (RSL) *Anclaje al esquema en Text-to-SQL
multiturno: revisión sistemática PRISMA 2020 de técnicas, efectos y brechas*, de Angela Lucia Jara Espinoza
(Universidad Nacional Mayor de San Marcos).

*Data, scripts and LaTeX sources of a PRISMA 2020 systematic review on multi-turn (conversational) Text-to-SQL,
written in Spanish.*

- Protocolo registrado en OSF: <https://osf.io/5usf3/> (DOI [10.17605/OSF.IO/5USF3](https://doi.org/10.17605/OSF.IO/5USF3)).
- Artículo compilado: [`latex/slr/main.pdf`](latex/slr/main.pdf); los apéndices A–G recogen las cadenas de búsqueda, los
  informes excluidos, el formulario de extracción, la evaluación de la calidad, las características de los estudios y
  el uso de modelos de IA.

## Contenido

| Carpeta | Contenido |
|---|---|
| `slr/protocolo/` | Protocolo (PRISMA-P), criterios de elegibilidad, protocolo de cribado y registro de enmiendas |
| `slr/busqueda/` | Cadenas, registro de búsquedas, exportaciones de arXiv y ACL Anthology, *scripts* de búsqueda y de bola de nieve |
| `slr/cribado/` | Cribado de título y resumen y de texto completo (sr-screener): registros, decisiones, conflictos, anulaciones |
| `slr/texto_completo/` | Registro de recuperación de textos completos (sin los textos) |
| `slr/extraccion/`, `slr/calidad/` | Formulario, extracción por estudio, resultados, contrastes, evaluación de la calidad y acuerdo |
| `slr/sintesis/` | Síntesis por pregunta de investigación (PI0–PI5), tablas y análisis de sensibilidad |
| `analysis/` | Proyecto Python (uv) que genera todas las figuras y tablas del artículo |
| `bib/` | Referencias verificadas y claves de los estudios incluidos |
| `latex/slr/` | Fuentes del artículo (IEEEtran) |
| `scripts/publicar.py` | *Script* que genera esta copia pública a partir del repositorio de trabajo |

## Qué no se publica

- **Textos completos** de los estudios y *prompts* que incluyen su texto: derechos de autor.
- **Exportaciones en bruto** de Scopus, IEEE Xplore, ACM DL y Semantic Scholar: sus términos de uso restringen la
  redistribución. Cada archivo omitido figura en [`MANIFIESTO_EXCLUIDOS.csv`](MANIFIESTO_EXCLUIDOS.csv) con su suma
  SHA-256; las cadenas exactas y las fechas (apéndice A del artículo y `slr/busqueda/`) permiten repetir las búsquedas.
- **Resúmenes** de los registros: se eliminaron de los registros de cribado y de las exportaciones derivadas. Se conservan
  títulos, DOI, decisiones y motivos. Las exportaciones de arXiv y ACL Anthology se publican sin cambios.

## Reproducir figuras, tablas y artículo

Requisitos: Python con [uv](https://docs.astral.sh/uv/), TeX Live (pdflatex, biber, latexmk).

```bash
make figs     # figuras (analysis/src/figs)
make tablas   # tablas, cifras y apéndices generados
make slr      # latex/slr/main.pdf
```

Todas las cifras del texto proceden de *scripts*; `slr/sintesis/scripts/verificar_numeros.py` comprueba que la prosa no
contiene números escritos a mano.

## Licencias

- Código (`*.py`, `*.sh`, `*.js`, `Makefile`): [MIT](LICENSE).
- Datos, texto y figuras propios: [CC BY 4.0](LICENSE-DATOS.md).
- Las exportaciones de arXiv y ACL Anthology conservan las licencias de sus fuentes.
