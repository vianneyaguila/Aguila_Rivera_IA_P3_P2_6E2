import tempfile
import os
import heapq

def external_sort(input_file_path, output_file_path, chunk_size=1000000):
    """
    Algoritmo de ordenamiento externo tipo Straight Merging.
    1. Divide el archivo en bloques pequeños.
    2. Ordena cada bloque y los guarda en archivos temporales.
    3. Fusiona los archivos ordenados en uno final.
    """
    temp_files = []

    # Fase 1: División en bloques y ordenamiento
    with open(input_file_path, 'r') as input_file:
        while True:
            lines = input_file.readlines(chunk_size)  # Leer hasta chunk_size caracteres
            if not lines:
                break
            lines.sort()  # Ordenar líneas en memoria
            temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')  # Crear archivo temporal
            temp_file.writelines(lines)
            temp_file.seek(0)
            temp_files.append(temp_file)

    # Fase 2: Fusión de archivos ordenados
    with open(output_file_path, 'w') as output_file:
        # Crear iteradores para cada archivo
        file_iters = [iter(temp_file) for temp_file in temp_files]
        
        # Usar heapq.merge para fusionar de forma eficiente
        for line in heapq.merge(*file_iters):
            output_file.write(line)

    # Cerrar y eliminar archivos temporales
    for temp_file in temp_files:
        temp_file.close()
        os.remove(temp_file.name)

# Ejemplo de uso:
# external_sort("entrada.txt", "salida_ordenada.txt")
