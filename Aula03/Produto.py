from Categoria import *
class Produto:
    def __init__(self, nome = None, preco = None, cat = Categoria()):
        self.nome = nome
        self.preco = preco
        self.categoria = cat 

    def __str__(self):
        texto = "Nome: " + self.nome + "\n"
        texto += "Preço: " + str(self.preco) + "\n"
        texto += "Categoria: " + str(self.categoria) + "\n"
        return texto

    def imprimir(self):
        print(self.__str__())
