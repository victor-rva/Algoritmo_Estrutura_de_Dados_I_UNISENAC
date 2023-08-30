from Pessoa import Pessoa
class Juridico:
    def __init__(self, nomeJ, telefoneJ, cnpj):
        super().__init__(nomeJ, telefoneJ)
        self.cnpj = cnpj 