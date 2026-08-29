"""Muestra los resultados: los guarda en un CSV y dibuja una grafica por algoritmo."""

import csv
import os

import matplotlib
matplotlib.use("Agg")  # para poder guardar las graficas sin necesitar pantalla
import matplotlib.pyplot as plt


def guardar_csv(resultados, ruta="datos/resultados.csv"):
    campos = ["algoritmo", "cantidad_datos", "caso", "tiempo_ms"]
    with open(ruta, "w", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)
    print(f"Tabla de resultados guardada en {ruta}")


def graficar_resultados(resultados, carpeta_salida="datos"):
    algoritmos = sorted(set(fila["algoritmo"] for fila in resultados))

    for algoritmo in algoritmos:
        filas_algoritmo = [f for f in resultados if f["algoritmo"] == algoritmo]

        plt.figure()
        for caso in ["Mejor", "Peor", "Promedio"]:
            filas_caso = [f for f in filas_algoritmo if f["caso"] == caso]
            filas_caso.sort(key=lambda f: f["cantidad_datos"])

            tamanos = [f["cantidad_datos"] for f in filas_caso]
            tiempos = [f["tiempo_ms"] for f in filas_caso]
            plt.plot(tamanos, tiempos, marker="o", label=caso)

        plt.title(f"Tiempos de ejecucion - {algoritmo}")
        plt.xlabel("Tamano del arreglo (N)")
        plt.ylabel("Tiempo (ms)")
        plt.legend()
        plt.tight_layout()

        ruta = os.path.join(carpeta_salida, f"grafica_{algoritmo}.png")
        plt.savefig(ruta)
        plt.close()
        print(f"Grafica guardada en {ruta}")
