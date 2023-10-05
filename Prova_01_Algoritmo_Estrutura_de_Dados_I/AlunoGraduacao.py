from Pessoa import Pessoa

class AlunoGraduacao(Pessoa):
    def __init__(self, id, nome, telefone, matricula, presenca):
        super().__init__(id, nome, telefone)
        self.__matricula = matricula
        self.presenca = presenca

    def matricular(self):
        print("Aluno matriculado com sucesso!")

    def marcarPresenca(self):
        presenca = input("Aluno veio na aula hoje? S/N ")
        if presenca == "S".upper():
            Npresenca = 1
            self.presenca += Npresenca
            return self.presenca

    def getInfoG(self):
        infoG = super().getInfo()
        infoG += "Matrícula: " + str(self.__matricula) + "\n"
        infoG += "Presença: " + str(self.presenca) + "\n"
        return print(infoG)


    def setMatricula(self):
        if self.__matricula == "":
            acrescentar = int(input("Acrescente o número de matrícula do aluno: "))
            self.__matricula = acrescentar
            print("N° de matrícula incluído!")
        else:
            print("Matrícula já incluída.")
        
            

    