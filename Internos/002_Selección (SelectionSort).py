def selection_sort(arr):
    """
    Ordenamiento por selección.
    Encuentra el elemento mínimo y lo coloca al principio.
    """
    for i in range(len(arr)):  # Recorre cada posición en la lista.
        min_idx = i  # Se asume que el elemento actual es el menor.
        for j in range(i+1, len(arr)):  # Busca el mínimo en la parte restante.
            if arr[j] < arr[min_idx]:  # Si encuentra un menor, actualiza min_idx.
                min_idx = j  
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambia el menor con el actual.

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
selection_sort(lista)
print("Lista ordenada:", lista)
