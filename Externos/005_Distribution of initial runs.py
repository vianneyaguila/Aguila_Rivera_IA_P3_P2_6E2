def distribute_initial_runs(data):
    """
    Distribuye secuencias ordenadas iniciales (runs) en dos archivos simulados.
    """
    runs = []                      # Lista para almacenar todas las secuencias (runs)
    run = [data[0]]                # Inicia con el primer elemento como primera run

    for i in range(1, len(data)):  # Recorre la lista desde el segundo elemento
        if data[i] >= data[i - 1]: # Si está ordenado, sigue en la misma run
            run.append(data[i])
        else:
            runs.append(run)       # Si se rompe el orden, termina la run y comienza una nueva
            run = [data[i]]
    runs.append(run)               # Añade la última run al final

    archivo_A = []                 # Simula un "archivo A" donde se guardarán algunas runs
    archivo_B = []                 # Simula un "archivo B" con el resto de las runs

    # Alterna las runs entre archivo A y B
    for i, r in enumerate(runs):
        if i % 2 == 0:
            archivo_A.append(r)
        else:
            archivo_B.append(r)

    return archivo_A, archivo_B    # Devuelve los dos "archivos" como listas separadas

# Ejemplo de uso
datos = [2, 3, 5, 1, 4, 6, 0, 7]   # Datos de entrada con secuencias parcialmente ordenadas
A, B = distribute_initial_runs(datos)
print("Archivo A:", A)            # Muestra las runs asignadas al archivo A
print("Archivo B:", B)            # Muestra las runs asignadas al archivo B
