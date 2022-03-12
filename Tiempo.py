from Nodo import nodoTiempo

class listaTiempo:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacioT(self):
        return self.primero == None

    def AgregarT(self, item):
        if self.vacio():
            self.primero = self.ultimo = nodoTiempo(item)
            return
        temporal = self.primero
        while temporal:
            if temporal.siguiente == None:
                temporal.siguiente = self.ultimo = nodoTiempo(item)
                self.ultimo.anterior = temporal
                return
            temporal = temporal.siguiente
    
    def RetirarT(self):
        temporal = self.primero
        if self.ultimo == temporal:
            print('Ultima orden pendiente.')
            self.primero = self.ultimo = None
            return temporal
        else: 
            self.primero = temporal.siguiente
            self.primero.anterior = None
            return temporal
        
    def enviarColaT(self):
        listaCola = []
        temporal = self.primero
        while temporal:
            listaCola.append(temporal)
            temporal = temporal.siguiente
        return listaCola