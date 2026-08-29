"""
Genera los archivos de números que se van a usar para las pruebas.

Se corre UNA sola vez (o cada vez que se quiera un conjunto nuevo) y
deja un .txt por cada tamaño N en la carpeta datos/. Esos mismos
archivos son los que hay que compartir con el compañero que hizo los
algoritmos en Java, para que los dos programas ordenen exactamente
los mismos números y la comparación de tiempos sea justa.

No hace falta volver a correr esto antes de cada prueba: una vez que
los .txt existen, tanto main.py como el programa en Java simplemente
los leen.
"""

import random
import os

TAMANOS = [3000, 30000, 300000, 3000000, 30000000]
CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")


def generar_archivo(cantidad, carpeta=CARPETA_DATOS):
    ruta = os.path.join(carpeta, f"numeros_{cantidad}.txt")
    with open(ruta, "w") as archivo:
        for _ in range(cantidad):
            numero = random.randint(1, 1_000_000)
            archivo.write(str(numero) + "\n")
    print(f"Generado {ruta} con {cantidad} numeros")


if __name__ == "__main__":
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    for n in TAMANOS:
        generar_archivo(n)
