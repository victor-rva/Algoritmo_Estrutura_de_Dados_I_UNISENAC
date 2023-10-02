"""
1. Construir código necessário em Python para implementar o seguinte projeto: Uma classe abstrata chamada de Veiculo que contém os atributos/propriedades: modelo, cor, preço e ano. Esta classe possui um método getInfo() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato ligar().
 
2. O projeto também deve possuir as classes Carro e Moto que herdam da classe Veiculo. A classe Carro possui o atributo/propriedade fracamente privado portas. Esta classe reimplementa o método getInfo() herdado de Veiculo.
 
3. A classe Moto possui o atributo/propriedade fortemente privado cilindradas. Esta classe reimplementa o método getInfo() herdado de Veiculo.
 
4. Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.
"""

from Carro import Carro
from Moto import Moto

c1 = Carro("Porsche", "Preto", 200000, 2019)
m1 = Moto("Honda", "Vermelho", 30000, 2022, 600)

c1.getInfo()
print()
m1.getInfo()
print()
c1.ligar()
m1.ligar()
