
def cargar_numeros(ruta_archivo):
    """Lee un archivo con un numero por linea y devuelve una lista de enteros."""
    with open(ruta_archivo, "r") as archivo:
        numeros = [int(linea.strip()) for linea in archivo]
    return numeros
