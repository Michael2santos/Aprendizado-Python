kms = float(input('Digite quantos Kms tem até o destino: '))

if kms <= 200:
    valor = kms * 0.50
else:
    valor = kms * 0.45
print('Sua viagem tem {} Kms e será cobrado {} reais'.format(kms, valor))
print('Boa viagem !!!!')
