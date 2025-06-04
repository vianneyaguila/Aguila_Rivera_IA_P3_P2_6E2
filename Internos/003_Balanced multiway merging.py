import heapq

def balanced_multiway_merge(input_files, output_file):
    """
    Fusión equilibrada de múltiples archivos ordenados.
    Utiliza un heap mínimo para mantener el orden global.
    """
    archivos = [open(f, 'r') for f in input_files]
    heap = []

    # Inicializa el heap con la primera línea de cada archivo
    for i, archivo in enumerate(archivos):
        linea = archivo.readline()
        if linea:
            heapq.heappush(heap, (linea, i))

    with open(output_file, 'w') as salida:
        while heap:
            menor, idx = heapq.heappop(heap)
            salida.write(menor)
            siguiente = archivos[idx].readline()
            if siguiente:
                heapq.heappush(heap, (siguiente, idx))

    # Cerrar todos los archivos
    for archivo in archivos:
        archivo.close()
