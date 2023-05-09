#criar programa que faça fatorial do numero digitado ex: 5 ai 5x4x3x2x1 = tanto, dez primeiros termos, e no fim perguntar se quer mostrar mais termos e quantos
from math import factorial

print('=-=' * 10)
print('PROGRAMA FATORIAL')
print('=-=' * 10)
#usuario digitando um numero para fatorar
numero = int(input('Digite um numero inteiro: '))

#programa usando estrutura de repeição while
'''
contador = numero
fatorial = 1

while contador > 0:
    print('{} '.format(contador), end=' ')
    print(' X ' if contador > 1 else ' = ', end=' ')
    fatorial *= contador
    contador -= 1

print('{}'.format(fatorial), end=' ')

'''

#programa usando biblioteca math com factorial
'''f = factorial(numero)
print('O fatorial de {} é: {}'.format(numero, f))'''

#programa usando estrurura de repetição for
fatorial = 1
for c in range(numero, 0, -1):
    print('{}'.format(c), end=' ')
    print(' X ' if c > 1 else ' = ', end=' ')
    fatorial *= c

print('{}'.format(fatorial), end=' ')
