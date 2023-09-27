from Desktop import Desktop
from Notebook import Notebook

d1 = Desktop("Lenovo", "vermelho", 2400, 1250)
n1 = Notebook("Apple", "preto", 3000, 12)

d1.cadastrar()
n1.cadastrar()

print(d1.getInformações())
print(n1.getInformações())
