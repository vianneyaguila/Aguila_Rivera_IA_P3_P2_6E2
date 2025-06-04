class Nodo:
    """
    Clase para representar un nodo en el árbol binario de búsqueda.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(nodo, valor):
    """
    Inserta un valor en el árbol binario de búsqueda.
    """
    if nodo is None:
        return Nodo(valor)
    if valor < nodo.valor:
        nodo.izquierda = insertar(nodo.izquierda, valor)
    else:
        nodo.derecha = insertar(nodo.derecha, valor)
    return nodo

def recorrido_en_orden(nodo, resultado):
    """
    Realiza un recorrido en orden del árbol y almacena los valores en la lista resultado.
    """
    if nodo:
        recorrido_en_orden(nodo.izquierda, resultado)
        resultado.append(nodo.valor)
        recorrido_en_orden(nodo.derecha, resultado)

def tree_sort(arr):
    """
    Ordenamiento por árbol.
    Construye un árbol binario de búsqueda y realiza un recorrido en orden.
    """
    raiz = None
    for valor in arr:
        raiz = insertar(raiz, valor)
    resultado = []
    recorrido_en_orden(raiz, resultado)
    return resultado

# Ejemplo de uso
lista = [5, 3, 7, 2, 4, 6, 8]
lista_ordenada = tree_sort(lista)
print("Lista ordenada:", lista_ordenada)
