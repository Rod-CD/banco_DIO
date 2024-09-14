import datetime
import pytz

def Deposito(saldo, limite_transacoes, historico):
    if limite_transacoes > 0:
        aux_deposito = float(input('quanto deseja depositar? '))
        saldo += aux_deposito
        horario = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
        historico.append(f'{str(aux_deposito)}     as {horario.strftime("%H:%M %d/%m/%Y")}')
        limite_transacoes -= 1
    else:
        print("Voce já atingiu o limite de transações diario")

    return saldo, limite_transacoes, historico

def Saque(LIMITE_PARA_SAQUE, limite_saque, saldo, limite_transacoes):
    if limite_saque > 0 and limite_transacoes > 0: 
        aux_saque = float(input('quanto deseja retirar? '))
        if LIMITE_PARA_SAQUE >= aux_saque > 0:
            if saldo >= aux_saque:
                saldo -= aux_saque
                horario = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
                historico.append(f'-{str(round(aux_saque,2))}     as {horario.strftime("%H:%M %d/%m/%Y")}')
                limite_saque -= 1
                limite_transacoes -= 1
            else:
                print('Saldo insuficiente.')
        else:
            print(f'vc digitou um valor maior que o limite de {LIMITE_PARA_SAQUE} ou um valor invalido.')
    else:
        if limite_saque == 0:
            print("Voce já atingiu o limite de transações diarias")
        else:
            print("Voce já atingiu o limite de saque diario")

    return limite_saque, saldo, limite_transacoes

def Extrato():
    if historico == []:
        print('Não foram realizadas movimentações')
    else:
        print(f'seu saldo é de: {saldo:.2f}, seu historico:\n{"\n".join(historico)}')
        

saldo = 0
historico = []
sair = False
LIMITE_PARA_SAQUE = 500
limite_saque = 3
limite_transacoes = 10

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
        saldo, limite_transacoes, historico = Deposito(saldo, limite_transacoes, historico)
    elif opcao == '2':
        limite_saque, saldo, limite_transacoes = Saque(LIMITE_PARA_SAQUE, limite_saque, saldo, limite_transacoes)
    elif opcao == '3':
        Extrato()
    elif opcao == '4':
        sair = True
    else:
        print('opção invalida, escolha uma opcao valida')
        
    


