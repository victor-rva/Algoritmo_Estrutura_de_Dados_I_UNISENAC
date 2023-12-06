from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, qtdHelices):
        super().__init__(marca, modelo)
        self.__qtdHelices = qtdHelices
        self.proximo = None

    def __str__(self):
        text = "Marca: " + self.marca
        text += "\nModelo: " + self.modelo
        text += "\nQuantidade de helices: " + self.__qtdHelices
        return text

    def imprimir(self):
        print(self)