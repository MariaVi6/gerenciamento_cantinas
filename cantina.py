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
    print("2 - Cardápio do dia")
    print("3 - Voltar para as cantinas")
    print("4 - Finalizar acesso")

def cardapioDoDia():
    print("\nComidas:")
    print("1 - Bolo Fofo")
    print("2 - Bolo Mole")
    print("3 - Torta de Frango")
    print("4 - Pratinho")
    print("5 - Cachorro Quente")

    print("\nBebidas:")
    print("6 - Suco de Goiaba")
    print("7 - Suco de Acerola")
    print("8 - Suco de Cajá")
    print("9 - Suco de Caju")
    print("10 - Suco de Maracujá")
    print("11 - Suco de Limão")

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
                cardapioDoDia() 
                opcaoPedido = int(input("\nEscolha um item do cardápio: "))
                match opcaoPedido:
                    case 1:
                        print("\nVocê escolheu Bolo Fofo.")
                    case 2:
                        print("\nVocê escolheu Bolo Mole.")
                    case 3:
                        print("\nVocê escolheu Torta de Frango.")
                    case 4:
                        print("\nVocê escolheu Pratinho.")
                    case 5:
                        print("\nVocê escolheu Cachorro Quente.")
                    case 6:
                        print("\nVocê escolheu Suco de Goiaba.")
                    case 7:
                        print("\nVocê escolheu Suco de Acerola.")
                    case 8:
                        print("\nVocê escolheu Suco de Cajá.")
                    case 9:
                        print("\nVocê escolheu Suco de Caju.")
                    case 10:
                        print("\nVocê escolheu Suco de Maracujá.")
                    case 11:
                        print("\nVocê escolheu Suco de Limão.")
                    case _:
                        print("\nOpção inválida no cardápio.")
            case 2:
                limparTela()
                cardapioDoDia()  
            case 3:
                limparTela()
                print("\nVoltando ao menu de cantinas...")
                menuCantinas()
            case 4:
                limparTela()
                print("\nSaindo... Até logo!")
                exit()
            case _:
                limparTela()
                print("\nOpção inválida. Escolha entre 1 e 4.")

menuCantinas()


