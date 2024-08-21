from Biblioteca.biblioteca import Biblioteca
from Biblioteca.livro import Livro
from datetime import datetime

# Inicializa a biblioteca
bib = Biblioteca()

def menu():
    print("Bem-vindo ao Sistema de Gerenciamento de Biblioteca!")
    print("Por favor, selecione uma opção:")
    print("1 - Adicionar Livro")
    print("2 - Remover Livro")
    print("3 - Buscar Livro")
    print("4 - Listar Livros")
    print("5 - Registrar Operação")
    print("6 - Sair")

def opcao1():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_pub = int(input("Digite o ano de publicação: "))
    isbn = input("Digite o ISBN: ")
    novo_livro = Livro(titulo, autor, ano_pub, isbn)
    bib.adicionar_livro(novo_livro)

def opcao2():
    isbn = input("Digite o ISBN do livro a ser removido: ")
    bib.remover_livro(isbn)

def opcao3():
    titulo = input("Digite o título do livro (ou deixe em branco): ")
    autor = input("Digite o autor do livro (ou deixe em branco): ")
    resultados = bib.buscar_livro(titulo, autor)
    if resultados:
        for livro in resultados:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_pub}, ISBN: {livro.isbn}")
    else:
        print("Nenhum livro encontrado.")

def opcao4():
    livros = bib.listar_livros()
    for livro in livros:
        print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_pub}, ISBN: {livro.isbn}")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            opcao1()
        elif escolha == '2':
            opcao2()
        elif escolha == '3':
            opcao3()
        elif escolha == '4':
            opcao4()
        elif escolha == '5':
            print("Operação não implementada.")
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

if __name__ == "__main__":
    main()
