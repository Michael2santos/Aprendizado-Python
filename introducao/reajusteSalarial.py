#calcular reajuste salarial dos funcionarios 15% de aumento

salarioAtual = float(input('Digite seu salário atual R$: '))
salarioReajustado = salarioAtual + (salarioAtual * 15)/100

print('Seu salário atual é {:.2f} reais !!'.format(salarioAtual))
print('Com o reajuste de 15% seu salário reajustado é de {:.2f}'.format(salarioReajustado))