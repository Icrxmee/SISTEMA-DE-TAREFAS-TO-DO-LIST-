from time import sleep 

def linha():
    print("~" * 40)

def menuInicio():
    linha()
    print("Seja Bem-Vindo".center(40))
    linha()
    sleep(0.5)

def menuPrincipal():

    print("1 - Criar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Remover Tarefas")
    print("0 - Sair do Sistema")

    escolha = input("Escolha uma das opções: ")
    return escolha