class Celda: ## tambien llamada nodo
    __dato: None
    __siguiente: object ## objeto de clase celda/nodo

    def __init__(self,dat):
        self.__dato = dat
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self,sig):
        self.__siguiente = sig

    def getDato(self):
        return self.__dato