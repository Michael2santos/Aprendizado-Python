numero = int(input('Digite um numero e veja sua tabuada: '))

for c in range(1, 11):
    print('{} X {} = {} '.format(numero, c, (numero * c)))
print('Tabuada finalizada')