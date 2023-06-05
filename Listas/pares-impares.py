listaNum = []
listaPar = []
listaImpar = []
while True:
    numero = int(input('Digite um numero: '))
    listaNum.append(numero)

    resposta = str(input('Quer continuar [S/N]: ')).upper()
    if resposta in 'N':
        break
for c in range(0, len(listaNum)):
    if listaNum[c] % 2 == 0:
        listaPar.append(listaNum[c])
    else:
        listaImpar.append(listaNum[c])

listaPar.sort()
listaImpar.sort()
listaNum.sort()
print('-=' * 25)
print(f'Foram adicionados na lista {len(listaNum)} numeros')
print(f'A lista completa é: {listaNum}')
print(f'Os numeros pares digitados são: {listaPar}')
print(f'Os numeros impares digitados são: {listaImpar}')
