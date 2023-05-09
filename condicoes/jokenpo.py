#jogo jokenpo pedra-papel-tesoura
#tesoura ganha do papel, papel da pedra, pedra ganha da tesoura
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)


jogador = int(input('''<====Itens====>!!
0-Pedra
1-Papel
2-Tesoura
Escolha seu item: '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

if jogador == 0:#jogador escolheu Pedra
    if computador == 0:
        print('Empatamos, você jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
    elif computador == 1:
        print('Você perdeu, você jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
    elif computador == 2:
            print('Você ganhou, você jogou {} e eu joguei {} '.format(itens[jogador], itens[computador]))

if jogador == 1:#jogador escolheu Papel
    if computador == 0:
        print('Você ganhou, Você jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
    elif computador == 1:
        print('Empatamos, Você jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
    elif computador == 2:
        print('Você perdeu, Você jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
if jogador == 2:#jogador escolheu Tesoura
    if computador == 0:
        print('Você perdeu, Você jogou {} e eu joguei {} '.format(itens[jogador], itens[computador]))
    elif computador == 1:
        print('Você ganhou, Você jogou {} e eu joguei {} '.format(itens[jogador], itens[computador]))
    elif computador == 2:
        print('Empatamos, Você jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
