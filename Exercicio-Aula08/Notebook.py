from Computador import Computador

class Notebook(Computador):

    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformações(self):
        info_note = str(super().getInformações())
        info_note += "Tempo de bateria: " + str(self.__tempoDeBateria) + "H" + "\n"
        return info_note

    def cadastrar(self):
        print("Cadastre o usuário")