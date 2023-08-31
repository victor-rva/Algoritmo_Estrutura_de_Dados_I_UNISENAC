from Aluno import Aluno
class AluEnsinoMedio(Aluno):
    def __init__(self, cod, name, matri, ano):
        super().__init__(self, cod, name, matri)
        self.ano = ano
        
    def __str__(self):
        text = "ID: " + self.codigo + "\n"
        text += "Nome: " + self.nome + "\n"
        text += "N° Matrícula: " + self.matricula + "\n"
        text += "Ano Escolar: " + self.ano + "\n"
        return text

    def imprimir(self):
        print(self)