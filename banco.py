import datetime
import pytz
import textwrap

def menu():
    print("""Bem vindo ao banco:

    1) Criar usuario
    2) Criar conta  
    3) listar contas         
    4) Deposito
    5) Saque
    6) Extrato
    9) Fechar
        
        """)

    opcao = input("O que deseja fazer? ")
    return opcao

def verificar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None
    ...

def cadastrar_usuario(usuarios):
    cpf = input('Digite seu CPF: ')
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print('Usuario ja cadastrado')
        return

    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    endereco = input('Digite seu endereço: ')
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco })
    print('usuario criado com sucesso!! ')

def criar_conta_corrente(AGENCIA, usuarios, numero_conta):
    cpf = input('Digite seu CPF: ')
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print('conta criada')
        return {'agencia': AGENCIA, 'numero_conta': numero_conta, 'usuario': usuario}

    print('Usuario nao encontrado')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def Deposito(saldo, limite_transacoes, historico, valor_escolhido):
    if limite_transacoes > 0:
        
        saldo += valor_escolhido
        horario = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
        historico.append(f'{str(saldo)}      as {horario.strftime("%H:%M %d/%m/%Y")}')
        limite_transacoes -= 1
        print(f'Deposito de {valor_escolhido}, realizado com sucesso')
    else:
        print("Voce já atingiu o limite de transações diario")

    return saldo, limite_transacoes, historico

def Saque(LIMITE_PARA_SAQUE, limite_saque, saldo, limite_transacoes,historico,valor_escolhido):
    #ex = excedeu 
    ex_limite_saque = LIMITE_PARA_SAQUE < valor_escolhido
    ex_saldo = valor_escolhido > saldo
    ex_limite_transacoes = limite_transacoes ==0 or limite_saque == 0
   
    if ex_limite_transacoes:
        print("Voce já atingiu o limite de transações diarias")
    elif ex_limite_saque:
        print(f'vc digitou um valor maior que o limite de {LIMITE_PARA_SAQUE} ou um valor invalido.')
    elif ex_saldo:
        print('Saldo insuficiente.')
    elif valor_escolhido > 0:
        saldo -= valor_escolhido
        horario = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
        historico.append(f'-{str(round(valor_escolhido,2))}     as {horario.strftime("%H:%M %d/%m/%Y")}')
        limite_saque -= 1
        limite_transacoes -= 1
    else:
        print ('entrada de dados invalidas')        

    return limite_saque, saldo, limite_transacoes

def Extrato(historico,saldo):
    if historico == []:
        print('Não foram realizadas movimentações')
    else:
        print(f'seu saldo é de: {saldo:.2f}, seu historico:\n{"\n".join(historico)}')
        
def main():
    saldo = 0
    sair = False
    AGENCIA = '0001'

    historico = []
    usuarios = []
    contas = []
    numero_conta = 1

    LIMITE_PARA_SAQUE = 500
    limite_saque = 3
    limite_transacoes = 10
    opcao = 0
        
    while sair == False:
        # Menu
        opcao = menu()

        if opcao == '1':
            cadastrar_usuario(usuarios)

        if opcao == '2': 
            conta = criar_conta_corrente(AGENCIA, usuarios, numero_conta)

            if conta:
                contas.append(conta)
                numero_conta += 1

        if opcao == '3': 
            listar_contas(contas)


        #passando os argumentos de modo posicional
        if opcao == '4':
            valor_escolhido = float(input('quanto sacar depositar? '))
            saldo, limite_transacoes, historico = Deposito(saldo, limite_transacoes, historico, valor_escolhido)

        #passando os argumentos de modo não posicional
        elif opcao == '5':
            valor_escolhido = float(input('quanto deseja sacar? '))
            limite_saque, saldo, limite_transacoes = Saque(LIMITE_PARA_SAQUE = LIMITE_PARA_SAQUE,
                                                            limite_saque = limite_saque,
                                                            saldo = saldo,
                                                            limite_transacoes = limite_transacoes,
                                                            historico = historico, 
                                                            valor_escolhido = valor_escolhido)
        elif opcao == '6':
            Extrato(historico,saldo)

        elif opcao == '9':
            sair = True

        else:
            print('opção invalida, escolha uma opcao valida')

    
main()
    


