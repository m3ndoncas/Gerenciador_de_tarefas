import datetime
import json

tarefas = []


def salvar_dados():
    with open('tarefas.json', 'w') as tarefas_file:
        json.dump(tarefas, tarefas_file, indent=4)


def carregar_dados():
    global tarefas  # torna tarefas global

    try:
        with open('tarefas.json', 'r') as tarefas_file:
            tarefas = json.load(tarefas_file)
            return tarefas
    except (FileNotFoundError, json.JSONDecodeError):  # trata erro de json vazio
        tarefas = []


def date():
    data = datetime.datetime.now()
    data_formatada = data.strftime('%d/%m/%Y %H:%M')
    return data_formatada


def adicionar_tarefa():
    nome_tarefa = input('Nome do tarefa: ').capitalize().strip()
    descricao_tarefa = input('Descricao da tarefa: ')
    data_criacao = date()

    tarefa = {
        "Tarefa": nome_tarefa,
        "Descricao": descricao_tarefa,
        "Data": data_criacao,
        "Concluida": False
    }

    tarefas.append(tarefa)
    salvar_dados()


def listar_tarefa():
    for i, tarefa in enumerate(tarefas):
        if tarefa["Concluida"] == False:
            print(f"\nTarefa {i + 1}:")
            print("Nome: ", tarefa["Tarefa"])
            print("Descrição: ", tarefa["Descricao"])
            print("Data: ", tarefa["Data"])
            print("Status: 🕒 - Em aberto.")
        else:
            print(f"\nTarefa {i + 1}:")
            print("Nome: ", tarefa["Tarefa"])
            print("Descrição: ", tarefa["Descricao"])
            print("Data: ", tarefa["Data"])
            print("✅- Concluido.")


def atualizar_status():
    print("\nIndex Tarefas:")

    for i, tarefa in enumerate(tarefas):
        print(f"\nTarefa {i} :", tarefa["Tarefa"])
    try:
        index = int(input('\nDigite o index da tarefa que deseja atualizar status: '))

        if tarefas[index]["Concluida"] == False:
            tarefa["Concluida"] = True
            tarefa["Data"] = date()
            print("Data de atualização: ", tarefa["Data"])
            salvar_dados()
        else:
            tarefa["Concluida"] = False
            print("Data de atualização: ", tarefa["Data"])
            salvar_dados()

    except IndexError:
        print("Tarefa inexistente!")



def editar_tarefa():
    print("\nIndex Tarefas:")

    for i, tarefa in enumerate(tarefas):
        print(f"\nTarefa {i} :", tarefa["Tarefa"])

    while True:
        try:
            index = int(input('\nDigite o index da tarefa que deseja editar: '))
            print(f"\nOque deseja editar:")
            print("1- Nome")
            print("2- Descricao")

            opcao = int(input("Digite a opção desejada: "))
            match opcao:
                case 1:
                    novo_nome = input("Digite o novo nome da tarefa: ")
                    tarefas[index]["Tarefa"] = novo_nome
                    salvar_dados()
                    print("Salvo com sucesso!")
                    break
                case 2:
                    nova_descricao = input("Digite a nova descrição da tarefa: ")
                    tarefas[index]["Descricao"] = nova_descricao
                    salvar_dados()
                    print("Salvo com sucesso!")
                    break
                case _:
                    print("Opção inválida!")
        except (IndexError, ValueError):
            print("Tarefa inexistente ou valor não esperado!")



def deletar_tarefa():
    print("\nIndex Tarefas:")

    for i, tarefa in enumerate(tarefas):
        print(f"\nTarefa {i} :", tarefa["Tarefa"])

    try:
        index = int(input('\nDigite o index da tarefa que deseja deletar: '))
        tarefas.pop(index)
        print("Tarefa removida com sucesso!")
        salvar_dados()
    except IndexError:
        print("Tarefa inexistente!")
