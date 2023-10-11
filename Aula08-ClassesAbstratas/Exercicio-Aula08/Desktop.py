from Computador import Computador

class Desktop(Computador):

    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformações(self):
        info_desk = str(super().getInformações())
        info_desk += "Potência: " + str(self._potenciaDaFonte) + "W" + "\n"
        return info_desk

    def cadastrar(self):
        print("Cadastre o usuário")