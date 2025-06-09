import tempfile  # Módulo para crear archivos temporales automáticamente
import os        # Módulo para operaciones del sistema de archivos (como eliminar archivos)
import heapq     # Módulo que permite operaciones con heaps, como fusión eficiente de listas ordenadas

def external_sort(input_file_path, output_file_path, chunk_size=1000000):
    """
    Algoritmo de ordenamiento externo tipo Straight Merging.
    1. Divide el archivo en bloques pequeños.
    2. Ordena cada bloque y los guarda en archivos temporales.
    3. Fusiona los archivos ordenados en uno final.
    """
    temp_files = []  # Lista para almacenar archivos temporales creados

    # Fase 1: División en bloques y ordenamiento
    with open(input_file_path, 'r') as input_file:  # Abre el archivo de entrada en modo lectura
        while True:
            lines = input_file.readlines(chunk_size)  # Lee hasta `chunk_size` caracteres como lista de líneas
            if not lines:  # Si no se leyó nada, fin del archivo
                break
            lines.sort()  # Ordena las líneas en memoria RAM (ordenamiento interno)
            
            # Crea un archivo temporal donde se escribirá el bloque ordenado
            temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')  # 'w+t': escritura y lectura en texto
            temp_file.writelines(lines)  # Escribe las líneas ordenadas al archivo temporal
            temp_file.seek(0)  # Regresa el cursor al inicio del archivo para leerlo luego
            temp_files.append(temp_file)  # Agrega el archivo temporal a la lista

    # Fase 2: Fusión de archivos ordenados
    with open(output_file_path, 'w') as output_file:  # Abre el archivo final donde se escribirá el resultado
        file_iters = [iter(temp_file) for temp_file in temp_files]  # Crea un iterador para cada archivo temporal
        
        # Fusiona todos los iteradores usando heapq.merge (fusión eficiente de listas ordenadas)
        for line in heapq.merge(*file_iters):  
            output_file.write(line)  # Escribe cada línea ordenada en el archivo final

    # Limpieza: cerrar y eliminar todos los archivos temporales creados
    for temp_file in temp_files:
        temp_file.close()
        os.remove(temp_file.name)  # Borra físicamente el archivo del disco

# Ejemplo de uso:
# external_sort("entrada.txt", "salida_ordenada.txt")
