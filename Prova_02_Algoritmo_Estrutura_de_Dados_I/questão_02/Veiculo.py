class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        text = "Marca: " + self.marca
        text += "\nmodelo: " + self.modelo
        return text

    def imprimir(self):
        print(self)
