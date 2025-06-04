def selection_sort(arr):
    """
    Ordenamiento por selección.
    Encuentra el elemento mínimo y lo coloca al principio.
    """
    for i in range(len(arr)):
        min_idx = i
        # Encontrar el índice del elemento mínimo
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el elemento mínimo con el primero no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
selection_sort(lista)
print("Lista ordenada:", lista)
