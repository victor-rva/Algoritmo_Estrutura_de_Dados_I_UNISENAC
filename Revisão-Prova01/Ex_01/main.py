"""
1. Construir código necessário em Python para implementar o seguinte projeto: Uma classe abstrata chamada de Computador que contém os atributos/propriedades: modelo, cor e preço. Esta classe possui um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().
 
2. O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Computador. A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. Esta classe reimplementa o método getInformacoes() herdado de computador.
 
3. A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. Esta classe reimplementa o método getInformacoes() herdado de computador.
 
4. Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.
"""

from Desktop import Desktop
from Notebook import Notebook

d1 = Desktop("Lenovo", "Preto", 2700, 1250)
n1 = Notebook("Apple", "Branco", 2500, 12)

d1.cadastrar()
n1.cadastrar()

print(d1.getInformacoes())
print()
print(n1.getInformacoes())


