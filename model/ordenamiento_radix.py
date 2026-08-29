"""Radix Sort - ordena de mayor a menor.

Ordena por cada digito (unidades, decenas, centenas...) usando counting
sort como paso auxiliar. Counting sort por digito da orden ascendente,
asi que al final se invierte la lista para dejarla descendente.
"""


def _counting_sort_por_digito(lista, exp):
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10

    for numero in lista:
        digito = (numero // exp) % 10
        conteo[digito] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    for i in range(n - 1, -1, -1):
        digito = (lista[i] // exp) % 10
        conteo[digito] -= 1
        salida[conteo[digito]] = lista[i]

    return salida


def ordenamiento_radix(arr):
    lista = arr.copy()
    if not lista:
        return lista

    maximo = max(lista)
    exp = 1
    while maximo // exp > 0:
        lista = _counting_sort_por_digito(lista, exp)
        exp *= 10

    lista.reverse()
    return lista


if __name__ == "__main__":
    prueba = [5, 2, 8, 1, 9, 3]
    print("Original:", prueba)
    print("Ordenado:", ordenamiento_radix(prueba))
