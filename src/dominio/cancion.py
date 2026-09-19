class Cancion:
    """Clase que representa una cancion individual dentro de la biblioteca."""

    def __init__(self, id_cancion: int, titulo: str, artista: str, anio: int, duracion: str):
        self.id = id_cancion
        self.titulo = titulo
        self.artista = artista
        self.anio = anio
        self.duracion = duracion

    def resumen(self) -> str:
        """Devuelve una representación legible de la canción."""
        return f"[{self.id}] '{self.titulo}' - {self.artista} ({self.anio}) [{self.duracion}]"