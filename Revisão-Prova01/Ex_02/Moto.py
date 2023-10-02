from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, cor, preco, ano, cilindradas):
        super().__init__(modelo, cor, preco, ano)
        self.__cili = cilindradas
      
    def getInfo(self):
        info_moto = super().getInfo()
        info_moto += "Cilindradas: " + str(self.__cili)
        return print(info_moto)
        
    def ligar(self):
        print("Moto ligada.")