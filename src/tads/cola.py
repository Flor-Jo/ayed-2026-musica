from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError

class Cola:

    def __init__(self):
        # La cola tambien usa internamente nuestra lista enlazada
        self._items = ListaEnlazada()

    def encolar(self, dato):
        # La cola es FIFO. Los elementos nuevos van al final de la fila
        self._items.insertar_al_final(dato)

    def desencolar(self):
        # Si nadie esta esperando en la fila, lanzamos la excepcion
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")
        # Obtenemos al que esta primero en la fila
        frente = self.ver_frente()
        # Lo sacamos de la lista
        self._items.eliminar(frente)
        return frente

    def ver_frente(self):
        # Vemos quien es el proximo a salir sin sacarlo
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()