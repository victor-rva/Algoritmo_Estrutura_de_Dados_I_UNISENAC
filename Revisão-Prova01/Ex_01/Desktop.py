from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potencialDaFonte):
        super().__init__(modelo, cor, preco)
        self._fonte = potencialDaFonte
        
    def getInformacoes(self):
        info_desk = super().getInformacoes()
        info_desk += "Potência da fonte: " + str(self._fonte) + "W"
        return info_desk
        
    def cadastrar(self):
        print("Cadastre o usuário.")
        