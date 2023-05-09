frase = str(input('Digite uma frase para analisarmos: ')).strip().lower()


print('Sua frase tem {} letras A'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a') + 1))
print('E a ultmia letra A nessa frase apareceu na posição {}'.format(frase.rfind('a') + 1))


