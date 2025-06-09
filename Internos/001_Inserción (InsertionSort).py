def insertion_sort(arr):
    """
    Ordenamiento por inserción.
    Recorre la lista y va insertando cada elemento en su posición correcta.
    """
    for i in range(1, len(arr)):  # Recorre cada elemento desde el segundo hasta el último.
        clave = arr[i]  # Se guarda el valor actual para comparaciones.
        j = i - 1  # Se inicia la comparación con el elemento anterior.
        while j >= 0 and arr[j] > clave:  # Si el elemento anterior es mayor, se mueve adelante.
            arr[j + 1] = arr[j]  # Se desplaza el elemento hacia la derecha.
            j -= 1  # Se decrementa el índice para comparar con el anterior.
        arr[j + 1] = clave  # Se inserta la clave en su posición correcta.

# Ejemplo de uso
lista = [5, 2, 9, 1, 5, 6]
insertion_sort(lista)
print("Lista ordenada:", lista)  # Imprime la lista ordenada.
