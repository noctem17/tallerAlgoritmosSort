"""Mide cuanto tarda una funcion de ordenamiento, sin que ella tenga que saberlo."""

import time


def medir_tiempo(funcion_ordenar, lista):
    """Ejecuta funcion_ordenar(lista) y devuelve resultado, tiempo_en_ms."""
    inicio = time.perf_counter()
    resultado = funcion_ordenar(lista)
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    return resultado, tiempo_ms