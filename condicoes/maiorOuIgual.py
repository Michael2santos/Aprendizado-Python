#receber dois numeros e compara-los qual o maior primeiro ou segundo ou iguais

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    print('O primeiro número é maior')
elif numero2 > numero1:
    print('O segundo numero é maior ')
else:
    print('Os números são iguais!!')