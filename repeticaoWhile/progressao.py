#fazer programa de progressao aritmetica com primeiro termo e a razão

print('GERADOR DE PA')
termo = int(input('Digite o primeiro termo: '))#inicio
razao = int(input('Digite a razão de PA: '))#salto

contador = 0
limite = 11
acumulador = 0
acrescimo = 10

while acrescimo != 0:
    while contador < limite:
        if contador < limite - 1:
            print('{} ->'.format(termo), end=' ')
            termo += razao
        else:

            print('{} ->'.format(termo), end=' ')

            # limite do while receber ele mais acrescimo para mostrar mais termos
            limite += acrescimo
            # termo recebe ele mais razao para pular de termo em termo
            termo += razao
            # acumulador faz a contagem de termos mostrados no programa
            acumulador = limite + acrescimo
    contador += 1

#variavel acrescimo para receber quantos termos a mais vão ser mostrados
acrescimo = int(input('\nQuer mostrar mais quantos termos: '))
print('Foram mostrados {} termos '.format(acumulador))
print('PAUSA')

