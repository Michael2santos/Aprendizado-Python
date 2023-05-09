contador = soma = numero = 0

while numero != 999:
    numero = int(input('Digite um valor para somar [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Foi digitado {contador} valores e a soma deles deu: {soma}')
