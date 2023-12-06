from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas
        self.proximo = None

    def __str__(self):
        text = "Marca: " + self.marca
        text += "\nModelo: " + self.modelo
        text += "\nQuantidade de portas: " + self._portas
        return text

    def imprimir(self):
        print(self)