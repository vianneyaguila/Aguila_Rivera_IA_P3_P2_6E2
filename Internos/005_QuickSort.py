def quick_sort(arr):
    """
    Ordenamiento rápido (Quick Sort).
    Selecciona un pivote y divide la lista en sublistas menores y mayores al pivote.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo de uso
lista = [10, 7, 8, 9, 1, 5]
lista = quick_sort(lista)
print("Lista ordenada:", lista)
