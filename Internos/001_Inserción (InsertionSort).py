def insertion_sort(arr):
    """
    Ordenamiento por inserción.
    Recorre la lista y va insertando cada elemento en su posición correcta.
    """
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        # Mover los elementos mayores que la clave una posición adelante
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave

# Ejemplo de uso
lista = [5, 2, 9, 1, 5, 6]
insertion_sort(lista)
print("Lista ordenada:", lista)
