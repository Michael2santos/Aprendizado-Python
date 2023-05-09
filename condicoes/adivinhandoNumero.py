from random import randint
from time import sleep
print('=' * 45)
print('Tente adivinhar o número que estou pensando!!')
print('=' * 45)


sorteado = randint(1, 10)
numero = int(input('Digite um número de 1 a 10 e tente acertar: '))
print('Processando...')
sleep(2)
if numero == sorteado:
    print('Parabens você acertou !!!')
    print('Pensei no numero {} também'.format(sorteado))
else:
    print('Voçê errou !!!')
    print('Pensei no número {}'.format(sorteado))





