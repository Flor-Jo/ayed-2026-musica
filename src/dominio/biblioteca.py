# OPTIMIZACION: Importamos Cancion usando la ruta absoluta desde 'src' 
# para que no tire error cuando corramos 'python -m src.main' desde la raíz del proyecto.
from src.dominio.cancion import Cancion
from src.config import CATALOGO_POP_2000S

class Biblioteca:
    """
    Esta es la clase gestora. 
    La creamos para sacar la logica del main.py (Ítem 1 de la rúbrica entrega 2).
    Esta clase sabe como guardar las canciones y como hacer operaciones con ellas.
    """

    def __init__(self):
        # En las entregas 1 y 2, guardamos el catálogo en memoria usando una list nativa de Python.
        self.canciones = []
        
        # Simulamos la relacion que va a venir del archivo versiones.txt (Ítem 2).
        # El mapa dice: la canción 2 (Bad Romance) tiene como versión derivada la 8 (Poker Face).
        # Y la 8 deriva a su vez en la 1 (Toxic). Esto nos sirve para probar la recursión.
        self.versiones_map = {
            2: [8],
            8: [1]
        }
        
        # Apenas creamos la Biblioteca, le decimos que se autollene con los datos.
        self._cargar_catalogo()

    def _cargar_catalogo(self):
        # Recorre la lista de diccionarios que está en config.py, crea objetos de tipo Cancion
        # y los guarda en nuestra lista interna self.canciones.
        for item in CATALOGO_POP_2000S:
            cancion = Cancion(
                id_cancion=item["id"],
                titulo=item["titulo"],
                artista=item["artista"],
                anio=item["anio"],
                duracion=item["duracion"]
            )
            self.canciones.append(cancion)

    def obtener_todas(self) -> list:
        # para que el main.py pueda pedir la lista y mostrarla.
        return self.canciones

    def buscar_por_id(self, id_cancion: int):
        # Busqueda lineal simple: recorremos la lista de objetos Cancion.
        # Si coincide el ID, devolvemos el objeto entero. Si termina el ciclo y no hay nada, devuelve None.
        for cancion in self.canciones:
            if cancion.id == id_cancion:
                return cancion
        return None

    def obtener_versiones_directas(self, id_cancion: int) -> list:
        # Devuelve las versiones inmediatas consultando nuestro mapa.
        # El .get(id, []) devuelve una lista vacía si el ID no esta en el diccionario.
        return self.versiones_map.get(id_cancion, [])

    # =========================================================================
    # RECURSIÓN DEL DOMINIO (Ítem 2)
    # =========================================================================
    def obtener_todas_las_versiones(self, id_cancion: int) -> list:
        """
        Este es el núcleo de la E2. 
        Busca una cancion y todas las versiones "hijas", "nietas", etc.
        """
        # 1. Buscamos las versiones de nivel 1.
        directas = self.obtener_versiones_directas(id_cancion)

        # 2. CASO BASE (Obligatorio en recursion)
        # Si la canción no tiene covers ni versiones (la lista esta vacia), 
        # devolvemos [] y cortamos este hilo de ejecución.
        if not directas:
            return []

        # 3. CASO RECURSIVO
        # Si encontramos versiones directas, las copiamos a nuestra lista 'resultado'.
        resultado = list(directas)
        
        # por cada versión que encontramos, nos volvemos a llamar 
        # a nosotros mismos para ver si ESA versión tiene sus propias versiones.
        for v_id in directas:
            resultado += self.obtener_todas_las_versiones(v_id)

        # Devolvemos la lista acumulada (se van desapilando los retornos).
        return resultado