from datetime import date
ano = int(input('Digite o ano para analisarmos se é BISSEXTO, ou aperte 0 para ano atual : '))


if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano de {} é BISSEXTO!!'.format(ano))
else:
    print('Ano de {} não é BISSEXTO!!'.format(ano))
