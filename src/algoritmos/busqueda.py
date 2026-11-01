"""
Modulo de algoritmos de busqueda propios para la Entrega 4.
Prohibido el uso de 'in', '.index()' o la biblioteca estandar (bisect).
"""

def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """
    Recorre secuencialmente la colección elemento por elemento.
    Funciona con la colección desordenada.
    Complejidad temporal: O(n) peor caso, O(1) mejor caso.
    Espacio auxiliar: O(1).
    """
    for elemento in coleccion:
        valor = obtener_clave(elemento) if obtener_clave else elemento
        if valor == clave:
            return elemento
    return None


def busqueda_binaria(coleccion, clave, obtener_clave):
    """
    Búsqueda binaria sobre una colección previamente ordenada.
    Divide el espacio de búsqueda a la mitad en cada iteración.
    Complejidad temporal: O(log n).
    Espacio auxiliar: O(1).
    """
    izq = 0
    der = len(coleccion) - 1

    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion[medio])

        if valor == clave:
            return coleccion[medio]
        elif valor < clave:
            izq = medio + 1  # La clave está en la mitad derecha
        else:
            der = medio - 1  # La clave está en la mitad izquierda

    return None