import numpy as np

class PilaSecuencial:
    ## atributos para numpy
    __dimension = 5
    __inscremento = 5  ## incremento del tamanio del arreglo

    ## atributos propios de la pila secuencial
    __items = None  ## arreglo
    __tope: int ## indice del tope de la pila
    __cant: int ## tamanio del arreglo y cantidad de elementos

    def __init__(self):
        self.__items = np.empty(self.__dimension,dtype=int)
        self.__tope = -1
        self.__cant = 0 ## la pila esta vacia

    def insertar(self,unElemento): ## cada nuevo elemento pasa a ser el tope de la pila (actualizar su indice)
        if self.__cant == self.__dimension:
            self.__items.resize(self.__inscremento)
            self.__dimension += self.__inscremento
        else:
            self.__tope += 1
            self.__items[self.__tope] = unElemento
            self.__cant += 1

    def vacia(self):
        result: bool
        if self.__cant == 0:
            result = True
        else:
            result = False
        return result

    def llena(self):
        result: bool
        if self.__cant == self.__dimension:
            result = True
        else:
            result = False
        return result

    def suprimir(self):
        aux = self.__items[self.__tope]
        self.__tope -= 1
        self.__cant -= 1
        return aux

    def recorrer(self):
        print('Recorrida de la pila')
        print('------------------------------')
        for i in range(self.__cant):
            print('{}'.format(self.__items[i]))