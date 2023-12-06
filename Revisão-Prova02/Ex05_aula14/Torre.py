class Torre:
    
    def __init__(self, nome, end):
        self.nome = nome
        self.endereco = end
        
    def cadastrar(self):
        print("Torre cadastradas!")
        
    def __str__(self) -> str:
        text = "Nome: " + self.nome
        text += "\nEndereço: " + self.endereco
        return text
    
    def imprimir(self):
        print(self)