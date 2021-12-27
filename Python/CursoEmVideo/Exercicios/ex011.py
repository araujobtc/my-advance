# Faça um programa que leia a largura e a altura de uma parede
# em metros. Calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

import math

larg = float(input('Largura (m): '))
alt = float(input('Altura (m): '))
area = larg * alt
litros = math.ceil(area/2)

print('Área da parede: {}m² | Quantidade mínima de tinta: {}L'.format(area, litros))

