"""Elegir un tema y no cambiarlo entre entregas."""

# "pokedex" | "recetario" | "musica"
TEMA = "musica"

# Por que los datos están acá?
# Según la guía de la E1 y E2, todavía no leemos los archivos .txt de la carpeta data/.
# Por ahora, los datos base los simulamos acá como una lista de diccionarios
# para poder probar que nuestras clases y la recursión funcionan.

CATALOGO_POP_2000S = [
    {
        "id": 1,
        "titulo": "Toxic",
        "artista": "Britney Spears",
        "anio": 2003,
        "duracion": "3:18"
    },
    {
        "id": 2,
        "titulo": "Bad Romance",
        "artista": "Lady Gaga",
        "anio": 2009,
        "duracion": "4:54"
    },
    {
        "id": 3,
        "titulo": "Hips Don't Lie",
        "artista": "Shakira feat. Wyclef Jean",
        "anio": 2006,
        "duracion": "3:38"
    },
    {
        "id": 4,
        "titulo": "Umbrella",
        "artista": "Rihanna feat. JAY-Z",
        "anio": 2007,
        "duracion": "4:35"
    },
    {
        "id": 5,
        "titulo": "Can't Get You Out of My Head",
        "artista": "Kylie Minogue",
        "anio": 2001,
        "duracion": "3:50"
    },
    {
        "id": 6,
        "titulo": "Bye Bye Bye",
        "artista": "*NSYNC",
        "anio": 2000,
        "duracion": "3:19"
    },
    {
        "id": 7,
        "titulo": "Crazy in Love",
        "artista": "Beyoncé feat. JAY-Z",
        "anio": 2003,
        "duracion": "3:56"
    },
    {
        "id": 8,
        "titulo": "Poker Face",
        "artista": "Lady Gaga",
        "anio": 2008,
        "duracion": "3:57"
    }
]

# esta funcion en el main.py original la usaba, pero en la E2 
# lo ideal es que la clase Biblioteca consuma la variable CATALOGO_POP_2000S directamente.
def obtener_catalogo():
    return CATALOGO_POP_2000S

