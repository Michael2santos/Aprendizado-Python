from datetime import date
maiores = 0
menores = 0
ano = date.today().year

for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - nascimento < 18:
        menores += 1
    else:
        maiores += 1
print('Total de maiores de idade: {}'.format(maiores))
print('Total de menores de idade: {}'.format(menores))