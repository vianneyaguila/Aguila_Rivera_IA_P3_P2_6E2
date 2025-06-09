def merge_sort(arr):
    """
    Ordenamiento por mezcla (Merge Sort).
    Divide la lista en mitades, ordena y luego combina.
    """
    if len(arr) > 1:
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        # Ordenar las mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Combinar las mitades ordenadas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Copiar los elementos restantes
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista)
print("Lista ordenada:", lista)
