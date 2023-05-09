# calcular se as medidas formam um triangulo e qual tipo de triangulo forma

reta1 = float(input('Primeira medida: '))
reta2 = float(input('Segunda medida: '))
reta3 = float(input('Terceira medida: '))

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1:
    print('Estas medidas formam um triangulo!!!')
    if reta1 == reta2 == reta3:#TODOS OS LADOS IGUAIS
        print('EQUILATERO.')
    elif reta1 != reta2 != reta3 != reta1: #TODOS OS LADOS DIFERENTES
        print('ESCALENO')
    else:# DOIS LADOS IGUAIS E UM DIFERENTES
        print('ISÓSCELES')
else:
    print('Estas medidas não formam um triangulo!')
