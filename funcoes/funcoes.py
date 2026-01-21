from interfacee.interface import *

def controleGeral():

    atividades = {}

    try:
        
        while True:
            
            escolha = menuPrincipal()
            match escolha:

                case "1":
                    adicionarTarefas(atividades)
                    print(atividades)
                
                case "2":
                    listarTarefas(atividades)

                case _:
                    print("Escolha uma alternativa válida")

    except KeyboardInterrupt:
        print("\nInterrompendo Sistema.")
        sleep(1)
        return


def adicionarTarefas(ativiades):

    while True:
    
        descrição = str(input("Qual a descrição da tarefa: "))

        if not descrição:
            linha()
            print("Não é aceito descrição em branco")
            linha()
            sleep(1)
            
        else:
            ativiades.update({
                "Descrição": descrição,
                "Concluída": False
                })
            return ativiades

def listarTarefas(atividades):

    linha()
    print("As suas atividades até  momento são: ")
    
    for des, ativ in range (atividades):
        print(f"{des} - {ativ}")
        sleep(1)
        return
        
