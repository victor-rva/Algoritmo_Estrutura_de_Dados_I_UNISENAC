from Lista import Lista

lista = Lista()

lista.imprimir()
lista.addNoInicio( 10 )
lista.addNoInicio(  8 )
lista.addNoInicio(  12 )
lista.addNoInicio(  9 )
lista.addNoInicio(  3 )
lista.addNoInicio(  2 )
lista.addNoFim(  1 )
lista.addNoFim(  14 )
lista.addNoFim(  19 )
lista.addNoFim(  20 )
lista.addNoFim(  21 )
lista.addNoFim(  13 )
lista.removerDoInicio()
lista.removerDoFim()
lista.removerDoInicio()
lista.removerDoFim()
lista.removerDoFim()
print("-----------------------")
lista.imprimir()
lista.imprimirReverso()