"""Test figure: checks fonts, palette, Spanish labels and export path.

Dummy data — not a result. Delete once real figures exist.
"""
import matplotlib.pyplot as plt

from estilo import ANCHO_COLUMNA, aplicar_estilo, guardar

aplicar_estilo()

anios = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
conteos = [2, 3, 5, 4, 7, 9, 12]  # datos ficticios

fig, ax = plt.subplots(figsize=(ANCHO_COLUMNA, 2.0))
ax.bar(anios, conteos, width=0.7)
ax.set_xlabel("Año de publicación")
ax.set_ylabel("Número de estudios")
ax.set_title("Figura de prueba (datos ficticios)")
ax.set_xticks(anios)

print(guardar(fig, "prueba"))
