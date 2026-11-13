# Importamos la variable TEMA de config.py para saber que catalogo cargar.
import os
from src.config import TEMA

# IMPORTANTE: Aca importamos la clase Biblioteca que armamos en la carpeta dominio.
# Porque el profe en la guía de la E2 dice que el main NO puede tener 
# la lógica de negocio. Todo el manejo de datos tiene que pasar por esta clase.
from src.dominio.biblioteca import Biblioteca
from src.dominio.playlist import Playlist
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import (
    PilaVaciaError,
    ColaVaciaError,
    ColeccionLlenaError,
)

# E4: Importamos los algoritmos propios de búsqueda y ordenamiento
# Prohibido el uso de in, .index(), sorted(), list.sort() y bisect
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def duracion_a_segundos(duracion_str: str) -> int:
    """Convierte 'mm:ss' a segundos totales enteros para ordenar correctamente."""
    try:
        partes = duracion_str.strip().split(":")
        if len(partes) == 2:
            return int(partes[0]) * 60 + int(partes[1])
        return int(duracion_str)
    except Exception:
        return 0

def mostrar_menu():
    # Imprime el menu principal en la consola.
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print(f"\n=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    # BIBLIOTECA
    # Para que al arrancar el programa, la clase cargue las canciones en la memoria.
    # Asi dejamos de usar diccionarios sueltos en el main, cumpliendo con la consigna de usar objetos.
    biblioteca = Biblioteca()
    playlist = Playlist(nombre="Favoritos Pop 2000s", capacidad_maxima=5)
    # E3: Pila para historial (deshacer) y Cola para reproducción
    historial = Pila()
    cola_reproduccion = Cola()

    # E4: Estado para registrar el criterio con el que se ordenó el catálogo
    # Nos permite cumplir la regla 4.2: la binaria requiere colección ordenada
    criterio_orden_actual = None

    opcion = None
    while opcion != "0":
        mostrar_menu()
        # El .strip() le saca los espacios en blanco adelante y atrás por si tipeo espacios sin querer al elegir opción.
        opcion = input("> ").strip()
        
        if opcion == "0":
            print("Chau.")
            
        elif opcion == "1":
            print("\n--- Catálogo de Música (Pop 2000s) ---")
            # Le pido a la biblioteca que me devuelva la lista de objetos Cancion entera.
            canciones = biblioteca.obtener_todas()
            for cancion in canciones:
                # Para que usamos .resumen() de la clase? 
                # Por encapsulamiento: el objeto Cancion sabe como imprimirse a si mismo mucho mejor que este main.
                print(cancion.resumen())
                
        elif opcion == "2":
            # Por que usamos try-except? 
            # Porque si pedimoas un ID (que tiene que ser numero) y tipeo "hola", 
            # el int() me tira un ValueError y el programa explota. Con el except lo atrapamos y el menu sigue vivo.
            try:
                id_buscar = int(input("Ingresá el ID de la canción a buscar: "))
                # Le delego la busqueda a la biblioteca en vez de meter un 'for' aca adentro.
                cancion = biblioteca.buscar_por_id(id_buscar)
                if cancion:
                    print("\nDetalle de la canción:")
                    print(cancion.resumen())
                    # Agregamos al historial (Pila) al consultar detalle
                    historial.apilar(cancion)
                else:
                    print("\nError: Canción no encontrada.")
            except ValueError:
                print("\nError: El ID debe ser un número entero.")

        elif opcion == "3":
            # OPCIÓN 3: BÚSQUEDA (E4 - Lineal y Binaria propias)
            canciones = biblioteca.obtener_todas()
            print("\n--- Buscar Canción ---")
            print("1. Búsqueda lineal (por título)")
            print("2. Búsqueda binaria (por título)")
            metodo = input("Elegí el método (1/2): ").strip()

            if metodo == "1":
                titulo_buscado = input("Ingresá el título de la canción: ").strip()
                encontrada = busqueda_lineal(canciones, titulo_buscado, obtener_clave=lambda c: c.titulo)
                if encontrada:
                    print(f"\n[Encontrada (lineal)]: {encontrada.resumen()}")
                    historial.apilar(encontrada)
                else:
                    print("\nCanción no encontrada.")

            elif metodo == "2":
                titulo_buscado = input("Ingresá el título de la canción: ").strip()
                # Regla 4.2 / Caso P11: si no está ordenado por título, reordena y notifica
                if criterio_orden_actual != "titulo":
                    print("Aviso: El catálogo no estaba ordenado por título. Reordenando automáticamente...")
                    ordenar_insercion(canciones, obtener_clave=lambda c: c.titulo)
                    criterio_orden_actual = "titulo"

                encontrada = busqueda_binaria(canciones, titulo_buscado, obtener_clave=lambda c: c.titulo)
                if encontrada:
                    print(f"\n[Encontrada (binaria)]: {encontrada.resumen()}")
                    historial.apilar(encontrada)
                else:
                    print("\nCanción no encontrada.")
            else:
                print("Opción de búsqueda inválida.")

        elif opcion == "4":
            # OPCIÓN 4: ORDENAMIENTO (E4 - Dos ordenamientos y dos criterios)
            canciones = biblioteca.obtener_todas()
            print("\n--- Ordenar Catálogo ---")
            print("Criterio de orden:")
            print("1. Por título")
            print("2. Por duración")
            crit_op = input("Elegí el criterio (1/2): ").strip()

            if crit_op == "1":
                clave_func = lambda c: c.titulo
                nombre_criterio = "título"
                criterio_clave = "titulo"
            elif crit_op == "2":
                clave_func = lambda c: duracion_a_segundos(c.duracion)
                nombre_criterio = "duración"
                criterio_clave = "duracion"
            else:
                print("Criterio inválido.")
                continue

            print("\nAlgoritmo:")
            print("1. Selección (no estable)")
            print("2. Inserción (estable)")
            alg_op = input("Elegí el algoritmo (1/2): ").strip()

            if alg_op == "1":
                ordenar_seleccion(canciones, obtener_clave=clave_func)
                criterio_orden_actual = criterio_clave
                print(f"\nCatálogo ordenado por {nombre_criterio} con éxito usando Selección.")
            elif alg_op == "2":
                ordenar_insercion(canciones, obtener_clave=clave_func)
                criterio_orden_actual = criterio_clave
                print(f"\nCatálogo ordenado por {nombre_criterio} con éxito usando Inserción.")
            else:
                print("Algoritmo inválido.")
                
        elif opcion == "5":
            # OPCIÓN 5: RECURSIÓN (LO MAS IMPORTANTE DE ESTA ENTREGA)
            # Igual que en la opción 2, atrapamos el error por si meten letras en vez de numeros.
            try:
                id_buscar = int(input("Ingresá el ID de la canción para ver sus versiones derivadas: "))
                
                # Primero nos fijamos si la cancion realmente existe en mi lista llamando al metodo que busca.
                cancion = biblioteca.buscar_por_id(id_buscar)
                if not cancion:
                    print("\nError: Canción no encontrada.")
                else:
                    # Si existe, llamo a mi funcion recursiva. Esto va a saltar al archivo 
                    # biblioteca.py, va a hacer la recursion alla (llamandose a ss misma), y me devuelve la lista armada.
                    versiones = biblioteca.obtener_todas_las_versiones(id_buscar)
                    print(f"\nVersiones derivadas del ID {id_buscar}: {versiones}")
            except ValueError:
                print("\nError: El ID debe ser un número entero.")
                
        elif opcion == "6":
            print(f"\n--- {playlist.nombre} ({playlist.cantidad()}/{playlist.capacidad_maxima}) ---")
            print("a. Ver canciones en la playlist")
            print("b. Agregar canción a la playlist")
            sub_op = input("Elige una opción (a/b): ").strip().lower()

            if sub_op == "a":
                if playlist.esta_vacia():
                    print("La playlist está vacía.")
                else:
                    print("\nCanciones en tu playlist:")
                    # Uso obligatorio del iterador de la ListaEnlazada
                    for c in playlist:
                        print(f" - {c.resumen()}")

            elif sub_op == "b":
                try:
                    id_c = int(input("ID de canción a agregar a la playlist: "))
                    c = biblioteca.buscar_por_id(id_c)
                    if not c:
                        print("Error: La canción no existe en el catálogo.")
                    else:
                        playlist.agregar_cancion(c)
                        print(f"'{c.titulo}' agregada con éxito a la playlist.")
                except ValueError:
                    print("Error: El ID debe ser un número entero.")
                except ColeccionLlenaError as e:
                    # Captura estricta de la excepción propia (Punto 6 de la consigna)
                    print(f"No se pudo agregar: {e}")
            else:
                print("Opción inválida dentro de playlist.")

        elif opcion == "7":
            print("\n--- Historial de navegación (Pila - LIFO) ---")
            print("a. Ver última canción consultada (tope)")
            print("b. Deshacer / quitar última consulta")
            sub_op = input("Elige una opción (a/b): ").strip().lower()

            if sub_op == "a":
                try:
                    ultima = historial.ver_tope()
                    print(f"Última canción en el tope: {ultima.resumen()}")
                except PilaVaciaError as e:
                    print(f"Aviso: {e}")

            elif sub_op == "b":
                try:
                    desapilada = historial.desapilar()
                    print(f"Se quitó del historial: {desapilada.resumen()}")
                except PilaVaciaError as e:
                    print(f"Aviso: {e}")
            else:
                print("Opción inválida dentro de historial.")

        elif opcion == "8":
            print("\n--- Cola de reproducción (Cola - FIFO) ---")
            print("a. Encolar canción para reproducir")
            print("b. Reproducir siguiente canción (desencolar)")
            print("c. Ver próxima canción en turno")
            sub_op = input("Elige una opción (a/b/c): ").strip().lower()

            if sub_op == "a":
                try:
                    id_c = int(input("ID de canción a poner en cola: "))
                    c = biblioteca.buscar_por_id(id_c)
                    if not c:
                        print("Error: Canción no encontrada.")
                    else:
                        cola_reproduccion.encolar(c)
                        print(f"'{c.titulo}' agregada a la cola de reproducción.")
                except ValueError:
                    print("Error: El ID debe ser un número entero.")

            elif sub_op == "b":
                try:
                    sonando = cola_reproduccion.desencolar()
                    print(f"Reproduciendo ahora: {sonando.resumen()}")
                except ColaVaciaError as e:
                    print(f"Aviso: {e}")

            elif sub_op == "c":
                try:
                    proxima = cola_reproduccion.ver_frente()
                    print(f"Próxima en la fila: {proxima.resumen()}")
                except ColaVaciaError as e:
                    print(f"Aviso: {e}")
            else:
                print("Opción inválida dentro de cola.")
                

        
        elif opcion == "9":
            # OPCIÓN 9: PERSISTENCIA EN TEXTO Y BINARIO + ABM PERSISTENTE (E5)
            ruta_txt = os.path.join("data", "canciones.txt")
            ruta_bin = os.path.join("data", "canciones.bin")

            print("\n--- Guardar / Cargar Archivos y ABM Persistente (E5) ---")
            print("a. Guardar catálogo en texto (.txt)")
            print("b. Cargar catálogo desde texto (.txt)")
            print("c. Guardar catálogo en binario (.bin)")
            print("d. Cargar catálogo desde binario (.bin)")
            print("e. Alta de canción (persistente en .txt y .bin)")
            print("f. Baja de canción (persistente en .txt y .bin)")
            print("g. Modificar canción (acceso directo seek en .bin + .txt)")
            sub_op = input("Elige una opción (a-g): ").strip().lower()

            try:
                if sub_op == "a":
                    biblioteca.guardar_en_texto(ruta_txt)
                    print(f"Catálogo guardado con éxito en '{ruta_txt}'.")

                elif sub_op == "b":
                    ruta_in = input(f"Ruta del archivo .txt [Enter para '{ruta_txt}']: ").strip() or ruta_txt
                    biblioteca.cargar_desde_texto(ruta_in)
                    criterio_orden_actual = None
                    print(f"Catálogo cargado desde '{ruta_in}' ({len(biblioteca.obtener_todas())} canciones).")

                elif sub_op == "c":
                    biblioteca.guardar_en_binario(ruta_bin)
                    print(f"Catálogo guardado con éxito en '{ruta_bin}' (registros fijos de 84 bytes).")

                elif sub_op == "d":
                    ruta_in = input(f"Ruta del archivo .bin [Enter para '{ruta_bin}']: ").strip() or ruta_bin
                    biblioteca.cargar_desde_binario(ruta_in)
                    criterio_orden_actual = None
                    print(f"Catálogo cargado desde '{ruta_in}' ({len(biblioteca.obtener_todas())} canciones).")

                elif sub_op == "e":
                    id_c = int(input("Nuevo ID (entero): "))
                    titulo = input("Título: ").strip()
                    artista = input("Artista: ").strip()
                    anio = int(input("Año: "))
                    duracion = input("Duración (ej. 03:45): ").strip()

                    nueva = Cancion(id_c, titulo, artista, anio, duracion)
                    biblioteca.agregar_cancion(nueva)
                    criterio_orden_actual = None

                    # Persistimos el alta en disco
                    biblioteca.guardar_en_texto(ruta_txt)
                    biblioteca.alta_en_binario(ruta_bin, nueva)
                    print(f"Canción '{titulo}' agregada y persistida en disco.")

                elif sub_op == "f":
                    id_c = int(input("ID de la canción a dar de baja: "))
                    pos, eliminada = biblioteca.eliminar_cancion(id_c)
                    criterio_orden_actual = None

                    # Persistimos la baja en disco
                    biblioteca.guardar_en_texto(ruta_txt)
                    if os.path.exists(ruta_bin):
                        biblioteca.baja_en_binario(ruta_bin, pos)
                    print(f"Canción '{eliminada.titulo}' eliminada y cambios persistidos.")

                elif sub_op == "g":
                    id_c = int(input("ID de la canción a modificar: "))
                    nuevo_tit = input("Nuevo título: ").strip()
                    nuevo_art = input("Nuevo artista: ").strip()
                    nuevo_anio = int(input("Nuevo año: "))
                    nueva_dur = input("Nueva duración (ej. 03:45): ").strip()

                    pos, actualizada = biblioteca.modificar_cancion(
                        id_c, nuevo_tit, nuevo_art, nuevo_anio, nueva_dur
                    )
                    criterio_orden_actual = None

                    # Persistimos en .txt y actualizamos por posición con seek() en .bin
                    biblioteca.guardar_en_texto(ruta_txt)
                    if os.path.exists(ruta_bin):
                        biblioteca.actualizar_en_binario_por_posicion(ruta_bin, pos, actualizada)
                        print(f"Registro en posición {pos} pisado con seek() en '{ruta_bin}' y actualizado en '{ruta_txt}'.")
                    else:
                        biblioteca.guardar_en_binario(ruta_bin)
                        print(f"Canción actualizada y guardada en '{ruta_txt}' y '{ruta_bin}'.")

                else:
                    print("Subopción inválida dentro de archivos.")
        else:
            # Si escriben cualquier otra cosa, aviso y el while vuelve a mostrar el menú.
            print("Opción inválida.")
            
            except ArchivoInvalidoError as e:
                print(f"\nError de archivo inválido: {e}")
            except ItemNoEncontradoError as e:
                print(f"\nError: {e}")
            except ValueError as e:
                print(f"\nError de datos: {e}")
            except IndexError as e:
                print(f"\nError de posición en archivo binario: {e}")

# Esta linea es para que todo esto solo arranque si ejecuto este archivo directamente 
# desde la terminal, y no si otra persona u otro archivo lo importa sin querer.
if __name__ == "__main__":
    main()
