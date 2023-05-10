print('=' * 30)
print('{:^30}'.format('Banco Curso em Video'))
print('=' * 30)
saque = int(input('Valor do Saque R$: '))
total = saque
cedula = 50
totalcedulas = 0

while True:
    if total >= cedula: #se o valor a ser sacado for maior que 50
        total -= cedula #valor do saque retiro 50
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cedulas de R${cedula}')

        if cedula <= 50:
            cedula = 20
        elif cedula <= 20:
            cedula = 10
        elif cedula <= 10:
            cedula = 1

        totalcedulas = 0
    if total == 0:
        break
