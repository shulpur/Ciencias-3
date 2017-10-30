import re
p = re.compile('ab*')
m = p.match('ab')
if m:
    print('Match found: ', m.group())
else:
    print('No match')


lista = ['1','1','1','+','-','mi_Casa22','=','%']
listaSalida = []
valor = re.compile('[0-9]')
operacion = re.compile('[\+\-\*\/\=]')
variable = re.compile('^[a-z][a-zA-Z0-9_]')

for i in lista:
    if valor.match(i):
        listaSalida.append(['valor', i])
    elif operacion.match(i):
        listaSalida.append(['operacion', i])
    elif variable.match(i):
        listaSalida.append(['variable', i])
    else:
        print('error tocken no valido: ', i)

print(listaSalida)

#mierda
