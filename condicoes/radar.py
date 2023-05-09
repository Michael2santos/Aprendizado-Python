#radar de 60km 7 reais por km excedente

km = int(input('Digite a velocidade em km que voçê está: '))

if km <= 60:
    print('Parabens voçê está na velocidade correta!!!')
else:
    excedente = km - 60
    multa: float = excedente * 7
    print('Voçê está acima da velocidade o limite é 60 Kms!!')
    print('Você passou a {} Kms no radar!!'.format(km))
    print('E o valor da multa foi de {:.2f} reais'.format(multa))
