from .livro import Livro
from .operacao import Operacao

#Contém a classe Biblioteca e sua lógica.

class Biblioteca:
    def __init__(self, livros, operacoes):
        self.livros = []
        self.operacoes = []
    
    def adicionar_livro(self, livro: Livro):
        for l in self.livros:
            if l.isbn == livro.isbn:
                print("Este ISBN já existe na biblioteca.")
                return
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")
        self.registrar_operacao(Operacao("Adição", livro, datetime.now()))

    def remover_livro(self):
        pass

    def buscar_livro(self, titulo, autor):
        pass

    def listar_livros(self):
        pass

    def registrar_operacao(self, operacao: Operacao):
        pass


