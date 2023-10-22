from No import No

# class Lista:
#     def __init__(self):
#         self.inicio = None
#         self.tamanho = 0

#     def addNoInicio(self, valor):
#         no = No(valor)
#         if self.inicio == None:
#             self.inicio = no
#             self.tamanho += 1
#         else:
#             no.proximo = self.inicio
#             self.inicio = no
#             self.tamanho += 1
#         # self.imprimir()

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def addNoInicio(self, valor):
        no = No(valor)
        if self.inicio == None:
            self.inicio = no
            self.fim = no
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.inicio = no
        self.tamanho += 1
        self.imprimir()

    def addNoFim(self, valor):
        no = No(valor)
        if self.inicio == None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.anterior = self.fim
            self.fim = no
        self.tamanho += 1
        self.imprimir()
        
    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.proximo
            print("Total: ", self.tamanho)

    def imprimirReverso(self):
        if self.inicio == None:
            print("Lista Vazia")
        else:
            aux = self.fim
            while aux:
                print(aux.dado)
                aux = aux.anterior
            print("Total: ", self.tamanho)

    # def removerDoInicio(self):
    #     if self.inicio == None:
    #         print("Lista Vazia")
    #     elif self.inicio.proximo == None:
    #         self.inicio = None
    #         self.tamanho = 0
    #     else:
    #         self.inicio = self.inicio.proximo
    #         self.tamanho -= 1
    #     self.imprimir()
    
    def removerDoInicio(self):
        if self.inicio == None:
            print("Lista Vazia")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.inicio.fim = None
            self.tamanho = 0
        else:
            self.inicio = self.inicio.proximo
            self.fim = None
            self.tamanho -= 1
        self.imprimir()

    def removerDoFim(self):
        if self.inicio == None:
            print("Lista Vazia")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.inicio.fim = None
            self.tamanho = 0
        else:
            self.inicio = self.inicio.anterior
            self.fim = None
            self.tamanho -= 1
        self.imprimir()
        