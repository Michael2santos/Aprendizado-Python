expressao = str(input('Digite a expressão: '))
lista = []

for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Expressão matemática é válida!!')
else:
    print('Expressão matemática é inválida!!')
