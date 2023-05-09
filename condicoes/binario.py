#converter numero inteiro em binario ou octal ou hexadecimal

numero = int(input('Digite um valor inteiro para conversão: '))
print('''[1]-Binario
[2]-Octal
[3]-Hexadecimal''')
opcao = int(input('Escolha uma opção para conversão: '))

if opcao == 1:
    print('{} Convertido para Binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Digite uma opcão valida!!!')