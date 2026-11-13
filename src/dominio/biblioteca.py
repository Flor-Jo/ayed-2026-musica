from pathlib import Path
from src.tads.lista_enlazada import ListaEnlazada
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
    """Clase gestora del catálogo musical basada en ListaEnlazada (E1-E5)."""

    def _init_(self):
        self.canciones = ListaEnlazada()
        self.versiones_matriz = {
            3: [8],
            8: [1],
        }
        self.cargar_datos_iniciales()

    def _iter_(self):
        return iter(self.canciones)

    def tamanio(self) -> int:
        return self.canciones.tamanio()

    def obtener_todas(self) -> list:
        """Devuelve una lista de Python con los elementos de la ListaEnlazada para listar y ordenar (E1/E4)."""
        return [c for c in self.canciones]

    def reemplazar_catalogo(self, lista_canciones):
        """Reconstruye la ListaEnlazada a partir de cualquier iterable (list o ListaEnlazada)."""
        if isinstance(lista_canciones, ListaEnlazada):
            self.canciones = lista_canciones
            return
        self.canciones = ListaEnlazada()
        for c in lista_canciones:
            self.canciones.insertar_al_final(c)

    def cargar_datos_iniciales(self):
        """Si existe data/canciones.txt lo carga; si no, inicializa con CATALOGO_POP_2000S."""
        ruta_txt = Path(_file_).resolve().parents[2] / "data" / "canciones.txt"
        if ruta_txt.exists():
            try:
                cargadas = cargar_texto(str(ruta_txt))
                self.reemplazar_catalogo(cargadas)
                return
            except Exception:
                pass

        for item in CATALOGO_POP_2000S:
            cancion = Cancion(
                id_cancion=item["id"],
                titulo=item["titulo"],
                artista=item["artista"],
                anio=item["anio"],
                duracion=item["duracion"],
            )
            self.canciones.insertar_al_final(cancion)

    def buscar_por_id(self, id_cancion: int):
        for cancion in self.canciones:
            if cancion.id == id_cancion:
                return cancion
        return None

    def obtener_posicion_por_id(self, id_cancion: int) -> int:
        """Devuelve el índice 0-based de la canción en la ListaEnlazada."""
        for idx, cancion in enumerate(self.canciones):
            if cancion.id == id_cancion:
                return idx
        raise ItemNoEncontradoError(f"No se encontró canción con ID {id_cancion}.")

    def obtener_versiones_directas(self, id_cancion: int) -> list:
        return self.versiones_matriz.get(id_cancion, [])

    # ---------------------------------------------------------
    # RECURSIÓN EN CATÁLOGO (E2)
    # ---------------------------------------------------------
    def obtener_todas_las_versiones(self, id_cancion: int) -> list:
        directas = self.obtener_versiones_directas(id_cancion)
        if not directas:
            return []
        resultado = list(directas)
        for v in directas:
            resultado += self.obtener_todas_las_versiones(v)
        return resultado

    # ---------------------------------------------------------
    # ABM Y PERSISTENCIA EN TEXTO Y BINARIO (E5)
    # ---------------------------------------------------------
    def agregar_cancion(self, nueva_cancion: Cancion):
        if self.buscar_por_id(nueva_cancion.id) is not None:
            raise ValueError(f"Ya existe una canción con el ID {nueva_cancion.id}.")
        self.canciones.insertar_al_final(nueva_cancion)

    def eliminar_cancion(self, id_cancion: int) -> tuple[int, Cancion]:
        """Elimina una canción y devuelve (posicion_0_based, cancion_eliminada)."""
        pos = self.obtener_posicion_por_id(id_cancion)
        cancion = self.buscar_por_id(id_cancion)
        self.canciones.eliminar(cancion)
        return pos, cancion

    def modificar_cancion(
        self,
        id_cancion: int,
        nuevo_titulo: str,
        nuevo_artista: str,
        nuevo_anio: int,
        nueva_duracion: str,
    ) -> tuple[int, Cancion]:
        """Modifica una canción en la ListaEnlazada y devuelve (posicion_0_based, cancion_actualizada)."""
        for idx, c in enumerate(self.canciones):
            if c.id == id_cancion:
                c.titulo = nuevo_titulo
                c.artista = nuevo_artista
                c.anio = nuevo_anio
                c.duracion = nueva_duracion
                return idx, c
        raise ItemNoEncontradoError(f"No se encontró canción con ID {id_cancion}.")

    def guardar_en_texto(self, ruta: str):
        guardar_texto(ruta, self.obtener_todas())

    def cargar_desde_texto(self, ruta: str):
        cargadas = cargar_texto(ruta)
        self.reemplazar_catalogo(cargadas)

    def guardar_en_binario(self, ruta: str):
        # Tu guardar_binario recibe directamente la ListaEnlazada o Biblioteca
        guardar_binario(ruta, self.canciones)

    def cargar_desde_binario(self, ruta: str):
        # Tu cargar_binario devuelve directamente una ListaEnlazada
        self.canciones = cargar_binario(ruta)

    def actualizar_en_binario_por_posicion(self, ruta: str, posicion: int, cancion: Cancion):
        actualizar_registro(ruta, posicion, cancion)

    def alta_en_binario(self, ruta: str, cancion: Cancion):
        alta_binario(ruta, cancion)

    def baja_en_binario(self, ruta: str, posicion: int):
        baja_binario(ruta, posicion)
