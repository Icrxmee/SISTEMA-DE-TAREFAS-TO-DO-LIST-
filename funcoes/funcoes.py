from interfacee.interface import *

def controleGeral():
    try:
        atividades = []
        
        while True:
            
            escolha = menuPrincipal()
            match escolha:

                case "1":
                    adicionarTarefas(atividades)
                
                case "2":
                    listarTarefas(atividades)

                case "3":
                    marcarConluida(atividades)
                
                case "4":
                    removerTarefa(atividades)
                
                case "0":
                    print("Saindo do Sistema.")
                    sleep(0.5)
                    return
                
                case _:
                    print("Escolha uma alternativa válida")

    except KeyboardInterrupt:
        print("\nInterrompendo Sistema.")
        linha()
        sleep(0.5)
        return


def adicionarTarefas(ativiades):

    while True:
    
        tarefa = str(input("Digite uma tarefa: "))

        if not tarefa or tarefa.isdigit():
            linha()
            print("Não é aceito descrição EM BRANCO ou NÚMEROS!!!")
            sleep(0.5)
            
        else:
            ativiades.append({
                "Tarefa": tarefa,
                "Concluída": False
                })
            
            linha()
            sleep(0.5)
            return ativiades

def listarTarefas(atividades):

    linha()
    print("Suas tarefas: ")
    
    for i, tarefa in enumerate(atividades):
        print(f"{i+1} - {tarefa}")
        linha()
        sleep(0.5)
        
    return

def marcarConluida(atividades):

    if not atividades:
        print("Nenhuma atividade salva até o momento.")
        sleep(0.5)
        return
    
    for i, tarefa in enumerate(atividades):
        print(f"{i+1} - {tarefa}")
        linha()
        sleep (0.5)

    while True:
            
        try:
            mudar = int(input("Qual tarefa deseja marcar como CONCLUÍDA: "))
            sleep(0.5)

            if not mudar:
                print("Por favor escreva uma opção válida!!!")
                sleep(0.5)

            elif mudar-1 >= len(atividades) or mudar < 1:
                print("Por favor escreva uma opção válida!!!")
                continue

            atividades[mudar-1]["Concluída"] = True
                
            print("Atividade atualizada com sucesso!!!")
            sleep(0.5)
            return
    
        except ValueError:
            print("Digite apenas números")

def removerTarefa(atividades):

    if not atividades:
        print("Nenhuma atividade salva até o momento.")
        sleep(0.5)
        return
    
    for i, tarefa in enumerate(atividades):
        print(f"{i+1} - {tarefa}")
        linha()
        sleep (0.5)

    while True:

        try:
        
            remover = int(input("Digite qual tarefa deseja remover: "))

            if not remover:
                print("Por favor escreva uma opção válida!!!")
                sleep(0.5)

            elif remover-1 >= len(atividades) or remover < 1:
                print("Por favor escreva uma opção válida!!!")
                sleep(0.5)
                continue
            
            atividades.pop(remover-1)
            return atividades
        
        except ValueError:
            print("Por favor escreva apenas números!!!")