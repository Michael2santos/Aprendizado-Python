#inserindo dados na lista
dados =[['Michael', 33, 'Casado', 'Desenvolvedor'], ['Natalie', 34, 'Casada', 'Auxiliar de vendas']]
#dados.append('Michael')
#dados.append(29)
#dados.append('Casado')
#dados.append('Desenvolvedor')

#dados.append('Natalie')
#dados.append(34)
#dados.append('Casada')
#dados.append('Auxiliar de vendas')


#listas dentro de listas
pessoa = dados[:] #copiando itens de uma lista para outra
#pessoa = dados[] atribuindo lista dados na pessoa, se houver mudar em qualquer uma altera a outra
#pessoa.append(dados[:])

print(f'{pessoa[1][0]} é {pessoa[1][2]}')
print(f'{pessoa[0][0]} é {pessoa[0][3]}')
print(pessoa)



#apagando dados da lista
#dado.clear()


#analisando dados da lista