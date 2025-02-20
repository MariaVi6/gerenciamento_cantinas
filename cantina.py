import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

pedidos = {
    "UMP": [],
    "UPH": [],
    "UPA": [],
    "SAF": []
}

cardapio = {
    1: "Bolo Fofo",
    2: "Bolo Mole",
    3: "Torta de Frango",
    4: "Pratinho",
    5: "Cachorro Quente",
    6: "Suco de Goiaba",
    7: "Suco de Acerola",
    8: "Suco de Cajá",
    9: "Suco de Caju",
    10: "Suco de Maracujá",
    11: "Suco de Limão"
}

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
    print("3 - Ver pedidos")
    print("4 - Voltar para as cantinas")
    print("5 - Finalizar acesso")

def cardapioDoDia():
    print("\nCardápio do dia:")
    
    for numero, nome in cardapio.items():
        print(f"{numero} - {nome}")
    print("12 - Voltar ao menu anterior")

def escolhaCantina():

    while True:
        cantina = int(input("\nEscolha uma cantina: "))
        
        match cantina:
            case 1:
                limparTela()
                print("\nSeja Bem-Vindo à Cantina UMP")
                escolhaOpcao("UMP")
            case 2:
                limparTela()
                print("\nSeja Bem-Vindo à Cantina UPH")
                escolhaOpcao("UPH")
            case 3:
                limparTela()
                print("\nSeja Bem-Vindo à Cantina UPA")
                escolhaOpcao("UPA")
            case 4:
                limparTela()
                print("\nSeja Bem-Vindo à Cantina SAF")
                escolhaOpcao("SAF")
            case 5:
                print("\nSaindo...")
                break
            case _:
                print("\nOpção inválida. Escolha entre 1 e 5.")

def escolhaOpcao(cantinaSelecionada):

    while True:
        menuOpcoes()
        opcao = int(input("\nEscolha uma opção: "))

        match opcao:

            case 1:
                limparTela()
                print("\nCardápio do dia...")
                cardapioDoDia()

                while True:
                    opcaoPedido = int(input("\nEscolha um item do cardápio (ou 12 para voltar): "))
                    
                    if opcaoPedido == 12:
                        limparTela()
                        break
                    
                    if opcaoPedido in cardapio:
                        nomeItem = cardapio[opcaoPedido]
                        print(f"\nVocê escolheu {nomeItem}.")
                        pedidos[cantinaSelecionada].append(nomeItem)
                    else:
                        print("\nOpção inválida no cardápio. Escolha um número válido.")
            case 2:
                limparTela()
                cardapioDoDia()
                input("\nPressione Enter para voltar ao menu anterior...")
                limparTela()
            case 3:
                limparTela()
                verPedidos(cantinaSelecionada)
                input("\nPressione Enter para voltar ao menu anterior...")
                limparTela()
            case 4:
                limparTela()
                print("\nVoltando ao menu de cantinas...")
                return menuCantinas()
            case 5:
                limparTela()
                print("\nSaindo... Até logo!")
                exit()
            case _:
                limparTela()
                print("\nOpção inválida. Escolha entre 1 e 5.")

def verPedidos(cantinaSelecionada):

    print(f"\nPedidos da Cantina {cantinaSelecionada}:")

    if not pedidos[cantinaSelecionada]:
        print("Nenhum pedido foi feito ainda.")
    else:
        for i, pedido in enumerate(pedidos[cantinaSelecionada], start=1):
            print(f"{i}. {pedido}")

menuCantinas()
