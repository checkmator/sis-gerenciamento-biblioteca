#O ponto de entrada do seu programa. Aqui você pode instanciar a classe Biblioteca e implementar a lógica principal do seu programa.

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
    print("Você escolheu a Opção 1")

def opcao2():
    print("Você escolheu a Opção 2")

def opcao3():
    print("Você escolheu a Opção 3")

def opcao4():
    print("Você escolheu a Opção 4")

def opcao5():
    print("Você escolheu a Opção 4")

def opcao6():
    print("Você escolheu a Opção 5")

def opcao7():
    print("Você escolheu a Opção 6")

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
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

if __name__ == "__main__":
    main()
