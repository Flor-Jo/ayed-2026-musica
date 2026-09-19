from cancion import Cancion
from src.config import CATALOGO_POP_2000S

class Biblioteca:
    """Gestiona el catálogo de canciones y la relación recursiva de versiones derivadas."""

    def __init__(self):
        # En E1/E2 la colección vive en memoria con un list
        self.canciones = []
        
        # Mapeo de derivaciones de versiones (ej: Canción ID 2 -> da origen a la ID 8, y la 8 a la 1)
        self.versiones_map = {
            2: [8],
            8: [1]
        }
        self._cargar_catalogo()

    def _cargar_catalogo(self):
        """Carga los datos iniciales transformándolos en objetos Cancion."""
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
        return self.canciones

    def buscar_por_id(self, id_cancion: int):
        for cancion in self.canciones:
            if cancion.id == id_cancion:
                return cancion
        return None

    def obtener_versiones_directas(self, id_cancion: int) -> list:
        """Devuelve la lista de IDs de versiones derivadas directamente."""
        return self.versiones_map.get(id_cancion, [])

    # =========================================================================
    # RECURSIÓN DEL DOMINIO (Ítem 2 )
    # =========================================================================
    def obtener_todas_las_versiones(self, id_cancion: int) -> list:
        """
        Obtiene de forma RECURSIVA todas las versiones derivadas (covers, remixes,
        lives) de una canción y las versiones de sus versiones.
        """
        directas = self.obtener_versiones_directas(id_cancion)

        # CASO BASE: Si no tiene versiones derivadas directas, corta la recursión.
        if not directas:
            return []

        # CASO RECURSIVO: Agrega las versiones directas y explora recursivamente cada una.
        resultado = list(directas)
        for v_id in directas:
            resultado += self.obtener_todas_las_versiones(v_id)

        return resultado