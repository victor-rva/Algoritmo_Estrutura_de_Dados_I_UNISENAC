"""Construa um algoritmo que possua uma tupla com os números escritos
por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
condicionais (if e switch)"""

numeros_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")

def algarismo():
    numero = int(input("Digite um número de 0 a 9: "))
    return print(numeros_extenso[numero])

algarismo()

# try:
#     numero_digitado = int(input('Digite um número de 0 a 9: '))
    
#     # Verifique se o número digitado está dentro do intervalo válido
#     validade = 0 <= numero_digitado <= 9
    
#     # Use a lógica matemática para calcular o índice e acessar o elemento na tupla
#     print(f'O número por extenso é: {numeros_extenso[validade * numero_digitado]}')
# except ValueError:
#     print('Por favor, digite um número válido.')
    
    # """
    #  Os valores booleanos (True/False) podem ser tratados numericamente como 1 e 0. Portanto, usando essa expressão, você obtém diretamente o número digitado 
    #  como índice quando ele está dentro do intervalo válido (de 0 a 9) e obtém 0 quando o número está fora desse intervalo.
    # """