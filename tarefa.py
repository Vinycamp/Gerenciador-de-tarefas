import json
import os

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "dados", "tarefas.json")

def carregar_tarefas():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                return []
            dados = json.loads(conteudo)
            return dados if isinstance(dados, list) else []
    except (json.JSONDecodeError, OSError):
        return []

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

def adicionar_tarefa():
    tarefa = input("Digite o titulo da tarefa: ")
    
    nova_tarefa = {
        "titulo": tarefa,
        "concluida": False
    }
    
    tarefas = carregar_tarefas()
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("Lista de Tarefas:\n")
    for tarefa in tarefas:
        nome_tarefa = tarefa.get("titulo", "Sem titulo")
        status = "Concluida" if tarefa.get("concluida", False) else "Pendente"
        print(f"{nome_tarefa} - {status}")

def remover_tarefa():
    titulo = input("Digite o titulo da tarefa que deseja remover: ").strip()
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa.get("titulo").strip() == titulo:
            deseja = input(f"Deseja realmente remover a tarefa '{titulo}'? (s/n): ").strip().lower()
            if deseja in ("s", "si", "sim")	:
                tarefas.remove(tarefa)
                salvar_tarefas(tarefas)
                print(f"Tarefa '{titulo}' removida com sucesso!")
                return
            if deseja in ("n", "nao", "não"):
                print("Remocao cancelada.")
                return
    print(f"Tarefa '{titulo}' nao encontrada.")

def concluir_tarefa():
    titulo = input("Digite o titulo da tarefa que deseja marcar como concluida: ").strip()
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa.get("titulo").strip() == titulo:
            deseja = input(f"Deseja marcar a tarefa '{titulo}' como concluida? (s/n): ").strip().lower()
            if deseja in ("s", "si", "sim"):
                tarefa["concluida"] = True
                salvar_tarefas(tarefas)
                print(f"Tarefa '{titulo}' concluida com sucesso!")
                return
            if deseja in ("n", "nao", "não"):
                print("Operacao cancelada.")
                return
    print(f"Tarefa '{titulo}' nao encontrada.")
