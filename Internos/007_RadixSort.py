def counting_sort(arr, exp):
    """
    Ordenamiento por conteo utilizado en Radix Sort.
    """
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10

    # Contar ocurrencias
    for i in range(n):
        index = arr[i] // exp
        conteo[index % 10] += 1

    # Actualizar conteo[i] para que contenga la posición real de este dígito en salida[]
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir la salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        salida[conteo[index % 10] - 1] = arr[i]
        conteo[index % 10] -= 1
        i -= 1

    # Copiar la salida al arreglo original
    for i in range(n):
        arr[i] = salida[i]

def radix_sort(arr):
    """
    Ordenamiento Radix Sort.
    Ordena los números procesando dígito por dígito.
    """
    maximo = max(arr)
    exp = 1
    while maximo // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
lista = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(lista)
print("Lista ordenada:", lista)
