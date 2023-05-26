tuplas = () #imutavel
lista = ['Computador', 'Mouse', 'Sanfona'] #mutavel

lista.append('teste')#insere item no final da lista
lista.insert(0, 'teste1')#insere item na chave solicitada

del lista[2]#apagando item pela chave
lista.pop(1)#apagando item pela chave, senao passar a chave apaga ultimo item
lista.remove('Sanfona')#apagando item pelo conteudo

valores = list(range(4, 15))

numeros = [1, 3, 8, 16, 2, 4, 20, 5]
numeros.sort()#sem parametro reverse=True , organiza crescente com reverse organiza forma decrescente

for c, v in enumerate(numeros):
    print(f'Na posição {c} encontrei o numero {v}')


print(f'Essa lista tem {len(numeros)} indices')#tamanho da minha lista
print(numeros)
print(valores)
print(lista)
