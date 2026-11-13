# src/persistencia/binario.py
import os
import struct
from src.dominio.cancion import Cancion
from src.excepciones import ArchivoInvalidoError
from src.tads.lista_enlazada import ListaEnlazada

# Layout binario definitivo
FORMATO_HEADER = "<4s1sI"
TAMANIO_HEADER = struct.calcsize(FORMATO_HEADER)  # 9 bytes

FORMATO_REGISTRO = "<I40s30sH8s"
TAMANIO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)  # 84 bytes

MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"M"


def _empaquetar_texto(texto: str, longitud: int) -> bytes:
    """Codifica a UTF-8 y rellena con bytes nulos hasta la longitud fija."""
    if texto is None:
        texto = ""
    return str(texto).encode("utf-8")[:longitud].ljust(longitud, b"\x00")


def _desempaquetar_texto(datos: bytes) -> str:
    """Decodifica desde UTF-8 quitando el relleno nulo."""
    return datos.rstrip(b"\x00").decode("utf-8", errors="replace")


def _empaquetar_cancion(cancion: Cancion) -> bytes:
    return struct.pack(
        FORMATO_REGISTRO,
        cancion.id,
        _empaquetar_texto(cancion.titulo, 40),
        _empaquetar_texto(cancion.artista, 30),
        cancion.anio,
        _empaquetar_texto(str(cancion.duracion), 8),
    )


def guardar_binario(ruta: str, biblioteca):
    """Guarda la colección completa (recibe Biblioteca o ListaEnlazada) en formato binario."""
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "wb") as f:
        # Usamos biblioteca.tamanio() en lugar de len() para evitar errores con la ListaEnlazada
        cantidad = biblioteca.tamanio() if hasattr(biblioteca, "tamanio") else len(biblioteca)
        header = struct.pack(FORMATO_HEADER, MAGIA_ESPERADA, TEMA_ESPERADO, cantidad)
        f.write(header)
        for cancion in biblioteca:  # Usa el iterador de la ListaEnlazada
            f.write(_empaquetar_cancion(cancion))


def cargar_binario(ruta: str) -> ListaEnlazada:
    """Lee el archivo binario validando header, magia, tema y tamaño exacto. Devuelve ListaEnlazada."""
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo binario '{ruta}' no existe.")

    tamanio_archivo = os.path.getsize(ruta)
    if tamanio_archivo < TAMANIO_HEADER:
        raise ArchivoInvalidoError("Archivo binario demasiado corto: header incompleto.")

    biblioteca = ListaEnlazada()
    with open(ruta, "rb") as f:
        header_bytes = f.read(TAMANIO_HEADER)
        magia, tema, cantidad = struct.unpack(FORMATO_HEADER, header_bytes)

        if magia != MAGIA_ESPERADA:
            raise ArchivoInvalidoError(f"Firma mágica inválida: se esperaba {MAGIA_ESPERADA}, se leyó {magia}.")
        if tema != TEMA_ESPERADO:
            raise ArchivoInvalidoError(f"Tema binario incompatible: se esperaba {TEMA_ESPERADO}, se leyó {tema}.")

        tamanio_esperado = TAMANIO_HEADER + (cantidad * TAMANIO_REGISTRO)
        if tamanio_archivo != tamanio_esperado:
            raise ArchivoInvalidoError(
                f"Archivo binario truncado o corrupto (esperados {tamanio_esperado} bytes, hay {tamanio_archivo})."
            )

        for _ in range(cantidad):
            reg_bytes = f.read(TAMANIO_REGISTRO)
            id_c, tit_b, art_b, anio, dur_b = struct.unpack(FORMATO_REGISTRO, reg_bytes)
            cancion = Cancion(
                id_cancion=id_c,
                titulo=_desempaquetar_texto(tit_b),
                artista=_desempaquetar_texto(art_b),
                anio=anio,
                duracion=_desempaquetar_texto(dur_b),
            )
            biblioteca.insertar_al_final(cancion)

    return biblioteca


def actualizar_registro(ruta: str, posicion: int, cancion: Cancion):
    """Pisa un registro puntual por posición (0-based) usando acceso directo seek()."""
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo binario '{ruta}' no existe.")

    with open(ruta, "r+b") as f:
        header_bytes = f.read(TAMANIO_HEADER)
        if len(header_bytes) < TAMANIO_HEADER:
            raise ArchivoInvalidoError("Header binario corrupto.")

        magia, tema, cantidad = struct.unpack(FORMATO_HEADER, header_bytes)
        if magia != MAGIA_ESPERADA or tema != TEMA_ESPERADO:
            raise ArchivoInvalidoError("Header binario inválido.")

        if posicion < 0 or posicion >= cantidad:
            raise IndexError(f"Posición {posicion} fuera de rango (0 a {cantidad - 1}).")

        offset = TAMANIO_HEADER + (posicion * TAMANIO_REGISTRO)
        f.seek(offset)
        f.write(_empaquetar_cancion(cancion))


def alta_binario(ruta: str, cancion: Cancion):
    """Agrega un registro al final del archivo binario y actualiza la cantidad en el header."""
    if not os.path.exists(ruta):
        # Si no existe, lo creamos con cantidad 1
        with open(ruta, "wb") as f:
            f.write(struct.pack(FORMATO_HEADER, MAGIA_ESPERADA, TEMA_ESPERADO, 1))
            f.write(_empaquetar_cancion(cancion))
        return

    with open(ruta, "r+b") as f:
        header_bytes = f.read(TAMANIO_HEADER)
        magia, tema, cantidad = struct.unpack(FORMATO_HEADER, header_bytes)
        
        # Ir al final del archivo para hacer append
        f.seek(0, 2)
        f.write(_empaquetar_cancion(cancion))
        
        # Volver al principio y actualizar la cantidad en el header (+1)
        f.seek(0)
        f.write(struct.pack(FORMATO_HEADER, magia, tema, cantidad + 1))


def baja_binario(ruta: str, posicion: int):
    """Elimina el registro en la posición indicada reescribiendo el archivo y actualizando el header."""
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo binario '{ruta}' no existe.")

    with open(ruta, "r+b") as f:
        header_bytes = f.read(TAMANIO_HEADER)
        magia, tema, cantidad = struct.unpack(FORMATO_HEADER, header_bytes)

        if posicion < 0 or posicion >= cantidad:
            raise IndexError(f"Posición {posicion} fuera de rango.")

        # Leer todos los registros
        registros = [f.read(TAMANIO_REGISTRO) for _ in range(cantidad)]
        
        # Quitar el registro dado de baja
        del registros[posicion]

        # Reescribir archivo con la nueva cantidad
        f.seek(0)
        f.truncate()
        f.write(struct.pack(FORMATO_HEADER, magia, tema, len(registros)))
        for reg in registros:
            f.write(reg)
