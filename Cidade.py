class Cidade:
    def __init__(self, nome = None, pop = None):
        self.nome = nome
        self.populacao = pop

    def __str__(self):
        texto = "Cidade: " + self.nome + "\n"
        texto += "População: " + str(self.populacao) + "\n"
        return texto

    def imprimir(self):
        print(self.__str__())

    def getPopulacao(self):
        return self.populacao