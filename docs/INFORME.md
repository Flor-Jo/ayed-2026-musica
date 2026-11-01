# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical
- Por qué lo eligieron (5–8 líneas):
Elegimos la Biblioteca Musical porque tiene una estructura de datos homogénea y directa (título, artista, año, duración).
Todos los integrantes estamos familiarizados con el uso de un reproductor de música y nos pareció la forma más intuitiva de abordar el proyecto.
Para el catálogo en memoria se utilizó una lista (list, mutable) que agrupa los elementos y permite modificar, agregar o reordenar canciones dinámicamente.
Cada tema se representó mediante diccionarios (dict, mutables) con pares clave-valor, otorgando acceso semántico directo a sus distintas propiedades.
Por último, los valores de cada campo se definieron con tipos inmutables como enteros (int) y cadenas de texto (str), garantizando la integridad de los datos primitivos.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## Recursión (E2)

Función: `obtener_todas_las_versiones(self, id_cancion)`
Caso base: si la canción no tiene versiones derivadas directas en el mapa, devuelve `[]`.
Caso recursivo: devuelve la lista de versiones directas + `obtener_todas_las_versiones(v_id)` por cada versión directa encontrada.

Traza para la canción ID 2 ("Bad Romance"): según el mapa en memoria, la ID 2 deriva en la 8, y la 8 deriva en la 1.
Llamada 1: `obtener_todas_las_versiones(2)` -> tiene directa [8]
   -> devuelve [8] + `obtener_todas_las_versiones(8)`
Llamada 2: `obtener_todas_las_versiones(8)` -> tiene directa [1]
   -> devuelve [1] + `obtener_todas_las_versiones(1)`
Llamada 3: `obtener_todas_las_versiones(1)` -> NO tiene directas (caso base)
   -> devuelve []

Resultado de la desapilación: 
Retorno Llamada 3: []
Retorno Llamada 2: [1] + [] = [1]
Retorno Llamada 1: [8] + [1] = [8, 1]
Resultado final: [8, 1]

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | insertar_al_inicio, insertar_al_final, eliminar, buscar, tamanio, esta_vacia, ver_primero, eliminar_primero, __ iter __ |Secuencia lineal encadenada por nodos contiguos; el último nodo referencia a None y tamanio equivale a la cantidad real de nodos enlazados. |
| Pila | apilar, desapilar, ver_tope, esta_vacia | Disciplina LIFO (Last In, First Out): el elemento consultado o extraído es siempre el último que fue insertado en el tope. |
| Cola | encolar, desencolar, ver_frente, esta_vacia | Disciplina FIFO (First In, First Out): el primer elemento insertado por el extremo final es siempre el primero en salir por el frente. |

Dónde se usa cada uno en el dominio.
- **ListaEnlazada:** Base estructural de la colección `

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |
Playlist` (con límite de capacidad) y contenedor interno de los TADs Pila y Cola.
- **Pila:** Historial de canciones consultadas (deshacer / última vista) en la Opción 7 del menú.
- **Cola:** Cola de turnos de reproducción secuencial de canciones en la Opción 8 del menú.
  
## 5. Complejidad (E4)

### 5.1 Tabla de complejidad de las operaciones del sistema

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) | Recorre de manera secuencial los n elementos del catálogo para imprimir el resumen de cada uno. |
| Búsqueda lineal | O(n) peor / O(1) mejor | O(1) | En el peor caso debe revisar los n elementos hasta el final; en el mejor caso encuentra la clave en la primera posición. |
| Búsqueda binaria | O(log n) | O(1) | En cada iteración descarta la mitad del rango de búsqueda dividiendo el intervalo por la mitad. |
| Ordenar por selección | O(n²) siempre | O(1) | Ejecuta dos bucles anidados independientes del orden inicial; realiza n(n - 1)/2 comparaciones siempre. |
| Ordenar por inserción | O(n) mejor / O(n²) peor y promedio | O(1) | Si está ordenado solo realiza una comparación por elemento; si está invertido desplaza todos los elementos previos. |
| Ver detalle de un ítem | O(n) | O(1) | Realiza un recorrido secuencial en memoria sobre la lista de canciones hasta dar con el ID solicitado. |
| Operación recursiva (versiones) | O(k) | O(k) | Siendo k la cantidad de versiones derivadas encadenadas; consume memoria proporcional en la pila de llamadas del sistema. |

### 5.2 Estabilidad y criterios de ordenamiento
- **Selección (No estable):** Puede alterar el orden relativo previo de dos canciones que tengan el mismo valor de clave, ya que efectúa intercambios entre posiciones no contiguas (`coleccion[i], coleccion[pos_min]`).
- **Inserción (Estable):** Conserva el orden original relativo entre elementos con idéntica clave porque efectúa desplazamientos ordenados hacia la derecha y solo inserta el elemento ante un valor estrictamente menor.

### 5.3 Mediciones reales (`time.perf_counter`)

Medición realizada sobre el catálogo original en memoria ($n = 8$) y sobre una copia ampliada 10 veces ($n \times 10 = 80$):

| Operación | n | segundos |
| --- | --- | --- |
| Búsqueda lineal (título) | 8 | 0.00000410 |
| Búsqueda lineal (n × 10) | 80 | 0.00000670 |
| Búsqueda binaria (título) | 8 | 0.00000240 |
| Búsqueda binaria (n × 10) | 80 | 0.00000180 |
| Ordenar por selección (título) | 8 | 0.00000640 |
| Ordenar por selección (n × 10) | 80 | 0.00021580 |
| Ordenar por inserción (título) | 8 | 0.00000350 |
| Ordenar por inserción (n × 10) | 80 | 0.00011490 |

**Análisis de los resultados:**
- **Búsquedas:** En la búsqueda lineal el tiempo se incrementa cuando el catálogo se multiplica por 10 ($O(n)$). En la búsqueda binaria, el tiempo se mantiene prácticamente plano en el orden de microsegundos ($O(\log n)$), demostrando que la partición sucesiva a la mitad amortigua el crecimiento del tamaño del conjunto[cite: 8, 9].
- **Ordenamientos:** Al multiplicar el tamaño del dataset por 10, ambos algoritmos de ordenamiento cuadrático ($O(n^2)$) sufren un salto notable en los tiempos medidos (de fracciones de microsegundo a décimas de milisegundo). Se aprecia también que Inserción resulta más veloz que Selección para este volumen de datos.

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)
 
| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
