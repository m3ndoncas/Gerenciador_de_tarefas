import datetime
import json

tarefas = []


def salvar_dados():
    with open('tarefas.json', 'w') as tarefas_file:
        json.dump(tarefas, tarefas_file, indent=4)


def carregar_dados():
    global tarefas #torna tarefas global

    try:
        with open('tarefas.json', 'r') as tarefas_file:
            tarefas = json.load(tarefas_file)
            return tarefas
    except (FileNotFoundError, json.JSONDecodeError): #trata erro de json vazio
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
            print("Descrição: ",tarefa["Descricao"])
            print("Data criação: ", tarefa["Data"])
            print("Status: 🕒 - Em aberto.")
        else:
            print("\nTarefa: ", tarefa["Tarefa"])
            print("Descrição: ", tarefa["Descricao"])
            print("Data criação: ", tarefa["Data"])
            print("✅- Concluido.")


def atualizar_status():
    buscar_tarefa = input('Qual tarefa deseja tarefa atualizar(digite o nome)?: ').capitalize().strip()

    for tarefa in tarefas:
        if buscar_tarefa == tarefa["Tarefa"]:
            tarefa["Concluida"] = True
            tarefa["Data"] = date()
            print("Data de finalização: ", tarefa["Data"])
            salvar_dados()




