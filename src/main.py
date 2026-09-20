# Importamos la variable TEMA de config.py para saber que catalogo cargar.
from src.config import TEMA

# IMPORTANTE: Aca importamos la clase Biblioteca que armamos en la carpeta dominio.
# Porque el profe en la guía de la E2 dice que el main NO puede tener 
# la lógica de negocio. Todo el manejo de datos tiene que pasar por esta clase.
from src.dominio.biblioteca import Biblioteca

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

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
                else:
                    print("\nError: Canción no encontrada.")
            except ValueError:
                print("\nError: El ID debe ser un número entero.")
                
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
                
        else:
            # Si escriben cualquier otra cosa, aviso y el while vuelve a mostrar el menú.
            print("Opción inválida.")

# Esta linea es para que todo esto solo arranque si ejecuto este archivo directamente 
# desde la terminal, y no si otra persona u otro archivo lo importa sin querer.
if __name__ == "__main__":
    main()