limite = 500
saldo = 0
extrato = ''
numero_saques = 0
limite_saques = 3

def menu():
    print('-'*30)
    print('\033[33mAGÊNCIA BANCÁRIA\033[0m'.center(40))
    print('-'*30)
    print('''[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair''')


def dados():
    while True:
        print('-'*30)
        print('\033[33mLOGIN DE ACESSO\033[0m'.center(40))
        print('-'*30)
        while True:
            escolha = input('Você já possui cadastro? [S/N]: ').upper().strip()[0]
            if escolha not in ['S','N']:
                print('\033[31mERRO! Selecione uma opção válida!\033[0m\n')
            elif escolha == '':
                print('\033[31mERRO! Selecione uma opção válida!\033[0m\n')
            else:
                break
        nome= input('\033[36mNome: \033[0m').upper()
        cpf = input('\033[36mCPF: \033[0m')
        encontrado = False
        registro = f'{nome}; {cpf}\n'

        try:
            with open ('dados.txt', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo: 
                    linha = linha.strip()
                    if ';' in linha:
                        nome_cadastrado, cpf_cadastrado = linha.split(';')
                        if cpf == cpf_cadastrado.strip():
                            encontrado = True
                            nome == nome_cadastrado.strip()
                            break
        except FileNotFoundError:
            pass

        if escolha == 'S':
            if encontrado:
                print(f'\033[32mBem-vindo de volta, {nome}!\033[0m')
            else: 
                print('\033[31mCPF não encontrado. Por favor, cadastre-se primeiro.\033[0m')
                dados()
        else:
            if encontrado:
                print('\033[31mCPF já cadastrado!\033[0m')
            else: 
                with open('dados.txt', 'a', encoding='utf-8') as arquivo:
                    arquivo.write(registro)
                    print('\033[32mCadastro realizado com sucesso!\033[0m')
        break     
                

def opcao1():
    global saldo, extrato, limite_saques, numero_saques
    try:
        saldo = float(input('Qual valor deseja depositar? R$'))
        if saldo > 0:
            print(f'\033[32mValor R${saldo:.2f} adicionado a sua conta com sucesso!\033[0m')
    except (ValueError, TypeError):
        print('\033[31mERRO! Digite uma respotas válida!\033[0m')


def opcao2():
    global saldo, extrato, numero_saques, limite_saques
    if numero_saques >= limite_saques:
        print('\033[31mLimite de 3 saques diários atingido.\033[0m')
        return
    try:
        valor = float(input('Qual valor deseja sacar? R$'))
        if valor > saldo:
             print(f'\033[31mSaldo insuficiênte!\033[0m')
        elif valor > limite: 
            print('\033[31mDigite um valor menor ou igual ao seu limite diário de R$500.00\033[0m')
        elif valor <= 0:
            print('\033[31mValor inválido.\033[0m')
        else:
            saldo -= valor
            numero_saques +=1
            extrato += f'Saque: R${valor:.2f}\n'
            print(f'\033[32mSaque de R${valor:.2f} efetuado com sucesso!\033[0m')
    except ValueError:
        print('\033[31mERRO! Digite um número válido!\033[0m')

def opcao3():
    global extrato, saldo, numero_saques
    print('-'*30)
    print('\033[33mEXTRATO\033[0m'.center(40))
    print('-'*30)
    with open ('extrato.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{extrato}\n Saldo atual: R${saldo:.2f}\n')
        if extrato == '':
            print('\033[31mNão foram feitas movimentações\033[0m')
        else:
            print(extrato)
            print(f'\033[32mSaldo atual: R${saldo:.2f}\033[0m')


dados()
while True:
    menu()
    try:
        opcao = int(input('Sua opção: '))
    except (ValueError, TypeError):
        print('\033[31mErro! Digite uma opção válida\033[0m')
        continue
    if opcao == 1:
        opcao1()
    elif opcao == 2:
        opcao2()
    elif opcao == 3:
        opcao3()
    elif opcao == 4:
        print('\033[36mEncerrando o programa!\033[0m')
        break
    else:
        print('\033[31mOperação inválida! Selecione um número válido!\033[0m')