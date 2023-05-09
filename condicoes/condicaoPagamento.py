#dinheiro/cheque 10% desconto
#avista cartão 5% desconto
#até 2 vezes preço normal
#mais de 3 vezes 20% juros

precoProduto = float(input('Qual o valor do produto R$: '))
formaPagamento = int(input('\n 1-Cheque ou Dinheiro\n 2-Avista cartão \n 3-Até duas vezes \n 4-3 Vezes ou mais \n Forma de Pagamento: '))

if formaPagamento == 1:
    novoValor = precoProduto - (precoProduto * 10 / 100)
elif formaPagamento == 2:
    novoValor = precoProduto - (precoProduto * 5 / 100)
elif formaPagamento == 3:
    novoValor = precoProduto
else:
    novoValor = precoProduto + (precoProduto * 20 / 100)

print('Com está forma de pagamento o valor do produto é R$ {:.2f} reais'.format(novoValor))