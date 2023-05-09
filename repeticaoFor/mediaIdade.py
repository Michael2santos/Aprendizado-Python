
mediaIdade = 0
somaIdade = 0
maiorIdadeHomem = 0
mulherMenorVinte = 0
nomeMaisVelho = ''
#nome do homem mais velho
#quantas mulheres tem menos de 20

for c in range(1, 6):
    print('===== {}ª pessoa ====='.format(c))

    nome = str(input('Qual o seu nome: ')).upper().strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo: [M/F]: ')).upper().strip()

    somaIdade += idade
    mediaIdade = somaIdade / 3


    if sexo == 'M':
        if idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomeMaisVelho = nome


    if sexo == 'F':
        if idade < 20:
            mulherMenorVinte += 1


print('A média de idade de todos é: {:.0f} anos'.format(mediaIdade))
print('Quantidade de mulheres com menos de vinte anos: {}'.format(mulherMenorVinte))
print('O nome do homem mais velho è {} e ele tem {} anos'.format(nomeMaisVelho, maiorIdadeHomem))
