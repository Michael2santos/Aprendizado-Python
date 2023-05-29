listaNum = []

while True:
    numero = int(input('Digite um numero: '))
    if numero not in listaNum:#adicionar numero na lista se ja não tiver o mesmo
        listaNum.append(numero)
    else:
        print('Numero duplicado, não vou adicionar!!!')

    resposta = str(input('Quer continuar [S/N]: '))
    while resposta not in 'SsNn':
        print('Opção invalída, Digite novamente!')
        resposta = str(input('Quer continuar [S/N]: '))

    if resposta in 'Nn':
        break

listaNum.sort()
print('-=' * 20)
print(f'Você digitou os numeros', listaNum)
