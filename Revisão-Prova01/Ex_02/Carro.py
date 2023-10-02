from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, cor, preco, ano, portas = None):
        super().__init__(modelo, cor, preco, ano)

        while True:
            portas = int(input("Digite o número de portas: "))
            if (portas < 2) or (portas > 4) or (portas == 3): 
                print("Número de portas incoerente.")
            else:
                break
                
        self._portas = portas
      
    def getInfo(self):
        info_carro = super().getInfo()
        info_carro += "N° de portas: " + str(self._portas)
        return print(info_carro)
        
    def ligar(self):
        print("Carro ligado.")