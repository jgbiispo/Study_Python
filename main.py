import Stack

def menu():
    print("Estruturas de dados — pilha, fila, árvore, grafo")
    print("1 - Stack")

    option = input("> ")

    match option:
        case "1":
            Stack.run_tests()
        case "0":
            print("Saindo...")


if __name__ == "__main__":
    menu()
