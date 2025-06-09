def detectar_runs(archivo):
    """
    Detecta secuencias ya ordenadas ('runs') en el archivo original.
    """
    with open(archivo, 'r') as f:     # Abre el archivo en modo lectura
        datos = f.readlines()         # Lee todas las líneas del archivo en una lista

    runs = []                         # Lista para almacenar las secuencias ordenadas ("runs")
    run_actual = [datos[0]]           # Inicia la primera run con la primera línea del archivo

    for i in range(1, len(datos)):    # Recorre el archivo desde la segunda línea
        if datos[i] >= datos[i - 1]:  # Si la línea actual es mayor o igual que la anterior, es parte de la run actual
            run_actual.append(datos[i])
        else:
            runs.append(run_actual)   # Si hay desorden, termina la run actual y empieza una nueva
            run_actual = [datos[i]]
    
    runs.append(run_actual)           # Añade la última run capturada
    return runs                       # Devuelve todas las runs detectadas

def natural_merge_sort(archivo_entrada, archivo_salida):
    """
    Implementación básica de Natural Merge Sort.
    """
    runs = detectar_runs(archivo_entrada)  # Detecta secuencias ordenadas dentro del archivo original

    # Mientras haya más de una run, sigue fusionando
    while len(runs) > 1:
        nuevas_runs = []                     # Lista para almacenar las runs fusionadas
        for i in range(0, len(runs), 2):     # Recorre de dos en dos las runs
            if i + 1 < len(runs):            # Si hay una pareja de runs, las une y las ordena
                nuevas_runs.append(sorted(runs[i] + runs[i + 1]))
            else:
                nuevas_runs.append(runs[i])  # Si queda una sola run, se añade tal cual (sin fusionar)
        runs = nuevas_runs                   # Actualiza las runs con las nuevas fusionadas

    # Una vez que queda una sola run, se escribe en el archivo final
    with open(archivo_salida, 'w') as out_file:
        out_file.writelines(runs[0])         # Escribe la run final (ordenada completamente) al archivo de salida
