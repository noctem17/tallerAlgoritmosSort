"""Bubble Sort - ordena de mayor a menor."""


def ordenamiento_burbuja(arr):
    lista = arr.copy()
    n = len(lista)

    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
        # si en una pasada completa no se movio nada, ya esta ordenado
        if not hubo_cambio:
            break

    return lista


if __name__ == "__main__":
    prueba = [5, 2, 8, 1, 9, 3]
    print("Original:", prueba)
    print("Ordenado:", ordenamiento_burbuja(prueba))
