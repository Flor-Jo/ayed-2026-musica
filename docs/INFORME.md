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
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
