class NodoCola:
	def __init__(self, dato):
		self.dato = dato
		self.sig = None

class Cola:
	def __init__(self):
		self.cab = None

	def meter(self, dato):
		nodo = NodoCola(dato)
		if self.cab == None:
			self.cab = nodo
		else:
			aux = self.cab
			while aux.sig != None:
				aux = aux.sig
			aux.sig = nodo

	def sacar(self):
		aux = self.cab
		self.cab = self.cab.sig
		return aux.dato

	def imprimir(self):
		aux = self.cab
		while aux != None:
			print(aux.dato)
			aux = aux.sig

    def vacia(self):
        return self.cab == None


if __name__ == "__main__":
	cola = Cola()
	cola.meter(['Bajaj', 'Jose Hernandez', 'pah-174'])
	cola.meter(['Yamaha', 'Maria Perez', 'owp-163'])
	cola.meter(['Honda', 'Ana Rodrigues', 'iep-945'])
	cola.meter(['Akt', 'Emilio Toro', 'ahd-278'])
	cola.meter(['Suzuki', 'Manuel Castellanos', 'yvt-782'])
	print(cola.sacar())
	print(cola.sacar())
	print(cola.sacar())
	print(cola.sacar())
	print(cola.sacar())

	#pila.imprimir()