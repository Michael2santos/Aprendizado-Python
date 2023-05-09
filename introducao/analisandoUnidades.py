num = int(input('Digite um número: '))

un = num // 1 % 10
dz = num // 10 % 10
cent = num // 100 % 10
milha = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {} '.format(un))
print('Dezena: {} '.format(dz))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(milha))
