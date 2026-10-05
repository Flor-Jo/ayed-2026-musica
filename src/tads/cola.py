from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError


class Cola:
    def __init__(self):
        # La cola guarda sus elementos internamente en nuestra lista enlazada
        self._items = ListaEnlazada()

    def encolar(self, dato):
        # La cola es FIFO: agregamos al final de la lista
        self._items.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")
        return self._items.eliminar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items.ver_primero()

    def esta_vacia(self):
        return self._items.esta_vacia()
