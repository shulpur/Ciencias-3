class NodoPila:
	def __init__(self, dato):
		self.dato = dato
		self.sig = None 
		
class Pila:
	def __init__(self):
		self.cab = None
		
	def meter(self, dato):
		nodo = NodoPila(dato)
		if self.cab == None:
			self.cab = nodo
		else:
			aux = self.cab
			while aux.sig != None:
				aux = aux.sig
			aux.sig = nodo
			
	def sacar(self):
		aux = self.cab
		auxAnterior = aux
		while aux.sig != None:
			auxAnterior = aux
			aux = aux.sig
		auxAnterior.sig = None
		return aux.dato
			
	def imprimir(self):
		aux = self.cab
		while aux != None:
			print(aux.dato)
			aux = aux.sig
			
if __name__ == "__main__":
	pila = Pila()
	pila.meter(['El señor de los añillos' ,'Peter Jackson' ,'2001'])
	pila.meter(['Sr. y Sra. Smith' ,'Doug Liman' ,'2005'])
	pila.meter(['El perfecto asesino' ,'Luc Besson' ,'1994'])
	pila.meter(['La lista de Schindler' ,'Steven Spielberg' ,'1993'])
	pila.meter(['El padrino' ,'Francis Ford Coppola' ,'1972'])
	print(pila.sacar())
	print(pila.sacar())
	print(pila.sacar())
	print(pila.sacar())
	print(pila.sacar())