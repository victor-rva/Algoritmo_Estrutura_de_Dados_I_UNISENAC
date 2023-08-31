class Aluno:
    def __init__(self, cod, name, matri):
        self.codigo = cod
        self.nome = name
        self.matricula = matri

    def __str__(self):
        text = "ID: " + self.codigo + "\n"
        text += "Nome: " + self.nome + "\n"
        text += "N° Matrícula: " + self.matricula + "\n"
        return text

    def imprimir(self):
        print(self)