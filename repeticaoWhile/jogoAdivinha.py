#criar jogo em que o computador escolha um numero e o jogador vai continuar tentando acertar até conseguir e dizer no final quantos tentativas foram necessarias para acertar
#bibliotecas python
from random import randint
from time import sleep

#computador sorteando um numero
computador = randint(1, 10)
print('Pensando em um numero....')
sleep(2)

acumulador = 0
jogador = ''
#jogador vai tentar até acertar
print('=== Tente adivinha o numero que pensei ===')
while jogador != computador:
    # jogador escolhendo um numero

    jogador = int(input('Digite um numero inteiro de 1 a 10: '))
    acumulador += 1
    if jogador < computador:
        print('O numero que pensei é maior, tente novamente!')
    elif jogador > computador:
        print('O numero que pensei é menor, tente novamente!')
print('Parabens você acertou, eu escolhi numero {} e você tambêm escolheu o numero {}'.format(computador, jogador))
print('E foram necessarias {} tentativas para acertar'.format(acumulador))
