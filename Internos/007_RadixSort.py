# Este código implementa el algoritmo Radix Sort, ideal para ordenar números utilizando dígitos individuales.
# Procesa cada número dígito por dígito de menor a mayor usando el algoritmo de conteo.
# Es útil para ordenar grandes volúmenes de números enteros de manera eficiente.

def counting_sort(arr, exp):
    """
    Ordenamiento por conteo utilizado en Radix Sort.
    """
    n = len(arr)
    salida = [0] * n  # Lista para almacenar resultados ordenados.
    conteo = [0] * 10  # Lista para contar la ocurrencia de dígitos.

    for i in range(n):  # Contar ocurrencias de cada dígito.
        index = arr[i] // exp
        conteo[index % 10] += 1

    for i in range(1, 10):  # Actualiza las posiciones reales en salida.
        conteo[i] += conteo[i - 1]

    i = n - 1
    while i >= 0:  # Construye la salida ordenada.
        index = arr[i] // exp
        salida[conteo[index % 10] - 1] = arr[i]
        conteo[index % 10] -= 1
        i -= 1

    for i in range(n):  # Copia la salida al arreglo original.
        arr[i] = salida[i]

def radix_sort(arr):
    """
    Ordenamiento Radix Sort.
    Ordena los números procesando dígito por dígito.
    """
    maximo = max(arr)  # Encuentra el número más grande.
    exp = 1
    while maximo // exp > 0:  # Itera sobre cada dígito.
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
lista = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(lista)  # Ordena la lista usando Radix Sort.
print("Lista ordenada:", lista)  # Imprime la lista ordenada.
