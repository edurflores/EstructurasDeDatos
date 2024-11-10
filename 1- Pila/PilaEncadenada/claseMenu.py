from clasePilaEncadenada import PilaEncadenada

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '0':self.salir
        }

        self.__pilaEnc = PilaEncadenada() ## esto se considera crear?

    def opcion(self,opc):
        func = self.__switcher.get(opc,lambda: print('Error. Opcion incorrecta.'))
        func()

    def opcion1(self):
        if self.__pilaEnc.vacia():
            print('La pila esta vacia.')
        else:
            print('La pila NO esta vacia.')
        print('----------------------------')

    def opcion2(self):
        num = int(input('Ingrese un numero: '))
        self.__pilaEnc.insertar(num)
        print('Se inserto el elemento.')
        print('----------------------------')

    def opcion3(self):
        self.__pilaEnc.suprimir()
        print('----------------------------')

    def opcion4(self):
        self.__pilaEnc.recorrer()
        print('----------------------------')

    def salir(self):
        print('Salio del programa.')
        print('----------------------------')