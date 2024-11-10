from claseNodo import Nodo

class ManejadorArbolBB: ## es el nodo. Es decir, cada nodo es un arbol.

    def insertar(self,arbol,X):
        nuevoNodo = Nodo(X)
        if arbol is None: ## arbol vacio
            arbol = nuevoNodo
        else:
            if X < arbol.getClave():
                if arbol.getIzquierdo() is None:
                    arbol.setIzquierdo(nuevoNodo)
                else:
                    self.insertar(arbol.getIzquierdo(),X)
            else:
                if X > arbol.getClave():
                    if arbol.getDerecho() is None:
                        arbol.setDerecho(nuevoNodo)
                    else:
                        self.insertar(arbol.getDerecho(),X)

    def suprimir(self,arbol,X): ## Se suprime en InOrden
        elemaux: int
        if arbol is None:
            print('No encontrado. No hay elemento a eliminar.')
            return -1
        else:
            print('Nodo correspondiente: {}'.format(arbol.getClave()))
            if X == arbol.getClave():
                print('LLego al nodo seleccionado.')
                if arbol.getGrado() == 0:
                    print('Es una hoja')
                    elemaux = arbol.getClave()
                    print('elemaux hoja: {}'.format(elemaux))
                    arbol = None
                    return elemaux
                else:
                    elemaux = arbol.getClave()
                    arbol = arbol.getDerecho()
                    return elemaux
            else:
                if X < arbol.getClave():
                    self.suprimir(arbol.getIzquierdo(),X)
                else:
                    if X > arbol.getClave():
                        self.suprimir(arbol.getDerecho(),X)

    def hijo(self,X,Z):
        resultado: bool
        if Z.getIzquierda().getClave() == X or Z.getDerecha().getClave() == X:
            resultado = True
        else:
            resultado = False
        return resultado

    def hoja(self,arbol,X):
        resultado: bool
        nodo = self.buscar(arbol,X)
        if nodo is not None:
            if nodo.getGrado() == 0: ## es hoja
                resultado = True
            else:
                resultado = False
        return resultado

    def camino(self,arbol,X,Z): ## intentar la busqueda antes
        if arbol.getGrado() == 0:
            print('El nodo es hoja, no tiene camino a Z.')
        else:
            if arbol.getGrado() == 1:
                print('')

    def preOrden(self,arbol):
        print('{}'.format(arbol.getClave()))
        if arbol.getIzquierdo() is not None:
            self.preOrden(arbol.getIzquierdo())
        if arbol.getDerecho() is not None:
            self.preOrden(arbol.getDerecho())

    def inOrden(self,arbol):
        if arbol.getIzquierdo() is not None:
            self.inOrden(arbol.getIzquierdo())
        print('{}'.format(arbol.getClave()))
        if arbol.getDerecho() is not None:
            self.inOrden(arbol.getDerecho())

    def postOrden(self,arbol):
        if arbol.getIzquierdo() is not None:
            self.postOrden(arbol.getIzquierdo())
        if arbol.getDerecho() is not None:
            self.postOrden(arbol.getDerecho())
        print('{}'.format(arbol.getClave()))

    def buscar(self,arbol,X):
        encontrado: bool
        if arbol is None:
            encontrado = False
            return encontrado
        else:
            if arbol.getClave() == X: ## encontrado
                print('Encontrado')
                encontrado = True
                return encontrado
            else:
                if X < arbol.getClave():
                    self.buscar(arbol.getIzquierdo(),X)
                else:
                    if X > arbol.getClave():
                        self.buscar(arbol.getDerecho(),X)



## Para crear la funcion grado, hacerlo en la clase nodo, ya que es atributo del nodo.