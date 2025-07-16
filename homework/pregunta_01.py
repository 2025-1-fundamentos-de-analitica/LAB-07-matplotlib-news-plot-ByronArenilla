"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Genera la gráfica de tendencias de fuentes de noticias.
    Guarda la imagen como 'files/plots/news.png'.
    """

    # Crear figura
    plt.figure()

    # Colores por categoría
    colores = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey"
    }

    # Z-order y grosor de línea por categoría
    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1
    }

    line_widths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2
    }

    # Cargar datos
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Graficar líneas
    for medio in df.columns:
        plt.plot(
            df[medio],
            color=colores[medio],
            label=medio,
            zorder=zorder[medio],
            linewidth=line_widths[medio]
        )

    # Estilo del gráfico
    plt.title("How people get their news", fontsize=16)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_visible(False)

    # Etiquetas iniciales y finales por medio
    for medio in df.columns:
        año_inicio = df.index[0]
        valor_inicio = df.loc[año_inicio, medio]

        plt.scatter(año_inicio, valor_inicio, color=colores[medio], zorder=zorder[medio])
        plt.text(año_inicio - 0.2, valor_inicio, f"{medio} {valor_inicio}%", ha='right', va='center', color=colores[medio])

        año_fin = df.index[-1]
        valor_fin = df.loc[año_fin, medio]

        plt.scatter(año_fin, valor_fin, color=colores[medio], zorder=zorder[medio])
        plt.text(año_fin + 0.2, valor_fin, f"{valor_fin}%", ha='left', va='center', color=colores[medio])

    # Etiquetas en eje x
    plt.xticks(ticks=df.index, labels=df.index, ha='center')

    # Guardar imagen
    os.makedirs("files/plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("files/plots/news.png")

