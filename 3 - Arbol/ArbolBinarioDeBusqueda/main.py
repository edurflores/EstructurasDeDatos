from claseMenu import Menu

if __name__ == '__main__':
    ban = False
    menu = Menu()
    menu.creaArbol()
    while not ban:
        print('Menu Arbol Binario de Busqueda')
        print('-----------------------------------')
        print('1- Insertar. 2- Suprimir. 3- Hijo. 4- Padre. 5- Nivel. 6- Hoja.')
        print('7- Altura. 8- Camino. 9- InOrden. 10- PreOrden. 11- PostOrden.')
        print('12- Buscar. 13- Recorrer.')
        print('0- Salir.')
        op = input('Seleccione opcion: ')
        menu.opcion(op)
        ban = op == '0'