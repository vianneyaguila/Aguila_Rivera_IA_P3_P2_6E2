# Este código implementa el algoritmo Merge Sort, un método basado en la división y combinación ordenada.
# Divide la lista en mitades hasta que cada una tenga un solo elemento y luego las combina ordenadamente.
# Es eficiente para grandes conjuntos de datos y tiene una complejidad de O(n log n), lo que lo hace estable.

def merge_sort(arr):
    """
    Ordenamiento por mezcla (Merge Sort).
    Divide la lista en mitades, ordena y luego combina.
    """
    if len(arr) > 1:  # Si la lista tiene más de un elemento, se debe dividir.
        medio = len(arr) // 2  # Encuentra el punto medio de la lista.
        izquierda = arr[:medio]  # Divide la lista en izquierda.
        derecha = arr[medio:]  # Divide la lista en derecha.

        merge_sort(izquierda)  # Ordena recursivamente la parte izquierda.
        merge_sort(derecha)  # Ordena recursivamente la parte derecha.

        i = j = k = 0  # Índices para recorrer ambas listas y combinarlas.

        while i < len(izquierda) and j < len(derecha):  # Combina ordenadamente.
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):  # Copia los elementos restantes.
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):  # Copia los elementos restantes.
            arr[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista)  # Ordena la lista usando Merge Sort.
print("Lista ordenada:", lista)  # Imprime la lista ordenada.
