from claseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    ban = False
    op: str
    while not ban:
        print('Test Pila Encadenada')
        print('----------------------------')
        print('1- Vacia.\n2- Insertar.\n3- Suprimir.\n4- Recorrer.')
        print('0- Salir.')
        op = input('Seleccione opcion: ')
        menu.opcion(op)
        ban = op == '0'