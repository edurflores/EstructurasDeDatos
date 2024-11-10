from claseMenu import Menu

if __name__ == '__main__':
    ban = False
    menu = Menu()

    while not ban:
        print('Menu Pila Secuencial')
        print('------------------------------')
        print('1- Insertar elemento.\n2- Suprimir elemento.\n3- Llena.\n4- Vacia.\n5- Recorrer.')
        print('0- Salir.')
        op = input('Seleccione opcion: ')
        menu.opcion(op)
        ban = op == '0'