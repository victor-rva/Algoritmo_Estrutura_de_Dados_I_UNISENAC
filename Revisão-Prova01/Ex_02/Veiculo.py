from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    def __init__(self, modelo, cor, preco, ano):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.ano = ano
        
    def getInfo(self):
        info = "Modelo: " + self.modelo + "\n"
        info += "Cor: " + self.cor + "\n"
        info += "Preco: R$" + str(self.preco) + "\n"
        info += "Ano: " + str(self.ano) + "\n"
        return info
        
    @abstractclassmethod    
    def ligar(self):
        pass