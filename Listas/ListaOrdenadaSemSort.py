listaNum = []
for c in range(0, 5):
    numero = int(input('Digite um número: '))

    if c == 0 or numero > listaNum[len(listaNum) - 1]:#primeiro laço de repetição
        listaNum.append(numero)
        print('Adicionado no final da lista...')
    else:# quando numero passa pela condição de cima ele só pode ser igual ou menor
        pos = 0#posição
        while pos < len(listaNum):# percorrer enquanto a posição atual for menor que tamanho da lista
            if numero <= listaNum[pos]:#se o numero que estou recebendo é menor ou igual as numero na posição atual
                listaNum.insert(pos, numero)#inserindo numero atual chave pos
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print(f'Os valores digitados foram: ', listaNum)
