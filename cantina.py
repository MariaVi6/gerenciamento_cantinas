import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

pedidos = {
    "UMP": [],
    "UPH": [],
    "UPA": [],
    "SAF": []
}

cardapios = {
    "UMP": {
        "Comidas": {
            1: "Bolo Fofo",
            2: "Bolo Mole",
            3: "Torta de Frango",
            4: "Empada de Frango"
        },
        "Bebidas": {
            5: "Suco de Laranja",
            6: "Suco de Maracuja",
            7: "Suco de Cajá",
            8: "Água Mineral"
        }
    },
    "UPH": {
        "Comidas": {
            1: "Pratinho",
            2: "Cachorro Quente",
            3: "Pastel de Frango",
            4: "Coxinha"
        },
        "Bebidas": {
            3: "Suco de Goiaba",
            4: "Suco de Acerola",
            5: "Suco de Limão",
            6: "Água Mineral"
        }
    },
    "UPA": {
        "Comidas": {
            1: "Pão de Queijo",
            2: "Coxinha de Carne",
            3: "Misto Quente",
            4: "Pão Com Ovo"
        },
        "Bebidas": {
            5: "Suco de Acerola",
            6: "Suco de Caju",
            7: "Suco de Manga",
            8: "Água Mineral"
        }
    },
    "SAF": {
        "Comidas": {
            1: "Bolo de Chocolate",
            2: "Enroladinho De Salsicha",
            3: "Pão Árabe",
            4: "Pizza de Calabresa (1 pedaço)"
        },
        "Bebidas": {
            5: "Suco de Maracujá",
            6: "Suco de Tangerina",
            7: "Suco de Morango",
            8: "Água Mineral"
        }
    }
}

def menu_cantinas():
    while True:
        print("\nSeja Bem-Vindo!")
        print("1 - UMP - União de Mocidade Presbiteriana")
        print("2 - UPH - União Presbiteriana de Homens")
        print("3 - UPA - União Presbiteriana de Adolescentes")
        print("4 - SAF - Sociedade Auxiliadora Feminina")
        print("5 - Finalizar acesso\n")
        
        try:
            cantina = int(input("Escolha uma cantina: "))
            if cantina in range(1, 5):
                limpar_tela()
                cantina_nome = list(pedidos.keys())[cantina - 1]
                print(f"\nSeja Bem-Vindo à Cantina {cantina_nome}")
                escolha_opcao(cantina_nome)
            elif cantina == 5:
                print("\nSaindo... Até logo!")
                break
            else:
                print("\nOpção inválida. Escolha um número entre 1 e 5.")
        except ValueError:
            print("\nEntrada inválida! Digite um número.")

def menu_opcoes():  
    print("\n1 - Fazer pedido")
    print("2 - Cardápio do dia")
    print("3 - Ver pedidos")
    print("4 - Voltar para as cantinas")
    print("5 - Finalizar acesso")

def cardapio_do_dia(cantina):
    print(f"\nCardápio do dia da Cantina {cantina}:")
    print("\n-- Comidas --")
    for numero, nome in cardapios[cantina]["Comidas"].items():
        print(f"{numero} - {nome}")
    print("\n-- Bebidas --")
    for numero, nome in cardapios[cantina]["Bebidas"].items():
        print(f"{numero} - {nome}")
    print("\n12 - Fazer um pedido")
    print("13 - Voltar ao menu anterior")

def escolha_opcao(cantina_selecionada):
    while True:
        menu_opcoes()
        try:
            opcao = int(input("\nEscolha uma opção: "))
            match opcao:
                case 1:
                    limpar_tela()
                    fazer_pedido(cantina_selecionada)
                case 2:
                    limpar_tela()
                    cardapio_do_dia(cantina_selecionada)
                    opcao_cardapio = int(input("\nEscolha uma opção: "))
                    if opcao_cardapio == 12:
                        limpar_tela()
                        fazer_pedido(cantina_selecionada)
                    limpar_tela()
                case 3:
                    limpar_tela()
                    ver_pedidos(cantina_selecionada)
                    input("\nPressione Enter para voltar...")
                    limpar_tela()
                case 4:
                    limpar_tela()
                    return
                case 5:
                    print("\nSaindo... Até logo!")
                    exit()
                case _:
                    print("\nOpção inválida. Escolha entre 1 e 5.")
        except ValueError:
            print("\nEntrada inválida! Digite um número.")

def fazer_pedido(cantina):
    print("\nCardápio do dia:")
    cardapio_do_dia(cantina)
    
    while True:
        try:
            opcao_pedido = int(input("\nEscolha um item do cardápio: "))
            if opcao_pedido == 13:
                limpar_tela()
                break
            elif opcao_pedido in cardapios[cantina]["Comidas"]:
                nome_item = cardapios[cantina]["Comidas"][opcao_pedido]
                pedidos[cantina].append(nome_item)
                print(f"\nVocê adicionou {nome_item} ao seu pedido.")
            elif opcao_pedido in cardapios[cantina]["Bebidas"]:
                nome_item = cardapios[cantina]["Bebidas"][opcao_pedido]
                pedidos[cantina].append(nome_item)
                print(f"\nVocê adicionou {nome_item} ao seu pedido.")
            else:
                print("\nNúmero inválido. Escolha um item do cardápio.")
        except ValueError:
            print("\nEntrada inválida! Digite um número válido.")

def ver_pedidos(cantina):
    print(f"\nPedidos da Cantina {cantina}:")
    if not pedidos[cantina]:
        print("Nenhum pedido foi feito ainda.")
    else:
        for i, pedido in enumerate(pedidos[cantina], start=1):
            print(f"{i}. {pedido}")

menu_cantinas()

