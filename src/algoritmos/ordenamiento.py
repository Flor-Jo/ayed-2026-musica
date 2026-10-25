"""
Módulo de algoritmos de ordenamiento propios para la Entrega 4.
Prohibido el uso de sorted() y list.sort().
"""

def ordenar_seleccion(coleccion, obtener_clave):
    """
    Ordenamiento por Selección (Selection Sort).
    Modifica la lista in-place buscando en cada iteración el elemento mínimo del resto.
    
    Estabilidad: NO es estable (puede cambiar el orden relativo de elementos con claves iguales al intercambiar posiciones no contiguas).
    Complejidad temporal: O(n²) en el mejor, peor y caso promedio (siempre recorre los dos bucles).
    Complejidad espacial: O(1).
    """
    n = len(coleccion)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            val_j = obtener_clave(coleccion[j])
            val_min = obtener_clave(coleccion[pos_min])
            
            # Normalización para texto si corresponde
            if isinstance(val_j, str) and isinstance(val_min, str):
                if val_j.strip().lower() < val_min.strip().lower():
                    pos_min = j
            else:
                if val_j < val_min:
                    pos_min = j
                    
        # Intercambio
        coleccion[i], coleccion[pos_min] = coleccion[pos_min], coleccion[i]
        
    return coleccion


def ordenar_insercion(coleccion, obtener_clave):
    """
    Ordenamiento por Inserción (Insertion Sort).
    Modifica la lista in-place insertando cada elemento en su lugar correspondiente entre los ya ordenados.
    
    Estabilidad: SÍ es estable (conserva el orden relativo previo de elementos con claves idénticas).
    Complejidad temporal: O(n) en el mejor caso (ya ordenado), O(n²) en el caso promedio y peor caso.
    Complejidad espacial: O(1).
    """
    n = len(coleccion)
    for i in range(1, n):
        actual = coleccion[i]
        val_actual = obtener_clave(actual)
        if isinstance(val_actual, str):
            val_actual = val_actual.strip().lower()
            
        j = i - 1
        while j >= 0:
            val_j = obtener_clave(coleccion[j])
            if isinstance(val_j, str):
                val_j = val_j.strip().lower()
                
            if val_j > val_actual:
                coleccion[j + 1] = coleccion[j]
                j -= 1
            else:
                break
                
        coleccion[j + 1] = actual
        
    return coleccion