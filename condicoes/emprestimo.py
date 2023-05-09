#valor casa, salario e em quanto tempo vai pagar

valorCasa = float(input('Qual o valor da casa em R$: '))
salario = float(input('Qual o valor do seu salário em R$: '))
qtdePrestacoes = int(input('Qual a quantidade de prestações em meses: '))

valorPrestacoes = valorCasa / qtdePrestacoes
porcent = salario * 30 / 100

if valorPrestacoes > porcent:
    print('INFELIZMENTE NÃO FOI POSSIVEL LIBERAR SEU FINANCIAMENTO!! ')
    print('O valor das prestações superou 30% do seu salário')
    print('Valor maximo da prestação é R$ {}'.format(porcent))
else:
    print('Obaaa!!!, seu financiamento foi autorizado')
print('Valor da prestação: R$ {:.2f}'.format(valorPrestacoes))
