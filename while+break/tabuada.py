
while True:
    numero = int(input('Tabuada de qual numero deseja ver: '))

    if numero < 0:
        break
    else:
        cont = 1
        while cont <= 10:
            print(f' {numero} x {cont} = {numero * cont}')
            cont += 1
print("=" * 33)
print('Programa finalizado com sucesso!!')
print("=" * 33)
