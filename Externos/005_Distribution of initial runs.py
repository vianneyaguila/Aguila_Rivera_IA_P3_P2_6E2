def distribute_initial_runs(data):
    """
    Distribuye secuencias ordenadas iniciales (runs) en dos archivos simulados.
    """
    runs = []
    run = [data[0]]
    for i in range(1, len(data)):
        if data[i] >= data[i - 1]:
            run.append(data[i])
        else:
            runs.append(run)
            run = [data[i]]
    runs.append(run)

    archivo_A = []
    archivo_B = []
    # Alternar la distribución
    for i, r in enumerate(runs):
        if i % 2 == 0:
            archivo_A.append(r)
        else:
            archivo_B.append(r)

    return archivo_A, archivo_B

# Ejemplo de uso
datos = [2, 3, 5, 1, 4, 6, 0, 7]
A, B = distribute_initial_runs(datos)
print("Archivo A:", A)
print("Archivo B:", B)
