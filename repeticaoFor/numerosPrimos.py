numero = int(input('Digite um numero inteiro: '))
total = 0
for contador in range(1, numero+1):
    if numero % contador == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contador), end=' ')
print('FIMMM')
if total == 2:
    print('O numero {} é PRIMO pois foi divisivel {} vezes '.format(numero, total))
else:
    print('O numero {} NÂO È PRIMO pois foi divisivel {} vezes '.format(numero, total))