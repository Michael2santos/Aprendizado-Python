num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

maior = num1
menor = num1
#maiores
'''if num1 > maior:
    maior = num1'''

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

#menores
'''if num1 < menor:
    menor = num1'''

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('Maior numero digitado foi: ', maior)
print('Menor numero digitado foi: ', menor)
