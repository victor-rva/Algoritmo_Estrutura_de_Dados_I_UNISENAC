from No import Livro 

class Pilha:
    def __init__(self):
        self.topo = None
        self.base = None
        self.tamanho = 0

    def add(self, titulo, autor, qtdPaginas ):
        livro = Livro(titulo, autor, qtdPaginas)
        if self.topo == None:
            self.topo = livro
        else:
            topo = self.topo
            self.topo = livro
            self.topo.proximo = topo
        self.tamanho += 1
        self.imprimir()

    def remover(self):
        if self.topo == None:
            print("Pilha Vazia!")
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1
            self.imprimir()

    def imprimir(self):
        print("--------------------------")
        if self.topo == None:
            print("Pilha Vazia!")
        else:
            aux = self.topo
            texto = ""
            while aux:
                texto += str(aux.titulo) + ", " + str(aux.autor) + ", " + str(aux.paginas) + " - " + "\n"
                aux = aux.proximo
                print(texto)
                print("Total: ", self.tamanho)       