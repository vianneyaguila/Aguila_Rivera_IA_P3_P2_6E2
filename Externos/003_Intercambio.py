def bubble_sort(arr):
    """
    Ordenamiento por burbuja.
    Recorre la lista y realiza intercambios de elementos adyacentes si están en el orden incorrecto.
    """
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso
lista = [5, 1, 4, 2, 8]
bubble_sort(lista)
print("Lista ordenada:", lista)
