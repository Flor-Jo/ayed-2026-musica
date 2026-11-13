from pathlib import Path
from src.dominio.cancion import Cancion
from src.config import CATALOGO_POP_2000S
from src.excepciones import ItemNoEncontradoError
from src.persistencia.texto import guardar_texto, cargar_texto
from src.persistencia.binario import (
    guardar_binario,
    cargar_binario,
    actualizar_registro,
    alta_binario,
    baja_binario,
)


class Biblioteca:
    """Clase gestora del dominio Biblioteca Musical (E1-E5)."""

    def __init__(self):
        self.canciones = []
        self.versiones_map = {
            3: [8],
            8: [1],
        }
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        """Si existe data/canciones.txt lo carga al arrancar; si no, usa CATALOGO_POP_2000S."""
        ruta_txt = Path(__file__).resolve().parents[2] / "data" / "canciones.txt"
        if ruta_txt.exists():
            try:
                self.canciones = cargar_texto(str(ruta_txt))
                return
            except Exception:
                pass
        self.cargar_catalogo()

    def cargar_catalogo(self):
        """Carga inicial desde la constante de config.py (E1/E2)."""
        self.canciones = []
        for item in CATALOGO_POP_2000S:
            cancion = Cancion(
                id_cancion=item["id"],
                titulo=item["titulo"],
                artista=item["artista"],
                anio=item["anio"],
                duracion=item["duracion"],
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
        return self.versiones_map.get(id_cancion, [])

    def obtener_todas_las_versiones(self, id_cancion: int) -> list:
        directas = self.obtener_versiones_directas(id_cancion)
        if not directas:
            return []
        resultado = list(directas)
        for v_id in directas:
            resultado += self.obtener_todas_las_versiones(v_id)
        return resultado

    def agregar_cancion(self, nueva_cancion: Cancion):
        if self.buscar_por_id(nueva_cancion.id) is not None:
            raise ValueError(f"Ya existe una canción con el ID {nueva_cancion.id}.")
        self.canciones.append(nueva_cancion)

    def eliminar_cancion(self, id_cancion: int) -> tuple[int, Cancion]:
        for idx, c in enumerate(self.canciones):
            if c.id == id_cancion:
                return idx, self.canciones.pop(idx)
        raise ItemNoEncontradoError(f"No se encontró canción con ID {id_cancion}.")

    def modificar_cancion(
        self,
        id_cancion: int,
        nuevo_titulo: str,
        nuevo_artista: str,
        nuevo_anio: int,
        nueva_duracion: str,
    ) -> tuple[int, Cancion]:
        for idx, c in enumerate(self.canciones):
            if c.id == id_cancion:
                c.titulo = nuevo_titulo
                c.artista = nuevo_artista
                c.anio = nuevo_anio
                c.duracion = nueva_duracion
                return idx, c
        raise ItemNoEncontradoError(f"No se encontró canción con ID {id_cancion}.")

    def guardar_en_texto(self, ruta: str):
        guardar_texto(ruta, self.canciones)

    def cargar_desde_texto(self, ruta: str):
        self.canciones = cargar_texto(ruta)

    def guardar_en_binario(self, ruta: str):
        guardar_binario(ruta, self.canciones)

    def cargar_desde_binario(self, ruta: str):
        self.canciones = list(cargar_binario(ruta))

    def actualizar_en_binario_por_posicion(self, ruta: str, posicion: int, cancion: Cancion):
        actualizar_registro(ruta, posicion, cancion)

    def alta_en_binario(self, ruta: str, cancion: Cancion):
        alta_binario(ruta, cancion)

    def baja_en_binario(self, ruta: str, posicion: int):
        baja_binario(ruta, posicion)
    def baja_en_binario(self, ruta: str, posicion: int):
        baja_binario(ruta, posicion)
