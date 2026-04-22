import os
from tarefas import adicionar_tarefa, listar_tarefa, atualizar_status, carregar_dados, deletar_tarefa, editar_tarefa


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        carregar_dados()

        try:
            print("\n1 - Adicionar tarefa")
            print("2 - Listar tarefa")
            print("3 - Atualizar status")
            print("4 - Editar tarefa")
            print("5 - Deletar tarefa")
            print("6 - Sair")

            opcao = int(input("Digite a opção desejada: "))

            limpar()

            match opcao:
                case 1:
                    adicionar_tarefa()
                case 2:
                    listar_tarefa()
                case 3:
                    atualizar_status()
                case 4:
                    editar_tarefa()
                case 5:
                    deletar_tarefa()
                case 6:
                    print("Saindo...")
                    break
                case _:
                    print("❗Opção inválida")
        except ValueError:
            limpar()
            print("\n ⚠️ Digite uma opção válida.")


if __name__ == '__main__':
    main()
