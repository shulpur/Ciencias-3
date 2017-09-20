from pila import Pila

class Nodo:
    def __init__(self, valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

def insertar(arbol, valor):
    if arbol == None:
        arbol = Nodo(valor)
    elif valor < arbol.valor:
        arbol = Nodo(arbol.valor,insertar(arbol.izq,valor))
    else:
        arbol = Nodo(arbol.valor,arbol.izq,insertar(arbol.der,valor))
    return arbol

def inorden(arbol):
    if arbol:
        inorden(arbol.izq)
        print(arbol.valor)
        inorden(arbol.der)

def postorden(arbol):
    if arbol:
        postorden(arbol.izq)
        postorden(arbol.der)
        print(arbol.valor)


def preorden(arbol):
    if arbol:
        print(arbol.valor)
        preorden(arbol.izq)
        preorden(arbol.der)

a = None
a = insertar(a,5)
a = insertar(a, 2)
a = insertar(a, 1)
a = insertar(a, 12)
a = insertar(a, 10)
a = insertar(a, 24)
a = insertar(a, 20)
a = insertar(a, 23)

print(a.der.izq.valor,'\n')
inorden(a)
print('\n')
preorden(a)
print('\n')
postorden(a)
print('\n')


b = None
pila = Pila()
b = insertarConSigno(b,'+',pila)
b = insertarConSigno(b,3, pila)
b = insertarConSigno(b,'-', pila)
b = insertarConSigno(b,'/', pila)
b = insertarConSigno(b,2, pila)
b = insertarConSigno(b,10, pila)
b = insertarConSigno(b,7, pila)

inorden(b)
print('\n')
preorden(b)
print('\n')
postorden(b)
print('\n')

c = Pila()
c.meter(5)
c.meter(6)
c.meter(8)

print(c.sacar())
print(c.sacar())
print(c.sacar())




