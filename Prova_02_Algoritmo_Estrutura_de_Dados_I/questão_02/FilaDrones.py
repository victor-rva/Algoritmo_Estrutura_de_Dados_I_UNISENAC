from Drone import Drone

class FilaDrones:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, drone):
        if self.inicio == None:
            self.inicio = drone
        else:
            self.fim.proximo = drone
        self.fim = drone
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print( "Fila Vazia ")
        else:
            aux = self.inicio
            texto = ""
            while( aux ):
                texto += str(aux) + " - "
                aux = aux.proximo
            print( texto )
            print( "Total: " , self.tamanho )

    def remover(self):
        if self.inicio == None:
            print("Fila Vazia!")
        else:
            if self.inicio.proximo == None:
                self.fim = None
            drone = self.inicio
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            self.imprimir()
            drone.proximo = None
            return drone