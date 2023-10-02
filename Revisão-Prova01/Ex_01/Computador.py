from abc import ABC, abstractclassmethod
class Computador(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        
    def getInformacoes(self):
        texto = "Modelo: " + self.modelo + "\n"
        texto += "Cor: " + self.cor + "\n"
        texto += "Preço: " + str(self.preco)
        return texto
    
    @abstractclassmethod
    def cadastrar(self):
        pass