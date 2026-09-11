# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical
- Por qué lo eligieron (5–8 líneas):
Elegimos el tema Biblioteca musical (Pop 2000s) porque es un dominio familiar con atributos heterogéneos como identificador, título, artista, año y duración.
Este dominio facilita implementar algoritmos de ordenamiento, búsquedas por filtros y estructuras lineales como playlists.
Para el catálogo en memoria se utilizó una lista (list, mutable) que agrupa los elementos y permite modificar, agregar o reordenar canciones dinámicamente.
Cada tema se representó mediante diccionarios (dict, mutables) con pares clave-valor, otorgando acceso semántico directo a sus distintas propiedades.
Por último, los valores de cada campo se definieron con tipos inmutables como enteros (int) y cadenas de texto (str), garantizando la integridad de los datos primitivos.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

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
