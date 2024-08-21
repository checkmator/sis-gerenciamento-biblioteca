#Testes para a classe Biblioteca.

# test_biblioteca.py

import unittest
from biblioteca import Biblioteca
from livro import Livro

class TestBiblioteca(unittest.TestCase):
    def test_adicionar_livro(self):
        bib = Biblioteca()
        livro = Livro("Título", "Autor", 2020, "1234567890")
        bib.adicionar_livro(livro)
        self.assertEqual(len(bib.livros), 1)

    def test_remover_livro(self):
        bib = Biblioteca()
        livro = Livro("Título", "Autor", 2020, "1234567890")
        bib.adicionar_livro(livro)
        bib.remover_livro("1234567890")
        self.assertEqual(len(bib.livros), 0)

if __name__ == '__main__':
    unittest.main()
