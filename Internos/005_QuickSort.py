# Este código implementa el algoritmo Quick Sort, un método eficiente de ordenamiento basado en particiones.
# Se elige un pivote, se dividen los elementos en menores y mayores al pivote, y se aplica recursión.
# Es uno de los algoritmos de ordenamiento más rápidos en la práctica, especialmente para grandes volúmenes de datos.

def quick_sort(arr):
    """
    Ordenamiento rápido (Quick Sort).
    Selecciona un pivote y divide la lista en sublistas menores y mayores al pivote.
    """
    if len(arr) <= 1:  # Si la lista tiene 1 o menos elementos, ya está ordenada.
        return arr
    else:
        pivote = arr[0]  # Se toma el primer elemento como pivote.
        menores = [x for x in arr[1:] if x <= pivote]  # Lista de elementos menores o iguales al pivote.
        mayores = [x for x in arr[1:] if x > pivote]  # Lista de elementos mayores al pivote.
        return quick_sort(menores) + [pivote] + quick_sort(mayores)  # Se combinan las listas ordenadas.

# Ejemplo de uso
lista = [10, 7, 8, 9, 1, 5]
lista = quick_sort(lista)  # Ordena la lista usando Quick Sort.
print("Lista ordenada:", lista)  # Imprime la lista ordenada.
