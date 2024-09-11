#banco
def Deposito(saldo):
    aux_deposito = float(input('quanto deseja depositar? '))
    saldo += aux_deposito
    historico.append(str(aux_deposito))

    return saldo

def Saque(limite_saque, saldo):
    if limite_saque > 0:
        aux_saque = float(input('quanto deseja retirar? '))
        if 500 >= aux_saque > 0:
            saldo -= aux_saque
            historico.append(f'-{str(round(aux_saque,2))}')
            limite_saque -= 1
        else:
            print('vc digitou um valor maior que o limite de 500 ou um valor invalido.')
    else:
        print("Voce já atingiu o limite de saque diario")

    return limite_saque, saldo

def Extrato():
    if historico == []:
        print('Não foram realizadas movimentações')
    else:
        print(f'seu saldo é de: {saldo:.2f}, seu historico:\n{"\n".join(historico)}')
        

saldo = 0
historico = []
sair = False
limite_saque = 3

# Menu
while sair == False:
    print("""Bem vindo ao banco:
        
    1) Deposito
    2) Saque
    3) Extrato
    4) Fechar
    
    """)

    opcao = input("O que deseja fazer? ")
    if opcao == '1':
        saldo = Deposito(saldo)
    elif opcao == '2':
        limite_saque, saldo = Saque(limite_saque, saldo)
    elif opcao == '3':
        Extrato()
    elif opcao == '4':
        sair = True
    else:
        print('opção invalida, escolha uma opcao valida')
        
    


