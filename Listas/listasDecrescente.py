numeros = []

while True:
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    resposta = str(input('Quer continuar: [S/N]: ')).upper()

    if resposta in 'N':
        break

numeros.sort(reverse=True)
print('-=' * 25)
print(f'Você adicionou {len(numeros)} numeros na lista')
print('-=' * 25)
print(f'Foram adicionados a lista os numeros {numeros}')
print('-=' * 25)
if 5 in numeros:
    print(f'O numero 5 foi localizado na lista')
else:
    print('O numero 5 não foi localizado na lista')
print('-=' * 25)
