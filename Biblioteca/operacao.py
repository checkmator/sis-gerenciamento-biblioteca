from .livro import Livro

#Contém a classe Operacao.

class Operacao:
    def __init__(self, tipo, livro: Livro, data_dia):
        self.tipo = tipo
        self.data = data_dia