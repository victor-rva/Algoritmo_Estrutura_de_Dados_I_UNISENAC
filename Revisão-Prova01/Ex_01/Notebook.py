from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDaBateria):
        super().__init__(modelo, cor, preco)
        self.__bateria = tempoDaBateria
        
    def getInformacoes(self):
        info_note = super().getInformacoes()
        info_note += "Tempo da bateria: " + str(self.__bateria) + "H"
        return info_note
        
    def cadastrar(self):
        print("Cadastre o usuário.")
        
    