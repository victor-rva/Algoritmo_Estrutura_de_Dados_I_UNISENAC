from Categoria import Categoria

class Veiculo:
    def __init__(self, marca, ano = 2014, cat = Categoria("Esportivo")):
        self.id = None
        self.marca = marca
        self.ano = ano
        self.cat = cat
        
    def __str__(self):
        text = "Veiculo: " + self.marca + "\n"
        text += "Ano: " + str(self.ano) + "\n"
        text += "Categoria: " + self.cat.nome + "\n"
        #não pode ser str(self.cat) porque o Categoria não possui o metodo str nele, então iria retornar o endereço dele
        return text
    
    def imprimir(self):
        print(self) #só funciona porque eu declarei o metodo str
        #print(self.__str__())