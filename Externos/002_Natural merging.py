def detectar_runs(archivo):
    """
    Detecta secuencias ya ordenadas ('runs') en el archivo original.
    """
    with open(archivo, 'r') as f:
        datos = f.readlines()

    runs = []
    run_actual = [datos[0]]

    for i in range(1, len(datos)):
        if datos[i] >= datos[i - 1]:
            run_actual.append(datos[i])
        else:
            runs.append(run_actual)
            run_actual = [datos[i]]
    runs.append(run_actual)
    return runs

def natural_merge_sort(archivo_entrada, archivo_salida):
    """
    Implementación básica de Natural Merge Sort.
    """
    runs = detectar_runs(archivo_entrada)

    # Continuar fusionando mientras haya más de una run
    while len(runs) > 1:
        nuevas_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                nuevas_runs.append(sorted(runs[i] + runs[i + 1]))
            else:
                nuevas_runs.append(runs[i])
        runs = nuevas_runs

    # Escribir resultado en archivo de salida
    with open(archivo_salida, 'w') as out_file:
        out_file.writelines(runs[0])
