numeros = (int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: ')),
           int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: ')))

print(f'Você digitou os numeros: {numeros}')
print(f'O numero 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 foi encontrado na {numeros.index(3) + 1}° posição')
else:
    print('Não foi digitado o numero 3 ')
print(f'Os numeros pares digitados foram:', end=' ')
for num in numeros:
    if num % 2 == 0:
        print(f'{num}', end=' ')
