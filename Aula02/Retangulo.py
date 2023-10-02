class Retangulo:
    def __init__(self, altura = float, largura = float):
        self.altura = altura
        self.largura = largura
        
    def calcular(self):
        area_triangulo = self.altura * self.largura
        text = "A area do trinângulo é: " + str(area_triangulo) + "m quadrados."
        return text
    
    def imprimir(self):
        texto = "Altura: " + str(self.altura) + "\n"
        texto += "Largura: " + str(self.largura)
        return texto