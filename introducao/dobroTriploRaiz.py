import math

numero = int(input('Digite um número e veja as operações realizadas com ele: '))

print('O dobro de {} é : {}'.format(numero, (numero*2)))
print('O triplo de {} é : {}'.format(numero, (numero * 3)))
print('A raiz quadrada de {} é igual a: {:.2f}'.format(numero, math.sqrt(numero)))
print('A raiz quadrada de {} é igual a: {:.2f}'.format(numero, (numero**(1/2))))
print('A raiz quadrada de {} é igual a: {:.2f}'.format(numero, pow(numero, (1/2))))
