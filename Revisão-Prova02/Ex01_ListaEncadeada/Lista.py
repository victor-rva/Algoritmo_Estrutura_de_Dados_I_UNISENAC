from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        
    def add(self,valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.proximo = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux != None:
                    if nodo.dado < aux.dado:
                        nodo.proximo = ant.proximo
                        ant.proximo = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None and nodo.dado >= ant.dado:
                    ant.proximo = nodo
                    
        self.tamanho += 1
        self.imprimir()
        
    def imprimir(self):
        print("------------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.proximo
            print("Tamanho: ", str(self.tamanho))
            
            