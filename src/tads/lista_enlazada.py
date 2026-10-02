from src.tads.nodo import Nodo # Importamos la clase Nodo que es el eslabón de la cadena

class ListaEnlazada:
    def __init__(self):
        # La lista inicia vacia, por lo que la cabeza (primer nodo) no apunta a nada (None)
        self._cabeza = None 
        # El tamaño inicial es 0 porque todavia no hay nodos
        self._tamanio = 0 

    def esta_vacia(self):
        # Devuelve True si no hay al menos un nodo en la cadena
        return self._cabeza is None

    def tamanio(self):
        # Devuelve la cantidad de nodos que hay actualmente en la lista
        return self._tamanio

    def insertar_al_inicio(self, dato):
        # Creamos un nuevo nodo que contiene el dato y que apunta a la cabeza actual
        # Luego, la cabeza de la lista pasa a ser este nuevo nodo
        self._cabeza = Nodo(dato, self._cabeza)
        # Sumamos 1 al tamaño de la lista
        self._tamanio += 1

    def insertar_al_final(self, dato):
        # Creamos un nuevo nodo con el dato a insertar
        nuevo = Nodo(dato)
        if self.esta_vacia():
            # Si la lista está vacía, el nuevo nodo se convierte directamente en la cabeza
            self._cabeza = nuevo
        else:
            # Si no está vacía, empezamos a recorrer desde la cabeza
            actual = self._cabeza
            # Avanzamos de nodo en nodo hasta llegar al que su 'siguiente' es None
            while actual.siguiente is not None:
                actual = actual.siguiente
            # Hacemos que el último nodo apunte al nuevo nodo recién creado
            actual.siguiente = nuevo
        # Sumamos 1 al tamaño de la lista
        self._tamanio += 1

    def eliminar(self, dato):
        if self.esta_vacia():
            # Si la lista está vacía, no hay nada que eliminar y salimos de la función
            return
        if self._cabeza.dato == dato:
            # Si el dato a eliminar está en el primer nodo, la cabeza pasa a ser el segundo nodo
            self._cabeza = self._cabeza.siguiente
            # Restamos 1 al tamaño de la lista
            self._tamanio -= 1
            return
        
        # Si el dato no era la cabeza, buscamos el nodo anterior al que queremos eliminar
        actual = self._cabeza
        while actual.siguiente is not None:
            # Si el nodo que le sigue al actual contiene el dato que buscamos
            if actual.siguiente.dato == dato:
                # El nodo actual pasa a apuntar al nodo que le sigue al que estamos eliminando, lo saltea
                actual.siguiente = actual.siguiente.siguiente
                # Restamos 1 al tamaño
                self._tamanio -= 1
                return
            # Si no es el dato, avanzamos al siguiente nodo para seguir buscando
            actual = actual.siguiente

    def buscar(self, dato):
        # Empezamos el recorrido desde el primer nodo
        actual = self._cabeza
        while actual is not None:
            # Si el dato del nodo actual coincide con lo que buscamos, devolvemos ese nodo
            if actual.dato == dato:
                return actual
            # Si no coincide, avanzamos al siguiente nodo
            actual = actual.siguiente
        # Si recorrimos toda la lista y no lo encontramos, devolvemos None
        return None

    def __iter__(self):
        # Empezamos el recorrido desde la cabeza cuando Python inicia un ciclo for
        actual = self._cabeza
        while actual is not None:
            # yield devuelve el dato y pausa la función hasta que el ciclo for pida el siguiente elemento
            yield actual.dato
            # Avanzamos al siguiente nodo
            actual = actual.siguiente
            
    def ver_primero(self):
        """Devuelve el dato del primer nodo sin quitarlo (None si está vacía)."""
        if self.esta_vacia():
            return None
        return self._cabeza.dato

    def eliminar_primero(self):
        """Desvincula y devuelve el dato del primer nodo en O(1)."""
        if self.esta_vacia():
            return None
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato
