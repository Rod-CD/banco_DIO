#banco
def Deposito(saldo):
    ...

def Saque():
    ...

def Extrato():
    ...

saldo = 0
historico = []
sair = False

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
        aux_deposito = float(input('quanto deseja depositar? '))
        saldo += aux_deposito
        historico.append(str(aux_deposito))

    elif opcao == '2':
        aux_saque = float(input('quanto deseja retirar? '))
        saldo -= aux_saque
        historico.append(f'-{str(aux_saque)}')

    elif opcao == '3':
        print(f'seu saldo é de: {saldo}, seu hsitorico:\n{"\n".join(historico)}')
        
    elif opcao == '4':
        print('selecionou 4')
        sair = True
    else:
        print('opção invalida, escolha uma opcao valida')
        
    


