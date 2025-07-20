saldo_da_conta = 0.0
depositos = []
saques = []
quantidade_saques_hoje = 0

def depositar(valor_depositado):
    global saldo_da_conta
    if valor_depositado <= 0:
        print("ERRO | O valor depositado deve ser positivo.\n")
        return
    else:
        saldo_da_conta += valor_depositado
        depositos.append(valor_depositado)
        
    print(f"Foi depositado R$ {valor_depositado:.2f} na conta.")    
    print(20*"-")    
    print(f"Saldo atual = R$ {saldo_da_conta:.2f}")
    print(20*"-")

def sacar(valor_sacado):
    global saldo_da_conta, quantidade_saques_hoje
    
    if quantidade_saques_hoje >= 3:
        print("ERRO | Limite diário de 3 saques atingido.\n")
        return

    if saldo_da_conta <= 0:
        print("ERRO | Sua conta está zerada, deposite dinheiro.\n")
        return
    else:
        if valor_sacado > saldo_da_conta:
            print("ERRO | Você não tem saldo suficiente.\n")
            return
        elif valor_sacado > 500:
            print("ERRO | O seu limite de saque por vez é de R$500,00.\n")
            return
        elif valor_sacado == 0:
            print("ERRO | Insira valores válidos para o saque.\n")
            return
        else:
            saldo_da_conta -= valor_sacado
            saques.append(valor_sacado)
            quantidade_saques_hoje += 1
            
        print(f"Foi sacado R$ {valor_sacado:.2f} da conta.")
        print(20*"-")
        print(f"Saldo atual = R$ {saldo_da_conta:.2f}")
        print(20*"-")

def extrato():
    if depositos:
        print("\nDepósitos já realizados:")
        for item in depositos:
            print(f"- R$ {item:.2f}")
    else:
        print("\nNão foram realizadas movimentações de depósitos.")
            
    if saques:
        print("Saques já realizados:")
        for item in saques:
            print(f"- R$ {item:.2f}")
    else:
        print("Não foram realizadas movimentações de saques.")
            
    print(20*"-")
    print(f"Saldo atual = R$ {saldo_da_conta:.2f}")
    print(20*"-")

def menu():
    return input(
            '''\n========MENU========\nEscolha o que deseja fazer:\n1 - Depositar na conta.\n2 - Sacar da conta.\n3 - Listar depósitos.\n4 - Encerrar Programa.\n====================\n''')

def main():
    while True:
        esc = menu()
        if esc == "1":
            valor_depositado = float(input("\nValor a depositar: "))
            depositar(valor_depositado)
                        
        elif esc == "2":
            valor_sacado = float(input("\nValor a sacar: "))
            sacar(valor_sacado)
            
        elif esc == "3":
            extrato()
            
        elif esc == "4":
            print("\nEncerrando programa...\n")
            break
        
        else:
            print("\nERRO | Opção inválida, escolha outra opção.\n")
            
if __name__ == '__main__':
    main()