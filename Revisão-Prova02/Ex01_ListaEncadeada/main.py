"""
Fazer um lista encadeada que armazene os valores em ordem crescente
"""

from Lista import Lista

lista = Lista()

lista.imprimir()
lista.add( 14 )
lista.add( 10 )
lista.add(  8 )
lista.add( 15 )
lista.add( 12 )

lista.remover( 12 )
lista.remover( 7 )
lista.remover( 15 )
lista.remover( 10 )
lista.remover( 14 )