class Livro:
    def __init__(self, titulo, autor, qtdPaginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = qtdPaginas
        self.proximo = None