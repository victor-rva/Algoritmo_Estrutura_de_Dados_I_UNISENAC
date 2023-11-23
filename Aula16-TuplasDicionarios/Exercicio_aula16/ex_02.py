"""
Construa um algoritmo que peça ao usuário para informar o nome, a
nota01 e a nota02 de um aluno. Guarde estas informações em um
dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
e adicione ao dicionário. Ao final, imprima todos os dados do
dicionário
"""

notas = {
    "nome": "",
    "nota01": "",
    "nota02": "",
    "notaFinal" : ""
}
nome = input("Digite o nome do aluno: ")
nota01 = int(input("Digite a nota da avaliação 01 do aluno: "))
nota02 = int(input("Digite a nota da avaliação 02 do aluno: "))
nota_final = (nota01 + nota02) /2
print("Nota final: ", nota_final)
print("------------------------")

notas["nome"] = nome
notas["nota01"] = nota01
notas["nota02"] = nota02
notas["notaFinal"] = nota_final

print(notas)
