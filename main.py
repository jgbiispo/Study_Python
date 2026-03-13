import modules.Queue as Queue
import modules.Stack as Stack


def menu():
    print("Estruturas de dados — pilha, fila, árvore, grafo")
    print("1 - Stack")
    print("2 - Queue")
    print("0 - Sair")

    option = input("> ")

    match option:
        case "1":
            Stack.run_tests()
        case "2":
            Queue.run_testes()
        case "0":
            print("Saindo...")


if __name__ == "__main__":
    menu()
