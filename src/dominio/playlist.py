from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError


class Playlist:
    """Colección principal de canciones basada en ListaEnlazada con un límite máximo."""

    def __init__(self, nombre: str, capacidad_maxima: int = 5):
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self._canciones = ListaEnlazada()

    def agregar_cancion(self, cancion):
        """Agrega una canción a la playlist si no superó la capacidad máxima."""
        if self._canciones.tamanio() >= self.capacidad_maxima:
            raise ColeccionLlenaError(
                f"La playlist '{self.nombre}' está llena (límite: {self.capacidad_maxima} canciones)."
            )
        self._canciones.insertar_al_final(cancion)

    def cantidad(self) -> int:
        return self._canciones.tamanio()

    def esta_llena(self) -> bool:
        return self._canciones.tamanio() >= self.capacidad_maxima

    def esta_vacia(self) -> bool:
        return self._canciones.esta_vacia()

    def __iter__(self):
        """Permite iterar directamente sobre las canciones usando el iterador del TAD."""
        return iter(self._canciones)
 
