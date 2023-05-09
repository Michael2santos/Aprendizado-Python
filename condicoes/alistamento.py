#verificar se está na hora de se alistar no exercito
from datetime import date

nascimento = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - nascimento

if idade < 18:
    diferenca = 18 - idade
    print('Você tem {} anos de idade e não pode se alistar! '.format(idade))
    print('E ainda falta {} anos para se alistar! '.format(diferenca))
elif idade >= 18 and idade <= 20:
    print('Você tem {} anos de idade e está na hora de se alistar!'.format(idade))
else:
    tempoPassado = idade - 20
    print('Você tem {} anos de idade e passou {} anos do tempo de alistamento! '.format(idade,tempoPassado))