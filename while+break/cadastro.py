#total de pessoas com mais de 18 anos
#quantos homens cadastrados
#mulheres com menos de 20 anos
maiorIdade = homens = mulheresMenos = 0

while True:
    #cadastrar dados do usuario
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        maiorIdade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheresMenos += 1

    adicionar = ' '
    while adicionar not in 'SN':
        adicionar = str(input('Cadastrar mais usuarios: [S/N]')).strip().upper()[0]
    if adicionar == 'N':
        break

print(f'Temos {maiorIdade} pessoas que são maiores de idade')
print(f'Temos {homens} homens cadastrados')
print(f'Temos {mulheresMenos} mulheres cadastradas com menos de 20 anos')




