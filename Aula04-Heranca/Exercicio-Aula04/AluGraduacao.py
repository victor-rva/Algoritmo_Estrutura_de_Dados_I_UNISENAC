from Aluno import Aluno
class AluGraduacao(Aluno):
    def __init__(self, cod, name, matri, sem):
        super().__init__(self, cod, name, matri)
        self.semestre = sem
        
    def __str__(self):
        text = "ID: " + self.codigo + "\n"
        text += "Nome: " + self.nome + "\n"
        text += "N° Matrícula: " + self.matricula + "\n"
        text += "Semestre: " + self.semestre + "\n"
        return text

    def imprimir(self):
        print(self)