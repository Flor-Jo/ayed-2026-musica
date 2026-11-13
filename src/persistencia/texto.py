import os
from src.dominio.cancion import Cancion
from src.excepciones import ArchivoInvalidoError

SEPARADOR = "|"


def guardar_texto(ruta: str, canciones: list):
    """Guarda el catálogo de canciones en un archivo de texto plano delimitado por '|'."""
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("id|titulo|artista|anio|duracion\n")
        for c in canciones:
            linea = f"{c.id}{SEPARADOR}{c.titulo}{SEPARADOR}{c.artista}{SEPARADOR}{c.anio}{SEPARADOR}{c.duracion}\n"
            archivo.write(linea)


def cargar_texto(ruta: str) -> list:
    """Carga canciones desde un .txt. Lanza ArchivoInvalidoError si el archivo no existe o está corrupto."""
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    canciones = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    if not lineas:
        raise ArchivoInvalidoError("El archivo de texto está vacío.")

    encabezado = lineas[0].strip()
    if encabezado != "id|titulo|artista|anio|duracion":
        raise ArchivoInvalidoError("Encabezado inválido o archivo corrupto.")

    for num_linea, linea in enumerate(lineas[1:], start=2):
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(SEPARADOR)
        if len(partes) != 5:
            raise ArchivoInvalidoError(f"Formato inválido en línea {num_linea}: se esperaban 5 campos.")
        try:
            id_cancion = int(partes[0])
            titulo = partes[1]
            artista = partes[2]
            anio = int(partes[3])
            duracion = partes[4]
        except ValueError:
            raise ArchivoInvalidoError(f"Tipos de datos corruptos en línea {num_linea}.")

        canciones.append(Cancion(id_cancion, titulo, artista, anio, duracion))

    return canciones


# Alias de compatibilidad con los nombres del esqueleto inicial
cargar_csv = cargar_texto
guardar_csv = guardar_texto
