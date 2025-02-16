def escolhaCantina(cantina):
    match cantina:
        case 1:
            print("Você escolheu a Cantina UMP")
        case 2:
            print("Você escolheu a Cantina UPH")
        case 3:
            print("Você escolheu a Cantina UPA")
        case 4:
            print("Você escolheu a Cantina SAF")
        case _:
            print("Opção inválida. Escolha entre 1 e 4.")
            return False

    print("\nEscolha uma opção:")
    print("1 - Fazer pedido")
    print("2 - Cardápio do dia")
    print("3 - Voltar")
    print("4 - Sair")
    return True

def escolhaOpcao(opcao):
    
    match opcao:
        case 1:
            print("\nFazer pedido")
        case 2:
            print("\nCardápio do dia")
        case 3:
            print("\nVoltando ao menu...")
        case 4:
            print("\nSaindo... Até logo!")
        case _:
            print("\n Opção inválida. Escolha entre 1 e 4.")

print("Seja Bem-Vindo! \n")
print("1 - UMP - União de Mocidade Presbiteriana")
print("2 - UPH - União Presbiteriana de Homens")
print("3 - UPA - União Presbiteriana de Adolescentes")
print("4 - SAF - Sociedade Auxiliadora Feminina\n")

cantina = int(input("Escolha uma cantina: "))

if escolhaCantina(cantina):
    opcao = int(input("\nEscolha uma opção: "))
    escolhaOpcao(opcao)
