nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiusculo: ', nome.upper())
print('Seu nome em minusculo: ', nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
firstName = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(firstName[0])))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))