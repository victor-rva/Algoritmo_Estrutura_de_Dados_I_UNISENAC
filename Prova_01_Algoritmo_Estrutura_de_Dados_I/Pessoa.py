from abc import ABC, abstractclassmethod
class Pessoa(ABC):
    def __init__(self,id, nome, telefone):
        self.id = id 
        self.nome = nome
        self._telefone = telefone

    def getInfo(self):
        info = "ID: " + str(self.id) + "\n"
        info += "Nome: " + self.nome + "\n"
        info += "Telefone: " + str(self._telefone) + "\n"
        return info

    @abstractclassmethod
    def marcarPresenca():
        pass
    
    def matricular():
        pass