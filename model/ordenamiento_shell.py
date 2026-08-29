"""Shell Sort - ordena de mayor a menor."""


def ordenamiento_shell(arr):
    lista = arr.copy()
    n = len(lista)

    salto = n // 2
    while salto > 0:
        for i in range(salto, n):
            actual = lista[i]
            j = i
            # va corriendo los elementos mas chicos hacia adelante
            # (recordar que aqui mas pequeñop pierde contra actual)
            while j >= salto and lista[j - salto] < actual:
                lista[j] = lista[j - salto]
                j -= salto
            lista[j] = actual
        salto //= 2

    return lista


if __name__ == "__main__":
    prueba = [5, 2, 8, 1, 9, 3]
    print("Original:", prueba)
    print("Ordenado:", ordenamiento_shell(prueba))
