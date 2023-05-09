from random import randint
print('=' * 25)
print('Vamos Jogar par ou impar')
print('=' * 25)
cont = 0

while True:
    #numero gerado pelo computador
    computador = randint(0, 10)
    # numero escolhido pelo jogador
    jogador = int(input('Digite um valor: '))
    #somar numero do jogador e do computador
    soma = computador + jogador
    # Par ou impar escolhido pelo jogador
    selecao = str(input('Par ou impar [P/I]: ')).strip().upper()

    while selecao not in 'PI':
        print('Valor invalido digite novamente')
        selecao = str(input('Par ou impar [P/I]: ')).strip().upper()

    if soma % 2 == 0 and selecao == 'P':#analise de par e se jogador ganhou ou perdeu
        print('Deu par e voçe venceu !!!')
        cont += 1
    elif soma % 2 == 0 and selecao == 'I':
        print('Deu par e voce perdeu, pois escolheu impar')
        break
    elif soma % 2 != 0 and selecao == 'I':
        print('Deu impar voçe venceu !!!')
        cont += 1
    else:
        print('Deu impar e voce perdeu, pois escolheu par')
        break

print('JOGO FINALIZADO')
print(f'Voce ganhou {cont} vezes')