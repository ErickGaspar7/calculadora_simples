
#bibliotecas
import os

#dicionario das operacoes
menu = '''
[0] Adição
[1] Subtração
[2] Multiplicação
[3] Divisão
[4] Sair

Escolha: '''

while True:
    os.system('cls')
    print('--- Calculadora ---')
    escolha = input(menu)

    if escolha == '0':
        print()
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        resultado = n1 + n2
        print()
        print(f'O resultado da conta: {resultado}')
        input('Continuar [Enter]')
    elif escolha == '1':
        print()
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        resultado = n1 - n2
        print()
        print(f'O resultado da conta: {resultado}')
        input('Continuar [Enter]')
    elif escolha == '2':
        print()
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        resultado = n1 * n2
        print()
        print(f'O resultado da conta: {resultado}')
        input('Continuar [Enter]')
    elif escolha == '3':
        print()
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        resultado = n1 / n2
        print()
        print(f'O resultado da conta: {resultado}')
        input('Continuar [Enter]')

    elif escolha == '4':
        print()
        print('Saindo do programa ..')
        break

    else:
        print()
        print('Opção inválida.')
        input('Continuar [Enter]')

