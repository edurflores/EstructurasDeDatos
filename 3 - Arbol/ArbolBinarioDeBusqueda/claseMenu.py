from claseNodo import Nodo
from claseManejadorArbolBB import ManejadorArbolBB


class Menu:
    __switcher: dict

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '6':self.opcion6,
            '9':self.opcion9,
            '10':self.opcion10,
            '11':self.opcion11,
            '12':self.opcion12,
            '0':self.salir
        }

        self.__ArbolBBusq = None
        self.__manejadorArbolBB = ManejadorArbolBB()

    def creaArbol(self): ## metodo crear
        num = int(input('Ingrese raiz del arbol: '))
        self.__ArbolBBusq = Nodo(num)

    def opcion(self,opc):
        func = self.__switcher.get(opc,lambda:print('Error. Opcion incorrecta.'))
        func()

    def opcion1(self):
        num = int(input('Ingrese numero a insertar: '))
        self.__manejadorArbolBB.insertar(self.__ArbolBBusq,num)
        print('-----------------------------------')

    def opcion2(self):
        num = int(input('Ingrese numero a suprimir: '))
        print('Elemento suprimido: {}'.format(self.__manejadorArbolBB.suprimir(self.__ArbolBBusq,num)))
        print('-----------------------------------')

    def opcion6(self):
        print('Comprobar si es hoja')
        print('-----------------------------------')
        num = int(input('Ingrese numero a comprobar: '))
        self.__manejadorArbolBB.hoja(self.__ArbolBBusq,num)
        print('-----------------------------------')

    def opcion9(self):
        print('Recorrido en InOrden')
        print('-----------------------------------')
        self.__manejadorArbolBB.inOrden(self.__ArbolBBusq)
        print('-----------------------------------')

    def opcion10(self):
        print('Recorrido en PreOrden')
        print('-----------------------------------')
        self.__manejadorArbolBB.preOrden(self.__ArbolBBusq)
        print('-----------------------------------')

    def opcion11(self):
        print('Recorrido en PostOrden')
        print('-----------------------------------')
        self.__manejadorArbolBB.postOrden(self.__ArbolBBusq)
        print('-----------------------------------')

    def opcion12(self):
        print('Busqueda en el arbol')
        print('-----------------------------------')
        num = int(input('Ingrese numero a buscar: '))
        print('Encontrado: {}'.format(self.__manejadorArbolBB.buscar(self.__ArbolBBusq,num)))
        print('-----------------------------------')

    def salir(self):
        print('Salio del programa.')
        print('-----------------------------------')