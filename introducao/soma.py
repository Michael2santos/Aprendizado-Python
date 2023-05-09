#comentario em python usa-se o #
#pow(3,2) potenciação
#
print('Digite os numeros para o sistema realizar a soma !!')
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
resultado = num1 + num2

print('A soma de {} + {} é igual a : {} '.format(num1, num2, resultado))

print('Agora digite dois valores para divisão: ')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
div = n1 / n2
print('A divisão de {} por {} é igual a {:.2f}'.format(n1, n2, div))
