from pila import Pila

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self):
        self.cab = None
        self.pila = Pila()

    def insertar(self, valor):
        aux = Nodo(valor)
        if not self.cab:
            self.cab = aux
            self.pila.meter(aux)
        else:
            self.insertar2(self.pila.sacar(), valor)

    def insertar2(self, nodo, valor):
        aux = Nodo(valor)
        if not nodo.der:
            nodo.der = aux
            self.pila.meter(nodo)
            if aux.valor == '+' or aux.valor == '-' or aux.valor == '*' or aux.valor == '/':
                self.pila.meter(aux)
        elif not nodo.izq:
            nodo.izq = aux
            if aux.valor == '+' or aux.valor == '-' or aux.valor == '*' or aux.valor == '/':
                self.pila.meter(aux)


    def evaluar(self):
        return self.evaluar2(self.cab)

    def evaluar2(self, nodo):
        if nodo:
            if nodo.valor == '+':
                return self.evaluar2(nodo.izq) + self.evaluar2(nodo.der)
            if nodo.valor == '-':
                return self.evaluar2(nodo.izq) - self.evaluar2(nodo.der)
            if nodo.valor == '*':
                return self.evaluar2(nodo.izq) * self.evaluar2(nodo.der)
            if nodo.valor == '/':
                return self.evaluar2(nodo.izq) / self.evaluar2(nodo.der)
            return int(nodo.valor)

    def inorden(self):
        print('inorden')
        self.inorden2(self.cab)

    def inorden2(self, nodo):
        if nodo:
            self.inorden2(nodo.izq)
            print(nodo.valor, end=' ')
            self.inorden2(nodo.der)

    def postorden(self):
        print('postorden')
        self.postorden2(self.cab)

    def postorden2(self, nodo):
        if nodo:
            self.postorden2(nodo.izq)
            self.postorden2(nodo.der)
            print(nodo.valor, end=' ')

    def preorden(self):
        print('preorden')
        self.preorden2(self.cab)

    def preorden2(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.preorden2(nodo.izq)
            self.preorden2(nodo.der)

if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertar('+')
    arbol.insertar(3)
    arbol.insertar('-')
    arbol.insertar('/')
    arbol.insertar('2')
    arbol.insertar('10')
    arbol.insertar('7')

    arbol.inorden()
    print('\n')
    arbol.preorden()
    print('\n')
    arbol.postorden()
    print('\n')
    print(arbol.evaluar())
    print('\n')

    arbol = Arbol()
    arbol.insertar('+')
    arbol.insertar('-')
    arbol.insertar('8')
    arbol.insertar('5')
    arbol.insertar('+')
    arbol.insertar('2')
    arbol.insertar('3')

    arbol.inorden()
    print('\n')
    arbol.preorden()
    print('\n')
    arbol.postorden()
    print('\n')
    print(arbol.evaluar())
    print('\n')



