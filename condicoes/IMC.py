#calcular IMC do usuario e dizer qual nivel está

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

print('Seu imc é {:.2f} '.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('Você está no peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade morbida. ')



