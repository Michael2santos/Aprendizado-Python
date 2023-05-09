#conversor de real em dolar 1 dolar é igual a 5,17 reais

real = float(input('Quantos reais R$ você tem ? '))
dolar = real / 5.17
euro = real / 5.56
print('Com R$ {} voçê pode comprar {:.2f}$ dolares '.format(real, dolar))
print('Com R$ {} voçê pode comprar {:.2f}€ Euros  '.format(real, euro))

