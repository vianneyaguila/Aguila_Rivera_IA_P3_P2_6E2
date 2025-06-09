import heapq  # Importa el módulo para manipulación de heaps (colas de prioridad)

def balanced_multiway_merge(input_files, output_file):
    """
    Fusión equilibrada de múltiples archivos ordenados.
    Utiliza un heap mínimo para mantener el orden global.
    """
    archivos = [open(f, 'r') for f in input_files]  # Abre todos los archivos de entrada en modo lectura
    heap = []  # Inicializa un heap (mínimo) vacío

    # Inserta la primera línea de cada archivo al heap
    for i, archivo in enumerate(archivos):       # i = índice del archivo
        linea = archivo.readline()               # Lee una línea del archivo
        if linea:                                # Si la línea no está vacía
            heapq.heappush(heap, (linea, i))     # Inserta una tupla (línea, índice archivo) al heap

    with open(output_file, 'w') as salida:       # Abre el archivo de salida para escribir el resultado final
        while heap:                              # Mientras el heap no esté vacío
            menor, idx = heapq.heappop(heap)     # Saca el menor elemento del heap (línea con menor valor)
            salida.write(menor)                  # Escribe esa línea en el archivo de salida

            siguiente = archivos[idx].readline() # Lee la siguiente línea del mismo archivo
            if siguiente:                        # Si hay más líneas en ese archivo
                heapq.heappush(heap, (siguiente, idx))  # Se vuelve a insertar en el heap

    # Cierra todos los archivos abiertos
    for archivo in archivos:
        archivo.close()
