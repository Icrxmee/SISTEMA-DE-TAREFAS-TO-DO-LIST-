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
                "Conluída?": False
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

    for i, tarefa in enumerate(atividades):
        print(f"{i+1} - {tarefa}")
        linha()
        sleep (0.5)
    
    while True:
        
        mudar = int(input("Qual atividade deseja marcar como CONCLUÍDA: "))
        sleep(5.0)

        if not mudar or mudar >= len(atividades):
            print("Por favor escreva uma opção válida!!!")

        


        
        



    

    