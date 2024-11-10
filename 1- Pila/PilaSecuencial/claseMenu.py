from clasePilaSecuencial import PilaSecuencial

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '0':self.salir
        }

        self.__pilaSec = PilaSecuencial()

    def opcion(self,opc):
        func = self.__switcher.get(opc,lambda: print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        elem = int(input('Ingrese un numero: '))
        self.__pilaSec.insertar(elem)
        print('Se inserto el elemento.')
        print('------------------------------')

    def opcion2(self):
        if self.__pilaSec.vacia():
            print('La pila ya esta vacia.')
        else:
            print('Elemento eliminado: {}'.format(self.__pilaSec.suprimir()))
        print('------------------------------')

    def opcion3(self):
        if self.__pilaSec.llena():
            print('La pila esta llena.')
        else:
            print('La pila NO esta llena.')
        print('------------------------------')

    def opcion4(self):
        if self.__pilaSec.vacia():
            print('La pila esta vacia.')
        else:
            print('La pila NO esta vacia.')
        print('------------------------------')

    def opcion5(self):
        if self.__pilaSec.vacia():
            print('La pila esta vacia.')
        else:
            self.__pilaSec.recorrer()
        print('------------------------------')

    def salir(self):
        print('Salio del programa.')