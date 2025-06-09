def polyphase_merge_sort(chunks):
    """
    Simulación conceptual de ordenamiento externo por Polyphase Merge.
    Distribuye los runs en forma desequilibrada y reorganiza estratégicamente.
    """
    # chunks representa una lista de listas (cada lista interna es un "run" previamente ordenado)
    while len(chunks) > 1:                         # Mientras haya más de un run
        merged = sorted(chunks[0] + chunks[1])     # Une los dos primeros runs y los ordena
        chunks = chunks[2:] + [merged]             # Elimina los dos primeros, añade el resultado al final
    return chunks[0]                               # Cuando queda uno solo, es la lista ordenada final

# Ejemplo de uso
datos = [[1, 5], [2, 4], [3, 6]]                   # Tres "runs" ordenados simulados
ordenado = polyphase_merge_sort(datos)            # Ejecuta el ordenamiento
print("Lista ordenada:", ordenado)                # Muestra la lista final completamente ordenada
