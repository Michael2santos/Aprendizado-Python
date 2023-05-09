#criar app que leia dois numeros, logo apos apareça menu de opções, 1-soma 2-subtrai 3-multiplica 4- dividi 5-escrever novos numeros 6- sair da calculadora e fazer opeção solicitada
from time import sleep

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
opcao = 0

while opcao != 5:
    print('''Selecione a opção desejada 
            1- Somar
            2-Multiplicar
            3-Maior
            4-Novos números
            5-Sair do programa 
            Opção selecionada: ''')
    opcao = int(input('Opção desejada: '))

    if opcao == 1:
        print('A soma de {} + {} é igual a: {} '.format(numero1, numero2, numero2+numero1))
    elif opcao == 2:
        print('A multiplicação de {} X {} é igual a: {}'.format(numero1, numero2, numero2 * numero1))
    elif opcao == 3:
        if numero1 > numero2:
            print('O maior numero digitado foi {}'.format(numero1))
        elif numero2 > numero1:
            print('O maior numero digitado foi {}'.format(numero2))
        else:
            print('Os numeros digitados são iguais')
    elif opcao == 4:
        print('Opção 4 selecionada, digite os novos numeros')
        numero1 = int(input('Digite o primeiro numero: '))
        numero2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Fechando programa ...')
        sleep(2)
        print('Programa fechado, até mais!!')
    else:
        print('Opção inválida, tente novamente')
