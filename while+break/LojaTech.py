print('=' * 15)
print('Loja Tech Info')
print('=' * 15)
print('Seja bem vindo, somos a maior loja de eletronicos')
totCompra = produtoMaiorMil = produtoMaisBarato= 0
nomeProduto = ' '

while True:
    produto= str(input('Produto comprado: '))
    preco = float(input('Valor do produto R$: '))

    if preco > 1000:
        produtoMaiorMil += 1

    if produtoMaisBarato == 0 or preco < produtoMaisBarato:
        produtoMaisBarato = preco
        nomeProduto = produto

    totCompra += preco

    sair = ' '
    while sair not in 'SN':
        print('-' * 20)
        sair = str(input('Quer comprar mais produtos? [S/N]: ')).upper().strip()[0]

    if sair == 'N':
        break

#valor total da compra
print(f'O valor total desta compra foi de {totCompra:.2f} Reais')
#quantos produtos custam mais de mil reais
print(f'Temos {produtoMaiorMil} produtos que custam mais de mil reais')
#qual o produto mais barato e quanto custa
print(f'O produto mais barato nesta compra é {nomeProduto} e custou R$ {produtoMaisBarato:.2f}')
print('Compra finalizada, Volte sempre')