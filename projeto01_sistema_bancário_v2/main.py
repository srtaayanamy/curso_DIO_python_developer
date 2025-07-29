from datetime import datetime

saldo_da_conta = 0.0
depositos = []
saques = []
usuarios = []
contas = []
quantidade_saques_hoje = 0
limite_transicao_hoje = 0
contador_contas = 1 

def criar_usuario():
    cpf = input("CPF (apenas números): ").strip()

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("ERRO | Já existe um usuário com esse CPF.")
            return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")

def encontrar_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta():
    global contador_contas

    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = encontrar_usuario_por_cpf(cpf)

    if not usuario:
        print("ERRO | Usuário não encontrado. Crie o usuário primeiro.")
        return

    nova_conta = {
        "agencia": "0001",
        "numero_conta": contador_contas,
        "usuario": usuario
    }

    contas.append(nova_conta)
    contador_contas += 1
    print(f"Conta criada com sucesso! Número da conta: {nova_conta['numero_conta']}")

def depositar(valor_depositado):
    global saldo_da_conta, limite_transicao_hoje
    
    if limite_transicao_hoje >= 10:
        print("ERRO | Limite diário de 10 transações atingido.\n")
        return
    
    if valor_depositado <= 0:
        print("ERRO | O valor depositado deve ser positivo.\n")
        return
    else:
        limite_transicao_hoje += 1
        saldo_da_conta += valor_depositado
        depositos.append((valor_depositado, datetime.now()))
        
    print(f"Foi depositado R$ {valor_depositado:.2f} na conta.")    
    print(20*"-")    
    print(f"Saldo atual = R$ {saldo_da_conta:.2f}")
    print(20*"-")

def sacar(valor_sacado):
    global saldo_da_conta, quantidade_saques_hoje, limite_transicao_hoje
    
    if limite_transicao_hoje >= 10:
        print("ERRO | Limite diário de 10 transações atingido.\n")
        return
    
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
            saques.append((valor_sacado, datetime.now()))
            quantidade_saques_hoje += 1
            limite_transicao_hoje += 1
            
        print(f"Foi sacado R$ {valor_sacado:.2f} da conta.")
        print(20*"-")
        print(f"Saldo atual = R$ {saldo_da_conta:.2f}")
        print(20*"-")

def extrato():
    if depositos:
        print("\nDepósitos já realizados:")
        for valor, data in depositos:
            print(f"- R$ {valor:.2f} em {data.strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("\nNão foram realizadas movimentações de depósitos.")
            
    if saques:
        print("Saques já realizados:")
        for valor, data in saques:
            print(f"- R$ {valor:.2f} em {data.strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("\nNão foram realizadas movimentações de saques.")
            
    print(20*"-")
    print(f"Saldo atual = R$ {saldo_da_conta:.2f}")
    print(20*"-")

def menu():
    return input(
            '''\n========MENU========
1 - Criar usuário
2 - Criar conta corrente
3 - Depositar na conta
4 - Sacar da conta
5 - Extrato
6 - Encerrar Programa
====================\n''')

def main():
    while True:
        esc = menu()
        if esc == "1":
            criar_usuario()

        elif esc == "2":
            criar_conta()
                        
        elif esc == "3":
            valor_depositado = float(input("\nValor a depositar: "))
            depositar(valor_depositado)
            
        elif esc == "4":
            valor_sacado = float(input("\nValor a sacar: "))
            sacar(valor_sacado)
            
        elif esc == "5":
            extrato()
            
        elif esc == "6":
            print("\nEncerrando programa...\n")
            break
        
        else:
            print("\nERRO | Opção inválida, escolha outra opção.\n")
            
if __name__ == '__main__':
    main()
