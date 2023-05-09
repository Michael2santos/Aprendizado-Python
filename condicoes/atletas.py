# classificação de atletas por idade

from datetime import date
anoAtual = date.today().year
nascimento = int(input('Data de nascimento: '))
idade = anoAtual - nascimento

print('Este candidato tem {} anos '.format(idade))
if idade <= 9:
    print('\033[1;30;44mClassificação: MIRIN\033[m')
elif idade <= 14:
    print('Classificação: INFANTIL ')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

