lista = ['A','B','C','D','E']
diccionario = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

for i in lista:
    for k, v in diccionario.items():
        if k == i:
            print(v, i)
            lista[lista.index(i)] = v

print(lista)
print(diccionario)