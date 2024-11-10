from claseCelda import Celda

class PilaEncadenada:
    __tope: Celda
    __cant: int

    def __init__(self):
        self.__tope = None
        self.__cant = 0

    def insertar(self,unDato):
        celda = Celda(unDato)
        celda.setSiguiente(self.__tope)
        self.__tope = celda
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print('La pila ya esta vacia.')
        else:
            aux = self.__tope
            print('Dato eliminado: {}'.format(aux.getDato()))
            self.__tope = self.__tope.getSiguiente()
            del aux
            self.__cant -= 1

    def recorrer(self):
        if self.vacia():
            print('La pila esta vacia.')
        else:
            aux = self.__tope
            while aux is not None:
                print(aux.getDato())
                aux = aux.getSiguiente()

    def vacia(self): ## true si esta vacia, false si esta llena
        if self.__cant == 0:
            return True
        else:
            return False