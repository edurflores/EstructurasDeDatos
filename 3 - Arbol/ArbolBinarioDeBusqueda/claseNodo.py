class Nodo:
    __clave: int ## ## puede ser dato o informacion, pero es el dato
    __izquierdo = None ## tipo celda (nodo izquierdo)
    __derecho = None ## tipo celda (nodo derecho)

    def __init__(self,X):
        self.__clave = X
        self.__izquierdo = None
        self.__derecho = None

    def setIzquierdo(self,izq):
        self.__izquierdo = izq

    def setDerecho(self,der):
        self.__derecho = der

    def getClave(self):
        return self.__clave

    def getIzquierdo(self):
        return self.__izquierdo

    def getDerecho(self):
        return self.__derecho

    def getGrado(self):
        grado = 0
        if self.__izquierdo is not None:
            grado += 1
        if self.__derecho is not None:
            grado += 1
        return grado