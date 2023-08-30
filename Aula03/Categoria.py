class Categoria:
    def __init__(self, nome = None, id = None):
        self.nome = nome
        self.id = id

    def __str__(self):
        texto = "Nome: " + self.nome + "\n"
        texto += "ID: " + int(self.id)
        return texto

    def imprimir(self):
        print(self.__str__())
