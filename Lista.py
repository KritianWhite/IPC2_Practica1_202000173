from Nodo import nodoSimple

class listaSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacio(self):
        return self.primero == None

    def Agregar(self, item):
        if self.vacio():
            self.primero = self.ultimo = nodoSimple(item)
            return
        temporal = self.primero
        while temporal:
            if temporal.siguiente == None:
                temporal.siguiente = self.ultimo = nodoSimple(item)
                self.ultimo.anterior = temporal
                return
            temporal = temporal.siguiente
    
    def Retirar(self):
        temporal = self.primero
        if self.ultimo == temporal:
            print('Ultima orden pendiente.')
            self.primero = self.ultimo = None
            return temporal
        else: 
            self.primero = temporal.siguiente
            self.primero.anterior = None
            return temporal
        
    def enviarCola(self):
        listaCola = []
        temporal = self.primero
        while temporal:
            listaCola.append(temporal)
            temporal = temporal.siguiente
        return listaCola
    
