def bubble_sort(arr):
    """
    Ordenamiento por burbuja.
    Compara e intercambia elementos adyacentes si están en el orden incorrecto.
    """
    n = len(arr)
    for i in range(n):  # Recorre la lista varias veces.
        for j in range(0, n - i - 1):  # Compara elementos adyacentes.
            if arr[j] > arr[j + 1]:  # Si el actual es mayor que el siguiente, los intercambia.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso
lista = [5, 1, 4, 2, 8]
bubble_sort(lista)
print("Lista ordenada:", lista)
