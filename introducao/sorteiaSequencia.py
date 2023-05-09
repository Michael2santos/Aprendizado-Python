from random import shuffle
#metodo shuffle embaralha itens de uma lista

print('digite o nome dos alunos para sorteio da apresentação !!')
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('A sequência de apresentação será : ')
print(alunos)
