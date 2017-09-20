from arbol import *

diccionario = {}

#expresion = ['7','10','2','/','-','3','+','A','=']
# 3 2 + 5 8 - + A =
# 5 6 + B =
# A B - C =
bucle = 's'
while(bucle != 'n'):
    expresion = input('ingrese una expresion en postorden: ')
    expresionSinEspacios = expresion.split(' ')
    expresionSinVariableNiIgual = expresionSinEspacios[:-2]      #El primer elemento es la variable, el segundo el = , el tercero es la expresion
    expresionSinVariableNiIgual.reverse()
    for i in expresionSinVariableNiIgual:                        #Reemplazo el valor de una variable por lo que contiene en el diccionario
        for k,v in diccionario.items():
            if k == i:
                expresionSinVariableNiIgual[expresionSinVariableNiIgual.index(i)] = v

    arbol = Arbol()
    for i in expresionSinVariableNiIgual:
            arbol.insertar(i)

    diccionario[expresionSinEspacios[-2]] = arbol.evaluar()
    print(diccionario)
    bucle = input('¿Desea continuar (s/n)?')
# print(expresionSinVariableNiIgual)




