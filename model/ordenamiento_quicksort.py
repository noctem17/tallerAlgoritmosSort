"""QuickSort - ordena de mayor a menor.

Version iterativa (con una pila propia) en vez de recursiva: con un
arreglo ya ordenado (que es justo el peor caso que se prueba en este
taller) una version recursiva normal se cae con RecursionError porque
la profundidad de la recursion termina siendo del tamano de N. Usando
una pila y procesando primero el lado mas chico de cada particion, la
pila nunca crece mas de log(N) elementos, sin importar que tan malo
sea el pivote.
"""


def ordenamiento_quicksort(arr):
    lista = arr.copy()
    pila = [(0, len(lista) - 1)]

    while pila:
        inicio, fin = pila.pop()
        if inicio >= fin:
            continue

        # particion tipo Lomuto, usando el ultimo elemento como pivote
        pivote = lista[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if lista[j] >= pivote:  # descendente: lo grande va antes
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        i += 1
        lista[i], lista[fin] = lista[fin], lista[i]

        izquierda = (inicio, i - 1)
        derecha = (i + 1, fin)

        # metemos primero la particion mas grande y de ultimo la mas
        # chica, para que la mas chica se procese primero (se saca
        # primero de la pila) y esta nunca crezca demasiado
        if (izquierda[1] - izquierda[0]) > (derecha[1] - derecha[0]):
            pila.append(izquierda)
            pila.append(derecha)
        else:
            pila.append(derecha)
            pila.append(izquierda)

    return lista


if __name__ == "__main__":
    prueba = [5, 2, 8, 1, 9, 3]
    print("Original:", prueba)
    print("Ordenado:", ordenamiento_quicksort(prueba))
