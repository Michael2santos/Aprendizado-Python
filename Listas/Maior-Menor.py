numeros = []
maior = menor = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite o valor para adicionar na posição {n}°: ')))
    if n == 0:
        menor = maior = numeros[n]
    else:
        if numeros[n] < menor:
            menor = numeros[n]
        if numeros[n] > maior:
            maior = numeros[n]

print('-=' * 25)
print(f'O maior numero digitado foi {maior} e está na posição: ', end=' ')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print('-=' * 25)
print(f'O menor numero digitado foi {menor} e está na posição:', end=' ')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end=' ')
print()
print('-=' * 25)
print(f'Numeros digitados', numeros)
print('-=' * 25)
