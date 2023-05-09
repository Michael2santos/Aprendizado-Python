#pegando a frase para analisar transformando para maiusculo e tirando espaços inicio e fim
frase = str(input('Digite uma frase para analisarmos: ')).strip().upper()
#dividindo a frase em indices
dividir = frase.split()
#removendo os espaços em branco entre as palavras
junto = ''.join(dividir)
inverso =''
#percorreendo a lista ao contrario
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print('A Frase digitada é {} e seu inverso é {} '.format(junto, inverso))
#comparando se as duas variaveis tem o mesmo conteudo
if junto == inverso:
    print('Está frase é um  PALINDROMO')
else:
    print('Está frase não é um PALINDROMO')
