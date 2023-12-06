valores = [40,300,2000]

def aumentarValor(x):
    return x * 1.1

novosValores = list(map(aumentarValor, valores))
print(novosValores)

#Sem a função map o resultado mostraria o endereçamento de memória da função aumentaValores e a lista valores, com a função map a função e a lista ficam no mesmo endereçamento de memória, fazendo com que o list mostre o resultado com os números inteiros.
""""Juros de uma compra: """
print("Com os juros as suas compras que possuiam os seguintes valores de R$: ", valores, ", agora estão com o valor de R$: ", novosValores)