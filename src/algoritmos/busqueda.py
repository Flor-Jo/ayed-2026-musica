"""
Modulo de algoritmos de busqueda propios para la Entrega 4.
Prohibido el uso de 'in', '.index()' o la biblioteca estandar (bisect).
"""

def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """
    Busca de forma secuencial un elemento en la coleccion.
    Funciona sobre colecciones en cualquier orden.
    
    - coleccion: iterable con los elementos (ej. lista de Canciones).
    - clave: valor que buscamos (ej. "Toxic" o un ID).
    - obtener_clave: función lambda o callable para extraer la clave del objeto.
                     Si es None, se compara el elemento directo.
                     
    Retorna el elemento si lo encuentra, o None si no existe.
    Complejidad temporal: O(n) en el peor caso, O(1) en el mejor.
    Complejidad espacial: O(1).
    """
    for elemento in coleccion:
        valor_actual = obtener_clave(elemento) if obtener_clave is not None else elemento
        
        # Si comparamos cadenas de texto, normalizamos con .strip().lower() para que sea flexible
        if isinstance(valor_actual, str) and isinstance(clave, str):
            if valor_actual.strip().lower() == clave.strip().lower():
                return elemento
        else:
            if valor_actual == clave:
                return elemento
                
    return None


def busqueda_binaria(coleccion, clave, obtener_clave):
    """
    Busca un elemento dividiendo el espacio de búsqueda a la mitad en cada paso.
    REQUIERE estrictamente que la colección esté ordenada previamente por esa clave.
    
    - coleccion: lista con acceso aleatorio (por índice).
    - clave: valor buscado.
    - obtener_clave: función para extraer el atributo a comparar.
    
    Retorna el elemento si lo encuentra, o None si no existe.
    Complejidad temporal: O(log n).
    Complejidad espacial: O(1).
    """
    izq = 0
    der = len(coleccion) - 1
    
    # Normalizacion si se busca texto
    clave_normalizada = clave.strip().lower() if isinstance(clave, str) else clave

    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion[medio])
        valor_normalizado = valor.strip().lower() if isinstance(valor, str) else valor

        if valor_normalizado == clave_normalizada:
            return coleccion[medio]
        elif valor_normalizado < clave_normalizada:
            # Descartamos la mitad izquierda
            izq = medio + 1
        else:
            # Descartamos la mitad derecha
            der = medio - 1

    return None