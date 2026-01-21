from interfacee.interface import *

def controleGeral():

    atividades = {}

    try:
        
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
            ativiades.update({
                "Tarefa": tarefa,
                "Conluída?": False
                })
            
            linha()
            sleep(0.5)
            return ativiades

def listarTarefas(atividades):

    linha()
    print("As suas atividades até  momento são: ")
    
    for des, ativ in atividades.items():
        print(f"{des}: - {ativ}")
        
    return

def marcarConluida(atividades):

    for des, ativ in atividades.items():
        print(f"{des} - {ativ}")
        linha(0.5)