#from abc import ABCMeta
from abc import ABC, abstractmethod 

#class Veiculo(metaclass=ABCMeta):
class Computador(ABC):

    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformações(self):
        info = "Modelo: " + self.modelo + "\n"
        info += "Cor: " + self.cor + "\n"
        info += "Preço: R$" + str(self.preco) + "\n"
        return info

    @abstractmethod
    def cadastrar(self):
        pass

