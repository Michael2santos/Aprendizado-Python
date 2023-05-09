sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Sexo informado é inválido, tente novamente!!')
print('Sexo {} registrado com sucesso!!'.format(sexo))


'''sexo = str(input('Informe  o seu sexo: [M/F]')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, informe seu sexo novamente: )).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
'''