import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuCantinas():
    print("\nSeja Bem-Vindo!")
    print("1 - UMP - União de Mocidade Presbiteriana")
    print("2 - UPH - União Presbiteriana de Homens")
    print("3 - UPA - União Presbiteriana de Adolescentes")
    print("4 - SAF - Sociedade Auxiliadora Feminina")
    print("5 - Finalizar acesso\n")
    
    escolhaCantina()

def menuOpcoes():  
    print("\n1 - Fazer pedido")
    print("2 - Visualizar pedido")
    print("3 - Cardápio do dia")
    print("4 - Voltar para as cantinas")
    print("5 - Finalizar acesso")

def escolhaCantina():
    while True:
        cantina = int(input("\nEscolha uma cantina: "))
        
        match cantina:
            case 1:
                limparTela()
                print("\nSeja Bem-Vindo à Cantina UMP")
            case 2:
                limparTela()
                print("\nSeja Bem-Vindo à Cantina UPH")
            case 3:
                limparTela()
                print("\nSeja Bem-Vindo à Cantina UPA")
            case 4:
                limparTela()
                print("\nSeja Bem-Vindo à Cantina SAF")
            case 5:
                print("\nSaindo...")
                break
            case _:
                print("\nOpção inválida. Escolha entre 1 e 5.")
                continue
        escolhaOpcao()

def escolhaOpcao():
    while True:
        menuOpcoes()
        opcao = int(input("\nEscolha uma opção: "))

        match opcao:
            case 1:
                limparTela()
                print("\nFazendo pedido...")
            case 2:
                limparTela()
                print("\nVisualizando pedido...")
            case 3:
                limparTela()
                print("\nExibindo o cardápio do dia...")
            case 4:
                limparTela()
                print("\nVoltando ao menu de cantinas...")
                menuCantinas()
            case 5:
                limparTela()
                print("\nSaindo... Até logo!")
                exit()
            case _:
                limparTela()
                print("\nOpção inválida. Escolha entre 1 e 5.")

menuCantinas()
