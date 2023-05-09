#receber numero float e mostrar somente sua parte inteira
from math import trunc
num = float(input('Digite um numero real para ver sua parte inteira: '))

print('O numero digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))
print('O numero digitado foi {} e sua parte inteira é {}'.format(num, int(num)))