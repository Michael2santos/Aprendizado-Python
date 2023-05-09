#calcular m² de uma parede, e para pintar a cada 2m² vamos precisar de 1 litro de tinta

print('<===Vamos calcular area da sua parede===>')

altura = float(input('Digite a altura da sua parede m²: '))
largura = float(input('Agora digite a largura em m²: '))

area = altura * largura
litros = area / 2

print("A area da sua parede corresponde a {:.2f} m²".format(area))
print('Para {}m² voçê irá precisar de {} litros de tinta !!'.format(area, litros))
