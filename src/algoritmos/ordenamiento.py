"""
Módulo de algoritmos de ordenamiento propios para la Entrega 4.
Regla estricta: Prohibido el uso de sorted() y list.sort().
"""

def ordenar_seleccion(coleccion, obtener_clave):
    """
    Ordenamiento por selección (Selection Sort).
    Criterio de estabilidad: NO ESTABLE.
    Busca repetidamente el menor elemento del resto de la lista y lo ubica al inicio.
    Complejidad temporal: O(n^2) en mejor, promedio y peor caso.
    Espacio auxiliar: O(1) (in-place).
    """
    n = len(coleccion)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if obtener_clave(coleccion[j]) < obtener_clave(coleccion[pos_min]):
                pos_min = j
        if pos_min != i:
            coleccion[i], coleccion[pos_min] = coleccion[pos_min], coleccion[i]
    return coleccion


def ordenar_insercion(coleccion, obtener_clave):
    """
    Ordenamiento por inserción (Insertion Sort).
    Criterio de estabilidad: ESTABLE (mantiene el orden relativo de claves iguales).
    Inserta cada elemento desplazando los elementos mayores hacia la derecha.
    Complejidad temporal: O(n) mejor caso, O(n^2) peor y promedio.
    Espacio auxiliar: O(1) (in-place).
    """
    n = len(coleccion)
    for i in range(1, n):
        actual = coleccion[i]
        clave_actual = obtener_clave(actual)
        j = i - 1
        while j >= 0 and obtener_clave(coleccion[j]) > clave_actual:
            coleccion[j + 1] = coleccion[j]
            j -= 1
        coleccion[j + 1] = actual
    return coleccion