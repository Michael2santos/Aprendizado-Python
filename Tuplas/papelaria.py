lista = ('Lapis', 0.50, 'Borracha', 1, 'Caderno', 5.60, 'Mochila', 165.20, 'Tesoura', 2.75, 'Regua', 1.80, 'Caneta', 1.25, 'Dicionario', 15.99, 'Apontador', 0.85)
print('-=' * 18)
print(f'{"Papelaria São João":^35}')
print('-=' * 18)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$ {lista[pos]:.2f}')
print('-'* 38)
print('Pedido Finalizado com sucesso!!!!')
