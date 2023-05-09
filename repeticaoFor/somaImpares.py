#somar todos os impares divisiveis por 3 de 1 até 500
soma = 0
acumuludador = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        print(cont, end=' \n')
        soma += cont
        acumuludador += 1
print('A soma dos {} numeros filtrados deu: {} '.format(acumuludador, soma))
