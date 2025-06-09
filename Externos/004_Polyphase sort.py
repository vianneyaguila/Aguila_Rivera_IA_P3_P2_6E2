def polyphase_merge_sort(chunks):
    """
    Simulación conceptual de ordenamiento externo por Polyphase Merge.
    Distribuye los runs en forma desequilibrada y reorganiza estratégicamente.
    """
    # Suponemos chunks como listas ordenadas representando "runs"
    while len(chunks) > 1:
        # Fusionar los dos primeros y añadir al final
        merged = sorted(chunks[0] + chunks[1])
        chunks = chunks[2:] + [merged]
    return chunks[0]

# Ejemplo de uso
datos = [[1, 5], [2, 4], [3, 6]]
ordenado = polyphase_merge_sort(datos)
print("Lista ordenada:", ordenado)
