from tarefa import *

while True:
    print("1. Adicionar Tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Concluir tarefa")
    print("5. Sair")

    opcao = input("Digite o numero da opcao:")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        concluir_tarefa()
    elif opcao == "5":
        break
    else:
        print("Opcao Invalida!")
