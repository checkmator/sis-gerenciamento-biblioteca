#Contém a classe Livro.

class Livro:
    def __init__(self, titulo: str, autor: str, ano_pub: int, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.ano_pub = ano_pub
        self.isbn = isbn
