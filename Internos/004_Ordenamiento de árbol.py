
# Este código implementa el algoritmo de ordenamiento Tree Sort utilizando un árbol binario de búsqueda.
# Primero, se insertan los elementos en un árbol binario de búsqueda. Luego, se recorren en orden para obtener la lista ordenada.
# Tree Sort es eficiente para conjuntos de datos que requieren búsquedas frecuentes, ya que aprovecha la estructura del árbol.

class Nodo:
    """
    Clase para representar un nodo en el árbol binario de búsqueda.
    """
    def __init__(self, valor):
        self.valor = valor  # Asigna el valor del nodo.
        self.izquierda = None  # Inicializa el nodo izquierdo como vacío.
        self.derecha = None  # Inicializa el nodo derecho como vacío.

def insertar(nodo, valor):
    """
    Inserta un valor en el árbol binario de búsqueda.
    """
    if nodo is None:  # Si el árbol está vacío, crea un nuevo nodo.
        return Nodo(valor)
    if valor < nodo.valor:  # Si el valor es menor, se inserta en la izquierda.
        nodo.izquierda = insertar(nodo.izquierda, valor)
    else:  # Si el valor es mayor o igual, se inserta en la derecha.
        nodo.derecha = insertar(nodo.derecha, valor)
    return nodo  # Retorna la raíz del árbol actualizada.

def recorrido_en_orden(nodo, resultado):
    """
    Realiza un recorrido en orden del árbol y almacena los valores en la lista resultado.
    """
    if nodo:  # Si el nodo existe, recorrer recursivamente.
        recorrido_en_orden(nodo.izquierda, resultado)  # Primero los valores menores.
        resultado.append(nodo.valor)  # Agrega el valor actual.
        recorrido_en_orden(nodo.derecha, resultado)  # Luego los valores mayores.

def tree_sort(arr):
    """
    Ordenamiento por árbol.
    Construye un árbol binario de búsqueda y realiza un recorrido en orden.
    """
    raiz = None  # Inicializa la raíz del árbol como None.
    for valor in arr:  # Recorre cada elemento de la lista.
        raiz = insertar(raiz, valor)  # Inserta cada elemento en el árbol.
    resultado = []  # Crea una lista vacía para almacenar el resultado ordenado.
    recorrido_en_orden(raiz, resultado)  # Obtiene los valores ordenados con recorrido en orden.
    return resultado  # Retorna la lista ordenada.

# Ejemplo de uso
lista = [5, 3, 7, 2, 4, 6, 8]
lista_ordenada = tree_sort(lista)  # Ordena la lista usando Tree Sort.
print("Lista ordenada:", lista_ordenada)  # Imprime la lista ordenada.
