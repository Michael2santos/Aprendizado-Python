# 15% para quem ganha ate 1300 e 10 % para quem ganha acima desse valor

salario = float(input('Digite o valor do seu salario atual R$: '))

if salario <= 1300:
    novoSalario = salario + (salario * 15 / 100)
else:
    novoSalario = salario + (salario * 10 / 100)
print('Seu salario teve um aumento e foi para R${:.2f}'.format(novoSalario))
