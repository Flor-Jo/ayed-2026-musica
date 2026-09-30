from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
  
    def __init__(self):
        # La pila guarda sus elementos en nuestra propia lista enlazada
        self._items = ListaEnlazada()

    def apilar(self, dato):
        # La pila es LIFO (Last In, First Out). Para que el ultimo en entrar quede arriba,siempre insertamos en la cabeza de la lista
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        # Si no hay historial para deshacer, lanzamos la excepcion propia
        if self.esta_vacia():
            raise PilaVaciaError("No hay elementos para deshacer.")
        # Obtenemos el dato de la cima usando nuestro metodo ver_tope
        tope = self.ver_tope()
        # Lo eliminamos de la lista enlazada
        self._items.eliminar(tope)
        return tope

    def ver_tope(self):
        # Miramos que hay arriba sin sacarlo
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        # Accedemos directamente al dato de la cabeza de la lista
        return self._items._cabeza.dato

    def esta_vacia(self):
        # Reutilizamos el metodo de la lista enlazada
        return self._items.esta_vacia()
