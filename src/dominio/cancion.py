class Cancion:
    """Clase que representa una canción individual (la entidad base de nuestro dominio)."""

    def __init__(self, id_cancion: int, titulo: str, artista: str, anio: int, duracion: str):
        # Convertimos los datos crudos (los diccionarios de config.py) en atributos del objeto.
        # Así en lugar de manejar diccionarios sueltos como diccionario["titulo"],
        # usamos orientación a objetos: mi_cancion.titulo.
        self.id = id_cancion
        self.titulo = titulo
        self.artista = artista
        self.anio = anio
        self.duracion = duracion

    def resumen(self) -> str:
        # En vez de que el main.py este armando el string a mano, cada Cancion sabe como imprimirse a si misma.
        # El main solo llama a este método.
        return f"[{self.id}] '{self.titulo}' - {self.artista} ({self.anio}) [{self.duracion}]"
        
