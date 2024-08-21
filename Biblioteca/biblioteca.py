from .livro import Livro
from .operacao import Operacao
from datetime import datetime

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

    def remover_livro(self, isbn: str):
        for l in self.livros:
            if l.isbn == isbn:
                self.livros.remove(l)
                print(f"Livro '{l.titulo}' removido com sucesso!")
                self.registrar_operacao(Operacao("Remoção", l, datetime.now()))
                return
        print("Livro não encontrado.")

    def buscar_livro(self, titulo: str = None, autor: str = None):
        resultados = []
        for l in self.livros:
            if (titulo and titulo.lower() in l.titulo.lower()) or (autor and autor.lower() in l.autor.lower()):
                resultados.append(l)
        return resultados

    def listar_livros(self):
        return sorted(self.livros, key=lambda x: x.ano_pub)
    
    class Operacao:
        def __init__(self, tipo: str, livro: Livro, data_dia: datetime):
            self.tipo = tipo
            self.livro = livro
            self.data = data_dia


    def registrar_operacao(self, operacao: Operacao):
        self.operacoes.append(operacao)
        print(f"Operação de {operacao.tipo} registrada em {operacao.data}.")


