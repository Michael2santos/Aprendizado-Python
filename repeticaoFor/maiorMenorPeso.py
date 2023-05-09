maiorPeso = 0
menorPeso = 0
for c in range(1, 7):
    peso = float(input('Digite o seu peso da {}ª pessoa : '.format(c)))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('Maior peso digitado foi {}'.format(maiorPeso))
print('Menor peso digitado foi {}'.format(menorPeso))
