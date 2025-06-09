# Entender diferentes métodos de ordenamiento te permite:

Elija el algoritmo adecuado según el tipo y tamaño de los datos.

Optimizar el rendimiento de las aplicaciones.

Comprender mejor los fundamentos de algoritmos y estructuras de datos.

# Algoritmos de Ordenamiento en Python

Este repositorio contiene la implementación de diversos **métodos de ordenamiento**, tanto internos como externos, escritos en Python. Cada algoritmo resuelve el mismo problema: **ordenar una lista de datos**, pero lo hace utilizando distintas estrategias, estructuras y niveles de eficiencia.

---

## ¿Qué es un método de ordenamiento?

Un método de ordenamiento es un algoritmo que organiza los elementos de una lista (números, letras, etc.) en un orden determinado, normalmente ascendente o descendente. Estos algoritmos son fundamentales en la informática, ya que permiten mejorar la eficiencia de búsqueda, procesamiento y visualización de datos.

---

## Tipos de Métodos de Ordenamiento

### Ordenamiento Interno

Estos algoritmos trabajan **completamente en memoria (RAM)**. Se utilizan cuando el conjunto de datos es lo suficientemente pequeño como para cargarse entero en la memoria.

#### 1. Inserción
- Inserta los elementos en su lugar correcto uno por uno.
- Bueno para listas pequeñas o casi ordenadas.
- Complejidad: `O(n^2)` en el peor caso.

#### 2. Selección
- Busca el menor elemento y lo coloca al principio, repitiendo este proceso.
- Simple de entender, pero ineficiente para listas grandes.
- Complejidad: `O(n^2)`.

#### 3. Intercambio
- Compara elementos adyacentes y los intercambia si están desordenados.
- No recomendado para listas grandes.
- Complejidad: `O(n^2)`.

#### 4. Ordenamiento de árbol
- Inserta los elementos en un árbol binario y luego los recorre en orden.
- Eficiente si el árbol está balanceado.
- Complejidad: `O(n log n)` promedio.

#### 5. Quick Sort
- Divide y conquista: elige un pivote y ordena elementos menores y mayores recursivamente.
- Muy eficiente para listas grandes.
- Complejidad promedio: `O(n log n)`.

#### 6. Merge Sort
- Divide la lista en mitades, ordena y luego las combina.
- Estable y eficiente, ideal para datos grandes.
- Complejidad: `O(n log n)`.

#### 7. Radix Sort
- Ordena los números por cada dígito, usando un algoritmo de conteo (Counting Sort).
- Ideal para enteros no negativos.
- Complejidad: `O(nk)`, donde `k` es el número de dígitos.

---

###  Ordenamiento Externo

Estos algoritmos se utilizan cuando el conjunto de datos es **demasiado grande para caber en memoria**, por lo que se almacenan en disco y se procesan en bloques.

#### 1. Straight Merging
- Divide el archivo en bloques que se ordenan por separado y luego se fusionan.
- Utiliza archivos temporales.
- Ideal para grandes volúmenes de datos.

#### 2. Natural Merge Sort
- Detecta secuencias ya ordenadas ("runs") en el archivo y las fusiona repetidamente.
- Aprovecha orden parcial para reducir pasos.

#### 3. Balanced Multiway Merge
- Fusión equilibrada de múltiples archivos ya ordenados.
- Usa un heap (cola de prioridad) para mantener el orden global.

#### 4. Polyphase Merge Sort
- Técnica avanzada de fusión que optimiza el número de lecturas/escrituras.
- Se simula dividiendo y fusionando sublistas desbalanceadas.

#### 5. Distribución de Runs Iniciales
- Se identifican secuencias crecientes en los datos y se distribuyen alternadamente entre dos archivos.
- Paso previo importante para métodos de fusión externa.



