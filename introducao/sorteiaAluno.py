from random import choice

print('Digite os nomes a seguir para sorteamos!!')
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

#choice sorteia um item da lista
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(lista)
print('O aluno sorteado para a tarefa foi a/o: {}'.format(sorteado))