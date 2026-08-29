"""
Orquesta las pruebas: por cada tamano N, carga los numeros del archivo
compartido, arma los casos mejor/peor/promedio, corre los 5 algoritmos
y guarda cuanto tardo cada uno.

No ordena nada aqui directamente -- eso lo hace el modelo. Este archivo
solo decide que correr, en que orden, y guarda los resultados.
"""

import os

from model.lector_datos import cargar_numeros
from model.medidor_tiempo import medir_tiempo
from model.ordenamiento_burbuja import ordenamiento_burbuja
from model.ordenamiento_shell import ordenamiento_shell
from model.ordenamiento_quicksort import ordenamiento_quicksort
from model.ordenamiento_radix import ordenamiento_radix
from model.ordenamiento_arbol import ordenamiento_arbol

TAMANOS = [3000, 30000, 300000, 3000000, 30000000]
CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")

ALGORITMOS = {
    "BubbleSort": ordenamiento_burbuja,
    "ShellSort": ordenamiento_shell,
    "QuickSort": ordenamiento_quicksort,
    "RadixSort": ordenamiento_radix,
    "BinaryTreeSort": ordenamiento_arbol,
}


def ejecutar_pruebas(tamanos=TAMANOS):
    """
    Devuelve una lista de diccionarios, uno por cada
    (algoritmo, tamano, caso), con el tiempo que tardo en ms.
    """
    resultados = []

    for n in tamanos:
        ruta = os.path.join(CARPETA_DATOS, f"numeros_{n}.txt")
        if not os.path.exists(ruta):
            print(f"No encontre {ruta}. Corre herramientas/generar_numeros.py primero.")
            continue

        base = cargar_numeros(ruta)  # este es el caso promedio (viene desordenado al azar)
        casos = {
            "Mejor": sorted(base, reverse=True),  # ya descendente
            "Peor": sorted(base),                 # ascendente, al reves de lo que buscamos
            "Promedio": base,
        }

        print(f"\n--- N = {n} ---")
        for nombre_algoritmo, funcion in ALGORITMOS.items():
            for nombre_caso, datos in casos.items():
                copia = datos.copy()
                _, tiempo_ms = medir_tiempo(funcion, copia)

                print(f"{nombre_algoritmo:15} {nombre_caso:10} {tiempo_ms:12.3f} ms")

                resultados.append({
                    "algoritmo": nombre_algoritmo,
                    "cantidad_datos": n,
                    "caso": nombre_caso,
                    "tiempo_ms": tiempo_ms,
                })

    return resultados
