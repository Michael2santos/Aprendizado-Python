#calcular desconto de uma mercadoria comprada

valorProduto = float(input('Qual o valor do produto comprado: '))
valorComDesconto = valorProduto - (valorProduto * 10)/100
print('Voçê comprou um produto no valor de {:.2f} reais e ganhou 10% de desconto !!'.format(valorProduto))
print('Com desconto de 10% o novo preço do produto é {:.2f} Reais'.format(valorComDesconto))
