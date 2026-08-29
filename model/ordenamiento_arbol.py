"""Binary Tree Sort - ordena de mayor a menor.

Se inserta cada numero en un arbol binario de busqueda y despues se
recorre en derecha, nodo, izquierda para leerlo directo en
orden descendente.

Tanto la insercion como el recorrido estan escritos sin recursion
(con while y una pila propia): si el arreglo ya viene ordenado, el
arbol termina degenerado -- basicamente una fila de nodos con un solo
hijo, de profundidad N -- y una version recursiva se cae con
RecursionError apenas con unos pocos miles de datos, justo el caso que
este taller pide medir como peor caso.
"""


class _Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def _insertar(raiz, valor):
    nuevo = _Nodo(valor)
    if raiz is None:
        return nuevo

    actual = raiz
    while True:
        if valor <= actual.valor:
            if actual.izquierda is None:
                actual.izquierda = nuevo
                return raiz
            actual = actual.izquierda
        else:
            if actual.derecha is None:
                actual.derecha = nuevo
                return raiz
            actual = actual.derecha


def _recorrido_descendente(raiz):
    resultado = []
    pila = []
    actual = raiz

    while pila or actual is not None:
        if actual is not None:
            pila.append(actual)
            actual = actual.derecha
        else:
            actual = pila.pop()
            resultado.append(actual.valor)
            actual = actual.izquierda

    return resultado


def ordenamiento_arbol(arr):
    raiz = None
    for valor in arr:
        raiz = _insertar(raiz, valor)

    return _recorrido_descendente(raiz)


if __name__ == "__main__":
    prueba = [5, 2, 8, 1, 9, 3]
    print("Original:", prueba)
    print("Ordenado:", ordenamiento_arbol(prueba))
