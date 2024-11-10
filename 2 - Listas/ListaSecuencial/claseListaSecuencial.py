import numpy as np

class ListaSecuencial:
    __items: np.ndarray
    __ultimo: int ## cantidad elementos lista
    __max: int ## tamaño de la lista

    def __init__(self):
        self.__items = np.empty(10,dtype=int)
        self.__ultimo = 0 ## indice del ultimo elemento, es tambien la cantidad de componentes
        self.__max = 4 ## lista de cuatro elementos, su tamanio es max-1 por iniciar desde cero

    def vacia(self):
        if self.__ultimo == 0:
            return True
        else:
            return False

    def insertar(self,elem,posi):
        if posi > self.__max - 1:
            print('Posicion no valida. Excede la lista')
        else:
            if